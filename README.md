# Raspberry Pi image process in python

## Hardware I'm using : 

* Raspberry Pi 4B with 4G RAM

* Raspberry Pi Camera

## Preparation :
### OpenCV : 

Not opencv-python but opencv, so that the whole content in git directory is complete.
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
### Gstreamer :

With OpenCV, you don't have to import gst from gi.repository in python and write a lot of codes to do pipeline. You can use cv2.VideoWriter() to write frames into a file and also a gstreamer pipeline. 

```
out = cv2.VideoWriter('appsrc ! queue ! videoconvert ! video/x-raw ! omxh264enc ! video/x-h264 ! h264parse ! rtph264pay ! udpsink host=127.0.0.0 port=5000', cv2.CAP_GSTREAMER, 0, fps, (WIDTH, HEIGHT), True)
```

WIDTH, HEIGHT and fps are variables.

After searching lots of stream receiving codes, I came up with this pipeline. In my case, I cannot send my video to the udpsink until I replaced *x264enc* with *omxh264enc*. This bothered me for a whole day.



