from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import openai
from openai import OpenAI
client = OpenAI(api_key="REMOVED_SECRET")

app = Flask(__name__)
CORS(app)


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Summarize this:"}, {"role": "user", "content": text}]
        )
        summary = response.choices[0].message.content
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
