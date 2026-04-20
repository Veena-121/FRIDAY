import webbrowser
import urllib.parse
import subprocess

def search_google(query):
    query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def search_youtube(query):
    query = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    


def play_my_song():
    url = "https://www.youtube.com/watch?v=bHy3fZPWhpg&list=RDbHy3fZPWhpg&start_radio=1&t=159s"
    
    brave_path = "YOUR_BRAVE_PATH"
    
    subprocess.Popen([brave_path, url])
    
def play_song(song):
    song= urllib.parse.quote(song)
    url= f"https://www.youtube.com/results?search_query={song}"
    webbrowser.open(url)
