# NameSync

**NameSync** is a simple Python script that renames Factorio mod folders to match the format required by the game.

## 🧩 Why This Exists

When downloading mods—especially from third-party sources or manual installations—the folder names are often incorrect or inconsistent. This tool was made to automatically fix that by reading each mod's `info.json` and renaming its folder accordingly.

See [Factorio Wiki](https://wiki.factorio.com/Tutorial:Modding_FAQ#%22C:\Factorio\mod_doesn't_match_the_expected_mod_version#_(case_sensitive!)%22) for details

## ⚙️ What It Does

- Scans the specified mods directory
- Looks for folders containing an `info.json` file
- Reads the `"name"` and `"version"` fields from each file
- Renames the folder to follow the `name_version` format

## 🚀 Usage

By default, the script will try to locate your Factorio mods directory automatically, ussualy:

```bash
C:\Users\YourName\AppData\Roaming\Factorio\mods
```

If it fails for any reason it will ask to manually input a directory.

If you'd like to **skip the auto detection**, you can run:

```bash
python NSmain.py --manual
```

And then provide a directory path when prompted.

## 📦 Downloads

Script and releases can be found under the [Releases](../../releases) section.
Use those instead of cloning the whole repository if you only want the script.

For issues or problems, feel free to open a new issue in the issues section.

## 🧪 Testing

A simple testing environment is included in the repository (located in the `test_environment` folder).  
This can be used to safely try the script without affecting your real mods.

To use it:

1. Run the script with the `--manual` option.
2. When prompted, enter the path to the `test_environment` directory.

Example:

```bash
python NSmain.py --manual
```

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
See [LICENSE](LICENSE) file for details.
