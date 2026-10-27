# Run it on an emulator or a phone

Build the APK first ([Build an APK](build-an-apk.md)).

```bash
./scripts/emulator.sh          # AVD already running (WSL → use Windows AVD + adb.exe)
./scripts/phone.sh             # USB-connected phone (skips emulators)
```

On WSL, start the AVD from **Windows** (Device Manager ▶), then talk to it with Windows `adb.exe` (e.g. a `~/bin/adb.exe` symlink to `%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe`).

## USB debugging on a Samsung phone (One UI)

USB debugging is hidden until Developer options are unlocked, and Samsung **Auto Blocker** can leave it greyed out (“blocked by auto blocker”).

1. **Settings → About phone → Software information** → tap **Build number** seven times (unlock Developer options).
2. If USB debugging says blocked by Auto Blocker:
   - **Settings → Security and privacy → Auto Blocker** → turn the **main switch off** (PIN/fingerprint if asked).
3. **Settings → Developer options** → enable **USB debugging** → OK.
4. Plug in a data USB cable; accept **Allow USB debugging?** on the phone.
5. Confirm from WSL: `adb.exe devices` shows a non-`emulator-*` line as `device`, then run `./scripts/phone.sh`.

You can turn Auto Blocker back on afterward; USB debugging may be blocked again until you disable it.

## Android SDK Command-line Tools (`sdkmanager`)

A Studio-installed SDK often has no `cmdline-tools/` folder until you add it. Without that package there is no `sdkmanager.bat` for CLI image installs.

1. Android Studio → **Settings → Languages & Frameworks → Android SDK → SDK Tools**
2. Check **Android SDK Command-line Tools (latest)** → Apply
3. The batch file lands at:

```text
%LOCALAPPDATA%\Android\Sdk\cmdline-tools\latest\bin\sdkmanager.bat
```

From WSL that path is typically:

```text
/mnt/c/Users/<you>/AppData/Local/Android/Sdk/cmdline-tools/latest/bin/sdkmanager.bat
```

Example (AMD64 Windows — use an **x86_64** system image, not arm64):

```bat
"%LOCALAPPDATA%\Android\Sdk\cmdline-tools\latest\bin\sdkmanager.bat" ^
  "system-images;android-37.1;google_apis_playstore_ps16k;x86_64"
```

An arm64 AVD on AMD64 Windows exits immediately (“emulator process for AVD … has terminated”). Until cmdline-tools are installed, download images from Studio’s Device Manager / SDK Manager UI instead.
