import os
import json
import getpass
import sys

# ANSI color codes
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Print formatted error message
def print_error(message):
    print(f"{RED}[ERROR]{RESET} {message}")

# Print formatted warning message
def print_warning(message):
    print(f"{YELLOW}[WARNING]{RESET} {message}")

# Print formatted info message
def print_info(message):
    print(f"{BLUE}[INFO]{RESET} {message}")

# Print formatted success message
def print_success(message):
    print(f"{GREEN}[SUCCESS]{RESET} {message}")

# Check if a folder contains at least one mod subfolder with info.json
def has_info_json(directory):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, "info.json")):
            return True
    return False

# Determine which mod folder to use, fallback to manual input if needed
def get_mods_directory(force_manual=False):
    if not force_manual:
        user_name = getpass.getuser()
        default_mod_path = f"C:\\Users\\{user_name}\\AppData\\Roaming\\Factorio\\mods"

        if os.path.isdir(default_mod_path) and has_info_json(default_mod_path):
            print_info(f"Default Factorio mods directory found and will be used: {default_mod_path}")
            return default_mod_path
        else:
            if os.path.isdir(default_mod_path):
                print_warning(f"No valid mod folders found in: {default_mod_path}")
            else:
                print_warning("Default Factorio mods directory not found.")

    # Ask the user to manually enter the directory
    manual_path = input("Please enter the mods directory path manually: ").strip('"')

    if not os.path.isdir(manual_path):
        print_error(f"'{manual_path}' is not a valid directory path.")
        return None

    if not has_info_json(manual_path):
        print_error(f"No valid mod folders with 'info.json' found in '{manual_path}'.")
        return None

    return manual_path

# Process each folder in the directory, renaming it to match mod_name_mod_version
def process_mods_directory(base_dir):
    print_info(f"Scanning directory: {base_dir}")

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)

        if not os.path.isdir(folder_path):
            print_warning(f"Skipping '{folder_path}' as it is not a directory.")
            continue

        print_info(f"Processing folder: {folder_path}")
        info_json_path = os.path.join(folder_path, "info.json")

        if not os.path.isfile(info_json_path):
            print_warning(f"'info.json' not found in '{folder_path}'. Skipping.")
            continue

        try:
            with open(info_json_path, 'r', encoding='utf-8') as file:
                info_data = json.load(file)

            mod_name = info_data.get("name")
            mod_version = info_data.get("version")

            if not mod_name or not mod_version:
                print_error(f"'name' or 'version' missing in '{info_json_path}'. Skipping.")
                continue

            expected_folder_name = f"{mod_name}_{mod_version}"
            new_folder_path = os.path.join(base_dir, expected_folder_name)

            if folder_path != new_folder_path:
                os.rename(folder_path, new_folder_path)
                print_success(f"Renamed '{folder_name}' to '{expected_folder_name}'.")
            else:
                print_info(f"No rename needed for '{folder_name}' (already correct).")

        except json.JSONDecodeError:
            print_error(f"Failed to parse 'info.json' in '{folder_path}'. Skipping.")
        except Exception as e:
            print_error(f"Unexpected error in '{folder_path}': {e}")

def main():
    print_info("Welcome to the directory Name Synchronizer for Factorio, or NameSync for short.")
    print_info("This tool will rename mod folders based on the 'name' and 'version' fields in their 'info.json' files.")
    print_info("It is recommended to run this tool with Factorio closed to avoid issues.")
    
    # Check if '--manual' or '--no-auto' was passed as argument
    force_manual = '--manual' in sys.argv or '--no-auto' in sys.argv

    mods_dir = get_mods_directory(force_manual=force_manual)
    if mods_dir:
        process_mods_directory(mods_dir)

if __name__ == "__main__":
    main()
