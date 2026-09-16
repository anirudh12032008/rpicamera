from gpiozero import Button, LED, DigitalInputDevice
from signal import pause
import subprocess

flash = LED(23)
ldr = DigitalInputDevice(24)
flash_btn = Button(17)
auto_btn = Button(27)
restart_btn = Button(22)
auto = False


def toggle_flash():
    global auto
    auto = False
    flash.toggle()


def toggle_auto():
    global auto
    auto = not auto
    flash.value = ldr.value if auto else 0


def sync():
    if auto:
        flash.value = ldr.value


def restart():
    subprocess.run(["sudo", "systemctl", "restart", "mediamtx"])


flash_btn.when_pressed = toggle_flash
auto_btn.when_pressed = toggle_auto
restart_btn.when_pressed = restart
ldr.when_activated = sync
ldr.when_deactivated = sync

pause()
