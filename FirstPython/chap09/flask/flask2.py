from flask import Flask, render_template

app = Flask(__name__)

@app.route('/echo/<thing>')
def echo(thing):
    '''jinja2 템플릿 시스템으로 렌더링'''
    return render_template('flask2.html', thing=thing)

app.run(port=9999, debug=True)