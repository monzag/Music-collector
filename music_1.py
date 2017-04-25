# Muzyczna playlista. Dane muzyki otwierane są z pliku csv. 
# Można szukać muzyki wg kryteriów podanych na ekranie startowym.

import csv
import random


def start_screen():
    print('''
    Welcome in the Music app! Choose the action:
    1) add new album,
    2) find albums by artist,
    3) find albums by year,
    4) find musican by album,
    5) find albums by letter(s),
    6) find albums by genre,
    7) calculate the average age of all albums,
    8) choose random album by genre,
    9) Show the amount of albums by an artist,
    10) find the longest-time album,
    0) exit;
    ''')


def open_file():
    '''Otwieranie pliku csv, pobieranie danych oraz dodanie ich do listy oraz tupli'''
    with open('music.csv') as csvfile:
        from_file = csvfile.readlines()
        splitted = [line.split(' | ') for line in from_file]
        music = [((line[0], line[1]), (int(line[2]), line[3], line[4].strip())) for line in splitted]
        csvfile.close()
    return(music)


def add_new_album():
    '''Dodanie nowego albumu do pliku csv'''
    if user_choice == '1':
        add_artist = str(input('Artist: '))
        add_album = str(input('Album: '))
        add_year = str(input('Year: '))
        add_genre = str(input('Genre: '))
        add_length = str(input('Length: '))
        new_album = [add_artist, add_album, add_year, add_genre, add_length]
        better_look_of_new_album = ' | '.join(new_album)
        with open('music.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([better_look_of_new_album])
            csvfile.close()
        print('You add new album!')


def find_by_artist(music):
    if user_choice == '2':
        artist = str(input('Write the artist: ')).lower()
        artist_and_album = [item[0] for item in music if artist == item[0][0].lower()]
        if artist_and_album == [] or artist_and_album is False:
            print('No result')
        else:
            for item in list(artist_and_album):
                print(', '.join(item))


def find_by_year(music):
    if user_choice == '3':
        try:
            year = int(input('Write year of release: '))
            artist_and_album = [item[0] for item in music if year == item[1][0]]
            if artist_and_album == [] or artist_and_album is False:
                print('No result',)
            else:
                for item in list(artist_and_album):
                    print(', '.join(item))
        except ValueError:
            print('Year is number!')


def find_musican_by_artist(music):
    if user_choice == '4':
        album = str(input('Write album: ')).lower()
        artist_and_album = [item[0] for item in music if album == item[0][1].lower()]
        if artist_and_album == [] or artist_and_album is False:
            print('No result')
        else:
            for item in list(artist_and_album):
                print(', '.join(item))


def find_by_letter(music):
    if user_choice == '5':
        letter = str(input('Write letter(s) of album: ')).lower()
        artist_and_album = [item[0] for item in music if letter in str(item[0][1].lower())]
        if artist_and_album == [] or artist_and_album is False:
            print('No result')
        else:
            for item in list(artist_and_album):
                print(', '.join(item))


def find_by_genre(music):
    if user_choice == '6':
        genre = str(input('Write genre: ')).lower()
        artist_and_album = [item[0] for item in music if genre == item[1][1].lower()]
        if artist_and_album == [] or artist_and_album is False:
            print('No result')
        else:
            for item in list(artist_and_album):
                print(', '.join(item))


def average_all_albums(music):
    '''Obliczenie średniej wieku albumów'''
    if user_choice == '7':
        year_of_album = [item[1][0] for item in music]
        actual = 2017
        age = 0
        count = 0
        for number in year_of_album:
            new_age = actual - number
            age += new_age
            count += 1
        print('Average age of your music: ', int(age/count))


def find_by_genre_random(music):
    '''Szukanie wg randomowego gatunku'''
    if user_choice == '8':
        genre = str(input('Write genre: ')).lower()
        artist_and_album = [item[0] for item in music if genre == item[1][1].lower()]
        if artist_and_album == [] or artist_and_album is False:
            print('No result')
        else:
            random_artist_and_album = random.choice(list(artist_and_album))
            print(', '.join(random_artist_and_album))


def amount_of_albums_by_artist(music):
    if user_choice == '9':
        artist = str(input('Choose an artist: ')).lower()
        amount = 0
        albums = []
        for item in music:
            if artist == item[0][0].lower():
                amount += 1
                albums.append(item[0][1])
        print('Amount of albums: ', amount)
        for item in albums:
            item.split(',')
            print('The album: ', item)


def the_longest_time_album(music):
    if user_choice == '10':
        time = 0
        for item in music:
            minutes_and_seconds = item[1][2].split(':')
            minutes_and_seconds_connected = str(''.join(minutes_and_seconds))
            if int(time) < int(minutes_and_seconds_connected):
                time = minutes_and_seconds_connected
                album = ', '.join(item[0])
        the_longest_time = time[:-2] + ':' + time[-2:]
        print('The longest-time album:', the_longest_time, ' - ', album)


while True:
    '''Uruchomienie programu'''
    music_data = open_file()
    start_screen()
    user_choice = input('Give a number: ')
    add_new_album()
    find_by_artist(music_data)
    find_by_year(music_data)
    find_musican_by_artist(music_data)
    find_by_letter(music_data)
    find_by_genre(music_data)
    average_all_albums(music_data)
    find_by_genre_random(music_data)
    amount_of_albums_by_artist(music_data)
    the_longest_time_album(music_data)

    if user_choice == '0':
        print('Good bye:)')
        break



