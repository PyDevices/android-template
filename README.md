# android-template

android-template is a starter for your own Android app made with the PyDevices
display stack: your Python in `p4a_app/main.py`, built into an APK with
[python-for-android](https://python-for-android.readthedocs.io/) and
[Buildozer](https://buildozer.readthedocs.io/).

If you only want to run a script on a phone or emulator, you don't need an APK
of your own: use `android.py`, which installs a prebuilt Runner
([how](https://github.com/PyDevices/pydevices/blob/main/docs/guides/run-on-android.md#staging-a-script-with-androidpy)).

On GitHub, press **Use this template**, or clone it, then draw the demo on your
desktop before you build anything for Android:

```bash
git clone https://github.com/PyDevices/android-template my-app
cd my-app
./scripts/test_desktop.sh
```

```text
== main.py: draw_demo() smoke (no event loop) ==
SDLDisplay: initialized.
smoke ok
Desktop smoke exited cleanly
```

That makes a virtual environment, installs the PyDevices desktop packages from
TestPyPI and draws `main.py`'s four colour bands once under Xvfb. The APK is one
more command, which needs the Android SDK, NDK and a JDK:

```bash
./build_android.sh -y
```

Prerequisites, installing on an emulator or phone, and what to change are in
the docs.

[Docs](https://github.com/PyDevices/android-template/blob/main/docs/index.md) · [Examples](https://pydevices.github.io/pydevices-examples/gallery/) · [Roadmap](ROADMAP.md)

OmniPython is made by [PyDevices](https://pydevices.com).
