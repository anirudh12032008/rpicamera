# RPI Camera

A Wi-Fi webcam built on a Raspberry Pi. It streams live video over your local network using MediaMTX, so you can open it in VLC, pull it into OBS, and use it as a webcam in Google Meet or any other video call app. Three buttons on the case control a flash, an automatic low light mode, and a stream restart.

Demo: https://www.youtube.com/watch?v=6PyWtzWBfDw


## why rpi camera?
i wanted to have a way to record myself externally without wasting much money on purchasing a new camera so I decided to use a rpi pico 2 w which was sitting ideally and create this!!


## features:
Wireless live stream from the Pi's IP address, served by MediaMTX
Works as a webcam in Google Meet, Zoom and similar apps via OBS Virtual Camera
Opens in VLC as a network stream for quick viewing
Flash button to toggle the light on and off
LDR auto mode: a light sensor turns the flash on automatically in low light
Stream restart button that stops the stream, then brings it back up automatically
Button handling done by a Python script running on the Pi
Transparent PLA case with a smooth sliding, adjustable mount
Portable power: runs from any power bank

Demo: https://www.youtube.com/watch?v=6PyWtzWBfDw


### About the COB LED

The large COB LED on the front is a 12 V part, and it can't be driven from the Pi's 3.3 V GPIO. It stays on the case because it looks good, and a smaller LED does the actual flash work for now.

To make it functional, either swap it for a 5 V COB LED or drive it through a relay or MOSFET from a 12 V supply. That was skipped here to keep the unit small.

<img width="338" height="316" alt="image" src="https://github.com/user-attachments/assets/21759ea1-d5ca-43f0-a123-f1be4bacdb77" />
<img width="974" height="709" alt="Screenshot 2026-09-16 at 5 11 31 PM" src="https://github.com/user-attachments/assets/99a4273d-ae05-41fa-91db-bda9b590fc0c" />


## Setup

### 1. Raspberry Pi

Flash Raspberry Pi OS, connect to Wi-Fi, and check the camera:

```bash
rpicam-hello
```

### 2. MediaMTX

Download the ARM build for your Pi from the [MediaMTX releases page](https://github.com/bluenviron/mediamtx/releases), extract it, and add a camera path to `mediamtx.yml`:

```yaml
paths:
  cam:
    source: rpiCamera
```

Install it as a service so it starts on boot and the restart button can control it:

```bash
sudo mv mediamtx /usr/local/bin/
sudo mv mediamtx.yml /usr/local/etc/
```

Create `/etc/systemd/system/mediamtx.service`:

```ini
[Unit]
Description=MediaMTX
After=network-online.target
[Service]
ExecStart=/usr/local/bin/mediamtx /usr/local/etc/mediamtx.yml
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable --now mediamtx
```

### 3. Button script

`gpiozero` comes preinstalled on Raspberry Pi OS, so there's nothing extra to install.

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python3 main.py
```

To run it on boot, add this with `crontab -e`:

```bash
@reboot python3 /home/<user>/<repo-name>/main.py
```
