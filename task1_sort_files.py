# task1_sort_files.py
import argparse
from pathlib import Path
import shutil
import sys


def parse_args() -> tuple[Path, Path]:
    """Grab CLI arguments (source is required, destination is optional)."""
    parser = argparse.ArgumentParser(
        description="Recursively copy files and sort them by extension."
    )
    parser.add_argument("source", type=Path, help="Where we copy files FROM.")
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Where we copy files TO (default: dist).",
    )
    args = parser.parse_args()
    return args.source, args.destination


def copy_tree(src: Path, dst_root: Path) -> None:
    """Walk through folders and drop each file into a folder named after its extension."""
    for entry in src.iterdir():
        try:
            if entry.is_dir():
                # If it's a folder — just dive into it recursively
                copy_tree(entry, dst_root)

            elif entry.is_file():
                # Take extension (fallback to 'no_ext' for files without one)
                ext_name = entry.suffix.lower().lstrip(".") or "no_ext"

                # Build a folder for this extension inside destination
                target_dir = dst_root / ext_name
                target_dir.mkdir(parents=True, exist_ok=True)

                # Copy the file into its extension folder
                target_path = target_dir / entry.name
                shutil.copy2(entry, target_path)

        except (OSError, shutil.Error) as err:
            # If something goes wrong with this file — skip it, keep going
            print(f"Skipped {entry}: {err}")


def main() -> None:
    """Validate paths and start the recursive copying."""
    src, dst = parse_args()

    if not src.exists() or not src.is_dir():
        print(f"Error: '{src}' does not exist or is not a directory.")
        sys.exit(1)

    try:
        dst.mkdir(parents=True, exist_ok=True)
    except OSError as err:
        print(f"Cannot create destination folder '{dst}': {err}")
        sys.exit(1)

    copy_tree(src, dst)
    print("All files copied and sorted successfully ✨")


if __name__ == "__main__":
    main()
# python task1_sort_files.py C:\Projects\folder_color_test
