import flet as ft
import vlc
import os

music_folder = "/Users/carlotamontasgrimaldi/Desktop/software development/"

songs = [
    {"title": "Hoy El Aire Huele a Ti - Luis Miguel", "file": music_folder + "1.mp3", "art": music_folder + "1.jpeg"},
    {"title": "No Soy El Aire - Thalia", "file": music_folder + "2.mp3", "art": music_folder + "2.jpeg"},
    {"title": "Me Dediqué a Perderte - Alejandro Fernández", "file": music_folder + "3.mp3", "art": music_folder + "3.jpeg"},
    {"title": "Herida - Myriam Hernández", "file": music_folder + "4.mp3", "art": music_folder + "4.jpeg"},
    {"title": "Por Amarte Así - Cristian Castro", "file": music_folder + "5.mp3", "art": music_folder + "5.jpeg"},
]
current_song_index = 0

instance = vlc.Instance()
player = instance.media_player_new()

def update_song_and_art(page: ft.Page, index: int):
    global current_song_index, player
    current_song_index = index
    song = songs[current_song_index]

    player.set_media(instance.media_new_path(song["file"]))
    player.play()

    album_art_ctrl.src = song["art"]
    title_ctrl.value = song["title"]
    page.update()

def main(page: ft.Page):
    page.title = "Cancioncitas Tristes de Doña ❤️‍🩹"
    global album_art_ctrl, title_ctrl

    album_art_ctrl = ft.Image(width=300, height=300)
    title_ctrl = ft.Text("", size=20)

    controls_row = ft.Row([
        ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, on_click=lambda e: prev_song(page)),
        ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=lambda e: play_song()),
        ft.IconButton(icon=ft.icons.PAUSE, on_click=lambda e: pause_song()),
        ft.IconButton(icon=ft.icons.SKIP_NEXT, on_click=lambda e: next_song(page)),
    ], alignment=ft.MainAxisAlignment.CENTER)

    page.add(album_art_ctrl)
    page.add(title_ctrl)
    page.add(controls_row)

    update_song_and_art(page, current_song_index)

def play_song():
    if not player.is_playing():
        player.play()

def pause_song():
    player.pause()

def next_song(page):
    global current_song_index
    next_index = (current_song_index + 1) % len(songs)
    update_song_and_art(page, next_index)

def prev_song(page):
    global current_song_index
    prev_index = (current_song_index - 1) % len(songs)
    update_song_and_art(page, prev_index)

ft.app(target=main)

#SOURCES:
#hola teacher, espero se encuentre bien! mire, le queria dejar saber que esta asignación me dio mucha brega. yo hasta tuve que bajarme el app de vlc media player para que funcionara todoo, pero me siento muy orgullosa de lo que he logrado aqui. espero que disfrute este trabajo
#https://www.programcreek.com/python/example/93375/vlc.Instance
#https://www.geeksforgeeks.org/python-vlc-instance/
#https://www.geeksforgeeks.org/vlc-module-in-python-an-introduction/
#https://flet.dev/docs/controls/iconbutton/ 
#https://flet.dev/docs/controls/buttons/
#https://flet.dev/docs/controls/audio/#audio-with-playback-controls 
#https://www.w3schools.com/python/python_lists.asp