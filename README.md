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

## Simple case

In the most simple situation, the desired curve have a unique color:  

1: To select a pixel color reference, just left click anywhere. The RGB color button will indicate the current selection

2: Click on get data. The selected points will be ploted whith black dots

3: If the points are ok, insert a file name in the “file name” text input and click in the “save” button. A file with two columns for the x and y coordinates will be created. Note that if there is a file with the same name, a numbe will be added to the saved file. e.g foo_1

![image](https://user-images.githubusercontent.com/78453361/118064417-54c7f900-b371-11eb-9230-9d632348d91e.png)

## Selecting regions and avoid some area

Sometimes the axis and/or other regions of the image have the same color as the desired line. In such scnerios, you can restrict the area where the program will look for points with the ‘left low lim’ and ‘right upper lim’ buttons and avoid some area with the 'blacklist' option:  

1: Click in the desired left lower limit and click on the ‘left low lim’ button
2: Click in the desired left lower limit and click on ‘right upper lim’ button (The program will only look for points within the dotted gray rectangle)
3: click in the ‘sel’ buttn
4: select the are where the program will skip
5: click on the ‘blacklist’ button

![image](https://user-images.githubusercontent.com/78453361/118064867-41695d80-b372-11eb-8e3c-988ab9456404.png)

## Start point

If there are two lines with similar colors, the first point might be indetermined. In this case, you can add a start point:  

1: left click the pixel where you would like to be your start point
2: click in get data

![image](https://user-images.githubusercontent.com/78453361/118064900-56de8780-b372-11eb-9292-615f08d37fa8.png)

## Method (mean, min,max)

The mean method (default) will choose the pixel at the center of the colored region. To resolve sharp peaks, one can try the min or max method, witch will choose the pixels on the lower or upper colored region.

![image](https://user-images.githubusercontent.com/78453361/118064985-8097ae80-b372-11eb-9575-e0baf6776573.png)
![image](https://user-images.githubusercontent.com/78453361/118064992-855c6280-b372-11eb-878a-4db557c9e7a6.png)

## Manually entering points

In some situations, might be necessary correct some points. To do that, click in the ‘change points’ button. When this button is selected, just left click in some place in the image to change the position of that point. It also works with click and drag. As an example, we can adjust two points on the graph above to get a better result:  

![image](https://user-images.githubusercontent.com/78453361/118065153-e08e5500-b372-11eb-89a5-fa17eb8174d0.png)

## Other options

- Clicking in the injective button to change between True and False the 'injective' variable. If True, will collect only one pixel per column. If False, will collect all pixels that satisfy the threshold condition, e.g. , get points of a circle.
- The program try to automatic choose a color for the collected data with some contrast with the original data. But you can choose the color and line width at the end of the lateral menu. 




