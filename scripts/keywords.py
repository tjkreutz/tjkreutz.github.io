#!/usr/bin/env python3

import sys
import posts
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer

def main(dir):

    allposts = posts.read_posts(dir)
    alltexts = [post.get_text() for post in allposts]
    
    vec = TfidfVectorizer()
    tfidf = vec.fit_transform(alltexts)
    features = vec.get_feature_names()
    
    postid = 0
    
    for doc in tfidf:
        zipped = zip(doc.data, doc.indices)
        sortedwords = [features[ind] for data, ind in reversed(sorted(zipped))]
        topfive = sortedwords[:5]
        curpost = allposts[postid]
        curpost.add_meta(['keywords'] + topfive)
        curpost.write(dir + '/' + curpost.filename)
        postid += 1
        
if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('Error: wrong number of arguments. Usage: ./keywords.py <_POSTS DIR>')
    else:
       main(sys.argv[1])
