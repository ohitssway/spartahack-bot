import re
import urllib
import urllib2
from bs4 import BeautifulSoup
class Music:
    def __init__(self):
        self.messagetext = ''
    def genius_song_request(self,messagetext):
        songRegex = re.compile(r'(.*),(.*)')
        song = songRegex.search(messagetext)
        artist,song = song.group(1), song.group(2)
        artist = artist.split()
        song = song.split()
        path = "https://genius.com/"
        
        for word in artist:
            path += word + "-"
        for word in song:
            path += word + "-"
        path += "lyrics"
        
        return path
    def youtube_video_request(self,messagetext):
        videoRegex = re.compile(r'.*')
        video = videoRegex.search(messagetext)
        video = video.group(0)
        path = "https://www.youtube.com/results?search_query="
        
        for word in video:
            path += word + "+"
        path = path[:-1]
        
        response = urllib.urlopen(path)
        html = response.read()
        soup = BeautifulSoup(html)
        videoList = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            videoList.append('https://www.youtube.com' + vid['href'])
        return videoList[0]
Music.youtube_video_request(Music(),"the needle drop")