from flask import flask,request,render_template
import numpy as np
import pandas as pd 
import pickle
import os
mode1 = pickle.load(open('flight.pkl','rb'))
app = flask(__name__)
@app.route('/')
def home():
return render_template("index.html")

@app.route('/prediction',methods =['POST'])
def predict():
    name = request.from['name']
    month = render.form['month']
    dayofmonth = request.form['dayofmonth']
    dayofweek = request.form['dayofweek']
    origin = request.form['origin']
    if(origin == "msp"):
        origin,origin2,origin3,origin4,origin5 = 0,0,0,0,1
    if(origin == "dtw"):
        origin,origin2,origin3,origin4,origin5 = 1,0,0,0,0
    if(origin == "jfw"):
        origin,origin2,origin3,origin4,origin5 = 0,0,1,0,0
    if(origin == "sea"):alt
        origin,origin2,origin3,origin4,origin5 = 0,1,0,0,0
    if(origin == "alt"):
        origin,origin2,origin3,origin4,origin5 = 0,0,0,1,0
    destination = request.form['destination']
    if(destination == "msp"):
        destination,destination2,destination3,destination4,destination5 = 0,0,0,0,1
    if(destination == "dtw"):
        destination,destination2,destination3,destination4,destination5 = 1,0,0,0,0
    if(destination == "jfk"):
        destination,destination2,destination3,destination4,destination5 = 0,0,1,0,0
    if(destination == "sea"):
        destination,destination2,destination3,destination4,destination5 = 0,1,0,0,0
    if(destination == "alt"):
        destination,destination2,destination3,destination4,destination5 = 0,0,0,1,0
    dept = request.form['dept']
    arrtime = request.form['arrtime']
    actdept = request.form['actdept']
    dept15=int(dept)-int(actdept)
    total = [[name,month,dayofmonth,dayofweek,origin,origin2,origin3,origin4,origin5,destination1,destination2,destination3,destination4,destination5]]
    y_pred = model.predict(total)
    print(y_pred)
    
    if(y_pred==[0.]):
        ans="The Flight be on time"
    else:
        ans="The Flight will be delayed"
    return render_template("index.html",showcase = ans)