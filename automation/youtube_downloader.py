import requests
import os, sys
from bs4 import BeautifulSoup

print('Enter 1 if you want to download a song from billboard top 100')
print('Enter 2 if you want to download a number of songs')


while True:
    try:
        user_input = int(input('Enter your response: '))
        # restarts prompt if user enters incorrect integer
        if (user_input != 1) or (user_input != 2):
            print('Enter correct input')
            continue
        break
    # if user enters non integer
    except ValueError:
        print('Enter correct input')
        continue


# Download top 100 Songs from billboard
if user_input == 1:
    file_writer = open('.songs.txt', 'w')
    # assumes there's already a list of songs downloaded
    try:
        # read that list
        file_reader = open('.downloaded.txt', 'r')
        already_downloaded = file_reader.read()
        already_downloaded = already_downloaded.split('\n')
        file_reader.close()
    except FileNotFoundError:
        # if there's no existing list of songs, make an empty one
        already_downloaded = []
    url1 = 'http://www.billboard.com/charts/hot-100'
    link = requests.get(url1)
    soup1 = BeautifulSoup(link.text, 'lxml')
    songz = soup1.findAll('h2', {'class': 'chart-row__song'})
    artist = soup1.findAll('h3', {'class': 'chart-row__artist'})
    # download current billboard's top 100
    for song in range(len(songz)):
        # write to songs.txt
        file_writer.write(songz[song].text + ' ' + artist[song].find('a').text.strip() + '\n')
    file_writer.close()
    # songs now contain current billboard's top 100
    file_reader = open('.songs.txt', 'r')
    songs = file_reader.read()
    songs = songs.split('\n')
    file_appender = open('.downloaded.txt', 'a')

    # for all top 100 song that's not already downloaded
    for each_song in songs:
        for saved_song in already_downloaded:
            # don't download
            if each_song == saved_song:
                break
        else:
            url2 = 'https://www.youtube.com/results?search_query=' + x
            link = requests.get(url2)
            soup2 = BeautifulSoup(sc.text, 'lxml')
            title = soup2.findAll('h3', {'class':'yt-lockup-title '})
            print('Downloading...')
            # download
            os.system("youtube-dl --extract-audio --audio-format mp3 "+'https://www.youtube.com'+title[0].find('a')['href'])
            print('Downloaded.')
            # add to the end of songs already downloaded
            fileappender.write(each_song + '\n')
    print('Download Complete')
    # closing unused resources
    filereader.close()
    fileappender.close()


# Download songs from a list
elif user_input == 2:
    songs = []
    print('Enter song names to download and Enter nothing to exit')
    while True:
        song_name = input('Enter song name: ')
        if song_name != '':
            songs.append(song_name)
        else:
            if len(songs) == 0:
                print('Enter at least one song')
                continue
            else:
                break
    for each_song in songs:
        url2 = 'https://www.youtube.com/results?search_query=' + each_song
        link = requests.get(url2)
        soup2 = BeautifulSoup(link.text, 'lxml')
        title = soup2.findAll('h3', {'class': 'yt-lockup-title '})
        print('Downloading...')
        os.system("youtube-dl --extract-audio --audio-format mp3 " + 'https://www.youtube.com'+title[0].find('a')['href'])
        print('Downloaded.')
    print('Download Complete')
