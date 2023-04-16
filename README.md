# PoseHID

> base on mediapipe's hand pose regression

## key point

1. mediapipe(0.9.1.0)
2. pyautogui(0.9.53)

## Arch

基于mediapipe的手部关键点检测 + 姿势回归

基于python库 | 基于tflite转onnx | 基于前者再转TensorRT

+++++++++++++++++++++++++++++++++++++

基于姿态解算 的 机器操作

PC | 带GPU的PC | Jetson和RPI4 | 其他不带操作系统、不带python、不能上tf的平台

+++++++++++++++++++++++++++++++++++++

基于HID模拟的模拟USB + 模拟键盘组合键

使用外部简易可配置的配置文件完成 姿态组合 => 机器操作 的映射

## 技术选项

> 目前只走能运行python, tf, mediapipe的路线

1. 使用mediapipe完成手部关键点捕捉 + 姿态回归
2. 使用pyautogui完成python控制键盘和鼠标
