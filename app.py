from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials,db

#initialize Flaskapp
app = Flask(__name__)

#firebase sonfig
cred=credentials. Certificate("D:/python1.0/python-cloud-computing-firebase-adminsdk-fbsvc-f1c0fed44f.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://python-cloud-computing-default-rtdb.firebaseio.com/"})
@app.route('/',methods=['GET','POST'])
def calculator():
    result=' '
    if request.method=="POST":
        num1=float(request.form['num1'])
        num2=float(request.form['num2'])
        op=request.form['operation']
        
        if op=='add':
            result=num1+num2
            operation=f"{num1}+{num2}={result}"
        elif op=="sub":
            result=num1-num2
            operation=f"{num1}-{num2}={result}"
        elif op=="mul":
            result=num1*num2
            operation=f"{num1}*{num2}={result}"
        elif op=="div":
            result=num1/num2 if num2 !=0 else "Error"
            operation=f"{num1}/{num2}={result}"
        
        #push to firebase realtime database
        if result !="Error":
            ref=db.reference("calculations")
            ref.push({"result":result,
                      "operation":operation})
    return render_template("index.html",result=result)

#run the app   
if __name__=='__main__':
 app.run(debug=True)