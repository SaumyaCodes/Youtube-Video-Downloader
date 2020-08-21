import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def CreateWidgets():
   linkLabel = Label(root, text='YouTube Link :',fg='white', bg='deepskyblue4')
   linkLabel.grid(row=1, column=0, pady=5, padx=5)

   root.linkText = Entry(root, width=55, textvariable=videoLink)
   root.linkText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

   destinationLabel=Label(root, text='DESTINATION :',fg='white', bg='deepskyblue4')
   destinationLabel.grid(row=2, column=0, pady=5, padx=5)

   root.destinationText=Entry(root,width=38,textvariable=downloadPath)
   root.destinationText.grid(row=2, column=1, pady=5, padx=5)

   browseButton=Button(root, text='BROWSE', command=Browse, width=15)
   browseButton.grid(row=2, column=2, pady=5, padx=5)

   dwldButton=Button(root, text='DOWNLOAD', command=Download, width=30)
   dwldButton.grid(row=3, column=1, pady=5, padx=5)

def Browse():
   downloadDirectory=filedialog.askdirectory(initialdir='D:/YouTube Videos')
   downloadPath.set(downloadDirectory)

def Download():
   yt_link=videoLink.get()
   dwldFolder=downloadPath.get()
   getVideo=YouTube(yt_link)
   videoStream=getVideo.streams.first()
   videoStream.download(dwldFolder)
   messagebox.showinfo('Success','Video Downloaded and Saved in\n '+dwldFolder)

root=tk.Tk()
root.geometry('520x110')
root.resizable(False, False)
root.title('PyYouTubeDownloader')
root.config(background='deepskyblue4')

videoLink=StringVar()
downloadPath=StringVar()
CreateWidgets()

root.mainloop()
