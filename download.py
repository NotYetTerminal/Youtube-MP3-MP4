# install pytube3 instead of pytube
from pytube import YouTube

# install these
from shutil import copyfile
import shutil
import moviepy.editor as mp
from bs4 import BeautifulSoup

import urllib.request
import re
import os

# need to make a temp folder called temp in your music directory
# replace these paths with your path
# make sure to use / and not \
path = "C:/Your/Path/To/Music/temp"
path2 = "C:/Your/Path/To/Music"

# list of video links
# copy and paste from youtube
videos = ['https://www.youtube.com/watch?v=', 'https://www.youtube.com/watch?v=']

# you can also search the names
# but set the below to True
listOfNames = False

# leave the d in, write the names in the list
names = [' ', 'd']

# optionally put in your artist name for easier search
artist = ' '
# put in extra like 'lyrics' to get a cleaner mp3
extra = ' '

# set whether you eant an mp3 or mp4
mp3 = False

def SearchVid(search):
    responce = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)

    soup = BeautifulSoup(responce)    
    divs = soup.find_all("div", { "class" : "yt-lockup-content"})
    href= divs[0].find('a', href=True)
    videos.append("https://www.youtube.com"+href['href']+'\n')
        

def downloadvid(i):
    if SearchVid.error > 5:
        return
    try:
        yt = YouTube(i)
        t = yt.streams.filter(mime_type="video/mp4")
        t[0].download(path)
    except:
        SearchVid.error-=-1
        downloadvid(i)

SearchVid.error = 0

while listOfNames == True:
    
    for vids in names:
        SearchString = vids
        
        if SearchString == 'd':
            listOfNames = False
            
        else:
            SearchString = artist + ' ' + SearchString + ' ' + extra
            print(SearchString)
            
            try:
                SearchVid(SearchString.replace(" ", "%20"))
                print('got')
                
            except:
                print('error')
    

for i in videos:
    downloadvid(i)
    
if mp3 == True:
    for file in [n for n in os.listdir(path) if re.search('mp4',n)]:
    
        full_path = os.path.join(path, file)
        output_path = os.path.join(path2, os.path.splitext(file)[0] + '.mp3')
        clip = mp.AudioFileClip(full_path)
        clip.write_audiofile(output_path)

else:
    for file in [n for n in os.listdir(path) if re.search('mp4',n)]:
        
        full_path = os.path.join(path, file)
        output_path = os.path.join(path2, os.path.splitext(file)[0] + '.mp4')
        copyfile(full_path, output_path)
        

shutil.rmtree(path)
os.mkdir(path)
    
print('Task Completed!')





