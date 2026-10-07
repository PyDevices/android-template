# Roadmap

The template is heading toward putting your own app on your phone without a
local APK build: no Android SDK, NDK or JDK, and no hour-long first build.

## Next

- Named shortcuts on the PyDevices Runner: `android.py --shortcut "Piano"
  examples/piano.py` stages the app and pins a home-screen icon for it. Apps
  share the Runner's package, permissions and data.

## Later

- A prebuilt base APK and a repack tool that swaps in your `main.py`, package
  id, name and icon, then signs the result in seconds. For an app you want to
  hand to other people as a standalone install.

Bugs, and things you need that don't work yet, go to
[issues](https://github.com/PyDevices/android-template/issues).
