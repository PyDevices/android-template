# SPDX-License-Identifier: MIT
"""python-for-android hooks (wired in via ``p4a.hook`` in buildozer.spec).

``before_apk_build`` runs inside the dist directory that gradle is about to
compile. It refuses a dist whose Python packages differ from the recipe pins
(``stale_dist.py``): p4a reuses an existing dist and keeps older installed
versions beside newer ones, so a moved pin could ship the old build.
"""

import os
import pathlib
import sys

_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import stale_dist  # noqa: E402


def before_apk_build(toolchain):
    sites = stale_dist.check(os.getcwd())
    print("p4a_hook: dist packages match the recipe pins (%d bundle(s))" % sites)
