# PoseHID

> hand pose control PC or some other thing (I mean anything)

## key point

1. mediapipe(0.9.3.0)
2. pyautogui(0.9.53)

## Architecture

``` log

    hand landmark detect and gesture regression based on `mediapipe`

      |   python   |   tflite  |  onnx(tf2onnx)  |  TensorRT  |

-----------------------------------------------------------------------------

              operation based on hand pose & landmark

PC | PC with GPU | Jetson | RPI4 | some other device without python or linux

-----------------------------------------------------------------------------

    mouse and keyboard simulation based on HID(Human Interface Device)

          map Pose to Operation, based on a json config file
```

## Technology Selection

### PC(Windows)

> python + mediapipe

1. Get hand landmark and gesture by `mediapipe`
2. Control mouse and keyboard using `pyautogui`

## Limitations

1. `pyautogui` not work on `Ubuntu` OS.
