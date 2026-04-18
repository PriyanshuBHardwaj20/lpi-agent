import json
import subprocess
import os
import requests
import sys

# CONFIGURATION
LPI_REPO_PATH = r"C:\Users\G15\lpi-developer-kit" 
LPI_SERVER_INDEX = os.path.join(LPI_REPO_PATH, "dist", "src", "index.js")
OLLAMA_MODEL = "qwen2.5:1.5b" 
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_mcp_tool(proc, tool_name, arguments={}):
    """Sends a JSON-RPC request to the LPI server."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments}
    }
    proc.stdin.write(json.dumps(payload) + "\n")
    proc.stdin.flush()
    line = proc.stdout.readline()
    if not line: 
        return "Error: No response from LPI server."
    
    try:
        data = json.loads(line)
        return data["result"]["content"][0]["text"]
    except Exception as e:
        return f"Error parsing tool output: {e}"

def run_agent(user_input):
    # START LPI SERVER 
    if not os.path.isdir(LPI_REPO_PATH):
        print(f"[!] ERROR: Path not found: {LPI_REPO_PATH}")
        return

    proc = subprocess.Popen(
        ["node", LPI_SERVER_INDEX],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        cwd=LPI_REPO_PATH
    )

    # Initial Handshake
    init = {"jsonrpc":"2.0","id":0,"method":"initialize","params":{"capabilities":{},"clientInfo":{"name":"lpi-agent","version":"1.0"}}}
    proc.stdin.write(json.dumps(init) + "\n")
    proc.stdin.flush()
    proc.stdout.readline() 

    # QUERY LPI TOOLS
    overview_data = call_mcp_tool(proc, "smile_overview")
    phase_1_data = call_mcp_tool(proc, "smile_phase_detail", {"phase": "reality-emulation"})
    phase_2_data = call_mcp_tool(proc, "smile_phase_detail", {"phase": "concurrent-engineering"})

    proc.terminate()

    # BUILD THE REASONING PROMPT
    system_prompt = f"""
    You are a SMILE Methodology Auditor. 
    Analyze the user's project and perform a 'Gap Analysis' using the LPI data provided.
    
    [CONTEXT - Source 1: smile_overview]
    {overview_data}
    
    [CONTEXT - Source 2: reality-emulation]
    {phase_1_data}

    [CONTEXT - Source 3: concurrent-engineering]
    {phase_2_data}

    USER PROJECT STATE:
    "{user_input}"
    
    INSTRUCTIONS:
    1. Determine which SMILE Phase the user is currently in.
    2. Explain why, using specific definitions from the sources.
    3. Identify what technical steps are needed to reach the next phase.
    4. CITATIONS: You MUST cite your sources using [Source 1], [Source 2], or [Source 3] for every claim.
    """

if __name__ == "__main__":
    user_query = sys.argv[1] 
    run_agent(user_query)