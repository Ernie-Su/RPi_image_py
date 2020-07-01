# Raspberry Pi image process in python

## Hardware I'm using : 

Raspberry Pi 4B with 4G RAM

Raspberry Pi Camera

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




