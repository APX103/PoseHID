# Plan

> This is plans to implement pose hid operation mapping

## A known

1. Use opencv capture pics from camera
2. Use mediapipe get hands/hands' keypoint/hands' gesture
3. Get 30 pics per seconds, pose data are highly variable, need noise reduction 

## Plans of implementation

### OP directly

1. Every frame can get an operation.
2. If it triggers, it won't trigger again for the next half second.

### OP buffer

1. A buffer of gesture in a time region. (slide window)
2. If triggers more than 50%(**hyperparameter**) in buffer (slide window), trigger. 
