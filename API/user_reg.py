from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/unprotected')
def unprotected():
    return ''

@app.route('/protected')
def protected():
    return ''


@app.route('/api/v1.0/register', methods=['GET' 'POST'])
def register():
    auth = request.authorization

    if auth and auth.password == 'password':
        token =


    return make_response()


if __name__ == '__main__':
    app.run(debug=True)