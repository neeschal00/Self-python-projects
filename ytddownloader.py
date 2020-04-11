from tkinter import *
from pytube import YouTube
from tkinter import filedialog

window = Tk()

window.geometry('350x100')
window.configure(background='#121212')
window.title('Youtube Video Downloader')


def downloady():
    try:
        link = YouTube(link_entry.get())
        # [print(li) for li in link.streams.all()]
        hel = link.streams.first()
        print(hel)
        hel.download('./videotesting')
    except:
        print('enter the link ')


link_label = Label(window,bg='#121212',fg='grey',text='Link')
link_label.grid(row=0,column=0)

link_entry = Entry(window,width=40)
link_entry.grid(row=0,column=1)


download_btn = Button(window,text='Download',bg='#121212',fg='grey',command=downloady)
download_btn.grid(row=1,column=1)


window.mainloop()
