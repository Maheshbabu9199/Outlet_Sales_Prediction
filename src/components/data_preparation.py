from src.utils.logger import logging
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from src.utils.utils import save_tocsv
import typing
from pathlib import Path

class DataPreparation:
    """
    this class deals with the data preparation process

    """
    def __init__(self, config):
        self.config = config


    def process(self):
        """
        this function processes the dataframe for the training and validation

        """
        df = pd.read_csv(self.config.filepath)
        
        df.drop(columns=self.config.unncessary_columns, inplace=True)
       
        X_train, X_test, y_train, y_test = self.data_split(df)

        X_train_scaled, X_test_scaled = self.data_conversion(X_train, X_test)

        X_train_scaled = pd.DataFrame(data=X_train_scaled, columns=X_train.columns.tolist())
        X_test_scaled = pd.DataFrame(data=X_test_scaled, columns=X_train.columns.tolist())

        X_train = pd.concat([X_train, y_train], axis=1)
        X_test = pd.concat([X_test, y_test], axis=1)

        save_tocsv(data = X_train, location= Path(self.config.local_folder), filename= 'train.csv')
        save_tocsv(data = X_test, location= Path(self.config.local_folder), filename= 'test.csv')

        logging.info('Data Preprocessing process completed successfully')

    
    def data_split(self, df):
        """
        this function takes the dataframe and splits it into train and test data according to the test_size in config file

        """
        
        features = df.drop(columns=[self.config.label])
        label = df[self.config.label]
        
        
        X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = self.config.test_size, random_state=0)
        return X_train, X_test, y_train, y_test


    def data_conversion(self, X_train, X_test):
        """
        this function is perform data transformation, scaling
        returns transformed, scaled data in numpy format

        """
        cat_cols = X_train.select_dtypes(include="object").columns.tolist()
        num_cols = X_train.select_dtypes(exclude="object").columns.tolist()

        label_encoder = LabelEncoder()
        scaler = StandardScaler()

        for cat_col in cat_cols:
            X_train[cat_col] = label_encoder.fit_transform(X_train[cat_col])
            X_test[cat_col] = label_encoder.transform(X_test[cat_col])
        

        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
    
        return X_train, X_test

    
        


               
