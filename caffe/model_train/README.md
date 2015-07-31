#Multi-label CNN Caffe Model Training

###Dependence
* [caffe](http://caffe.berkeleyvision.org/) installed
* google_net or other pre-trained model installed, [ImageNet example](http://caffe.berkeleyvision.org/gathered/examples/imagenet.html)

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
