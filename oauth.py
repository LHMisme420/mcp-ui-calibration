# MEDIUM A1: authorize handler trusts client_id / redirect_uri with no allowlist
from flask import Flask, redirect, request

app = Flask(__name__)


def authorize():
    if request.args.get("response_type") != "code":
        return "unsupported_response_type", 400
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    state = request.args.get("state", "")
    return redirect(f"{redirect_uri}?code=calib-{client_id}&state={state}")


app.add_url_rule("/authorize", view_func=authorize)
