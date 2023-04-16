# Config

> 本目录用于存放config, 这里介绍姿态和操作的定义，以及config写法

## 姿态

1. 能识别的姿态目前共计7种 [i.e. 👍, 👎, ✌️, ☝️, ✊, 👋, 🤟]
   1. Closed_Fist
   2. Open_Palm
   3. Pointing_Up
   4. Thumb_Down
   5. Thumb_Up
   6. Victory
   7. ILoveYou
2. 能计算的距离的目前共计2种
   1. 食指和拇指的距离(Dis_Thumb_Index_Tip)
   2. 中指和拇指的距离(Dis_Thumb_Middle_Tip)
   3. 食指指尖之间的距离(Dis_Index_Index_Tip)
3. 能计算角度的共计1种
   1. 食指与拇指连线的角度(Angel_Thumb_Index_Tip)

## 姿势语义定义

### 要点

1. 先左手后右手
2. 使用加号(+)连接
3. 左手的姿势添加`Left/`前缀, 右手的姿势添加`Right/`前缀
4. 目前的建议是左手的1种手势用于1种操作，也就是说，目前最好仅仅支持`7`种操作

### 语义定义

> 语义可扩展

1. 左手选择功能，右手实现逻辑
2. 双手同时实现一个功能(直接映射，手势部保持时失效)
3. 双手确定某种功能，则双手都能在之后实现逻辑，然后双手关闭它(需要设计，否则会很难)

惯用1,2

## 操作

> 由于操作的实时性，不建议、也暂时没有设置键盘敲击映射，如有需求可扩展

1. 键盘长按/组合键盘长按(动作结束之后自动松开)
2. 鼠标移动
3. 鼠标按住
4. 快捷键组合

### 操作的尺度

对于需要尺度(参数)的操作，使用`|`分隔操作与尺度(参数)

## Config 写法

1. json格式，由`map`和`lock`定义
2. `lock`中定义了是否开启锁，开锁和关锁的快捷键定义
3. `map`定义了pose => operation的映射
   1. 左手单一姿势确认种类
   2. 右手动作需与左手姿势配合才能定义
4. 以下是demo

``` json
{
    "map": {
        "Left/Open_Palm": "mouse_move|1000",
        "Left/Open_Palm+Right/Dis_Thumb_Index_Tip": "mouse_press_left|50",
        "Left/Open_Palm+Right/Dis_Thumb_Middle_Tip": "mouse_press_right|50"
    },
    "lock": {
        "on": true,
        "lock": "Left/Closed_Fist+Right/Closed_Fist",
        "unlock": "left/Thumb_Up+Right/Thumb_Up"
    }
}
```
