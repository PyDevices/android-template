# Change the icon and splash screen

`buildozer.spec` points both at the same asset:

```ini
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/icon.png
```

| Spec | Details |
|------|---------|
| File | [`p4a_app/icon.png`](../../p4a_app/icon.png) (default: copy of [PyDevices logo-512.png](https://github.com/PyDevices/PyDevices.github.io/blob/main/assets/img/logo-512.png)) |
| Format | PNG, square, RGBA preferred |
| Size | **512×512** (buildozer resizes into density buckets) |
| `icon` | Launcher / home-screen icon |
| `presplash` | Startup splash while Python/SDL bootstrap |

Replace `icon.png` (or change the paths) and rebuild for a new look.
