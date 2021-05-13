# Get-data-from-image
Program to colect data from a graph printed on a image file

## About

This code implements a Kivy based GUI for an algorithm to collect data from a graph printed on a image file.

## Dependencies
- python 3
- numpy
- kivy
- matplotlib version 3.1.0. New versions may have problems with the kivy garden implementation for matplotlib

## Instalation

Download the ‘gdfi.py’ and ‘kivyplt.py’ files. The latter contains classes and functions for the GUI.
Just call ‘python gdfi.py igmage_path’

## Algorithm Description

The algorithm search in every column of the pixel matrix for pixels that are bellow a minimum “distance” threshold of a fixed pixel, determined by the user. The pixel distance mimics the euclidean distance.  
If more then one pixel falls bellow the threshold, the program will choose the pixel closest to the previous one.

# Documentation

## Mouse and zoom functions

- left click and drag: Linear change the x and y limits
- right click and drag: Change the zoom. In the righ upper direction, increases the x and y zoom respectivly. In the left low direction, decreases the zoom.
- ‘rz’ button: Reset the zoom to view the whole image.

The menu at the right is a scroll. To navigate on it, click and drag, or use the mouse scroll.

## Calibrating the axis

First off all, the x and y axis should be calibrated to correct convert the pixel coordinates in the real data coordinates. The steps are:

1: click on ‘sel’ button
2: click and drag between two positions in the x axis where you can read the data
3: click on the ‘x axis sel.’ button
4: write the data on the text input bellow the ‘x axis sel.’ button
5 to 7: Repeat steps 2 to 4 for the y axis
8: clear the ‘sel’ button

![image](https://user-images.githubusercontent.com/78453361/118064260-0b77a980-b371-11eb-8aaf-4169a6930136.png)

