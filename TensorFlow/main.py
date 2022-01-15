import os
import sys

#Load Config
import config

#Import Script Modules
from scripts.preprocessing import xml_to_csv
from scripts.preprocessing import generate_pbtxt
#from scripts.preprocessing import generate_tf_record

#Generate CSV File
xml_to_csv.xml_to_csv(config.paths['TRAIN_IMAGE_PATH'], config.files['CSV_FILE'])

#Generate pbtxt
generate_pbtxt.pbtxt_from_csv(config.files['CSV_FILE'], config.files['LABELMAP'])

# #Generate train tf record
# generate_tf_record.generate_tf_record(config.paths['TRAIN_IMAGE_PATH'], config.files['LABELMAP'], config.paths['ANNOTATION_PATH'] + '\\train.record')

# #Generate test tf record
# generate_tf_record.generate_tf_record(config.paths['TEST_IMAGE_PATH'], config.files['LABELMAP'], config.paths['ANNOTATION_PATH'] + '\\test.record')

#python generate_tf_record.py -x C:\Users\alex\Documents\coding_workspace\dbd_match_analysis\dbd-vod-object-detection\TensorFlow\workspace\training\images\train -l C:\Users\alex\Documents\coding_workspace\dbd_match_analysis\dbd-vod-object-detection\TensorFlow\workspace\training\annotations\label_map.pbtxt -o C:\Users\alex\Documents\coding_workspace\dbd_match_analysis\dbd-vod-object-detection\TensorFlow\workspace\training\annotations\train.record
