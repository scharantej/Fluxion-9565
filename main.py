
from flask import Flask, render_template, request

app = Flask(__name__)

blocks = []

@app.route('/')
def index():
    return render_template('index.html', blocks=blocks)

@app.route('/build_block', methods=['POST'])
def build_block():
    block = request.form['block']
    blocks.append(block)
    return '', 204

@app.route('/dissolve_block', methods=['POST'])
def dissolve_block():
    block = request.form['block']
    blocks.remove(block)
    return '', 204

if __name__ == '__main__':
    app.run()
