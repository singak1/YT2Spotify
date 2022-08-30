# YT2Spotify
Import YouTube Playlist to Spotify

This project transfers over a YT Playlist of songs and makes a new playlist on spotify and adds songs to that playlist. It is written in Python and uses the following APIs:

1. Youtube v3 Data | Reference: https://developers.google.com/youtube/v3/docs
2. Spotipy for Spotify API | Reference: https://spotipy.readthedocs.io/en/master/

# Getting Started
PLEASE DOWNLOAD BOTH THE PYTHON FILES AND SAVE THEM IN THE SAME FOLDER/DIRECTORY
**For Spotify Client Secret and Client ID:**
1. Log onto developer.spotify.com and then click DASHBOARD on the menu at the top of the page.
2. Once logged in click on create an app, once created you will see the CLient ID and to view your client secret click in SHOW CLIENT SECRET

**For Youtube Developer ID:**
1. Log onto console.cloud.google.com
2. Once on the landing page, you will need to create a project which can be done by clicking on select a project on the top menu bar.
3. Once created click on library on the left hand menu and search for  YouTube Data API v3  and enable it.
4. Once enabled you can go back and click on credentials on the left hand menu and click on create credentials and select API key from the menu
5. This should get you your API key.

Once you get all the items needed from above, run the spotifySide.py file, you may need to install python on your system before you can run the files but a simple how to install python your_OS_here on google will help you, replace your_OS_here with Windows/Mac/LinuxDistro whatever youre using.

When you successfully run the python file, it will ask for a client id/client secret and API key from you. Once feeded a browser window should open up and you will need to copy the entire URL and head back to your spotify dashboard where you got your client id and secret from. Once there click on edit settings and paste the URL on redirect URLs and click add. You will only need to do this once. Once added to your dashboard, the same URL can be entered as the scrip will ask for a URL as well.

After that, you should be able to go through with the script without neeeding any help.

If you still have any questions...you can always add it to issues on here and I will take a look and help you as soon as I can get to it.

**This is a work in progress and some songs might not be added and a known issue is that another artist has a song which is named the same, the script might add that song instead of the one on the playlist, but as mentioned before please add issues to this repo and I will get back as soon as I can.
**
