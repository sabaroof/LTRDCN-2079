from flask import Flask, jsonify, url_for

app = Flask(__name__)

@app.route('/version')
def version_api():
    image_url = url_for('static', filename='background.png')
    return jsonify(
        version='1.0.0',
        content='<h1 style="color:white;">Version: 2.0.0</h1>',
        image_url=image_url
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)