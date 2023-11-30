from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/calculator')
def calcu():
    return render_template("second.html")
@app.route('/calc',methods=['post'])
def calculator():
    num1=int(request.form["num1"])
    num2=int(request.form["num2"])
    ops=request.form.get("operation")
    if ops=="Add":
        res=num1+num2
    elif ops=="Sub":
        res=num1-num2
    elif ops=="Mul":
        res=num1*num2
    else:
        res=num1/num2
    return f"Result is {res}"
if __name__=="__main__":
    app.run(debug=True)