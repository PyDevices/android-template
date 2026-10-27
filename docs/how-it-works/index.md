# How android-template builds an APK

`android-template` is a starting repository for a standalone PyDevices Android
application. It builds an APK containing CPython through python-for-android
and the SDL2 bootstrap—there is no Kivy application layer and no separate
runner or REPL sidecar.

Use it when you want an APK with your own app code. [Make your first app](../get-started/index.md) walks through it. If you only need to run a
script on a connected device or emulator, download `android.py` and use it
instead ([how](https://github.com/PyDevices/pydevices/blob/main/docs/guides/run-on-android.md#staging-a-script-with-androidpy)); that does not require creating an APK.

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

The resulting debug APK is placed under `p4a_app/bin/`. [Build an APK](../guides/build-an-apk.md) has the commands and prerequisites.

## What is and isn't in the APK


This template has no `boot.py` / stdio sidecar / attach REPL — that machinery belongs to the separate [android-runner](https://github.com/PyDevices/android-runner) repo, which builds a generic debuggable host APK (`org.pydevices.runner`) that `pydevices/bin/android.py` stages scripts onto. Here, `p4a_app/main.py` is p4a's normal SDL2 bootstrap entrypoint and needs no patching of `getEntryPoint`.

The `displaydev` module ships inside the **pydevices** distribution itself (there is no separate `pydevices-displaydev` package on TestPyPI); `p4a_recipes/pydevices/` pulls it in as part of `pydevices`.

## Important boundaries

The default build intentionally uses published TestPyPI packages. The
`--local-modules` flag is for local debugging only: it copies selected sibling
checkout modules into `p4a_app/`, shadowing their installed packages. Do not
turn it into the normal build path or commit those generated shadows.

`p4a_app/` is this template's product surface. `build_android.sh` and
`p4a_recipes/` come from [android-runner](https://github.com/PyDevices/android-runner),
which builds the generic Runner APK; this template keeps its own copy so a
clone builds without it.

The script deliberately preserves Buildozer caches for incremental builds and
refuses clean/distclean operations unless `ALLOW_CLEAN=1` explicitly confirms
that a cold rebuild is wanted.
