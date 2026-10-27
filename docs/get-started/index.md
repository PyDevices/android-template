# Make your first app

You need a copy of the template, then the app in `p4a_app/main.py` and the
settings in `p4a_app/buildozer.spec`. If you only want to run a script on a
phone or emulator, you don't need this repository: download `android.py` and
follow [its guide](https://github.com/PyDevices/pydevices/blob/main/docs/guides/run-on-android.md#staging-a-script-with-androidpy).

## Use the template

Press **Use this template** on the
[android-template](https://github.com/PyDevices/android-template) page, or
clone it:

```bash
git clone https://github.com/PyDevices/android-template my-app
cd my-app
```

## Try it on your desktop

Before a full Android build, draw the demo on your computer. The
script makes a virtual environment, installs the PyDevices desktop packages
from TestPyPI and draws the demo once under Xvfb (a virtual display, so no window opens), then exits:

```bash
./scripts/test_desktop.sh
```

It needs `xvfb-run` (the `xvfb` package on Ubuntu).

## Make it yours

1. Change `p4a_app/main.py` to your own PyDevices code.
2. Set `title`, `package.name` and `package.domain` in `p4a_app/buildozer.spec`.
   The template's id is `org.pydevices.myapp`; make yours unique before you
   give the APK to anyone.
3. Replace `p4a_app/icon.png`. [Change the icon](../guides/change-the-icon.md)
   has the size.
4. Build and install it: [Build an APK](../guides/build-an-apk.md), then
   [Run it on an emulator or a phone](../guides/run-on-a-device.md).

[What to change, and where](../reference/customization.md) lists every
setting you are likely to touch.
