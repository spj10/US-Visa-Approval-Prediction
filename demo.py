#from us_visa.logger import logging
#from us_visa.exception import USvisaException
#import sys

'''
try:
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys) from e
'''

from us_visa.pipline.training_pipeline import TrainPipeline


pipline  = TrainPipeline()
pipline.run_pipeline()