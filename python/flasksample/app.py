from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/param1/<name>')
def hello(name):
    return render_template('hello.html', title='flask sample', name=name)


@app.route('/param2/')
def paramtest():
    flargs = {}
    flargs['id'] = request.args.get('id')
    flargs['name'] = request.args.get('name')
    return render_template('paramtest.html', **flargs)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
