import time

from pose_hid.HID_link.operations import Operations


def test_mouse_move():
    op = Operations()
    op.mouse_move(0.5, 0.5)
    print(op.screen_size)
    # # Test passed bellow
    # op.mouse_click(100, 100, 1)
    # op.mouse_click(1000, 500, 1, 'right')


def test_mouse_press():
    op = Operations()
    op.mouse_press("right")
    op.mouse_release("right")


def test_mouse_press_with_sleep():
    op = Operations()
    op.mouse_press("right")
    time.sleep(1)
    op.mouse_release("right")
    op.mouse_press("left")
    time.sleep(1)
    op.mouse_release("left")


def test_mouse_drag():
    op = Operations()
    time.sleep(1)
    op.mouse_press("left")
    op.mouse_move(0.5, 0.5)
    time.sleep(2)
    op.mouse_release("left")

