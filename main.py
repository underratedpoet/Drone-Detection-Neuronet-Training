from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="drone")

trainer.setTrainConfig(object_names_array=["drone"], batch_size=4, num_experiments=30,
 train_from_pretrained_model="detection_model-ex-030--loss-0013.333.h5")

trainer.trainModel()

# from imageai.Detection.Custom import CustomVideoObjectDetection
# import os
#
# execution_path = os.getcwd()
#
# video_detector = CustomVideoObjectDetection()
# video_detector.setModelTypeAsYOLOv3()
# video_detector.setModelPath("detection_model-ex-013--loss-0012.549.h5")
# video_detector.setJsonPath("detection_config.json")
# video_detector.loadModel()
#
# video_detector.detectObjectsFromVideo(input_file_path="drone5.mp4",
#                                           output_file_path=os.path.join(execution_path, "detected5"),
#                                           frames_per_second=20,
#                                           minimum_percentage_probability=40,
#                                           log_progress=True)