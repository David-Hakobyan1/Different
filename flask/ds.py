from flask import Flask,render_template,url_for,request

app = Flask(__name__)

with open("file.txt") as f:
    fc = f.read().strip().split(",")


@app.route("/")
@app.route('/home')
def nk():
    return render_template('boks.html',fc=fc)

if __name__ == "__main__":
    app.run(debug=True)

