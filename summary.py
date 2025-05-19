from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"
@app.route("/summarize", methods=["POST"])
def summarize():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415
    data = request.get_json()
    contract_text = data.get("text", "")
    prompt = f"提取这份合同的关键条款（如金额、期限）：{contract_text}"
    response = ollama.generate(model="mistral", prompt=prompt)
    return jsonify({"summary": response["response"]})

if __name__ == "__main__":
    app.run(debug=True)