# Change the icon and splash screen

`buildozer.spec` points both at the same asset:

```ini
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/icon.png
```

| Spec | Details |
|------|---------|
| File | [`p4a_app/icon.png`](../../p4a_app/icon.png) (default: the OmniPython app icon, 512 px) |
| Format | PNG, square, RGBA preferred |
| Size | **512×512** (buildozer resizes into density buckets) |
| `icon` | Launcher / home-screen icon |
| `presplash` | Startup splash while Python/SDL bootstrap |

Replace `icon.png` (or change the paths) and rebuild for a new look.
