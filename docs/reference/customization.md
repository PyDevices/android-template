# What to change, and where

Almost everything a user customizes for their APK lives under **`p4a_app/`**:

| Customize | Where |
|-----------|--------|
| Entry / demo code | `p4a_app/main.py` |
| Display size / rotation / scale | `board_config_tv.py` from `main.py` for TV; otherwise the defaults from `pydevices-desktop`'s `board_config` |
| Title, package id, orientation, version, permissions, `requirements` | `p4a_app/buildozer.spec` |
| Icon / presplash | `p4a_app/icon.png` (paths in the spec) |

Leave **`p4a_app/`** alone only when you need packaging or host tooling changes:

| Need | Where |
|------|--------|
| New / different CPython wheel install from TestPyPI | `p4a_recipes/` (+ list the recipe name in `buildozer.spec` `requirements`) |
| Build / install / smoke helpers | `build_android.sh`, `scripts/` |

Keep `p4a.local_recipes` pointed at this repo’s `p4a_recipes/` unless you are shipping your own recipe tree.

## `build_android.sh`

| Option or variable | Effect |
|---|---|
| `-y`, `--yes`, `--no-prompt` | Keep the current `title` in `buildozer.spec` instead of asking. A non-interactive stdin does the same. |
| `--title NAME` | Set the launcher title without asking. |
| `--local-modules`, `ANDROID_DEBUG_LOCAL_MODULES=1` | Shadow the TestPyPI `displaydev`, `boarddev`, `usdl2` and `audiodev` with copies from sibling checkouts. For local debugging only. |
| `ALLOW_CLEAN=1` | Let a `clean` or `distclean` argument through. Without it the script refuses, so a build keeps its caches. |
| `VENV_DIR`, `REQUIREMENTS` | The host build virtual environment (default `.venv`) and its requirements file (default `requirements-dev.txt`). |
| `ANDROID_HOME`, `ANDROID_NDK_HOME`, `JAVA_HOME` | The SDK, NDK and JDK to build with. Unset values are detected. |
| `PYDEVICES_EXAMPLES_UTILS`, `PYDEVICES_PRODUCT_ROOT` | Where to sync `p4a_app/utils/` from, when sibling checkouts exist. |
