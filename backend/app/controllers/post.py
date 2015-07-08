from flask import Flask
app = Flask('Djangyll')

@app.route('/post')
def get():
    return 'Hello World!'

