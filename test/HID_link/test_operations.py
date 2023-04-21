from pose_hid.HID_link.operations import Operations


def test_mouse_move():
    op = Operations()
    op.mouse_move(100, 100)
    # # Test passed bellow
    # op.mouse_click(100, 100, 1)
    # op.mouse_click(1000, 500, 1, 'right')


