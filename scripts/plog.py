import datetime
import json
import os
import sys
from pathlib import Path
from shutil import copy

from PIL import Image


def write_header(outfile, title):
    outfile.write("---\n")
    outfile.write("layout: plog\n")
    outfile.write(f'title: "{title}"\n')
    outfile.write(f"date: {title}\n")
    outfile.write("exclude: true\n")
    outfile.write("---\n\n")
    outfile.write("class: middle, center\n")
    outfile.write("layout: true\n\n")


def write_picture(outfile, path):
    outfile.write("---\n\n")
    outfile.write("class: middle, center\n\n")
    outfile.write(
        '<img class="plog-picture" src="{{{{ site.baseurl }}}}/{0}" />\n\n'.format(path)
    )


def write_description(outfile, description):
    outfile.write(f"{description}\n\n")


def get_takeout_metadata(date: datetime.date, source_directory: Path) -> list[Path]:
    takeout_metadata = []

    for file in source_directory.iterdir():
        if file.suffix.lower() != ".json":
            continue

        with open(file, "r") as f:
            metadata = json.load(f)

        taken_time = datetime.datetime.fromtimestamp(
            float(metadata["photoTakenTime"]["timestamp"]), tz=datetime.timezone.utc
        )

        if taken_time.date() == date.date():
            takeout_metadata.append((taken_time, metadata))

    return [path for _, path in sorted(takeout_metadata)]


def save_image(source_path: Path, destination_path: Path) -> None:
    ext = source_path.suffix.lower()

    if ext == ".gif":
        copy(source_path, destination_path)
        return

    with Image.open(source_path) as img:
        if ext in {".jpg", ".jpeg"}:
            img = img.convert("RGB")
        img.thumbnail((512, 512), Image.LANCZOS)
        img.save(destination_path)


def main(datestring):
    title = datestring
    date = datetime.datetime.strptime(datestring, "%Y-%m-%d")
    source_directory = Path(f"Takeout/Google Photos/Photos from {date.year}")
    takeout_metadata = get_takeout_metadata(date, source_directory)

    if not takeout_metadata:
        print(f"No plog pictures found for {title}. Exiting.")
        exit(0)

    target_directory = Path(f"img/plog/{title}")
    target_directory.mkdir(parents=True, exist_ok=True)

    with open(f"_plog/{title}.md", "w") as outfile:
        write_header(outfile, title)

        for i, metadata in enumerate(takeout_metadata, start=1):
            filename = metadata["title"]
            description = metadata["description"]

            istr = f"{i:02}"
            _, ext = os.path.splitext(filename.lower())
            source_path = source_directory / filename
            destination_path = target_directory / f"{istr}{ext}"

            save_image(source_path, destination_path)
            write_picture(outfile, destination_path)
            write_description(outfile, description)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: wrong number of arguments. Usage: ./plog.py <DATE>")
    else:
        main(sys.argv[1])
