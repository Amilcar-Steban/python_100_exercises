from pytube import YouTube
import os

def downloadYT(page_url, option):
    op = int(option)
    url = page_url
    current_folder = os.getcwd()#directorio actual
    yt = YouTube(url)
    
    if not op or not url:
        print("campo vacío")
    else:
        if op >2 and op <1:
            print("Seleccione una opción válida")
        else:
            if op == 1:
                
                cabeceraTable(False)
                getAudio(current_folder, yt)
            else:
                cabeceraTable(True)
                getVideo(current_folder, yt)

def getAudio(current_folder, yt: YouTube):
    itag_list = []
    
    for stream in yt.streams.filter(only_audio=True):
        if stream.abr != 'None':
            print(f"{str(stream.itag)+" "  if len(str(stream.itag)) == 2 else stream.itag}  |  {str(stream.abr)+" " if len(str(stream.abr)) == 6  else stream.abr}   |   {stream.mime_type[6:]}")
            itag_list.append(str(stream.itag))
    itag = input("\nid: ")
    if not any(itag == item for item in itag_list) or not itag:
        print("Valor no encontrado")
    else:
        audio = yt.streams.get_by_itag(itag)
        audio_file_path = audio.download(output_path=current_folder)
        audio_mp3_file_path = os.path.splitext(audio_file_path)[0] + ".mp3"
        os.rename(audio_file_path, audio_mp3_file_path)
        print("\nDescarga exitosa!\n")

def getVideo(current_folder, yt:YouTube):
    itag_list = []
    for stream in yt.streams.filter():
        if stream.resolution is not None:
            print(f"{str(stream.itag)+" "  if len(str(stream.itag)) == 2 else stream.itag}  |   {str(stream.resolution)+" " if len(str(stream.resolution)) == 4  else stream.resolution}    |    {stream.fps}   |    {stream.mime_type[6:]}")
            itag_list.append(str(stream.itag))
    itag = input("\nid: ")
    if not any(itag == item for item in itag_list) or not itag:
        print("Valor no encontrado")
    else:
        video = yt.streams.get_by_itag(itag)
        video.download(output_path=current_folder)

def cabeceraTable(boo:bool):
    cabecera = ""
    if boo == True:
        print("\nID     Resolución      FPS       Tipo\n-----------------------------------------")
    else:
        print("\nID      Calidad      Tipo\n----------------------------------")

url = input("Url: ")
option = int(input("Seleccione \n1. Audio\n2. Video\n\n opción: "))
downloadYT(url, option)