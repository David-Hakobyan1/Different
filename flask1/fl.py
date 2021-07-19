from flask import Flask,render_template
st = "ashxarhi mec get:anapa"
s = st.split(":")
print(s)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def  hello():
    return render_template("hello.html",info=s)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
