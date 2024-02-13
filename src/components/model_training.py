from src.utils.logger import logging
from src.utils.utils import create_directory, save_models
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
import pandas as pd


class ModelTraining:
    def __init__(self,config):
        self.config = config

    
    def create_models(self):
        linear = LinearRegression()
        lasso = Lasso()
        ridge = Ridge()
        elasticnet = ElasticNet(alpha=self.config.alpha, l1_ratio = self.config.l1_ratio)

        return linear, lasso, ridge, elasticnet

    def process(self):

        linear, lasso, ridge, elasticnet = self.create_models()

        train_data = pd.read_csv(self.config.filepath)

        train_features, train_labels = train_data.drop(columns=['Item_Outlet_Sales']), train_data['Item_Outlet_Sales']

        linear.fit(train_features, train_labels) 
        lasso.fit(train_features, train_labels)
        ridge.fit(train_features, train_labels)
        elasticnet.fit(train_features, train_labels)

        create_directory(self.config.models_path)

        save_models(linear, 'linear', self.config.models_path)
        save_models(lasso, 'lasso', self.config.models_path) 
        save_models(ridge, 'ridge', self.config.models_path)
        save_models(elasticnet, 'elasticnet', self.config.models_path)  
