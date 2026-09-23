# Newcomer's guide to android-template

`android-template` is a starting repository for a standalone PyDevices Android
application. It builds an APK containing CPython through python-for-android
and the SDL2 bootstrap—there is no Kivy application layer and no separate
runner or REPL sidecar.

Use it when you want an APK with your own app code. If you only need to run a
script on a connected device or emulator, use `pydevices/bin/android.py`
instead; that does not require creating an APK.

## Start with the app, not the build system

Your code starts in [`p4a_app/main.py`](../p4a_app/main.py). The template's
demo gets the configured display from `board_config`, draws a few bands, and
runs an SDL event loop until Android asks it to exit. Replace that demo with
your application logic.

The primary customization points are:

| Change | Location |
|---|---|
| Application entry point and UI | `p4a_app/main.py` |
| App title, package identity, version, permissions, orientation, dependencies | `p4a_app/buildozer.spec` |
| Launcher icon and presplash | `p4a_app/icon.png` |
| Android TV intent/features | `p4a_app/intent_filters_tv.xml`, `p4a_app/tv_features.xml` |
| Foreground media-playback service | `p4a_app/services/mediaplayback.py` |

Keep the package identifier unique before distributing an APK: the template
defaults to `org.pydevices.myapp` in `buildozer.spec`.

## How an APK is assembled

```text
p4a_app/main.py + buildozer.spec
             |
             v
      build_android.sh
             |
             v
 Buildozer / python-for-android
             |
             |-- SDL2 bootstrap and CPython
             |-- local PyDevices p4a recipes
             `-- TestPyPI and PyPI runtime wheels
                         |
                         v
                    debug APK
```

`build_android.sh` creates a host virtual environment, prepares the Android
SDK/NDK configuration, synchronizes the app utility files, and invokes
Buildozer. The app's `requirements` list names PyDevices packages; the local
recipes in `p4a_recipes/` tell python-for-android how to install the matching
wheels. TestPyPI is the primary runtime index and PyPI is a secondary index
for dependencies unavailable there.

Run the normal build path with:

```bash
./build_android.sh -y
./scripts/emulator.sh
```

The resulting debug APK is placed under `p4a_app/bin/`. The detailed
[build guide](building.md) covers SDK/NDK prerequisites, emulator and phone
use, icons, and the Desktop Xvfb smoke test.

## Repository map

| Path | Purpose |
|---|---|
| `p4a_app/` | The application source and Android-facing configuration you normally customize. |
| `p4a_app/buildozer.spec` | Buildozer/p4a app metadata, ABI targets, permissions, dependencies, and recipe configuration. |
| `p4a_recipes/` | Thin p4a recipes for PyDevices wheels installed while the APK is built. |
| `build_android.sh` | Safe incremental-build wrapper; creates the host environment and protects caches from accidental cleaning. |
| `scripts/` | Emulator, phone, APK-install, desktop-smoke, and recipe-pin helpers. |
| `docs/building.md` | The authoritative build and customization reference. |

## Important boundaries

The default build intentionally uses published TestPyPI packages. The
`--local-modules` flag is for local debugging only: it copies selected sibling
checkout modules into `p4a_app/`, shadowing their installed packages. Do not
turn it into the normal build path or commit those generated shadows.

`build_android.sh`, `p4a_recipes/`, and `scripts/` are shared machinery owned
by [android-runner](https://github.com/PyDevices/android-runner) and manually
synced here. Change their canonical implementation there, then synchronize it
to this template. The exception is `scripts/check_recipe_pins.py`, which
exists only here. In contrast, `p4a_app/` is this template's product surface.

The script deliberately preserves Buildozer caches for incremental builds and
refuses clean/distclean operations unless `ALLOW_CLEAN=1` explicitly confirms
that a cold rebuild is wanted.

## Safe first changes

1. Replace the demo in `p4a_app/main.py`.
2. Set a unique title, package name, and domain in `p4a_app/buildozer.spec`.
3. Replace `p4a_app/icon.png`.
4. Run `./scripts/test_desktop.sh` to exercise the draw path before a full
   Android build.
5. Build and install the debug APK with the documented emulator or phone
   helpers.

When adding a new PyDevices runtime dependency, add or update its recipe and
the `requirements` entry together, then run
`python3 scripts/check_recipe_pins.py` to confirm any pinned TestPyPI release
still exists. For platform prerequisites and behavior that is intentionally
shared with android-runner, read [the build guide](building.md) rather than
duplicating its scripts locally.
