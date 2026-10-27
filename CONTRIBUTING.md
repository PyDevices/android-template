# Contributing

Bug reports and fixes are welcome; open an
[issue](https://github.com/PyDevices/android-template/issues) first for
anything larger than a fix.

## Where a change goes

`build_android.sh`, `p4a_recipes/` and most of `scripts/` are shared with
[android-runner](https://github.com/PyDevices/android-runner), which builds the
generic Runner APK. Change the shared files there first, then copy the change
here. They are copies, not links, and they are not all identical: `scripts/`
differs in `install_apk_main.sh`, `p4a_hook.py` and `test_desktop.sh`, and
[`scripts/check_recipe_pins.py`](scripts/check_recipe_pins.py) exists only in this repository. Compare the two
trees before you copy.

`p4a_app/` is this repository's own.

## Checks

CI runs shellcheck on `build_android.sh` and `scripts/*.sh`, checks that
[`p4a_app/buildozer.spec`](p4a_app/buildozer.spec) parses and has `title`, `package.name`,
`package.domain` and `version`, and checks that every pin in `p4a_recipes/`
resolves on TestPyPI. It doesn't build an APK. Run the same checks yourself:

```bash
shellcheck build_android.sh scripts/*.sh
python3 scripts/check_recipe_pins.py
./scripts/test_desktop.sh
```

A change to the packaging layer also needs a real build: see
[Build an APK](docs/guides/build-an-apk.md).

## Pins

When you add a runtime dependency, add or update its recipe in `p4a_recipes/`
and the `requirements` line in `p4a_app/buildozer.spec` together, then run
`python3 scripts/check_recipe_pins.py`. The default build installs from
TestPyPI; don't make `--local-modules` the normal path or commit the shadow
copies it creates.

## Docs

The pages are plain Markdown under `docs/`, starting at
[docs/index.md](docs/index.md). There is no docs build; check that links you add
resolve.
