# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# import sys

# try:
#     logging.info("Exception OCCurred");

#     a= 1/"jdksajd"

# except USvisaException as e:
#     raise USvisaException(e,sys) from e

from us_visa.pipeline.training_pipeline import TrainPipeline


pipeline = TrainPipeline()
pipeline.run_pipeline()