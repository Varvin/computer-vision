# computer-vision homework 10

[Results and data](https://drive.google.com/file/d/1Ywf0TzrHV7bmbT2EgWJKFf_Dhz-VQDxt/view?usp=sharing)

Video Fields.mp4:

Tracking by each frame

![img](https://drive.google.com/uc?export=view&id=1ibjY4U14iJr1CZ_Ey__8j9k1w1XP4L_o)

Tracking by every 3rd frame

![img](https://drive.google.com/uc?export=view&id=1s2nK75RKRBLEn9j62BmRq11wfc-o8M1p)

Tracking by every 7 frame

![img](https://drive.google.com/uc?export=view&id=1FlKsPxwxa7xyEU_3W7tTsTH0TPMZWftm)

Video Escalator.mp4:

Tracking by each frame

![img](https://drive.google.com/uc?export=view&id=1yn4gKNakrs9ZbveQcZJxiE7q-aCO2yMn)

Tracking by every 3rd frame

![img](https://drive.google.com/uc?export=view&id=12wziXMka1ToYdjO_ZQYalpjsfPUkwRcl)

Tracking by every 7 frame

![img](https://drive.google.com/uc?export=view&id=1elcXBlkRzoCWSa98TW6aHO-mGaXMqGaU)

Video Track.mp4:

Tracking by each frame

![img](https://drive.google.com/uc?export=view&id=1mKM2Q2yErRYOv_NR_W0qDTHfyc6Twr2W)

Tracking by every 3rd frame

![img](https://drive.google.com/uc?export=view&id=1xWEVR6QZ2gvwM_zYlS1dIEG6yWMN2_q2)

Tracking by every 7 frame

![img](https://drive.google.com/uc?export=view&id=11wH6oTjsr3ZR-LYONCGiE7GJyjuw9Cbt)

* Do you see any differences? If so, what are they?

    All trackers work fine when tracking per frame. When tracking for every 3 or 7 frames, some of the object is being tracked or the tracking accuracy is falling.

* Does one tracker perform better than the other? In what way?

    The MIL tracker worked best of all, but it does not change the size bounding box, the CSRT tracker also copes well, but when tracking a fast moving object, it points to false places, the KCF tracker loses the object during non-frame-by-frame processing and after that it cannot find the object
