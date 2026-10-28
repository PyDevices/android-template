# Build an APK

Prerequisites: [Android SDK + NDK](https://python-for-android.readthedocs.io/en/latest/quickstart.html), Ubuntu/WSL build tools (`git`, `zip`, `openjdk-17-jdk`, `autoconf`, …). Tooling already downloaded by buildozer lives under `~/.buildozer/android/platform/` by default.

A practical workflow is to iterate on the app logic first, then only change the packaging layer when you need a new dependency or a different build setting. In most cases that means editing **[`p4a_app/main.py`](../../p4a_app/main.py)** (app entry — this is the whole app, there is no separate boot/launcher split here) and **[`p4a_app/buildozer.spec`](../../p4a_app/buildozer.spec)** or **`p4a_recipes/`** when the APK’s runtime package list changes. Display wiring comes from TestPyPI **pydevices-desktop** (`board_config` + pure-Python `usdl2`); do not add a local `board_config.py` that shadows it.

```bash
./build_android.sh              # prompts for app title (Enter = current)
./build_android.sh -y           # keep current title (CI / automation)
./build_android.sh --title MyApp
# APK: p4a_app/bin/myapp-0.1.0-*-debug.apk (name may vary)
./scripts/emulator.sh
```

`build_android.sh` creates `.venv/` and installs host deps from `requirements-dev.txt`. It rsyncs sibling `gallery/lib/utils/` into [`p4a_app/utils/`](../../p4a_app/utils/), then overlays canonical `pydevices/utils/mip.py`. Override the sources with `PYDEVICES_EXAMPLES_UTILS` and `PYDEVICES_PRODUCT_ROOT`. Runtime distributions (**pydevices-desktop**, **pydevices-pygraphics**, …) come from TestPyPI via `p4a_recipes/`. For local iteration only, pass `--local-modules` (or `ANDROID_DEBUG_LOCAL_MODULES=1`) to shadow the `displaydev/`, `boarddev.py`, `usdl2.py`, and `audiodev/` imports from sibling checkouts into `p4a_app/`; default builds remove those shadows. Package id: **`org.pydevices.myapp`**. App label comes from `title` in `p4a_app/buildozer.spec` (`PyDevices App` by default).

## Building from a second checkout

Build from a checkout whose path has no directory starting with `.`. buildozer leaves out every source file under such a directory, so a git worktree in `.worktrees/<name>` would package an APK with no app in it; `build_android.sh` refuses to start there.

Copying `p4a_app/.buildozer` from another checkout saves the full recipe build, but p4a records that checkout's absolute `hostpython` path in the dist's `dist_info.json`, and packaging then fails in `make_tar` with `TypeError: expected str, bytes or os.PathLike object, not NoneType`. Point the path at the new checkout and the build goes through:

```bash
sed -i "s#<old checkout>#<new checkout>#g" p4a_app/.buildozer/android/platform/build-arm64-v8a/dists/<dist>/dist_info.json
```

## After you change a recipe's pin

Just build again. p4a matches an existing dist by its recipe names alone and keeps older installed versions beside newer ones, so on its own it would repackage whatever it installed last time. `build_android.sh` drops any cached package (and the dist built from it) whose version isn't the pin in `p4a_recipes/`, and the p4a hook ([`scripts/p4a_hook.py`](../../scripts/p4a_hook.py), wired in by `p4a.hook` in `buildozer.spec`) fails the build if the dist still differs from the pins. Every Python recipe that moved reinstalls; the compiled ones (CPython, SDL2) are reused. [`scripts/stale_dist.py`](../../scripts/stale_dist.py) holds the logic if you want to run `prune` or `check` by hand.

To see what an APK carries, list the dist-info folders in its bundle:

```bash
unzip -p p4a_app/bin/<apk> lib/arm64-v8a/libpybundle.so | tar -tz | grep 'dist-info/$'
```
