from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/version')
def version_api():
    return jsonify(
        version='2.0.0', 
        content='<body style="background-color:pastelgreen;"><h1>Version: 2.0.0</h1></body>'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)