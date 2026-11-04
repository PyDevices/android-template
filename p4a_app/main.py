# SPDX-FileCopyrightText: 2026 Brad Barnett
#
# SPDX-License-Identifier: MIT
"""Application entry point for the PyDevices Android template."""

import time
from board_config import display_drv

COLORS = (0xF800, 0x07E0, 0x001F, 0xFFE0)


def draw_demo():
    """Draw a simple portability demo with the displaydev API."""
    display_drv.fill(0x1082)
    margin = 24
    band_height = 72
    for index, color in enumerate(COLORS):
        display_drv.fill_rect(
            margin,
            margin + index * (band_height + 12),
            display_drv.width - margin * 2,
            band_height,
            color,
        )
    display_drv.show()


def main():
    draw_demo()
    print("PyDevices Android Template running. Touch screen or press back to exit.")
    try:
        import usdl2
        event = usdl2.SDL_Event()
        running = True
        while running:
            while usdl2.SDL_PollEvent(event):
                if event.type in (usdl2.SDL_QUIT, usdl2.SDL_APP_TERMINATING):
                    running = False
                    break
            time.sleep(0.05)
    except Exception:
        pass


if __name__ == "__main__":
    main()
