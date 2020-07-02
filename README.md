# Raspberry Pi image process in python

## Hardware I'm using : 

* Raspberry Pi 4B with 4G RAM

* Raspberry Pi Camera

## Preparation :
### OpenCV : 
* Simple but not complete way :

Can be installed on Windows and MacOS.

```
pip3 install opencv-python
pip3 install opencv_contrib-python
```

* Complex but complete way :
1. To avoid errors during compiling, it's recommended to increase the swapfile size.
```sudo vi /etc/dphys-swapfile``` and change ```CONF_SWAPSIZE=100``` to ```CONF_SWAPSIZE=2048```

2. Reboot swapfile service.
```
sudo /etc/init.d/dphys-swapfile  stop
sudo /etc/init.d/dphys-swapfile  start
```
You can use ```htop``` to check whether the swap size is incresed to 2048

3. Install packages and libraries.
```
sudo apt-get install build-essential cmake
sudo apt-get install libjpeg-dev libpng-dev libtiff5-dev libjasper-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev libcanberra-gtk*
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install at-spi2-core
sudo apt-get install python-dev python3-dev
pip install numpy
pip3 install numpy
```
Check whether there's no error during the installation.

4. Download the source code of OpenCV
```
mkdir opencv
cd opencv
wget https://github.com/opencv/opencv/archive/master.zip
wget https://github.com/opencv/opencv_contrib/archive/master.zip

unzip master.zip
unzip master.zip1

cd opencv-master
mkdir build
cd build
```

5. Excute cmake.
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv/opencv_contrib-master/modules \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D WITH_TBB=ON \
-D WITH_OPENMP=ON \
-D BUILD_TESTS=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D BUILD_EXAMPLES=OFF \
-D OPENCV_EXTRA_EXE_LINKER_FLAGS=-latomic \
-D PYTHON_EXECUTABLE=/usr/bin/python3 \
-D PYTHON_EXECUTABLE=/usr/bin/python \
..
```
Check two places in the finish message. First, ```Non-free algorithm``` returns YES. Second, Python 2 and Python 3 do exist in the message.

6. Compile under /build. This may take around 50 minutes to finish.
```
make -j4
```
If no error ocurred, we can install it now.
```
sudo make install
sudo ldconfig
cd python_loader
sudo python setup.py install
sudo python3 setup.py install
```

7. Try to import cv2 in python
```
$ python3
>>> import cv2
>>> cv2.__version__
'4.4.0-pre'
```

### Gstreamer :

With OpenCV, you don't have to ```import gst from gi.repository``` in python and write a lot of codes to do pipeline. You can use cv2.VideoWriter() to write frames into a file and also a gstreamer pipeline. 

```
out = cv2.VideoWriter('appsrc ! queue ! videoconvert ! video/x-raw ! omxh264enc ! video/x-h264 ! h264parse ! rtph264pay ! udpsink host=127.0.0.0 port=5000', cv2.CAP_GSTREAMER, 0, fps, (WIDTH, HEIGHT), True)
```

WIDTH, HEIGHT and fps are variables.

After searching lots of stream receiving codes, I came up with this pipeline. In my case, I cannot send my video to the udpsink until I replaced *x264enc* with *omxh264enc*. This bothered me for a whole day.



