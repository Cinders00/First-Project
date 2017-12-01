import blinkt
from blinkt import set_pixel, set_brightness, show, clear
import time
import XboxController

xboxCont = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo = 0,
    deadzone = 0.1,
    scale = 1,
    invertYAxis = False)

xboxCont.start()
def startButtonCallBack(value):
    clear()
    show()
    set_pixel(0,238,17,0)
    set_brightness(1)
    show()
    time.sleep(0.5)
    clear()
    show()
    
xboxCont.setupControlCallback(
    xboxCont.XboxControls.START,
    startButtonCallBack)
