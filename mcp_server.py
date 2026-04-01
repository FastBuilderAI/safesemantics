import json
import os
from typing import Any, Dict, List, Optional
from mcp.server.fastapi import Context
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
