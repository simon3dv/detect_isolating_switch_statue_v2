#README.md
Use  [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet) to detect

## How to use
### 1.download data and pretrained models
from https://pan.baidu.com/s/1pD4qYmq0mzd-ULaVZ81Bfw
(code:2yzg)

and organize as follows:
```
darknet
├── backup
│   ├── my_yolov3-tiny_obj_final.weights
│   ├── yolo-obj_final.weights(optional)
├── obj
├── obj_resized
├── obj_resized_detected
├── train.txt
├── validation.txt
├── validation_resized.txt
```
 
2.git clone AlexeyAB/darknet
```
cd darknet
git clone https://github.com/AlexeyAB/darknet.git
cd darknet
```
3.follow README.md on [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)

specifically,

3-1. install dependecies following https://github.com/AlexeyAB/darknet#requirements
3-2. compile
```
# for example, compile CPU version on Linux(using make)
make
```
```
# for example, compile on Linux(using cmake)
mkdir build-release
cd build-release
cmake ..
make
make install
```
After compiling, test if success
```
./darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg ./yolov3.weights
```
3-3. run yolo-v3
See "How to use" on [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet#how-to-use-on-the-command-line)
You can detect from images, videos, webcam etc.
Here is an example of detect from images:
```
#yolov3-tiny(CPU:650ms, 1080ti:2ms)
./darknet detector test ../obj.data ../yolov3-tiny_obj.cfg ../backup/my_yolov3-tiny_obj_final.weights -ext_output ../obj/IMG_20200108_163825.jpg -thresh 0.4
```
```
#yolov3(CPU:22000ms, 1080ti:30ms)
./darknet detector test ../obj.data ../yolo-obj.cfg ../backup/my-yolo-obj_final.weights -ext_output ../obj/IMG_20200108_163825.jpg -thresh 0.4
```

Then you can see
```
(torch1.3tf2.0cu100) aming@aming-All-Series:/media/aming/2400391B0038F580/RGB/detect_isolating_switch_statue_v2/darknet/darknet$ ./darknet detector test ../obj.data ../yolov3-tiny_obj.cfg ../backup/my_yolov3-tiny_obj_final.weights -ext_output ../obj/IMG_20200108_163825.jpg
 OpenCV isn't used 
batch = 1, time_steps = 1, train = 0 
   layer   filters  size/strd(dil)      input                output
   0 conv     16       3 x 3/ 1    416 x 416 x   3 ->  416 x 416 x  16 0.150 BF
   1 max                2x 2/ 2    416 x 416 x  16 ->  208 x 208 x  16 0.003 BF
   2 conv     32       3 x 3/ 1    208 x 208 x  16 ->  208 x 208 x  32 0.399 BF
   3 max                2x 2/ 2    208 x 208 x  32 ->  104 x 104 x  32 0.001 BF
   4 conv     64       3 x 3/ 1    104 x 104 x  32 ->  104 x 104 x  64 0.399 BF
   5 max                2x 2/ 2    104 x 104 x  64 ->   52 x  52 x  64 0.001 BF
   6 conv    128       3 x 3/ 1     52 x  52 x  64 ->   52 x  52 x 128 0.399 BF
   7 max                2x 2/ 2     52 x  52 x 128 ->   26 x  26 x 128 0.000 BF
   8 conv    256       3 x 3/ 1     26 x  26 x 128 ->   26 x  26 x 256 0.399 BF
   9 max                2x 2/ 2     26 x  26 x 256 ->   13 x  13 x 256 0.000 BF
  10 conv    512       3 x 3/ 1     13 x  13 x 256 ->   13 x  13 x 512 0.399 BF
  11 max                2x 2/ 1     13 x  13 x 512 ->   13 x  13 x 512 0.000 BF
  12 conv   1024       3 x 3/ 1     13 x  13 x 512 ->   13 x  13 x1024 1.595 BF
  13 conv    256       1 x 1/ 1     13 x  13 x1024 ->   13 x  13 x 256 0.089 BF
  14 conv    512       3 x 3/ 1     13 x  13 x 256 ->   13 x  13 x 512 0.399 BF
  15 conv     21       1 x 1/ 1     13 x  13 x 512 ->   13 x  13 x  21 0.004 BF
  16 yolo
[yolo] params: iou loss: mse (2), iou_norm: 0.75, cls_norm: 1.00, scale_x_y: 1.00
  17 route  13 		                           ->   13 x  13 x 256 
  18 conv    128       1 x 1/ 1     13 x  13 x 256 ->   13 x  13 x 128 0.011 BF
  19 upsample                 2x    13 x  13 x 128 ->   26 x  26 x 128
  20 route  19 8 	                           ->   26 x  26 x 384 
  21 conv    256       3 x 3/ 1     26 x  26 x 384 ->   26 x  26 x 256 1.196 BF
  22 conv     21       1 x 1/ 1     26 x  26 x 256 ->   26 x  26 x  21 0.007 BF
  23 yolo
[yolo] params: iou loss: mse (2), iou_norm: 0.75, cls_norm: 1.00, scale_x_y: 1.00
Total BFLOPS 5.449 
Loading weights from ../backup/my_yolov3-tiny_obj_final.weights...
 seen 64, trained: 256 K-images (4 Kilo-batches_64) 
Done! Loaded 24 layers from weights-file 
../obj/IMG_20200108_163825.jpg: Predicted in 654.199000 milli-seconds.
on: 100%	(left_x: 1628   top_y:  583   width: 2143   height:  718)
on: 100%	(left_x: 1748   top_y: 2094   width: 1565   height:  625)
Not compiled with OpenCV, saving to predictions.png instead
```


