"""
CS 5001 Final Project
Spring 2023
Tingyu Li

This project creates a simple puzzle game to play with functions learnt during this semester.
Additional features can be added in the future to provide a better user experience.
References will be documented in the presentation.
"""

# To import pygame zero, pygame and random libraries
import pgzrun, pygame, random
from pgzero.actor import Actor
from pgzero.screen import Screen
from pygame.locals import Rect

screen: Screen

# Initial screen size setting
pygame.init()
row = 4
column = 4
image_size = 100
WIDTH = row * image_size
HEIGHT = column * image_size

# Initial based variables setting
count = 0
count_2 = 0
image_first = image_second = -1
win = False

images = []
for i in range(row):  # Import all the puzzle images to the file
    for j in range(column):
        images.append(Actor(str(i) + str(j)))

images_list = []
for i in range(row):  # Put all the images into correct order
    for j in range(column):
        tile = images[i * row + j]
        tile.left = j * image_size  # tile.left shows the location number of the image left end on x-axis
        tile.top = i * image_size  # tile.left shows the location number of the image left end on y-axis
        images_list.append(tile)


def switch(i, j):  # Switch position of two images
    temp = images_list[i].pos
    images_list[i].pos = images_list[j].pos
    images_list[j].pos = temp


for k in range(17):  # Place images in random positions for each game
    i = random.randint(0, 15)
    j = random.randint(0, 15)
    switch(i, j)


def draw():  # Images, Text, Shapes that needed to be placed on the screen
    screen.clear()
    for image in images_list:
        image.draw()  # Images displayed
    # Texts displayed
    if win:
        screen.draw.text('YOU WIN!!', (60, 170), fontsize=80, color='#FF914D', gcolor='#FF5757')
        screen.draw.text('Used ' + str(count_2) + ' moves', (110, 250), fontsize=36, color='#FF914D',
                         background='#FFF1BA')
    else:
        if image_first == -1:
            screen.draw.text('Welcome To Puzzle Game', (30, 190), shadow=(0.5, 0.5), fontsize=40, color='white',
                             background='#5271FF')
        else:
            screen.draw.text('Moves: ' + str(count_2), (15, 15), fontsize=24, color='red')
            screen.draw.rect(
                Rect((images_list[image_first].left, images_list[image_first].top), (image_size, image_size)),
                '#FF005C')  # Place rectangle around selected image


def on_mouse_down(pos):  # When clicking the screen
    global count, count_2, image_first, image_second, win
    for image in range(row * column):
        if images_list[image].collidepoint(pos):  # When lick on the images
            break
    if count % 2 == 0:  # When the click time is even number
        image_first = image
        count += 1
    elif count % 2 == 1:  # When the click time is odd number
        image_second = image
        count += 1
        count_2 += 1
        switch(image_first, image_second)
    win = True  # Set the winning condition
    for i in range(row):
        for j in range(column):
            selected_image = images_list[i * row + j]  # Go through all the images
            if selected_image.left != j * image_size or selected_image.top != i * image_size:  # Compare positioning
                win = False
                break


pgzrun.go()
