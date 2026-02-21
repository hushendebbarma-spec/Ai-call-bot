from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "AI Call Bot Running"

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()

    gather = Gather(
        input="speech",
        action="/process",
        method="POST",
        timeout=5
    )
    gather.say("Hello. You are speaking to an AI assistant. Please say your message.")
    response.append(gather)

    response.say("No input received. Goodbye.")
    response.hangup()

    return str(response)

@app.route("/process", methods=["POST"])
def process():
    speech_text = request.form.get("SpeechResult")

    response = VoiceResponse()

    if speech_text:
        reply = f"You said: {speech_text}. The user is currently busy. Goodbye."
    else:
        reply = "I did not understand. Goodbye."

    response.say(reply)
    response.hangup()

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
