# MEDIUM A6: authorization only enforced on tools/call; other methods bypass it
def dispatch(req, tenant):
    if req["method"] == "tools/call":
        if not tenant.tool_allowed(req["params"]["name"]):
            raise PermissionError("forbidden: tool not allowed")
    return forward(req)


def forward(req):
    return {"jsonrpc": "2.0", "id": req.get("id"), "result": {}}
