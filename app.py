from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('first.html')
@app.route('/sec')
def second():
    data=request.args.get("name")
    return f"{data}"
@app.route('/cr',methods=["post"])
def third():
    user=request.form["user"]
    password=request.form.get("password")
    print(user)
    print(password)
    return f"hello indians i am {user} and my password is {password}"
if __name__=="__main__":
    app.run(debug=True)