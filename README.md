# android-template

Android APK starter template for the [PyDevices](https://github.com/PyDevices/pydevices) product stack: **python-for-android** recipes and a **Buildozer** app (`p4a_app/`) you can clone and customize with your own code.

> **Testing without building an APK:**
> If you just want to run scripts or test applications on an Android device or emulator from the terminal, use **`pydevices/bin/android.py`** with `adb`. You do not need to build your own APK.

New here? Start with the [newcomer's guide](docs/newcomers.md) for the app
surface, APK assembly path, and shared-tooling boundaries.

## Architecture

On Android, PyDevices applications run under **CPython** in a **python-for-android** APK using the **SDL2 bootstrap** (no Kivy). Runtime packages install from **[TestPyPI](https://test.pypi.org/)** as CPython wheels. Pure-Python `usdl2` and the MCU-shaped `board_config` come from **pydevices-desktop**; p4a’s `sdl2` recipe supplies `libSDL2.so`.

## 🚀 Build Your Own APK

```bash
./build_android.sh -y
./scripts/emulator.sh
```

Full prerequisites, icon/presplash, emulator/phone setup, and `sdkmanager` notes: **[docs/building.md](docs/building.md)**.

> **Ownership:** `build_android.sh`'s core, `p4a_recipes/`, and `scripts/` are owned by [android-runner](https://github.com/PyDevices/android-runner) and hand-synced here — edit them there, then sync to this template. As of this writing `p4a_recipes/` and `scripts/` are byte-identical between the two repos.

## App Layout

| File / Folder | Role |
|---------------|------|
| `p4a_app/main.py` | Your Python application entrypoint |
| `p4a_app/buildozer.spec` | Buildozer configuration (app title, package ID, icon, permissions) |
| `p4a_app/icon.png` | App launcher icon + presplash screen |
| `p4a_recipes/` | TestPyPI / PyPI `PyProjectRecipe` build recipes |
| `build_android.sh` | Build the debug APK |
| `scripts/` | Host emulator/device launcher helpers |

## Customizing Your App

1. Modify **`p4a_app/main.py`** with your PyDevices logic and UI code.
2. Edit **`p4a_app/buildozer.spec`** to customize `title`, `package.name`, and `package.domain`.
3. Replace **`p4a_app/icon.png`** with your app's icon.
4. Run `./build_android.sh` to generate your `.apk`.
