from pytube import YouTube
import os

print("|-------------------------|"
      "|---Youtube Downloader ---|"
      "|-------------------------|")

link = input("Please enter the link of the youtube video: ")

format = input("Choose the output format:\n"
               "(a) MP4\n"
               "(b) MP3\n--> ")

youtubeLink = YouTube(link)

if format == "a":
    stream = youtubeLink.streams.get_highest_resolution()
    print("Downloading.. Please wait")
    stream.download()
    print("Downloaded completely")

elif format == "b":
    stream = youtubeLink.streams.filter(only_audio=True).first()
    print("Downloading.. Please wait")
    download = stream.download()
    base, ext = os.path.splitext(download)
    new_file = base + '.mp3'
    os.rename(download, new_file)
    print("Downloaded completely")