import json
from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if "lgb360.com/aqy/regist/competition" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode("UTF-8"))
        print(f"信息 {content}")
        if data := content.get("data"):
            data['points'] = 999
        flow.response.content = json.dumps(content).encode("UTF-8")

    if "lgb360.com/aqy/regist/activity" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode("UTF-8"))
        if data := content.get("data"):
            data["userCode"] = 7777777
        flow.response.content = json.dumps(content).encode("UTF-8")
