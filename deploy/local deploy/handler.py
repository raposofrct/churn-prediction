from flask import Flask,request,Response
from churn import Churn
import os
import pickle as pkl
import pandas as pd

app = Flask(__name__)
@app.route('/predict',methods=['POST'])

def predict():
    model = pkl.load(open('pkl/model.pkl','rb'))
    json = request.get_json()
    if json:
        dados = pd.DataFrame(json)
        dados = Churn().data_cleaning(dados)
        dados = Churn().feature_engineering(dados)
        dados = Churn().data_filtering(dados)
        dados = Churn().data_preparation(dados)
        return Churn().get_predictions(model,dados)
    else:
        return Response('{}',status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=os.environ.get('PORT',8080),debug=False)