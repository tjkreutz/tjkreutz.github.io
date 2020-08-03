import os
import sys
from PIL import Image
from posts import Post

class Plog(Post):
    def __init__(self, meta, images):
        super(Plog, self).__init__(meta)
        self.images = images

    def write(self, filepath):
        super(Plog, self).write(filepath)
        filehandle = open(filepath, 'a')
        for image in self.images:

            image.show()
            comment = input("Comment: ")

            filehandle.write(image_md(image))
            filehandle.write("\n\n")
            filehandle.write(comment_md(comment))
            filehandle.write("\n\n")

def image_md(image):
    html = '![img]({{ "/' + image.filename + '" | prepend: site.baseurl }})'
    return html

def comment_md(comment):
    html = comment
    return html

def plog_from_directory(directory):
    title = os.path.basename(os.path.normpath(directory))

    images = []
    extensions = [".jpg", ".jpeg"]
    for filename in os.listdir(directory):
        extension = os.path.splitext(filename)[-1].lower()
        if extension in extensions:
            image = process_image(os.path.join(directory, filename))
            images.append(image)

    meta = {"title": title, "date": title, "type": "plog", "layout": "plog", "pictures": str(len(images))}
    plog = Plog(meta, images)
    return plog

def process_image(filepath):
    image = Image.open(filepath)
    # resize
    if image.width > 400:
        factor = 400 / image.width
        image = image.resize((int(image.width * factor), int(image.height * factor)))

    image.save(filepath)
    return image

def main(directory, outfile):
    plog = plog_from_directory(directory)
    plog.write(outfile)

if __name__ == '__main__':
    if not len(sys.argv) == 3:
        print('Error: wrong number of arguments. Usage: ./plog.py <IMAGE DIR> <PLOG FILE>')
    else:
        main(sys.argv[1], sys.argv[2])