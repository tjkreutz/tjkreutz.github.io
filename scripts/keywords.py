import sys
import posts
from sklearn.feature_extraction.text import TfidfVectorizer


def main(directory):

    allposts = posts.read_posts(directory)
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
        curpost.write(directory + '/' + curpost.filename)
        postid += 1
        
if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print('Error: wrong number of arguments. Usage: ./keywords.py <_POSTS DIR>')
    else:
        main(sys.argv[1])
