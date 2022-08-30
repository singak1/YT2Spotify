import spotipy
from spotipy.oauth2 import SpotifyOAuth

print("WELCOME TO YT2SPOTIFY!! \nPLEASE READ THE README.md on my github for the client secret,id and developer key needed!!")
secret = str(input("Enter the Client Secret: "))
client_id = str(input("Enter the Client ID: "))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id, client_secret= secret, redirect_uri='http://localhost/',scope='user-library-read user-read-playback-state app-remote-control user-modify-playback-state playlist-modify-public playlist-modify-private'))

global resultDict
resultDict = {}
import ytSide
ytSide.getYTplaylistItems(resultDict)
uri_lst = []

def getSongURI() :
    for keys in resultDict:
        result = sp.search(q=keys, type='track', limit=10)
        for songs in result['tracks']['items'] :
            uri_lst.append(songs['uri'])
            break

def createAndAddSongs() :
     getSongURI()
     playlistname = input("Please name your spotify Playlist(this is where the songs will be imported to): ")
     username = input("Please enter you spotify username: ")
     res = sp.user_playlist_create(user = username, name = playlistname, description= "Imported YT Playlist Songs")
     playlistID = res['id']
     if(len(uri_lst) > 0) :
         sp.playlist_add_items(playlist_id=playlistID, items=uri_lst)
     print("Added " + str(len(uri_lst)) + " out of " + str(len(resultDict)) + " songs")

createAndAddSongs()
