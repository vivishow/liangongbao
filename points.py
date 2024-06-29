import json
from mitmproxy import http

print("****************************************************************\n已加载")

USERCODE = 15305433
POINTS = 99
DRAWNUM = 99


def response(flow: http.HTTPFlow) -> None:
    if "lgb360.com/aqy/" in flow.request.pretty_url:
        request = {
            "token": flow.request.headers["token"],
            "id": flow.request.headers["memberid"],
            "cookie": flow.request.headers["cookie"],
        }
        print(f"{request=}")
        content = json.loads(flow.response.content.decode("UTF-8"))
        print(f"{flow.request.pretty_url=}\n{content=}")
        # if data := content.get("data"):
        #     data["points"] = POINTS
        # flow.response.content = json.dumps(content).encode("UTF-8")

    if "lgb360.com/aqy/regist/competition" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode("UTF-8"))
        if data := content.get("data"):
            data["points"] = POINTS
            data["drawNum"] = DRAWNUM
        flow.response.content = json.dumps(content).encode("UTF-8")

    if "lgb360.com/aqy/regist/activity" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode("UTF-8"))
        if data := content.get("data"):
            data["userCode"] = USERCODE
        flow.response.content = json.dumps(content).encode("UTF-8")

    if "lgb360.com/aqy/prize/getDrawSurplusNum" in flow.request.pretty_url:
        content = json.loads(flow.response.content.decode("UTF-8"))
        if data := content.get("data"):
            data["surplusNum"] = DRAWNUM
        flow.response.content = json.dumps(content).encode("UTF-8")
