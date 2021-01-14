from pytube import YouTube
from os import path as path
import os 
while True:
    link = input("Enter Youtube Link:  ")
    yt = YouTube(link)
    print("Title",yt.title)
    print("Length of video", yt.length, "seconds")

    print(yt.streams.filter(progressive=True))

    ys = yt.streams.get_highest_resolution()

    if path.exists("location/" + yt.title + ".mp4"):
        if input("This Already Exists. Overwrite?(Y/N): ").lower() == ("n"):
            os.system("ytdownloader.py")
            break
    else: 
       
            
        print("Downloading")
        ys.download('location')
        print("Done")
    
        agn = input("Download Again? (Y/N):"  )
        if agn == ("N"):
            break
   
        
    

