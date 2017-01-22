import re
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