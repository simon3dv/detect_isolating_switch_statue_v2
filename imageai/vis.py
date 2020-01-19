from imageai.Detection.Custom import CustomObjectDetection
import os 
dataset_name = 'dataset'
model_name = 'detection_model-ex-043--loss-0005.352.h5'
input_dir = 'dataset/validation/images'
input_images =  os.listdir(input_dir)
output_dir = 'dataset/validation_detected'
detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(dataset_name+"/models/"+model_name)
detector.setJsonPath(dataset_name+"/json/detection_config.json")
detector.loadModel()
for i,image_name in enumerate(input_images):
    detections = detector.detectObjectsFromImage(input_image=input_dir+"/"+image_name, output_image_path=output_dir+'/'+image_name)
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

