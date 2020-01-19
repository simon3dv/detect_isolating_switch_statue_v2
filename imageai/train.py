from imageai.Detection.Custom import DetectionModelTrainer

names = ['on','off']
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory='dataset')
trainer.setTrainConfig(object_names_array=names, batch_size=4, num_experiments=100, train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()
