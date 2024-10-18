from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/cachetadita')
def cachetadita():
    return jsonify(message="Hola, gracias a tu error hay una cachetadita con truchita!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
