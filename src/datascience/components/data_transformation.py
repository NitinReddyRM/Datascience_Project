import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

## Note :- you can add different data transformation techniques such as scale, PCA and all
# you can perform all kids of EDA in ML cycle here before passing this data to the model 

# I am only adding train_test_spliting cz this data is already cleaned up
    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)

        train,test=train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)

        logger.info('Splitted the data into train and test')
        logger.info(train.shape)
        logger.info(test.shape)


        print(train.shape)
        print(test.shape)



    
