from flask import Flask, request, jsonify
import openai
import os

app = Flask(_name_)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/consulta-angelito", methods=["POST"])
def consulta_ia():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return jsonify(response.choices[0].message)
