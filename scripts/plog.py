import os
import sys
import requests
import datetime
from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client import file, client, tools

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

def main(datestring):
    title = datestring
    date = datetime.datetime.strptime(datestring, '%Y-%m-%d')

    api = connect()
    media_items = api.mediaItems()
    query = media_items.search(body={'filters': {'dateFilter': {'dates': [{'year': date.year, 'month': date.month, 'day': date.day}]}}})
    results = query.execute()
    
    if not results:
        return
    
    directory = os.path.join(f"img/plog/{title}")
    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(f"_plog/{title}.md", "w") as outfile:
        
        write_header(outfile, title)
        
        for i, result in enumerate(reversed(results['mediaItems']), start=1):
            istr = '0' + str(i) if i < 10 else str(i)
            description = result['description']
            extension = result['filename'].split(".")[-1]
            path = os.path.join(f"{directory}/{istr}.{extension}")
            download_file(result['baseUrl'], path)

            write_picture(outfile, path)
            write_description(outfile, description)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: wrong number of arguments. Usage: ./plog.py <DATE>')
    else:
        main(sys.argv[1])