import shutil
import argparse
from pathlib import Path


def copy_files(src_dir, dest_dir):
    src_path = Path(src_dir)
    dest_path = Path(dest_dir)

    for src_item in src_path.glob('**/*'):
        if src_item.is_file():
            extension = src_item.suffix[1:]
            dest_subdir = dest_path / extension
            dest_subdir.mkdir(parents=True, exist_ok=True)

            dest_file = dest_subdir / src_item.name

            try:
                shutil.copy(src_item, dest_file)
                print(f"Зроблено копію {src_item} до {dest_file}")
            except Exception as e:
                print(f"Не вдалося скопіювати {src_item} до {dest_file}: {e}")

# /usr/local/bin/python3 /Users/aneliamashevska/Documents/GitHub/goit-algo-hw-03/ДЗ3_Машевська.py /Users/aneliamashevska/Documents/d/hello /Users/aneliamashevska/Documents/d/hello2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src_dir", type=Path)
    parser.add_argument('dest_dir', type=Path, nargs='?', default='dist',
                        help='Тека призначення за замовчуванням (default: dist)')
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    if not src_dir.exists():
        print(f"Вихідної директорії '{src_dir}' не існує.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)

    copy_files(src_dir, dest_dir)


if __name__ == "__main__":
    main()
