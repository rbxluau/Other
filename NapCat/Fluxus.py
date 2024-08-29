from websockets.sync.client import connect
from re import fullmatch
import requests
import json

with connect("ws://127.0.0.1:3001") as websocket:
    while True:
        Recv = json.loads(websocket.recv())
        if "post_type" in Recv and Recv["post_type"] == "message" and Recv["message_type"] == "group" and fullmatch(r"https://flux\.li/android/external/start\.php\?HWID=[a-z0-9]{96}", Recv["raw_message"]):
                websocket.send(json.dumps(({
                    "action":"send_msg",
                    "params":{
                        "group_id":Recv["group_id"],
                        "message":"\n".join([f"{i}: {v}" for i, v in requests.get("https://bypass-beta.vercel.app/api/bypass?url="+Recv["raw_message"]).json().items()])
                    }
                })))
