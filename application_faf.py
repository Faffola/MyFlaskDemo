from flask import Flask, render_template, request, redirect
app_faf = Flask(__name__)

app_faf.vars={}

@app_faf.route('/index', methods=['GET','POST'])
def index_faf():
    if request.method == 'GET':
        render_template ('default.html')
    else:
        app_faf.vars['ticker'] = request.form['ticker']
        app_faf.vars['features'] = request.form['features']

    return 'request.method was not a GET!'

if __name__ == "__main__":
    app_faf.run(host='0.0.0.0')
