import pickle
from flask import Flask, request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

## import ridge regressor model and standard scaleer pickle
ridge_model=pickle.load(open('Models/ridge.pkl','rb'))
Standard_Scaler=pickle.load(open('Models/scaler.pkl','rb'))

##Rout for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
       Temperature =float(request.form.get('Tempearture'))
       RH =float(request.form.get('RH'))
       Ws =float(request.form.get('Ws'))
       Rain =float(request.form.get('Rain'))
       FFMC =float(request.form.geet('FFMC'))
       ISI =float(request.form.geet('ISI'))
       Classes =float(request.form.geet('Classes'))
       Region =float(request.form.geet('Region'))
       
       new_data_scaled= Standard_scalr.transform([[Tempearture,RH,Ws, Rain,FFMC,DMC,ISI,Classes,Region]])
       result= ridge_model.predict(new_data_scaled)

       return render_template('home.html', result=result[0])
        
    else:

       return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
