'''
This script uses the Google YouTube Data v3 API
The script requires a playlist ID which can be found on the Url of the playlist
after the id being feed it stores the song and artist names in a dictionary
'''

from googleapiclient.discovery import build
devkey= str(input("Please enter the developer key for YT: "))
playlist_id = str(input("Please enter the YT Playlist ID: "))
with build('youtube', 'v3', developerKey= devkey) as serviceYoutube:
    request = serviceYoutube.playlistItems().list(part='snippet',maxResults=1000,playlistId=playlist_id)
    response = request.execute()

def getYTplaylistItems(resultDict) :
    for vids in response['items'] :
         resultDict.update({vids['snippet']['title'] : ((vids['snippet']['videoOwnerChannelTitle']).replace("- Topic",''))})
