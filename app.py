from flask import Flask, render_template , redirect,request,jsonify
from main import generate_summary


app = Flask(__name__,static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert',methods=["POST"])
def convert():
    data = request.form
    data = dict(data)
    para = data['paragraph']
    top_n = int(data['topN'])
    summary = generate_summary(para,top_n-1)
    return jsonify({'summary':summary})


if __name__ ==  "__main__":
    app.run(debug=True ,port=8000)

