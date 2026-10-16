"""UI calibration MCP server for mcp-authscan.

Deliberately vulnerable. Expected scan result: 1 CRITICAL, 2 HIGH, 3 MEDIUM
(6 total). See EXPECTED.json. Do not deploy.
"""
import requests
from fastmcp import FastMCP
from fastmcp.client.auth import ClientCredentialsOAuthProvider

API_KEY = "sk-live-calibration"  # CRITICAL A2: hardcoded credential

mcp = FastMCP("ui-calibration", auth=None)  # HIGH A10 (with the http transport below)

# HIGH C1: M2M OAuth client with no issuer= binding
upstream_auth = ClientCredentialsOAuthProvider(
    server_url="https://upstream.example.com/mcp",
    client_id="calibration",
    client_secret=API_KEY,
)


@mcp.tool()
def get_page(url: str) -> str:
    """Fetch a URL."""
    return requests.get(url, timeout=5).text  # MEDIUM A4: outbound request to a caller-controlled URL


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
