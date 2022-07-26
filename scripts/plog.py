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
            
def write_header(outfile, title, no):
    outfile.write("---\n")
    outfile.write("layout: plog\n")
    outfile.write(f'title: "{title}"\n')
    outfile.write(f'date: {title}\n')
    outfile.write(f'pictures: {str(no)}\n')
    outfile.write("exclude: true\n")
    outfile.write("---\n\n")
    outfile.write("class: middle, center\n")
    outfile.write("layout: true\n\n")
    
def write_picture(outfile, path):
    outfile.write("---\n\n")
    outfile.write("class: middle, center\n\n")
    outfile.write('<img class="plog-picture" src="{{{{ site.baseurl }}}}/{0}" />\n\n'.format(path))
    
def write_description(outfile, description):
    outfile.write(f"{result['description']}\n\n")

def main():
    start, end = get_window()
    title = start.strftime("%Y-%m-%d")
    
    api = connect()
    media_items = api.mediaItems()
    query = media_items.search()
    results = query.execute()
    hits = []

    for result in results['mediaItems']:
        # filter outside window
        creation_time =  result['mediaMetadata']['creationTime']
        creation_datetime = datetime.datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%SZ')
        if start < creation_datetime < end:
            hits.append(result)
     
    hits.reverse()
    with open(f"_plog/{title}.md", "w") as outfile:
        write_header(outfile, title, len(hits))
        for i, hit in enumerate(hits, start=1):
            istr = '0' + str(i) if i < 10 else str(i)

            description = hit['description']
            directory = os.path.join(f"img/plog/{title}")
            extension = result['filename'].split(".")[-1]
            path = os.path.join(f"{directory}/{istr}.{extension}")

            os.mkdir(directory)

            download_file(result['baseUrl'], path)

            write_picture(outfile, path)
            write_description(outfile, description)

main()