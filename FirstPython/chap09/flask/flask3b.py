from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/')
def echo():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask3.html', thing=thing, place=place)

@app.route('/echo2/')
def echo2():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    # **kwargs는 thing=thing, place=place 처럼 작동함
    return render_template('flask3.html', **kwargs)


app.run(port=9999, debug=True)