import os
import sys
import datetime
import zipfile
from pathlib import Path
            
def write_header(outfile, title):
    outfile.write("---\n")
    outfile.write("layout: plog\n")
    outfile.write(f'title: "{title}"\n')
    outfile.write(f'date: {title}\n')
    outfile.write("exclude: true\n")
    outfile.write("---\n\n")
    outfile.write("class: middle, center\n")
    outfile.write("layout: true\n\n")
    
def write_picture(outfile, path):
    outfile.write("---\n\n")
    outfile.write("class: middle, center\n\n")
    outfile.write('<img class="plog-picture" src="{{{{ site.baseurl }}}}/{0}" />\n\n'.format(path))
    
def write_description(outfile, description):
    outfile.write(f"{description}\n\n")

def extract_date_from_filename(filename):
    try:
        _, rawdate, _ = filename.split('_')
        return datetime.datetime.strptime(rawdate, "%Y%m%d").strftime("%Y-%m-%d")
    except ValueError:
        return None

def extract_dates_from_namelist(namelist):
    dates = set()
    for filename in namelist:
        if date := extract_date_from_filename(filename):
            dates.add(date)
    return dates

def process_zip_file(zip_path):
    zip_ref = zipfile.ZipFile(zip_path, 'r')
    namelist = zip_ref.namelist()
    dates = extract_dates_from_namelist(namelist)

    if len(dates) != 1:
        print(f"Error: multiple dates found in {zip_path}: {dates}")
        return

    title = dates.pop()
    directory = Path(f"img/plog/{title}")
    directory.mkdir(parents=True, exist_ok=True)
        
    zip_ref.extractall(directory)

    with open(f"_plog/{title}.md", "w") as outfile:
        write_header(outfile, title)
        
        for i, file in enumerate(os.listdir(directory), start=1):
            _, ext = os.path.splitext(file.lower())
                
            istr = f"{i:02}"
            source_path = directory / file
            destination_path = directory / f"{istr}{ext}"
            source_path.rename(destination_path)
            write_picture(outfile, destination_path)
            write_description(outfile, "")

def main(zip_files):
    for zip_path in zip_files:
        process_zip_file(zip_path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: wrong number of arguments. Usage: ./plog.py <ZIP_FILE> [ZIP_FILE ...]')
    else:
        main(sys.argv[1:])