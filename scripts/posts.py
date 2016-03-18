import os

class Post():
    def __init__(self, dir, filename):
        self.dir = dir
        self.filename = filename
        self.meta, self.text = self.read(os.path.join(dir,filename))

    def read(self, filepath):
        filehandle = open(filepath, 'r')
        closingtag = 0
        meta = {}
        text = ''
        for line in filehandle:
            if '---' in line:
                closingtag += 1
            else:
                if closingtag<2:
                    linesplit = line.split(':')
                    tag, value = linesplit[0].strip(), (':').join(linesplit[1:]).strip()
                    meta[tag] = value
                else:
                    text += line
        return meta, text

    def write(self, filepath):
        closetag = '---'
        newline = '\n'
        filehandle = open(filepath, 'w')
        filehandle.write(closetag)
        filehandle.write(newline)
        for tag, value in self.meta.items():
            filehandle.write(':'.join((tag, value)))
            filehandle.write(newline)
        filehandle.write(closetag)
        filehandle.write(newline)
        filehandle.write(self.get_text())
        filehandle.close()
    
    def get_text(self):
        return self.text    
    
    def get_meta(self):
        return self.meta

    def add_meta(self, tuple):
        self.meta[tuple[0]] = tuple[1:]

def read_posts(dir):
    posts = []
    for filename in os.listdir(dir):
        if filename.endswith(('md', 'markdown')):
            post = Post(dir, filename)
            posts.append(post)
    return posts

def write_posts(posts):
    for post in posts:
        post.write()
    
