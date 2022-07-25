# Drone-Detection-Neuronet-Training

Решение задачи покадрового обнаружения объекта осуществлялось с помощью обучения нейросети.

Обучение нейросети и сам процесс обнаружения написан на языке Python 3.7 в среде PyCharm с помощью библиотек машинного обучения и компьютерного зрения -- Tensorflow и ImageAI соответственно. Для их установки использовались система упраления пакетами pip и дистирибутив anaconda.

Команды терминала для установки библиотек и зависимостей:
```
pip install tensorflow-gpu==2.4.0
```
Или
```
pip install tensorflow==2.4.0
```
В зависимости от возможности компьютера осуществлять обучение, используя графический процессор. Для этого требуется архитектура параллельных вычислений CUDA (версии 11.0) а так же cuDNN (версии 8.0):
```
conda create --name tf python=3.7
conda activate tf
conda install -c conda-forge cudatoolkit=11.0 cudnn=8.0
```
![image](https://user-images.githubusercontent.com/103249547/180806660-21401264-5aa9-4974-8cd1-ec0a156d0b97.png)

Другие зависимости ImageAI:
```
pip install keras==2.4.3 numpy==1.19.3 pillow==7.0.0 scipy==1.4.1 h5py==2.10.0 matplotlib==3.3.2 opencv-python keras-resnet==0.2.0
```
И установка самого ImageAI:

```
pip install imageai --upgrade
```
