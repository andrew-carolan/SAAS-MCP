# Plan for MCP Auto-Coder

## Goal
Create a specialized version of the Auto-Coder that autonomously generates, tests, and iterates on Model Context Protocol (MCP) servers based on extracted API definitions (JSON files containing curl commands, parameters, and descriptions).

## 1. Input Analysis
- **Source**: JSON files from the `llm_successful_scripts` directory (e.g., `extracted_cryptocurrency#airdrops.json`).
- **Key Data**: 
    - `name`: Tool name.
    - `curl`: The actual API call to implement.
    - `params`: Input arguments for the tool.
    - `description`: Tool description for the LLM.

## 2. Architecture of `AutoCoderMCP`
The `AutoCoderMCP` will be a Python class (extending or mimicking `AutoCoder`) with the following workflow:

### A. Prompt Engineering
- **Context Injection**: Feed the LLM the MCP SDK documentation (specifically the Python `mcp` library) and the target API JSON.
- **Instruction Set**: 
    - Map each JSON endpoint to an `@server.tool()`.
    - Implement the `requests` logic to execute the `curl` command.
    - Handle API keys via environment variables.
    - Ensure proper type hinting for tool arguments.

### B. Implementation Loop
1. **Generate**: LLM produces the full `server.py` code.
2. **Save**: Write code to a temporary file `temp_mcp_server.py`.
3. **Verify**:
    - **Static Analysis**: Run `python3 -m py_compile temp_mcp_server.py` to check for syntax errors.
    - **Runtime Check**: Attempt to start the server and check for immediate crashes.
    - **Functional Test (Mock Client)**: 
        - Implement a lightweight MCP client that connects to the server.
        - Call each tool with dummy data.
        - Verify that the server responds (even if the API returns a 401/403, as long as the server logic is correct).
4. **Feedback**: Capture any tracebacks or functional failures and feed them back to the LLM.
5. **Iterate**: Repeat until the server starts and all tools are registered and callable, or max retries are reached.

## 3. Testing Strategy
Since MCP servers are designed to be used by clients, the "Evaluator" will be a mock client:
- Use the `mcp` Python SDK to create a client.
- `client.list_tools()` to ensure all expected tools are present.
- `client.call_tool(name, arguments)` to ensure no internal crashes.

## 4. Final Output
- The final, verified code will be saved to a new file (e.g., `mcp_server_final.py`) to avoid overwriting existing codebase.

## 5. Success Criteria
- [ ] Server compiles without syntax errors.
- [ ] Server starts and registers all tools defined in the input JSON.
- [ ] All tools are callable via the MCP protocol without crashing the server.
- [ ] API calls are correctly constructed based on the provided curl commands.
