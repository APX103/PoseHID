# Config

> put config in this dir. I introduce the definition of attitude and operation here, as well as the syntax of the configuration.

## Pose

1. 7 poses can be detected [i.e. 👍, 👎, ✌️, ☝️, ✊, 👋, 🤟]
   1. Closed_Fist
   2. Open_Palm
   3. Pointing_Up
   4. Thumb_Down
   5. Thumb_Up
   6. Victory
   7. ILoveYou
2. 3 kinds of distance
   1. Distance between thumb and index finger(Dis_Thumb_Index_Tip)
   2. Distance between thumb and middle finger(Dis_Thumb_Middle_Tip)
   3. Distance between index and index finger(Dis_Index_Index_Tip)
3. 1 kind of angle
   1. Angle between thumb and index finger(Angel_Thumb_Index_Tip)

## Affordance semantics definition.

### Keypoint

1. Left to Right
2. concat with `+`
3. Left hand gesture add `Left/` prefix, Right hand gesture add `Right/` prefix
4. Currently, the recommendation is that one gesture of the left hand is used for one operation. Therefore, it is best to support only 7 operations at present.

### Semantics definition

> Currently, the following semantics are defined, and support for semantic extension is provided.

1. Left hand operates the function, right hand implements the logic.
   1. for example, left hand `Open_Palm` means mouse simulation, right hand wrist point(`Right/Wrist`) present position
2. Both hands achieve the same function simultaneously.
3. If both hands determine a certain function, both hands can implement the logic after that, and then both hands can close it.

using 1,2 yet

## Operations

> Due to the real-time nature of the operation, it is not recommended and there is no need to set keyboard keystroke mapping at present. If there is a demand, it can be expanded.

1. mouse move
2. mouse press
3. keyboard input combination

### Operation scale

Operations always need a scale，split op and scale with `|`

## Config Syntax

1. yaml format，define with `pose` and `op`
2.  demo as follows

``` yaml
Left/Open_Palm: mouse_move|1000
Left/Open_Palm+Right/Dis_Thumb_Index_Tip: mouse_press_left|30
Left/Open_Palm+Right/Dis_Thumb_Middle_Tip: mouse_press_right|30
Left/Closed_Fist+Right/Closed_Fist: lock
Left/Thumb_Up+Right/Thumb_Up: unlock
```
