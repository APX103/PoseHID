# pose regressor

> 用于获取收的姿势

## get gesture

### mediapipe output

``` shell
top_gesture:  [[Category(index=-1, score=0.6962020993232727, display_name='', category_name='Open_Palm')], 
               [Category(index=-1, score=0.7948184013366699, display_name='', category_name='Open_Palm')]]
handness:  [[Category(index=1, score=0.9288433790206909, display_name='Right', category_name='Right')], 
            [Category(index=0, score=0.9481089115142822, display_name='Left', category_name='Left')]]
hand_landmarks [[NormalizedLandmark(x=0.7983127236366272, y=0.8592564463615417, z=3.735851805686252e-07, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.7063477039337158, y=0.8106436729431152, z=-0.053631994873285294, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.6315605044364929, y=0.7125087380409241, z=-0.08613883703947067, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.576614499092102, y=0.622820258140564, z=-0.11381294578313828, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.5228546857833862, y=0.5612127780914307, z=-0.1423361599445343, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.6988224983215332, y=0.5374166965484619, z=-0.06307648867368698, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.6618598699569702, y=0.41212886571884155, z=-0.09968209266662598, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.6450362801551819, y=0.32531851530075073, z=-0.1289813220500946, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.6342939734458923, y=0.2474776804447174, z=-0.15179438889026642, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.7658398747444153, y=0.5119722485542297, z=-0.06399892270565033, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.7663316130638123, y=0.3587753176689148, z=-0.09830926358699799, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.771141529083252, y=0.2607364356517792, z=-0.1248849555850029, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.7784479260444641, y=0.17534193396568298, z=-0.14515633881092072, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.8271933794021606, y=0.5295525193214417, z=-0.07065733522176743, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.8561619520187378, y=0.39535534381866455, z=-0.10770875215530396, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.8800244331359863, y=0.3051367700099945, z=-0.1377287656068802, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.8982376456260681, y=0.22251826524734497, z=-0.15822860598564148, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.8805734515190125, y=0.5774149298667908, z=-0.08122369647026062, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.9328066110610962, y=0.4842841625213623, z=-0.11171607673168182, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.966982364654541, y=0.4228142201900482, z=-0.12950585782527924, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.9916521906852722, y=0.3595851957798004, z=-0.14259368181228638, visibility=0.0, presence=0.0)], 
                [NormalizedLandmark(x=0.015271171927452087, y=0.8340616226196289, z=8.026320870158088e-07, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.11968950927257538, y=0.821951150894165, z=-0.05384239926934242, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.2043214589357376, y=0.7301610708236694, z=-0.06704332679510117, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.26581814885139465, y=0.6360896825790405, z=-0.0733448714017868, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.31527286767959595, y=0.5617136359214783, z=-0.07932562381029129, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.1590138077735901, y=0.5411259531974792, z=-0.039608974009752274, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.21880817413330078, y=0.41824984550476074, z=-0.059593018144369125, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.2537243962287903, y=0.33938759565353394, z=-0.07738904654979706, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.280991792678833, y=0.26847246289253235, z=-0.09350065141916275, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.1019575372338295, y=0.5009169578552246, z=-0.032331496477127075, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.13806313276290894, y=0.35193830728530884, z=-0.05292456969618797, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.1652100831270218, y=0.25299471616744995, z=-0.08063182979822159, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.18337827920913696, y=0.16672587394714355, z=-0.10245157778263092, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.03930105268955231, y=0.502631664276123, z=-0.03065064176917076, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.04548117518424988, y=0.3516773581504822, z=-0.061589695513248444, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.0536995604634285, y=0.2506345510482788, z=-0.099046990275383, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=0.05926071107387543, y=0.16213157773017883, z=-0.12564219534397125, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=-0.01861429214477539, y=0.5399627089500427, z=-0.03234335407614708, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=-0.04102626442909241, y=0.4422123432159424, z=-0.06864987313747406, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=-0.05578649044036865, y=0.3820079565048218, z=-0.09665652364492416, visibility=0.0, presence=0.0),
                 NormalizedLandmark(x=-0.06722646951675415, y=0.3267180323600769, z=-0.11539426445960999, visibility=0.0, presence=0.0)]]
```

> 需要说明，landmark的顺序如下

``` python
class HandLandmark(enum.IntEnum):
  """The 21 hand landmarks."""

  WRIST = 0
  THUMB_CMC = 1
  THUMB_MCP = 2
  THUMB_IP = 3
  THUMB_TIP = 4
  INDEX_FINGER_MCP = 5
  INDEX_FINGER_PIP = 6
  INDEX_FINGER_DIP = 7
  INDEX_FINGER_TIP = 8
  MIDDLE_FINGER_MCP = 9
  MIDDLE_FINGER_PIP = 10
  MIDDLE_FINGER_DIP = 11
  MIDDLE_FINGER_TIP = 12
  RING_FINGER_MCP = 13
  RING_FINGER_PIP = 14
  RING_FINGER_DIP = 15
  RING_FINGER_TIP = 16
  PINKY_MCP = 17
  PINKY_PIP = 18
  PINKY_DIP = 19
  PINKY_TIP = 20
```

### function output

在此定义一下获取的手部姿态、landmark、指尖距离等信息

``` json
{
    handness: {
        left: {
            exist: bool,
            gesture: xx,
            confidence: 0.9
        },
        right: {
            exist: bool,
            gesture: xx,
            confidence: 0.9
        },
    }
    landmarker: {
        left: [
            ···
            左手所有的点
        ],
        right: [
            ···
            右手所有的点
        ]
    },
    distance(based on image size): {
        left: {
            Left/Dis_Thumb_Index_Tip
            Left/Dis_Thumb_Middle_Tip
            Left/Dis_Index_Index_Tip
        },
        right: {
            Right/Dis_Thumb_Index_Tip
            Right/Dis_Thumb_Middle_Tip
            Right/Dis_Index_Index_Tip
        }
    },
    angle: {
        left: {
            Left/Angel_Thumb_Index_Tip
        },
        right: {
            Right/Angel_Thumb_Index_Tip
        }
    },
    process_time: "0:00"
}
```
