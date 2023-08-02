# Authors: Ishan Prasad and Sourjyamoy Barman
# Date: 8 July 2023
# Project: Lyrics guessing game
##############################################
3.9
# here is where we will run the game

import pandas as pd
import os

path1 = os.getcwd() + '/cleanedData_2.pkl'
df = pd.read_csv("raw_songs.csv")
df.to_pickle(path1)
df1 = pd.read_pickle(path1)

"Ensuring that the game can access the songs"
print(df1['Lyrics'][0]) 
print(type(df1['Lyrics'][0]))
print(df1['Artist'][0])
df1['Lyrics'] = df1['Lyrics'].str.replace('\n', '') # removing the '\n' in the lyrics

"The game is as follows:"

import random
play = True
while play:
    random_row = df1.sample(n=1) # gets a random row
    song_lyrics = random_row.iloc[0]['Lyrics'] # extracts the song lyrics from the random row
    song_lyrics = song_lyrics.split(sep="Lyrics")[1]
    song_name = random_row.iloc[0]["Name"] # extracts its name
    print("Can you guess the song based on the lyrics?")
    print(song_lyrics)
    user_guess = input("What is your guess?: ")
    if user_guess.casefold() == song_name.casefold(): # makes the game case-insensitive
        print("Congratulations! You got it right!!")
    else:
        print(f"Sorry, the correct answer is {song_name}")
    r1 = input("Do you want to play again? (y/n): ")
    if r1 == "n":
        play = False
    elif r1 != "y":
        print("Sorry, that is an invalid response. Your game has been terminated.")
        break


"The game is ready to play!!!"


