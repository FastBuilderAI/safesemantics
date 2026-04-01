import re
import math
from typing import List, Dict, Any
import mcp.types as types

# ─── Tool Description Injection Patterns ───
INJECTION_PATTERNS = [
    (re.compile(r"ignore\s+(previous|prior|above|all)\s+(instructions?|prompts?|rules?)", re.I), "instruction_override", "CRITICAL"),
    (re.compile(r"disregard\s+(previous|prior|above|all)", re.I), "instruction_override", "CRITICAL"),
    (re.compile(r"you\s+are\s+now\s+a", re.I), "role_hijack", "CRITICAL"),
    (re.compile(r"forget\s+(everything|all|previous)", re.I), "memory_wipe", "CRITICAL"),
    (re.compile(r"instead\s+of\s+\w+,?\s*(call|use|execute|run)", re.I), "tool_redirect", "HIGH"),
    (re.compile(r"also\s+(call|execute|run|invoke)\s+", re.I), "hidden_action", "HIGH"),
    (re.compile(r"do\s+not\s+(tell|show|reveal|mention)\s+(the\s+)?user", re.I), "concealment", "HIGH"),
    (re.compile(r"secretly|covertly|without\s+(the\s+)?user\s+knowing", re.I), "stealth_action", "HIGH"),
    (re.compile(r"override|bypass|skip|ignore\s+(auth|security|permission|validation)", re.I), "security_bypass", "CRITICAL"),
    (re.compile(r"base64|atob|btoa|eval\s*\(", re.I), "encoded_payload", "MEDIUM"),
    (re.compile(r"\{%|<%|<\?|\{\{.*\}\}", re.I), "template_injection", "MEDIUM"),
    (re.compile(r"\\u[0-9a-f]{4}|\\x[0-9a-f]{2}", re.I), "unicode_obfuscation", "MEDIUM"),
]

# ─── Dangerous Tool Name Patterns ───
DANGEROUS_TOOL_PATTERNS = [
    (re.compile(r"^(delete|remove|drop|truncate|purge|destroy|wipe|erase)", re.I), "destructive", "HIGH"),
    (re.compile(r"(delete|remove|drop|truncate|purge|destroy|wipe|erase)$", re.I), "destructive", "HIGH"),
    (re.compile(r"^(execute|exec|run|eval|shell|cmd|command|bash|terminal)", re.I), "execution", "CRITICAL"),
    (re.compile(r"^(deploy|publish|release|push|ship)", re.I), "deployment", "HIGH"),
    (re.compile(r"^(admin|root|sudo|superuser|elevate)", re.I), "privilege", "CRITICAL"),
    (re.compile(r"(password|secret|key|token|credential|auth)", re.I), "credential_access", "HIGH"),
    (re.compile(r"^(send|email|message|notify|post|tweet|slack)", re.I), "external_action", "MEDIUM"),
    (re.compile(r"(payment|charge|bill|invoice|transfer|withdraw)", re.I), "financial", "CRITICAL"),
    (re.compile(r"^(create|insert|update|modify|set|write)", re.I), "mutation", "MEDIUM"),
    (re.compile(r"^(read|get|list|show|describe|fetch|query|search|find)", re.I), "read_only", "INFO"),
]

def check_unbounded_strings(schema: Dict) -> bool:
    try:
        props = schema.get('properties', {})
        for k, v in props.items():
            if v.get('type') == 'string':
                if not v.get('maxLength') and not v.get('pattern') and not v.get('enum'):
                    return True
    except Exception:
        pass
    return False

SCHEMA_WEAKNESS_PATTERNS = [
    (lambda s: not s or len(s) == 0, "no_schema", "HIGH", "Tool accepts arbitrary input with no schema validation"),
    (lambda s: s.get('type') == 'object' and (not s.get('properties') or len(s.get('properties', {})) == 0), "empty_schema", "MEDIUM", "Schema defined but no properties specified"),
    (lambda s: s.get('type') == 'object' and not s.get('required'), "no_required_fields", "LOW", "No required fields — all input is optional"),
    (check_unbounded_strings, "unbounded_strings", "MEDIUM", "String parameters without length limits or pattern validation"),
]

DEDUCTIONS = {
    "CRITICAL": 25,
    "HIGH": 15,
    "MEDIUM": 8,
    "LOW": 3,
    "INFO": 0
}

def scan_tool_descriptions(tools: List[types.Tool]) -> List[Dict]:
    findings = []
    for tool in tools:
        desc = (tool.description or "")
        name = tool.name or ""
        for pattern, rule_name, severity in INJECTION_PATTERNS:
            if pattern.search(desc):
                findings.append({
                    "category": "injection",
                    "severity": severity,
                    "tool": name,
                    "message": f"Tool description contains potential prompt injection pattern: '{rule_name}'"
                })
        if len(desc) > 1000:
            findings.append({
                "category": "injection",
                "severity": "MEDIUM",
                "tool": name,
                "message": f"Tool description is {len(desc)} chars — unusually long, may contain hidden instructions"
            })
    return findings

def scan_tool_names(tools: List[types.Tool]) -> List[Dict]:
    findings = []
    for tool in tools:
        name = tool.name or ""
        for pattern, risk, severity in DANGEROUS_TOOL_PATTERNS:
            if pattern.search(name) and severity != "INFO":
                findings.append({
                    "category": "permissions",
                    "severity": severity,
                    "tool": name,
                    "message": f"Tool '{name}' classified as '{risk}' — requires permission controls."
                })
    return findings

def scan_input_schemas(tools: List[types.Tool]) -> List[Dict]:
    findings = []
    for tool in tools:
        # Pydantic dict serialization handling for MCP inputs
        schema = tool.inputSchema if isinstance(tool.inputSchema, dict) else (tool.inputSchema.model_dump() if hasattr(tool.inputSchema, 'model_dump') else {})
        name = tool.name or ""
        for check_func, rule_name, severity, desc_text in SCHEMA_WEAKNESS_PATTERNS:
            if check_func(schema):
                findings.append({
                    "category": "validation",
                    "severity": severity,
                    "tool": name,
                    "message": desc_text
                })
    return findings

def scan_auth_indicators(tools: List[types.Tool]) -> List[Dict]:
    findings = []
    has_auth = any(re.search(r"auth|login|token|credential|session", tool.name, re.I) for tool in tools)
    if not has_auth:
        findings.append({
            "category": "auth",
            "severity": "HIGH",
            "tool": "*",
            "message": "Server exposes no authentication-related tools — may accept unauthenticated connections"
        })
    if len(tools) > 20:
        findings.append({
            "category": "permissions",
            "severity": "MEDIUM",
            "tool": "*",
            "message": f"Server exposes {len(tools)} tools — large attack surface without per-tool permission controls"
        })
    return findings

def get_grade(score: int) -> str:
    if score >= 90: return "A"
    if score >= 75: return "B"
    if score >= 60: return "C"
    if score >= 40: return "D"
    return "F"

def grade_mcp_server(tools: List[types.Tool]) -> Dict[str, Any]:
    findings = []
    findings.extend(scan_tool_descriptions(tools))
    findings.extend(scan_tool_names(tools))
    findings.extend(scan_input_schemas(tools))
    findings.extend(scan_auth_indicators(tools))
    
    score = 100
    for finding in findings:
        score -= DEDUCTIONS.get(finding["severity"], 0)
    score = max(0, score)
    
    return {
        "score": score,
        "grade": get_grade(score),
        "findings": findings
    }
