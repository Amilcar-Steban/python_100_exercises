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
                print("\n----------------------------------------------------------")
                getAudio(current_folder, yt)
            else:
                print("\n----------------------------------------------------------")
                getVideo(current_folder, yt)

def getAudio(current_folder, yt: YouTube):
    shown_abr = []
    itag_list = []
    
    for stream in yt.streams.filter(only_audio=True):
        if stream.abr is not None:
            if stream.abr not in shown_abr:
                shown_abr.append(stream.abr)
                itag_list.append(str(stream.itag))
                print(f"id: {stream.itag} --> calidad: {stream.abr}")
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
    
    shown_resolutions = []
    itag_list = []
    
    for stream in yt.streams.filter(progressive=True):
        if stream.resolution is not None:
            if stream.resolution not in shown_resolutions:
                shown_resolutions.append(stream.resolution)
                itag_list.append(str(stream.itag))
                print(f"id: {stream.itag} --> Resolución: {stream.resolution}")
                
    itag = input("\nid: ")
    if not any(itag == item for item in itag_list) or not itag:
        print("Valor no encontrado")
    else:
        video = yt.streams.get_by_itag(itag)
        video.download(output_path=current_folder)
        print("\nDescarga exitosa!\n")

url = input("Url: ")
option = int(input("Seleccione \n1. Audio\n2. Video\n\n opción: "))
downloadYT(url, option)