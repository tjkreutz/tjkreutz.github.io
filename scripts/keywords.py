import sys
import posts
from sklearn.feature_extraction.text import TfidfVectorizer


def main(filenames):
    filenames = [filename for filename in filenames if filename.endswith(('md', 'markdown'))]
    allposts = [posts.read_post(filename) for filename in filenames]
    alltexts = [post.get_text() for post in allposts]
    
    vec = TfidfVectorizer(stop_words='english')
    tfidf = vec.fit_transform(alltexts)
    features = vec.get_feature_names()
    postid = 0
    
    for doc in tfidf:
        zipped = zip(doc.data, doc.indices)
        sortedwords = [features[ind] for data, ind in reversed(sorted(zipped))]
        topfive = sortedwords[:5]
        curpost = allposts[postid]
        curpost.add_meta(['keywords'] + topfive)
        curpost.write(filenames[postid])
        postid += 1
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: wrong number of arguments. Usage: ./keywords.py <LIST OF POSTS>')
    else:
        main(sys.argv[1:])
