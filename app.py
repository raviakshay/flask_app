from flask import Flask,render_template,request,flash
app=Flask(__name__)
app.secret_key="pass1"
@app.route('/home')
def index():
    flash("What's your name?")
    return render_template("index.html")
@app.route('/greet',methods=['post','get'])
def greet():
    flash('HI '+str(request.form['name'])+', Great to see you')
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)