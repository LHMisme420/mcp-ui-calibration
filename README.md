# mcp-ui-calibration

**Deliberately vulnerable. Do not deploy or reuse this code.** The credential in
`server.py` is fake.

A small MCP server with a known answer key, used to check that the mcp-authscan
UI reports findings correctly. Scan this repo and compare the result with the
table below and `EXPECTED.json`.

| Severity | Rule | Location | Finding |
|---|---|---|---|
| CRITICAL | A2 | `server.py:10` | Hardcoded credential `API_KEY` |
| HIGH | A10 | `server.py:12` | FastMCP on HTTP transport with `auth=None` |
| HIGH | C1 | `server.py:15` | `ClientCredentialsOAuthProvider` without `issuer=` |
| MEDIUM | A1 | `oauth.py:7` | Authorize handler trusts `redirect_uri` |
| MEDIUM | A6 | `proxy.py:3` | Authorization enforced only on `tools/call` |
| MEDIUM | A4 | `server.py:25` | Outbound request to a caller-controlled URL |

**Expected totals: 1 CRITICAL, 2 HIGH, 3 MEDIUM, 6 total.**

Common miscounts and what they mean:

| UI shows | Likely cause |
|---|---|
| 4 | HIGH findings dropped |
| 3 | MEDIUM findings dropped |
| 0 | Clone failed and an empty directory was scanned |

Check locally with the scanner from mcp-authscan:

```
python3 mcp_authscan.py /path/to/mcp-ui-calibration
```

Keep the files at the repo root. mcp-authscan's A4 rule skips paths under
`examples/`, which would drop the expected total to 5.
