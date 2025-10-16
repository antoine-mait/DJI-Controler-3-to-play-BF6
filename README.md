# DJI Controller → Xbox 360 Virtual Gamepad Bridge

This project lets you use your **DJI controller** (VID `0x2CA3`, PID `0x1021`) as a **virtual Xbox 360 controller** on Windows using Python.

It reads the DJI controller's HID data and translates it into Xbox controller input using [`vgamepad`](https://pypi.org/project/vgamepad/).

---

## Features
- Maps DJI joysticks to Xbox left/right sticks  
- Maps buttons to Xbox A/B/X/Y  
- Maps the right "gâchette" (trigger) to Xbox RT  
- (Optional) Map the left scroll wheel or other controls to buttons/triggers

---

## Requirements

- Windows 10 or 11  
- Python 3.9+  
- Xbox 360 Controller driver (usually already included in Windows)  
- DJI controller connected via USB

---

## Installation

1. Clone or download this repository  
2. Run the installer to set up dependencies:

```
install_requirements.bat
```

This will:
- Create a virtual environment
- Install all required Python packages automatically

---

## Dependencies

This will install:
- hidapi
- vgamepad
- pywin32

After that, you can run the main script directly with:

'''
python dji_to_xbox.py
'''

You should see:
'''
✅ DJI controller connected. Move sticks, triggers, or buttons…
'''

Now your DJI controller will appear as an **Xbox 360 Controller for Windows**.

You can test it using:
'''
joy.cpl
'''

---

## Customization

Inside the Python script (`dji_to_xbox.py`):
- Adjust **axis mappings** or **neutral values** if your sticks drift.
- Game need restart. But even so it's doesn't seems to be seens by the game, so you'll have to modify the input ingame to make it work with this setup ( that what i did )

---

## Troubleshooting

| Problem | Solution |
|----------|-----------|
| Controller not detected | Make sure your DJI controller is plugged in and the VID/PID are correct (`0x2CA3` / `0x1021`). |
| Sticks off-center | Adjust midpoints in the `map_axis()` function. |
| No virtual controller appears | Run Python as **Administrator** (vgamepad requires elevated privileges). |

---

## Credits

Created by **Antoine.M**, powered by Python and `vgamepad`.

---

## Disclaimer

This software is an unofficial tool and not affiliated with DJI or Microsoft.  
Use responsibly and at your own risk.