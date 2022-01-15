import os
import sys

#Load Config
import config

#Import Script Modules
from scripts.preprocessing import xml_to_csv
from scripts.preprocessing import generate_pbtxt
from scripts.preprocessing import generate_tf_record

#Generate CSV File
xml_to_csv.xml_to_csv(config.paths['TRAIN_IMAGE_PATH'], config.files['CSV_FILE'])

#Generate pbtxt
generate_pbtxt.pbtxt_from_csv(config.files['CSV_FILE'], config.files['LABELMAP'])

#Generate tf record


