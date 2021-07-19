from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route("/x0")
def x_0():
    return render_template('x0.html')

if __name__ == "__main__":
        app.run(host='0.0.0.0',debug=True)
