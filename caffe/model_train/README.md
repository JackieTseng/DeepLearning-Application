#Multi-label CNN Caffe Model Training

###Dependence
* [caffe](http://) installed
* google_net or other pre-trained model installed, [example](http://)

###Model Adjustment (mark following TODO comment)
* include/data_layers.hpp
* models/bvlc_googlenet/jd_solver.prototxt
* models/bvlc_googlenet/jd_train_val.prototxt
* src/layers/my_image_data_layer.cpp
* src/layers/accuracy_layer.cpp
* src/proto/caffe.proto

###Run Model-training
* Setting right: label_file.txt and source picture files
```
./build/tools/caffe train --solver=models/bvlc_googlenet/jd_solver.prototxt
```
* Continue training with existing model : set right the file path
```
./train_quick.sh
```

###Fix Bugs
* Exception handling when picture read is broken or no-exist
* Reduce the batch size of train or test when memory limited
