from imageai.Detection.Custom import DetectionModelTrainer

dataset_name = 'dataset'
names = ['on','off']
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory=dataset_name)
metrics = trainer.evaluateModel(model_path=dataset_name+"/models", json_path=dataset_name+"/json/detection_config.json", iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)
print(metrics)
