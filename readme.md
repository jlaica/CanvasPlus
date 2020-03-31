# Canvas Plus #
## V1.1.0 ##
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/CanvasPlus.svg)](https://pypi.python.org/pypi/CanvasPlus/)
[![GitHub release](https://img.shields.io/github/release/Luke-zhang-04/CanvasPlus)](https://GitHub.com/Luke-zhang-04/CanvasPlus/releases/)
[![GitHub license](https://img.shields.io/github/license/Luke-zhang-04/CanvasPlus)](https://github.com/Luke-zhang-04/CanvasPlus/blob/master/LICENSE)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/CanvasPlus.svg)](https://pypi.python.org/pypi/CanvasPlus/)


An improved Canvas widget for tkinter with more functionality to display graphical elements like lines or text. 

Tkinter's Canvas widget has some limitations which are adressed in this package.

Simmilar to the default tkinter Canvas widget, e.g canvas.create_rectangle, other canvas objects can be created.

## Availability ##
### Option 1: Pip ###
Pip install this package
```
pip install CanvasPlus
```
### Option 2: Github ###
Download a zip file containing all files.
```
git clone https://github.com/Luke-zhang-04/CanvasPlus.git
```
or
![Screen Shot 2020-03-31 at 2 48 23 PM](https://user-images.githubusercontent.com/55749227/78063759-b4766700-735e-11ea-8ba7-6cfe3b72bcb0.png)

## Usage ##
Usage is very simple, especially for those with experience using tkinter canvas.

For complete documentation, head over the [the wiki](https://github.com/Luke-zhang-04/CanvasPlus/wiki)

### Example: ###
```python
#Imports
from tkinter import Tk, StringVar, DoubleVar
import math

#set up canvas
root = Tk()
canvas = CanvasPlus(root, width=800, height=800, background = "white")
canvas.pack()

#create circle function
canvas.create_circle(300, 300, 100, fill = "black", outline = "green", width = 3)

#create rounded rectangle function
canvas.create_round_rectangle(
    400, 400, 500, 500, radius = 75, fill = "blue", outline = "orange", width = 5
)   

#create arrow function and rotate it to by 310 degrees clockwise
arrow = canvas.create_arrow(600, 600, 50, 50, 150, 20, fill = "grey", outline = "black")
canvas.rotate(arrow, 600, 600, 310, unit="deg")

#create a rectangle and convert it to a polygon; then rotate it by pi/4 radians (45 degrees)
rect = canvas.create_rectangle(100, 100, 200, 200, fill = "#f7a8c6", width = 0)
rect = canvas.poly(rect)
canvas.rotate(rect, 150, 150, math.pi/4)

#create an entry and set it's default value
content = StringVar()
canvas.create_entry(0, 0, anchor = "nw", textvariable = content, fg = "blue", bg = "gold")
content.set("a default value")

#create button to print the value in the previously cretaed entry
canvas.create_button(
    5, 25, anchor = "nw", text = "button", width = 50, highlightbackground = "red",
    command = lambda e = content: print(e.get())
)

#create checkbutton and toggle it
_, checkbutton = canvas.create_checkbutton(
    5, 50, anchor = "nw", bg = "brown", fg = "white", text = "My Checkbutton"
)
checkbutton.toggle()

#create a label
canvas.create_label(
    5, 75, font = ("Times", "24"), fg = "black", bg = "green", text = "Hello World!", anchor = "nw"
)

#create a scale
canvas.create_scale(
    5, 100, anchor = "nw", bg = "yellow", activebackground = "gold", from_ = 0, to = 100
)

canvas.update()
canvas.mainloop()
```

![Screen Shot 2020-03-31 at 2 44 02 PM](https://user-images.githubusercontent.com/55749227/78063360-12567f00-735e-11ea-8b4e-066e9e681a92.png)