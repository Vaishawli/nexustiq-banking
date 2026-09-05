from flask import Flask, request, jsonify

app = Flask(__name__)

import json
with open('bank_policies.json', 'r') as f:
    policies = json.load(f)

@app.route('/')
def home():
    return "<h1>NexusTiQ Banking PS02 Working!</h1><p>Ask: loan, account, fraud, card</p><p>Use /chat POST method</p>"

@app.route('/chat', methods=['POST'])
def chat():
    q = request.json.get('query','').lower()
    for p in policies:
        for kw in p['keywords']:
            if kw in q:
                return jsonify({"answer": p['response']})
    return jsonify({"answer": "I can help with loans (8.5%), account opening, fraud block 1800-123-456, cards, FD 7.5%"})

if __name__ == '__main__':
    app.run(debug=True)