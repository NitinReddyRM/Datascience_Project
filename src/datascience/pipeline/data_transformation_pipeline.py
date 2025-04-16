from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME="Data Ingestion stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),'r') as f:
                status=f.read().split(' ')[-1]
            if status==True:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
        except Exception as e:
            raise Exception('Your data scheme is not valid')

if __name__=='__main__':
	try:
		logger.info(f'>>>>>>> stage{STAGE_NAME} started <<<<<')
		obj=DataTransformationTrainingPipeline()
		obj.initiate_data_transformation()
		logger.info(f'>>>>>>> stage {STAGE_NAME} Completed <<<<<\n\nx=======================x')
	except Exception as e:
		logger.exception(e)
		raise e
