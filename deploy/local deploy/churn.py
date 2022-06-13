import pandas as pd
import pickle as pkl
import inflection

class Churn():
    def __init__(self):
        self.le = pkl.load(open('pkl/le.pkl','rb'))
        self.te = pkl.load(open('pkl/te.pkl','rb'))
        self.mms = pkl.load(open('pkl/mms.pkl','rb'))
        
    def data_cleaning(self,dados):

        ## 2.1 Drop Irrelevant Features

        dados.drop('RowNumber',1,inplace=True)

        ## 2.2 Rename Values and Columns

        # CamelCase to snake_case

        # Columns
        for column in dados.columns:
            dados.rename(columns={column:inflection.underscore(column)},inplace=True)

        # Values
        for column in dados.select_dtypes('object').columns:
            dados[column] = dados[column].apply(lambda x: inflection.underscore(x))
        
        return dados
    
    def feature_engineering(self,dados):
    
        # Surname Size
        dados['surname_size'] = dados['surname'].apply(lambda x: len(x))
    
        return dados
    
    def data_filtering(self,dados):
        dados.drop(['customer_id','surname'],1,inplace=True)
        return dados
    
    def data_preparation(self,dados):

        ## 6.2 Encoding
        dados = self.te.transform(dados)
        dados['gender'] = self.le.transform(dados['gender'])

        ## 6.4 Rescaling
        columns = ['credit_score', 'geography', 'gender', 'age','tenure', 'balance', 'num_of_products', 'has_cr_card','is_active_member', 'estimated_salary', 'surname_size']
        dados = self.mms.transform(dados)
        dados = pd.DataFrame(dados,columns=columns)

        ## 6.5 Feature Selection
        cols = ['credit_score', 'geography', 'gender', 'age', 'balance', 'num_of_products', 'is_active_member','estimated_salary']
        dados = dados[cols]
        
        return dados
    
    def get_predictions(self,model,dados):
        return_data = dados.copy()
        return_data['predictions'] = model.predict(dados)
        return_data['predictions_proba'] = model.predict_proba(dados)[:,1]
        return_data = return_data.sort_values('predictions_proba',ascending=False)
        return return_data.to_json()