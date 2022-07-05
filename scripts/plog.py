import os
import requests
import datetime
from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client import file, client, tools

def get_window(days=1):
    now = datetime.datetime.now()
    five = now.replace(hour=5, minute=0, second=0, microsecond=0)
    if now.hour > 19: # window is today
        start = five
        end = now
    else: # window is yesterday
        start = five - datetime.timedelta(days=days)
        end = five
    return start, end

def connect():
    scope = 'https://www.googleapis.com/auth/photoslibrary.readonly'
    store = file.Storage('plog.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', scope)
        creds = tools.run_flow(flow, store)
    api = build('photoslibrary', 'v1', http=creds.authorize(Http()), static_discovery=False)
    return api

def download_file(url, outfile):
    response = requests.get(url)
    if response.status_code == 200:
        with open(outfile, 'wb') as f:
            f.write(response.content)
            f.close()

def main():
    start, end = get_window()
    title = start.strftime("%Y-%m-%d")
    api = connect()
    media_items = api.mediaItems()
    query = media_items.search(body={
        "pageSize": 30,
        "filters": {
            "mediaTypeFilter": {"mediaTypes": ["PHOTO"]},
        }
    })
    
    results = query.execute()
    hits = []
    if results:
        for result in results['mediaItems']:
            # filter outside window
            creation_time =  result['mediaMetadata']['creationTime']
            creation_datetime = datetime.datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%SZ')
            
            if start < creation_datetime < end:
                hits.append(result)
    
    hits.reverse()
    if hits:
        with open(f"_plog/{title}.md", "w") as outfile:
            
            outfile.write("---\n")
            outfile.write("layout: plog\n")
            outfile.write(f'title: "{title}"\n')
            outfile.write(f'date: {title}\n')
            outfile.write(f'pictures: {str(len(hits))}\n')
            outfile.write("exclude: true\n")
            outfile.write("---\n\n")
            outfile.write("class: middle, center\n")
            outfile.write("layout: true\n\n")
            
            for i, hit in enumerate(hits):

                path = os.path.join("img/", hit['filename'])
                download_file(hit['baseUrl'], os.path.join("img/", hit['filename']))
                
                outfile.write("---\n\n")
                
                outfile.write("class: middle, center\n\n")
                
                outfile.write('<img class="plog-picture" src="{{{{ site.baseurl }}}}/{0}" alt="picture {1}" />\n\n'.format(path, str(i+1)))
                
                # temporary solution. How to get MediaItem Description?
                hit['description'] = input(f"Describe picture {str(i+1)}:\n")
                outfile.write(f"{hit['description']}\n\n")
                                    
                
main()