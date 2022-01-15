import os

CUSTOM_MODEL_NAME = 'dbd_efficient_det'
PRETRAINED_MODEL_NAME = 'efficientdet_d3_coco17_tpu-32'
PRETRAINED_MODEL_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d3_coco17_tpu-32.tar.gz'
TF_RECORD_SCRIPT_NAME = 'generate_tfrecord.py'
CSV_FILE_NAME = 'csv_output.csv'
LABEL_MAP_NAME = 'label_map.pbtxt'

paths = {
    'WORKSPACE_PATH': os.path.join('workspace', 'training'),
    'SCRIPTS_PATH': os.path.join('scripts', 'preprocessing'),
    'APIMODEL_PATH': os.path.join('models'),
    'ANNOTATION_PATH': os.path.join('workspace', 'training', 'annotations'),
    'IMAGE_PATH': os.path.join('workspace', 'training', 'images'),
    'TRAIN_IMAGE_PATH': os.path.join('workspace', 'training', 'images', 'train'),
    'TEST_IMAGE_PATH': os.path.join('workspace', 'training', 'images', 'test'),
    'MODEL_PATH': os.path.join('workspace', 'training', 'models'),
    'PRETRAINED_MODEL_PATH': os.path.join('workspace', 'training', 'pre-trained-models'),
    'CHECKPOINT_PATH': os.path.join('workspace','training', 'models',CUSTOM_MODEL_NAME), 
    'OUTPUT_PATH': os.path.join('workspace','models',CUSTOM_MODEL_NAME, 'export'), 
    'PROTOC_PATH':os.path.join('protoc')
 }

files = {
    'PIPELINE_CONFIG':os.path.join('workspace', 'training', 'models', CUSTOM_MODEL_NAME, 'pipeline.config'),
    'TF_RECORD_SCRIPT': os.path.join(paths['SCRIPTS_PATH'], TF_RECORD_SCRIPT_NAME),
    'CSV_FILE': os.path.join(paths['SCRIPTS_PATH'], CSV_FILE_NAME), 
    'LABELMAP': os.path.join(paths['ANNOTATION_PATH'], LABEL_MAP_NAME)
}