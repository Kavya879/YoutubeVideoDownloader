#I Have placed comments in different parts of code for understanding

import tkinter
import customtkinter as ct
from pytube import YouTube
import os
from moviepy.editor import *
import time

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Part-IV Download (First 3 Choices))
# STEP4
def down(itag, name, location, url1,a3,flag):
#Here the flag is used to segregate the .mp3 and .mp4 files so the user doesn't have to specify the file format (It is different from the flag mentioned below)
    try:
        yt = YouTube(url1)
        stream = yt.streams.get_by_itag(itag)
        if(flag==1):
            stream.download(output_path=location, filename=f"{name}.mp3")
            while not (os.path.exists(os.path.join(location, f"{name}.mp3"))):
                time.sleep(1) #Logic is mentioned below in downl(parameters) function
        elif(flag==2):
            stream.download(output_path=location, filename=f"{name}.mp4")
            while not (os.path.exists(os.path.join(location, f"{name}.mp4"))):
                time.sleep(1)
        print("Download completed successfully!")
        a3.destroy()
    except Exception as e:
        print("An error occurred while downloading:", e)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Part-III Name And Location(First 3 Choices))
def common(tag, url1,a2,flag):
    try:
        a2.destroy()
        a3 = ct.CTk()
        a3.geometry("720x480")
        a3.title("Location And Name Of the file")
        
        title = ct.CTkLabel(a3, text="Enter location of the file:")
        title.pack(padx=10, pady=10)
        loc = tkinter.StringVar()
        loca = ct.CTkEntry(a3, width=350, height=40, textvariable=loc)
        loca.pack()
        
        title = ct.CTkLabel(a3, text="Enter Name of the file:")
        title.pack(padx=10, pady=10)
        name = tkinter.StringVar()
        n = ct.CTkEntry(a3, width=350, height=40, textvariable=name)
        n.pack()
        
        buttonn = ct.CTkButton(a3, text="Download", command=lambda: down(tag, name.get(), loc.get(), url1,a3,flag))
        buttonn.pack()
        
        a3.mainloop()
    except Exception as e:
        print("An error occurred:", e)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Part-II Audio Only)
def parta(url_v,a1):
    url1 = url_v.get()
    a2 = ct.CTk()
    a2.geometry("720x480")
    a2.title("Audio Only options")
    
    title = ct.CTkLabel(a2, text="Choose itag of One Of the following formats:")
    title.pack(padx=10, pady=10)
    yt = YouTube(url1)
    flag=1
    for k in yt.streams.filter(only_audio=True):
        button = ct.CTkButton(a2, text=k, command=lambda itag=k.itag: common(itag, url1,a2,flag))
        button.pack()
    
    app.destroy()
    a1.destroy()
    a2.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Part-II Video Only)

def partv(url_v,a1):
    url1 = url_v.get()
    a2 = ct.CTk()
    a2.geometry("720x480")
    a2.title("Video Only options")
    
    title = ct.CTkLabel(a2, text="Choose itag of One Of the following formats:")
    title.pack(padx=10, pady=10)
    yt = YouTube(url1)
    flag=2
    for k in yt.streams.filter(only_video=True):
        button = ct.CTkButton(a2, text=k, command=lambda itag=k.itag: common(itag, url1,a2,flag))
        button.pack()
    
    app.destroy()
    a1.destroy()
    a2.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Part-II (Audio+Video) Lower Quality)

def partav(url_v,a1):
    url1 = url_v.get()
    a2 = ct.CTk()
    a2.geometry("720x480")
    a2.title("Audio+Video options(Lower Quality)")
    
    title = ct.CTkLabel(a2, text="Choose itag of One Of the following formats:")
    title.pack(padx=10, pady=10)
    yt = YouTube(url1)
    for k in yt.streams.filter(progressive=True):
        button = ct.CTkButton(a2, text=k, command=lambda itag=k.itag: common(itag, url1,a2))
        button.pack()
    
    app.destroy()
    a1.destroy()
    a2.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Part-II (Audio+Video) Better Quality - FULL CODE IN THIS BLOCK (In current Version) )

#This is the most interesting part of this program  , I applied an alternative approach to create a global variable called flag , then i added if statement in audio and video only functions w.r.t the flag value which i changed when this part of code was called)
#If you have a better alternative , feel free to submit a pull request (It's Free)

def partgv(url_v,a1): 
    url1=url_v.get()
    a3 = ct.CTk()
    a3.geometry("720x480")
    a3.title("Location And Name Of the file")
    
    title = ct.CTkLabel(a3, text="Enter location of the file:")
    title.pack(padx=10, pady=10)
    loc = tkinter.StringVar()
    loca = ct.CTkEntry(a3, width=350, height=40,textvariable=loc)
    loca.pack()

    title = ct.CTkLabel(a3, text="Enter Name of the file:")
    title.pack(padx=10, pady=10)
    name = tkinter.StringVar()
    n = ct.CTkEntry(a3, width=350, height=40, textvariable=name)
    n.pack()
    buttonn = ct.CTkButton(a3, text="Proceed", command=lambda:cvtag(url1,loca,n,a1,a3))
    buttonn.pack()
    # a1.destroy()
    a3.mainloop()

def cvtag(url1,loc,name,a1,a3):
    a2 = ct.CTk()
    a2.geometry("720x480")
    a2.title("Audio+Video (Video) options")
    
    title = ct.CTkLabel(a2, text="Choose itag of One Of the following formats:")
    title.pack(padx=10, pady=10)
    yt = YouTube(url1)
    for k in yt.streams.filter(only_video=True):
        button = ct.CTkButton(a2, text=k, command=lambda vtag=k.itag: catag(url1,vtag,loc,name,a1,a3,a2))
        button.pack()
    
    # app.destroy()
    # a1.destroy()
    a2.mainloop()

def catag(url1,vtag,loc,name,a1,a3,a2):
    a4 = ct.CTk()
    a4.geometry("720x480")
    a4.title("Video Only options")
    
    title = ct.CTkLabel(a4, text="Choose itag of One Of the following formats:")
    title.pack(padx=10, pady=10)
    yt = YouTube(url1)
    for k in yt.streams.filter(only_audio=True):
        button = ct.CTkButton(a4, text=k, command=lambda atag=k.itag: downl(url1,vtag,atag,loc.get(),name.get(),a1,a2,a3,a4))
        button.pack()

    # app.destroy()
    # a1.destroy()
    a4.mainloop()


def downl(url1,vtag,atag,location,na,a1,a2,a3,a4):
    try:
        print(location)
        yt = YouTube(url1)
        stream1 = yt.streams.get_by_itag(vtag)
        stream1.download(output_path=location, filename="test69.mp4") #You can change this to any name you want
        print("PART-I completed successfully!") #Just to confirm

        stream2 = yt.streams.get_by_itag(atag)
        stream2.download(output_path=location, filename="test70.mp3")
        print("Part-II completed successfully!")

        video_path = os.path.join(location, "test69.mp4") #To prevent retyping
        audio_path = os.path.join(location, "test70.mp3")
        start_time=time.time
        while not (os.path.exists(os.path.join(location, "test69.mp4")) and os.path.exists(os.path.join(location, "test70.mp3"))): #Couldn't figure this out so referred ChatGPt and bard
            time.sleep(1)
            #It basically makes the program wait until both the files are downloaded which can be checked by checking once both the directories come into existence
            #If we don't use this part of code , it will download your video in the fastest downloadable file (which is *GENERALLY* of low quality)
            
            
        if os.path.exists(video_path) and os.path.exists(audio_path): #Just an extra check for my self satisfaction you are free to remove this as we have already checked the file above
            os.chdir(location)
            videoclip = VideoFileClip( "test69.mp4")
            audioclip = AudioFileClip( "test70.mp3")
            new_audioclip = CompositeAudioClip([audioclip])
            videoclip.audio = new_audioclip
            videoclip.write_videofile((os.path.join(location,  f"{na}.mp4")))
            os.remove("test69.mp4")
            os.remove("test70.mp3")
            a1.destroy()
            a3.destroy()
            a2.destroy()
            a4.destroy()
            app.destroy()
    except Exception as e:
        print("An error occurred while downloading:", e) #Idea to use exception handling was also given by ChatGPT and bard (Me being transparent :-))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Part-I Choice)STEP 2 - provides different buttons to choose between different modes in a new window -> Proceed to respective function
        
def step1(url_v):
    a1 = ct.CTk()
    a1.geometry("720x480")
    a1.title("Download options")
    
    title = ct.CTkLabel(a1, text="Choose What Task Do you want to perform")
    title.pack(padx=10, pady=10)
    options = ["Audio Only", "Video Only", "Audio+Video(Less Range Of Choices)" , "Audio+Video(More Range Of Choices)"]

    for option in options:
        if option == options[0]:
            abutton = ct.CTkButton(a1, text=options[0], command=lambda: parta(url_v,a1))
            abutton.pack()
        elif option == options[1]:
            abutton = ct.CTkButton(a1, text=options[1], command=lambda: partv(url_v,a1))
            abutton.pack()
        elif option == options[2]:
            abutton = ct.CTkButton(a1, text=options[2], command=lambda: partav(url_v,a1))
            abutton.pack()
        elif option == options[3]:
            abutton = ct.CTkButton(a1, text=options[3], command=lambda: partgv(url_v,a1))
            abutton.pack()
  
    a1.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ (Main Frame Begins)(Provides Textbox,button and interface to input url and proceed further) - STEP 1 -> Proceed to STEP1
    
ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

app = ct.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

title = ct.CTkLabel(app, text="Youtube Video Downloader")
title.pack(padx=10, pady=10)

url_v = tkinter.StringVar()
link = ct.CTkEntry(app, width=350, height=40, textvariable=url_v)
link.pack()

Proceed = ct.CTkButton(app, text="Download", command=lambda: step1(url_v))
Proceed.pack()

app.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
