# Object Color Recognization 

### Algorithm used : Yolo algorithm for detection + Opencv used to identify object color
### Backend : opencv
### Library required:

- opencv = 4.5.4-dev'

### IMPORTANT:

- I hadn't uploaded model weights and configuration file because that is already available in yolo_detection repo
- download those files from here : [https://github.com/hasit73/yolo_detection]
- For detection i was using same code that is available in yolo_detection repo.

# Quick Overview about structure

#### 1) main.py

- Loading model and user configurations
- perform interfacing tasks


#### 2) yolo.py

- use opencv modules to detect objects from user given media(photo/video)
- detection take place inside this file


#### 3) config.json

- user configuration are mentioned inside this file
- for examples : input shapes and model parameters(weights file path , config file path etc) are added in config.json


#### 4) color_identification.json

- recognize object color
- it uses HSV color range to identify object color
- this module is also implemented using opencv

# How to use 

1) clone this directory

 
2) use following command to run detection on your custom video

  ```
  python main.py -c config.json -v <media_path>
  ```

  Example: 
  ```
  python main.py -c config.json -v car1.mp4
  ```
  
- Note : Before executing this command ensure that you had downloaded model weights and config file.

### Results

![colo1](https://user-images.githubusercontent.com/69752829/141614750-7fba0507-3802-49a6-9459-e3fcac7e72af.PNG)

![colo2](https://user-images.githubusercontent.com/69752829/141614752-c3b3a451-ebcb-4672-91c2-63823fac3004.PNG)

![colo3](https://user-images.githubusercontent.com/69752829/141614755-7571524e-dc97-45a1-9b42-ea713868f13f.PNG)

![colo4](https://user-images.githubusercontent.com/69752829/141614761-4a8b0e55-550f-4add-899c-031ac6fee186.PNG)


## If it's helful for you then please give star :)
