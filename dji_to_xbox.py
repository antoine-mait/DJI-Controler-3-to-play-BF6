import hid
import vgamepad as vg
import time

DJI_VID = 0x2CA3
DJI_PID = 0x1021

# --- Axis mapping ---
def map_axis(value):
    if value == 0:
        return 0
    return int(((value - 108) / (253 - 108)) * 65535 - 32768)

def map_reverse(value):
    return -map_axis(value)

# --- HID setup ---
h = hid.device()
h.open(DJI_VID, DJI_PID)
h.set_nonblocking(True)

pad = vg.VX360Gamepad()

print("✅ DJI controller connected. Move sticks or use scroller…")

# --- Helper for button presses ---
def pressed(mask, b):
    return (b & mask) != 0

while True:
    data = h.read(64)
    if not data:
        time.sleep(0.01)
        continue

    # --- Joysticks ---
    rx = map_reverse(data[3])
    ry = map_axis(data[5])
    lx = map_reverse(data[9])
    ly = map_axis(data[7])

    pad.left_joystick(x_value=lx, y_value=ly)
    pad.right_joystick(x_value=rx, y_value=ry)

    # --- Buttons (bitmask from data[0]) ---
    b = data[0]

    if pressed(1, b): pad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else: pad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    if pressed(2, b): pad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else: pad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    if pressed(4, b): pad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else: pad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

