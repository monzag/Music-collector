# Muzyczna playlista. Dane muzyki otwierane są z pliku csv. 
# Można szukać muzyki wg kryteriów podanych na ekranie startowym.

import csv
import random


def start_screen():
    print("""Welcome in the Music app! Choose the action:
    1) add new album,
    2) find albums by artist,
    3) find albums by year,
    4) find musican by album,
    5) find albums by letter(s),
    6) find albums by genre,
    7) calculate the average age of all albums,
    8) choose random album by genre,
    0) exit;
    """)


def open_file():                    # otwieranie pliku csv, pobieranie danych oraz dodanie ich do listy oraz tupli
    with open('music.csv') as csvfile:
        from_file = csvfile.readlines()
        splitted = [line.split(" | ") for line in from_file]
        music = [((line[0], line[1]), (int(line[2]), line[3], line[4].strip())) for line in splitted]
        csvfile.close()
    return(music)


def choice_1():                    # dodanie nowego albumu
    if choice == "1":
        add_artist = str(input("Artist: "))
        add_album = str(input("Album: "))
        add_year = str(input("Year: "))
        add_genre = str(input("Genre: "))
        add_length = str(input("Length: "))
        new_album = [add_artist, add_album, add_year, add_genre, add_length]
        result1 = " | ".join(new_album)
        with open('music.csv', "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([result1])
            csvfile.close()
        print("You add new album!")


def choice_2(music):                # szukanie wg artysty
    if choice == "2":
        artist = str(input("Write the artist: ")).lower()
        result2 = [item[0] for item in music if artist == item[0][0].lower()]
        if result2 == [] or result2 is False:
            print("No result", "\n")
        else:
            print(' '.join(str(i) for i in result2))


def choice_3(music):                 # szukanie wg roku 
    if choice == "3":
        try:
            year = int(input("Write year of release: "))
            result3 = [item[0] for item in music if year == item[1][0]]
            if result3 == [] or result3 is False:
                print("No result", "\n")
            else:
                print(result3)
        except ValueError:
            print("Year is number!")


def choice_4(music):                 # szukanie wg albumu
    if choice == "4":
        album = str(input("Write album: ")).lower()
        result4 = [item[0] for item in music if album == item[0][1].lower()]
        if result4 == [] or result4 is False:
            print("No result", "\n")
        else:
            print(result4)


def choice_5(music):                 # szukanie wg liter
    if choice == "5":
        letter = str(input("Write letter(s) of album: ")).lower()
        result5 = [item[0] for item in music if letter in str(item[0][1].lower())]
        if result5 == [] or result5 is False:
            print("No result", "\n")
        else:
            print(result5)


def choice_6(music):                 # szukanie wg gatunku
    if choice == "6":
        genre = str(input("Write genre: ")).lower()
        result6 = [item[0] for item in music if genre == item[1][1].lower()]
        if result6 == [] or result6 is False:
            print("No result", "\n")
        else:
            print(result6)


def choice_7(music):                 # Obliczenie średniej wieku albumów
    if choice == "7":
        result7 = [item[1][0] for item in music]
        actual = 2017
        age = 0
        count = 0
        for num in result7:
            new_age = actual - num
            age += new_age
            count += 1
        print("Average age of your music: ", int(age/count))


def choice_8(music):                 # szukanie wg randomowego gatunku
    if choice == "8":
        genre = str(input("Write genre: ")).lower()
        result8 = [item[0] for item in music if genre == item[1][1].lower()]
        if result8 == [] or result8 is False:
            print("No result", "\n")
        else:
            print(random.choice(result8))


while True:                     # uruchomienie programu
    music_data = open_file()
    start_screen()

    choice = input("Give a number: ")
    choice_1()
    choice_2(music_data)
    choice_3(music_data)
    choice_4(music_data)
    choice_5(music_data)
    choice_6(music_data)
    choice_7(music_data)
    choice_8(music_data)

    if choice == "0":
        print("Good bye:)")
        break



