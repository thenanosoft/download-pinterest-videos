'''
Developer: Farhan Ellahi
Organization: Nanosoft
Date: 5-Apr-2021, Monday

Website: thenanosoft.com
Email: support@thenanosoft.com
'''

import requests
from bs4 import BeautifulSoup

# input from user pinterest video link
url = input()

# generate api link
videoLinkApi = "https://pinterest-video-api.herokuapp.com/"+ url

# parsing html data
request = requests.get(videoLinkApi)
soup = BeautifulSoup(request.content, "html.parser")

# Convert Video Link into String
videoLink = str(soup)

# remove quotation marks from string at starting and ending points
videoLink = videoLink.strip('\"')

# function for download video
def download_file(url):
    
    # local file name for video after last slash "/"
    local_filename = url.split('/')[-1]
    
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    
    # create video file
    with open(local_filename, 'wb') as videoFile:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                videoFile.write(chunk)
                
    return local_filename

download_file(videoLink)