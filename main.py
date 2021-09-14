def on_gesture_tilt_right():
    basic.show_icon(IconNames.SMALL_HEART)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_a():
    basic.show_icon(IconNames.CHESSBOARD)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_icon(IconNames.SWORD)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
