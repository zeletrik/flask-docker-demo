from flask import Flask, Blueprint, request, Response

app = Flask(__name__)

# Index
@app.route('/', methods=['GET'])
def app_index():
    return 'Hello World'
