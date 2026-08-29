#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Run the template app on desktop (Xvfb) before building an APK.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
APP="$ROOT/p4a_app"
VENV_DIR="${VENV_DIR:-$ROOT/.venv}"
TESTPYPI="https://test.pypi.org/simple/"
PYPI="https://pypi.org/simple/"

PYTHON="$VENV_DIR/bin/python3"
PIP="$VENV_DIR/bin/pip"

if [[ ! -x "$PYTHON" ]]; then
  python3 -m venv "$VENV_DIR"
  "$PIP" install -q -U pip
fi

"$PIP" install -q \
  -i "$TESTPYPI" --extra-index-url "$PYPI" \
  pydevices-desktop pydevices-pygraphics

cd "$APP"

echo "== main.py: draw_demo() smoke (no event loop) =="
# Import main.py and call draw_demo() directly -- main()'s SDL event loop only
# returns on SDL_QUIT/SDL_APP_TERMINATING, which nothing sends headlessly.
# xvfb-run supplies a virtual X display; use --auto-servernum -a if Xvfb is
# unavailable, this script still runs against a dummy SDL video driver.
if command -v xvfb-run >/dev/null 2>&1; then
  xvfb-run -a "$PYTHON" -c "import main; main.draw_demo(); print('smoke ok')"
else
  echo "xvfb-run not found; falling back to SDL_VIDEODRIVER=dummy"
  SDL_VIDEODRIVER=dummy "$PYTHON" -c "import main; main.draw_demo(); print('smoke ok')"
fi

echo "Desktop smoke exited cleanly"
