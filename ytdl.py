#!/usr/bin/python3
# https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
import sys, getopt
from pytube import Playlist
from pytube import YouTube
import re


def main(argv):
    playlist_url = ''
    outputflag = ''
    try:
        opts, args = getopt.getopt(argv, "hp:u:", ["pflag=","uflag="])
    except getopt.GetoptError:
        print (sys.argv[0],'-p <playlist_url> -u <clip_url>')
        sys.exit(2)

    if not opts:
         print (sys.argv[0],'-p <playlist_url> -u <clip_url>')
         sys.exit(2)

    for opt, arg in opts:
        if opt == '-h' :
            print (sys.argv[0],'-p <playlist_url> -u <clip_url>')
            sys.exit()
        elif opt in ("-p", "--pflag"):
            print ('Playlist Url is :', arg)
            playlist=Playlist(arg)
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            for video in playlist:
                YouTube(video).streams.get_highest_resolution().download()

        elif opt in ("-u", "--uflag"):
            print ('Clip Url is :', arg)
            YouTube(arg).streams.get_highest_resolution().download()

        else:
            print('An exception is reached....')

"""
need to add 3rd flag , to 1) grep the playlist file 2) take specific video file and download the rest onward.
-> do a search for the file and create a new list to download items on that new list.
-> alternatively, do the video id trick.  Leave the list and search in codewar game.
"""

if __name__ == "__main__":
    main(sys.argv[1:])
