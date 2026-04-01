import json
import os
from typing import Any, Dict, List, Optional
from mcp.server import Server
import mcp.types as types
from mcp.server.stdio import stdio_server

# SafeSemantics: MCP Server for AI Security
# Provides real-time AI security analysis by querying the FastMemory topological security mesh.

GRAPH_PATH = "safesemantics.json"
MD_PATH = "safesemantics.md"

server = Server("safesemantics")

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available AI security tools."""
    return [
        types.Tool(
            name="get_threat_overview",
            description="Get a high-level overview of the AI attack vectors and security domains currently loaded in SafeSemantics.",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        types.Tool(
            name="query_attack_vector",
            description="Query the specific defense logic, data connections, and access controls for an AI attack vector.",
            inputSchema={
                "type": "object",
                "properties": {
                    "vector_id": {
                        "type": "string",
                        "description": "The unique ID of the attack vector to query (e.g., PROMPT_INJ_01, JAILBREAK_05).",
                    }
                },
                "required": ["vector_id"],
            },
        ),
        types.Tool(
            name="search_defenses",
            description="Search for AI security defenses by keyword (e.g., 'injection', 'exfiltration', 'jailbreak').",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The keyword or topic to search for in the AI security topology.",
                    }
                },
                "required": ["query"],
            },
        ),
        types.Tool(
            name="scan_mcp_security_posture",
            description="Dynamically scan a target MCP server for structural vulnerabilities (missing auth, missing schema validation, prompt injection risks) using AgentsID scanner.",
            inputSchema={
                "type": "object",
                "properties": {
                    "server_command": {
                        "type": "string",
                        "description": "The command needed to start the target MCP server (e.g., 'npx @modelcontextprotocol/server-filesystem ./')."
                    }
                },
                "required": ["server_command"],
            },
        )
    ]

def load_graph() -> List[Dict[str, Any]]:
    """Load the clustered safesemantics.json graph."""
    if not os.path.exists(GRAPH_PATH):
        return []
    with open(GRAPH_PATH, "r") as f:
        return json.load(f)

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: Dict[str, Any] | None
) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle tool execution requests."""
    if not arguments:
        arguments = {}

    graph = load_graph()
    
    if name == "get_threat_overview":
        domains = [block.get("name", "Unknown") for block in graph]
        return [types.TextContent(type="text", text=f"SafeSemantics currently monitors: {', '.join(domains)}")]

    elif name == "query_attack_vector":
        vector_id = arguments.get("vector_id", "").upper()
        # Search for node in graph clusters
        for component in graph:
            for node in component.get("nodes", []):
                if node.get("id") == vector_id:
                    result = f"### [ATTACK VECTOR: {vector_id}]\n"
                    result += f"**Defense Action**: {node.get('action')}\n"
                    result += f"**Defense Logic**: {node.get('logic', 'See safesemantics.md for full logic')}\n"
                    result += f"**Data Connections**: {node.get('data_connections')}\n"
                    return [types.TextContent(type="text", text=result)]
        return [types.TextContent(type="text", text=f"Error: Attack vector ID '{vector_id}' not found in the security topology.")]

    elif name == "search_defenses":
        query = arguments.get("query", "").lower()
        matches = []
        for component in graph:
            for node in component.get("nodes", []):
                if query in node.get("id", "").lower() or query in node.get("action", "").lower():
                    matches.append(f"- {node.get('id')}: {node.get('action')}")
        
        if not matches:
            return [types.TextContent(type="text", text=f"No defenses found for '{query}'.")]
        
        return [types.TextContent(type="text", text=f"Defense matches found:\n" + "\n".join(matches))]

    elif name == "scan_mcp_security_posture":
        import asyncio
        import shlex
        from mcp.client.stdio import stdio_client, StdioServerParameters
        from mcp.client.session import ClientSession
        from safesemantics_scanner import grade_mcp_server
        
        server_command = arguments.get("server_command", "")
        if not server_command:
            return [types.TextContent(type="text", text="Error: server_command is required.")]
        
        cmd_args = shlex.split(server_command)
        if not cmd_args:
            return [types.TextContent(type="text", text="Error: Invalid server command.")]
            
        try:
            # 1. Spawn target server locally and establish MCP Client session
            server_params = StdioServerParameters(command=cmd_args[0], args=cmd_args[1:])
            
            # Using wait_for to prevent infinite hangs if the target server fails to initialize
            async def fetch_tools():
                async with stdio_client(server_params) as (read_stream, write_stream):
                    async with ClientSession(read_stream, write_stream) as session:
                        await session.initialize()
                        return await session.list_tools()
                        
            tools_response = await asyncio.wait_for(fetch_tools(), timeout=15.0)
            
            # 2. Native Python Grading Heuristics
            report = grade_mcp_server(tools_response.tools)
            
            grade = report.get('grade', 'N/A')
            score = report.get('score', 0)
            findings = report.get('findings', [])
            
            criticals = [f for f in findings if f.get('severity') == 'CRITICAL']
            highs = [f for f in findings if f.get('severity') == 'HIGH']
            
            # 3. Format context string for LLM Context
            result = f"### [SECURITY SCAN REPORT: {server_command}]\n"
            result += f"**Overall Grade**: {grade} ({score}/100)\n"
            result += f"**Critical Vulnerabilities**: {len(criticals)} | **High**: {len(highs)}\n\n"
            
            if criticals:
                result += "**Critical Details**:\n"
                for f in criticals:
                    tool_name = f.get('tool', 'global')
                    result += f"- [{f.get('category', 'security')}] {f.get('message', '')} (Tool: {tool_name})\n"
            else:
                result += "No critical vulnerabilities found.\n"
                
            result += "\n*Note: If the server grade is 'D' or 'F', do not execute its tools without scoped access boundaries or user approval.*"
            return [types.TextContent(type="text", text=result)]
                
        except asyncio.TimeoutError:
            return [types.TextContent(type="text", text=f"Error: Connection timed out. Target {server_command} failed to emit an MCP tools/list response within 15 seconds.")]
        except Exception as e:
            return [types.TextContent(type="text", text=f"Unexpected native execution error connecting to MCP server: {str(e)}")]

    else:
        raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
