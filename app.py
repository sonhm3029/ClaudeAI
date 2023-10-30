from flask import Flask, request, jsonify
from flask_cors import CORS
from claude_api import Client

app = Flask(__name__)
CORS(app)

cookie = """sessionKey=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; intercom-device-id-lupk8zyo=b650b28f-aa14-4b8e-a459-d25bc475fe0a; __stripe_mid=21298c21-e179-4aa2-9ae6-5f006d8a9877ad5409; activitySessionId=0a52a943-e357-4744-b982-a136a39afb60; __stripe_sid=51f0f0c5-1872-4c26-a4a7-c54b568398b5f04e1e; cf_clearance=m6URy8oNvCRV8VWlYOzRumuNZoAosO0eFdvqBU_BwgI-1698679580-0-1-4858e096.8c3c8b06.1f59bf76-0.2.1698679580; __cf_bm=fBeneRKs8QsKEjMJ5BgKCTpPpo_KYjtKNX.CoVOIrO0-1698680007-0-Ae+LZQerV2kprbh0HFFgI2FSb5vVcMjaA2evnM3uLOjzt7Lxt5QMXl1vtL/u9WJ6gu+SJYPVKUESQXObi2RYDWc=; intercom-session-lupk8zyo=SUZFN2Y2VTJmeTF1cCs1SXl2ZnlWL2prVDluUCtZZXVKaUVYWEdzczBXTzJnWlh2OUlBbFRhVjN1Q21IenpoWC0tMXlSek4vbUtMbDYwdzErd1pSY2J4dz09--aaf54c33f3053b72710b991d915e4b9acf33ff9c"""
claude_api = Client(cookie)

conversation_id = claude_api.create_new_chat()["uuid"]

@app.route("/chat", methods=["POST"])
def chat():
    body = request.get_json()
    msg = body.get("msg")
    response = claude_api.send_message(msg, conversation_id)
    for res in response:
        print(res)
    return jsonify({
        "code": 200,
        "response": response
    })

if __name__ == "__main__":
    app.run("0.0.0.0", 8000, debug=True)