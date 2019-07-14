from __future__ import unicode_literals
import youtube_dl
import pyglet
import json
player = pyglet.media.Player()

modes = [
    "Show All songs",
    "Show details of a song",
    "Play a song",
    "Search and download songs",
    "Exit",
]

require_details = ["id","title","creator","duration","webpage_url"]

song_infos = {}

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading.')

print("Hello this is a music app.")
while True:
    print("\nOptions:")
    for i,mode in enumerate(modes):
        print(i+1,". ",mode,sep = "")
    
    # Get user choice
    while True:
        with open('data.json') as f:
            song_list = json.load(f)

        user_opt = input()
        if not user_opt.isdigit():
            print("Please enter a number")
        elif 1 <= int(user_opt) <= 5:
            user_opt = int(user_opt)
            break
        else:
            print("Invalid option.")
    
    # Show All songs
    if user_opt == 1:
        if song_list == []:
            print("\nSong list is empty")
            
        else:
            print("\nSong list:")
            for i,song in enumerate(song_list):
                print(i+1,". ",song["title"],sep = "") 
        input("Press enter to continue ...\n")       
    
    # Show details of a song
    elif user_opt == 2:
        if song_list == []:
            print("\nSong list is empty")
        else:
            print("\nSong list:")
            for i,song in enumerate(song_list):
                print(i+1,". ",song["title"],sep = "")
            while True: 
                numb_to_detail = input("Enter song number? ")
                if numb_to_detail.isdigit():
                    if 1 <= int(numb_to_detail) <= len(song_list):
                        numb_to_detail = int(numb_to_detail) - 1
                        break
                    else:
                        print("Invalid number")
                else:
                    print("Invalid option")
            print("\n",numb_to_detail + 1,". ",song_list[numb_to_detail]["title"],":",sep = "")
            for k,v in song_list[numb_to_detail].items():
                if k != "webpage_url":
                    print(k.upper(),": ",v,sep = "")
        input("Press enter to continue ...\n")
    
    # Play a song
    elif user_opt == 3:

        #Print song list
        if song_list == []:
            print("\nSong list is empty")
            input("Press enter to continue ... ")
        else:
            print("\nSong list:")
            for i,song in enumerate(song_list):
                print(i+1,". ",song["title"],sep = "")

            # Check input
            while True: 
                numb_to_play = input("Enter song number? ")
                if numb_to_play.isdigit():
                    if 1 <= int(numb_to_play) <= len(song_list):
                        numb_to_play = int(numb_to_play) - 1
                        break
                    else:
                        print("Invalid number")
                else:
                    print("Invalid option")

            # Play song                 
            file_name = song_list[numb_to_play]["id"] + ".mp3"
            source = pyglet.media.load(file_name)
            player.queue(source)
            player.play()

            # Playback option
            while True:
                playback_opt = input("Enter playback options (play,pause,stop)\n")
                if playback_opt == "pause":
                    player.pause()
                elif playback_opt == "play":
                    player.play()
                elif playback_opt == "stop":
                    player.delete()
                    break
                else:
                    print("Invalid option")    
    
    # Search and download songs
    elif user_opt == 4:
        # Get song name
        song_name = input("Enter the song you want to search:\n")
        print("Searching for songs, please wait... ")
        
        # Search for song by song_name
        options = {
            'default_search': 'ytsearch5',
            'logger': MyLogger(),
            }
        ydl = youtube_dl.YoutubeDL(options)
        search_result = ydl.extract_info(song_name, False)
        with open('search_data.json', 'w', encoding = "utf-8",) as f:
            json.dump(search_result, f)

        # Print out search result
        for i,result in enumerate( search_result["entries"]):
            print(i+1,". ",result["title"],sep = "")
        
        # Choose a song after searching    
        valid_pos = False
        while True:
            print("Enter the song position you want to download")
            print("Enter (n) if you don't want to download anything")
            song_pos = input()
            if song_pos == "n":
                break
            elif not song_pos.isdigit():
                print("Please enter a number")
            elif 1 <= int(song_pos) <= 5:
                valid_pos = True
                song_pos = int(song_pos) - 1
                break
            else:
                print("Invalid position")
        
        # Get data of the song
        if valid_pos:

            # Save song infos
            for d in require_details:
                song_infos[d] = search_result["entries"][song_pos][d]
            song_list.append(song_infos)
            with open('data.json', 'w') as f:
                json.dump(song_list, f)
            
            # Download the song
            print("Downloading please wait ...")
            ydl_opts = {
                'outtmpl' : "%(id)s.mp3",       # lấy tên file đown về là id của video
                'logger': MyLogger(),           
                'progress_hooks': [my_hook],
            #     'postprocessors': [{

            #     'key': 'FFmpegExtractAudio', # Tách lấy audio

            #     'preferredcodec': 'mp3', # Format ưu tiên là mp3

            #     'preferredquality': '192', # Chất lượng bitrate

            # }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([song_infos["webpage_url"]])
            

            # Ask to play
            while True:
                want_play = input("Do you want to play it?(y/n) ").lower()
                if want_play == "y":
                    file_name = song_infos["id"] + ".mp3"
                    source = pyglet.media.load(file_name)
                    player.queue(source)
                    player.play()
                    while True:
                        playback_opt = input("Enter playback options (play,pause,stop)\n")
                        if playback_opt == "pause":
                            player.pause()
                        elif playback_opt == "play":
                            player.play()
                        elif playback_opt == "stop":
                            player.delete()
                            break
                        else:
                            print("Invalid option")   
                    break 
                elif want_play == "n":
                    break
                else:
                    print("Invalid option")  
    else:
        break