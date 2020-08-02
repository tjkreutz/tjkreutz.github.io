class Post:
    def __init__(self, meta, text=""):
        self.meta = meta
        self.text = text

    def write(self, filepath):
        closetag = '---'
        newline = '\n'
        filehandle = open(filepath, 'w')
        filehandle.write(closetag)
        filehandle.write(newline)
        for tag, value in self.meta.items():
            filehandle.write(': '.join((tag, value)))
            filehandle.write(newline)
        filehandle.write(closetag)
        filehandle.write(newline)
        filehandle.write(self.get_text())
    
    def get_text(self):
        return self.text    
    
    def get_meta(self):
        return self.meta

    def add_meta(self, metatuple):
        self.meta[metatuple[0]] = str(metatuple[1:])


def read_post(filepath):
    filehandle = open(filepath, 'r')
    closingtag = 0
    meta = {}
    text = ''
    for line in filehandle:
        if '---' in line:
            closingtag += 1
        else:
            if closingtag < 2:
                linesplit = line.split(':')
                tag, value = linesplit[0].strip(), (':').join(linesplit[1:]).strip()
                meta[tag] = value
            else:
                text += line
    return Post(meta, text)
