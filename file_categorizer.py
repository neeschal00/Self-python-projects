import os , shutil
os.chdir('C:\\Users\\Aykdk\\Downloads\\Telegram Desktop')
# print(os.getcwd())
f_pdf = 'C:\\okpython\\pdf files'
f_text = 'C:\\okpython\\text files'
f_image = 'C:\\okpython\\image'
f_powerpoint = 'C:\\okpython\\powerpoint'
f_music = 'C:\\Users\\Aykdk\\Music\\music files'
for filename in os.listdir():
    # print(filename)
    try:
        if filename.endswith(('.txt','.docx')) is True:
            shutil.move(filename,f_text)
        elif filename.endswith('.pptx') is True:
            shutil.move(filename,f_powerpoint)
        elif filename.endswith('.pdf') is True:
            shutil.move(filename,f_pdf)
        elif filename.endswith(('.jpg','.png','.jpeg')) is True :
            shutil.move(filename,f_image)
        elif filename.endswith(('.mp3','.m4a')) is True:
            shutil.move(filename,f_music)
    except shutil.Error as e:
        print(e)
