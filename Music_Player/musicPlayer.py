# importing important modules....................................
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3


# function for bg image.............................................
def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

# main window creation...............................................
root = Tk()
root.title("Music Player")
root.geometry('900x500+150+50')
# root.iconbitmap('music.ico')
root.resizable(False, False)

frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

copy_of_image = Image.open("bg321.jpg")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

# global variable declaration..........................................
audiotrack = StringVar()
currentvol = 0
songLenth = 0


# Important Functions Definition........................................

def musicUrl():
    mus = filedialog.askopenfilename()
    audiotrack.set(mus)
    playButton.grid()

def playMusic():
    track = audiotrack.get()
    mixer.music.load(track)
    volBar.grid()
    root.muteButton.grid()
    stopButton.grid()
    VolUpButton.grid()
    volDownButton.grid()
    root.pauseButton.grid()
    SongLabel.grid()
    mixer.music.play()
    statusLabel.configure(text='Playing')

    def timer():
        currentLength = mixer.music.get_pos()//1000
        SongProgress['value'] = currentLength
        SongProgress.after(2, timer)
        SongEnd.configure(text='{}'.format(str(datetime.timedelta(seconds=currentLength))))
    timer()


def pauseMusic():
    mixer.music.pause()
    root.pauseButton.grid_remove()
    root.resumeButton.grid()
    statusLabel.configure(text='Paused')


def resumeMusic():
    mixer.music.unpause()
    root.resumeButton.grid_remove()
    root.pauseButton.grid()
    statusLabel.configure(text='Playing')

def volD():
    vol = mixer.music.get_volume()
    if (vol <= vol * 100):
        mixer.music.set_volume(vol - 0.03)
    else:
        mixer.music.set_volume(vol - 0.05)
    volPercentage.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    volLevel['value'] = mixer.music.get_volume() * 100


def volU():
    vol = mixer.music.get_volume()
    if(vol>=vol*100):
        mixer.music.set_volume(vol + 0.1)
    else:
        mixer.music.set_volume(vol + 0.05)
    volPercentage.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    volLevel['value'] = mixer.music.get_volume()*100


def stopIt():
    root.destroy()

def muteMus():
    global currentvol
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)
    root.muteButton.grid_remove()
    root.unmuteButton.grid()
    statusLabel.configure(text='Muted')

def unmuteMus():
    root.unmuteButton.grid_remove()
    root.muteButton.grid()
    mixer.music.set_volume(currentvol)
    statusLabel.configure(text='Playing')



def widgets():

    global statusLabel
    global volPercentage
    global volBar
    global volLevel
    global stopButton
    global VolUpButton
    global volDownButton
    global pauseButton
    global SongLabel
    global SongProgress
    global SongEnd
    global playButton

    global imgPlay
    global imgPause
    global imgSearch
    global imgVolUp
    global imgVolDown
    global imgStop
    global imgResume
    global imgMute
    global imgUnmute

# Button Icon Creation....................................
    imgPlay = PhotoImage(file='play.png')
    imgPause = PhotoImage(file='pause.png')
    imgSearch = PhotoImage(file='searching.png')
    imgVolUp = PhotoImage(file='volUp.png')
    imgVolDown = PhotoImage(file='volDn.png')
    imgStop = PhotoImage(file='stop.png')
    imgResume = PhotoImage(file='resume.png')
    imgMute = PhotoImage(file='mute.png')
    imgUnmute = PhotoImage(file='unmute.png')

    imgPlay = imgPlay.subsample(7,7)
    imgPause = imgPause.subsample(7,7)
    imgSearch = imgSearch.subsample(7,7)
    imgVolUp = imgVolUp.subsample(7,7)
    imgVolDown = imgVolDown.subsample(7,7)
    imgStop = imgStop.subsample(7,7)
    imgResume = imgResume.subsample(7,7)
    imgMute = imgMute.subsample(7,7)
    imgUnmute = imgUnmute.subsample(7,7)



# Label and Button Creation................................................................

    tLabel1 = Label(frame, text='Select a Song: ',bg='black',fg='white', font=('Comic Sans MS' ,'12' ,'italic  bold'))
    tLabel1.grid(row=0, column=0, padx=20, pady=20)


    statusLabel = Label(frame, text='' ,bg='black',fg='white', font=('Comic Sans MS' ,'12' ,'italic  bold'),width=15)
    statusLabel.grid(row=4, column=0)

    trackEntry = Entry(frame, bg='black', fg='white', font=('Comic Sans MS' ,'14' ,'italic  bold'),
                       width=35, textvariable=audiotrack)
    trackEntry.grid(row=0, column=1, padx=10, pady=10)


    searchButton = Button(frame,text='Browse  ' ,bg='black', fg='white',font=('Comic Sans MS' ,'12' ,'italic  bold'),
                          width=100, height=25, image=imgSearch, compound=RIGHT, command=musicUrl)
    searchButton.grid(row=0, column=2)


    playButton = Button(frame, text='Play ', bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                        width=100, height=25, image=imgPlay, compound=RIGHT, command=playMusic)
    playButton.grid(row=1, column=0)
    playButton.grid_remove()

    root.pauseButton = Button(frame, text='Pause ', bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                         width=100, height=25, image=imgPause, compound=RIGHT, command=pauseMusic)
    root.pauseButton.grid(row=1, column=1)
    root.pauseButton.grid_remove()

    root.resumeButton = Button(frame, text='Resume ', bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                         width=100, height=25, image=imgResume, compound=RIGHT, command=resumeMusic)
    root.resumeButton.grid(row=1, column=1)
    root.resumeButton.grid_remove()

    stopButton = Button(frame, text='Stop  ', bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                        width=100, height=25, image=imgStop, compound=RIGHT, command=stopIt)
    stopButton.grid(row=1, column=2, padx=10, pady=10)
    stopButton.grid_remove()

    volDownButton = Button(frame, bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                        width=25, height=25, image=imgVolDown, compound=RIGHT, command=volD)
    volDownButton.grid(row=4, column=3, padx=30, pady=30)
    volDownButton.grid_remove()


    VolUpButton = Button(frame, bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                        width=25, height=25, image=imgVolUp, compound=RIGHT, command=volU)
    VolUpButton.grid(row=0, column=3)
    VolUpButton.grid_remove()

    root.muteButton = Button(frame, text='Mute  ', bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                        width=100, height=25, image=imgMute, compound=RIGHT, command=muteMus)
    root.muteButton.grid(row=3, column=2)
    root.muteButton.grid_remove()

    root.unmuteButton = Button(frame, text='Unmute  ', bg='black', fg='white', font=('Comic Sans MS', '10', 'italic  bold'),
                             width=100, height=25, image=imgUnmute, compound=RIGHT, command=unmuteMus)
    root.unmuteButton.grid(row=3, column=2)
    root.unmuteButton.grid_remove()

    volBar = Label(frame, text='', bg='steel blue')
    volBar.grid(row=1, column=3, rowspan=3, padx=5, pady=5)
    volBar.grid_remove()
    volLevel = Progressbar(volBar, orient=VERTICAL, mode='determinate', value=100,length=150)
    volLevel.grid(row=1, column=0)

    volPercentage = Label(volBar, text='100%', bg='steel blue', width=3)
    volPercentage.grid(row=0, column=0)

    SongLabel = Label(frame, bg='steel blue')
    SongLabel.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    SongLabel.grid_remove()


    SongEnd = Label(SongLabel, text='00:00', bg='steel blue')
    SongEnd.grid(row=0, column=2)

    SongProgress = Progressbar(SongLabel, orient=HORIZONTAL, mode='determinate', value=0)
    SongProgress.grid(row=0, column=1, ipadx=200, ipady=2 , padx=5, pady=5)




#developers detail Aniamtion...................................................................................
dev = 'Developed By\n Rahul Singh, Shubham kumar, Sai Kiran, '
center_frame = Frame(frame, relief='raised',bg='black')
center_frame.pack(side = BOTTOM)
sliderlabel = Label(center_frame, text=dev,bg='black',fg='white', font=('Comic Sans MS' ,'18' ,'italic  bold'))
sliderlabel.grid(row=6, column=0, padx=10, pady=0, rowspan=8,columnspan=3)

#Function Calling..............................................................................................
mixer.init()
widgets()
root.mainloop()

# END OF PROGRAME..........................