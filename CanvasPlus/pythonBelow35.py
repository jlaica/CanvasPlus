'''The CanvasPlus package, version 1.3.0 for Python 3.0-3.4'''
'''
Luke-zhang-04
CanvasPlus v1.3.0 (https://github.com/Luke-zhang-04/CanvasPlus)
Copyright (C) 2020 Luke Zhang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
'''

#This file is meant for those who intend on using this package for Python versions 3.0 - 3.4
#For Python 3.5 and above, use the main CanvasPlus folder

#tkinter
from tkinter import (
    Canvas, Button, Checkbutton, Entry, Frame, Label, LabelFrame, Listbox,
    PanedWindow, Radiobutton, Scale, Scrollbar, Spinbox
)

#complex numbers and stuff
import cmath, math

#warnings
import warnings

#regex
import re

#asyncio
try: import asyncio
except ImportError:
    print("Library Asyncio not found. You have four options\n1. use python 3.7 or higher\n2. install asyncio with pip (pip install asyncio)\n3. Download CanvasPlus version 1.2.2 which does not use asyncio, but loose async features\n4. Use the programs default mechanism which imports an older version of asyncio")
    print("importing The asyncio package, tracking PEP 3156")
    import CanvasPlus.asyncio_old as asyncio

_canvasPlusVersion = "v1.3.0"

print("This is CanvasPlus %s" % _canvasPlusVersion)

class Error(Exception):
   '''Base class for other exceptions'''
   pass

class InvalidUnitError(Error):
    '''Raised when unit is not recognised'''
    pass

class UnsupportedObjectType(UserWarning):
    '''raised when object type is not supported'''
    pass

class InvalidObjectType(Error):
    '''raised when object type not supported'''
    pass

class InvalidEquation(Error):
    '''raised when euqtion of a line is invalid'''
    pass


class WidgetWindows:
    '''Class for createing widgets as windows within the canvas'''

    windowProperties = ["anchor", "height", "state", "tags", "width", "window"]

    def _create_widget(self, x, y, widget, **kwargs):
        '''internal function: creates widget of widget type and puts it onto the canvas'''
        widgetKwargs = {}
        windowKwargs = {}
        for key, val in kwargs.items():
            if key in self.windowProperties:
                windowKwargs[key] = val
            else:
                widgetKwargs[key] = val

        newWidget = widget(self, **widgetKwargs)
        if "window" not in windowKwargs: windowKwargs["window"] = newWidget
        return self.create_window(x, y, **windowKwargs), newWidget
    
    def create_button(self, x, y, **kwargs):
        '''
        create button with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Button widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Button, **kwargs)
        
    def create_checkbutton(self, x, y, **kwargs):
        '''
        create checkbutton with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Checkbutton widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Checkbutton, **kwargs)

    def create_entry(self, x, y, **kwargs):
        '''
        create text entry box with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Entry widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Entry, **kwargs)
    
    def create_frame(self, x, y, **kwargs):
        '''
        create frame with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Frame widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Button, **kwargs)

    def create_label(self, x, y, **kwargs):
        '''
        create label with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Label widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Label, **kwargs)

    def create_labelframe(self, x, y, **kwargs):
        '''
        create label with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the LabelFrame widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, LabelFrame, **kwargs)

    def create_listbox(self, x, y, **kwargs):
        '''
        create listbox with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Listbox widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Listbox, **kwargs)

    def create_panedwindow(self, x, y, **kwargs):
        '''
        create panned window with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the PanedWindow widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, PanedWindow, **kwargs)

    def create_radiobutton(self, x, y, **kwargs):
        '''
        create radiobutton with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Radiobutton widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Radiobutton, **kwargs)
    
    def create_scale(self, x, y, **kwargs):
        '''
        create scale with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Scale widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Scale, **kwargs)
    
    def create_scrollbar(self, x, y, **kwargs):
        '''
        create scrollbar with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Scrollbar widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Scrollbar, **kwargs)

    def create_spinbox(self, x, y, **kwargs):
        '''
        create spinbox with cordinates x y

        Kwargs are automatically allocated to the correct element, i.e background will be "allocated" towards the Spinbox widget while "anchor" will be allocated to the window creation
        '''
        return self._create_widget(x, y, Spinbox, **kwargs)


class AnalyticGeometry:
    '''perform basic analytic geometry'''

    @staticmethod
    def make_eqn(slope, *pt):
        '''gets the parts of an equation'''
        properties = {}
        if slope == None: #got errors becase 0 evaulates to False
            properties = {
                "m": None,
                "x": pt[0]
            }
        
        elif slope == 0:
            properties = {
                "m": 0,
                "y": pt[1]
            }
        
        else:
            properties = {
                "m": slope,
                "b": pt[1]-slope*pt[0]
            }

        return properties

    @staticmethod
    def perpendicular_slope(eqn):
        '''gets the perpendicular slope of an equation'''
        if "m" not in eqn or not eqn["m"]:
            if "y" in eqn:
                perpendicular = None
            elif "x" in eqn:
                perpendicular = 0
        else:
            if float(eqn["m"]) == 0: perpendicular = None
            else: perpendicular = -(1/float(eqn["m"]))
        return perpendicular

    @staticmethod
    def get_poi(eqn1, eqn2):
        '''gets the point of intersection between two lines'''
        poi = ()

        flat = False
        if "x" in eqn1:
            flat = eqn1["m"] in (None, 0) and eqn2["m"] in (None, 0)
        elif "y" in eqn1:
            flat = eqn2["m"] in (None, 0) and eqn1["m"] in (None, 0)

        if flat:
            if "x" in eqn1:
                poi = float(eqn1["x"]), float(eqn2["y"])
            else:
                poi = float(eqn2["x"]), float(eqn1["y"])
        else:
            if "b" not in eqn1: eqn1["b"] = 0
            if "b" not in eqn2: eqn2["b"] = 0
            x = (
                (float(eqn1["b"])-float(eqn2["b"])) /
                (float(eqn2["m"])-float(eqn1["m"]))
            )
            y = float(eqn1["m"])*x + float(eqn1["b"])
            poi = (x, y)

        return poi


class Transformations:
    '''define transformation methods'''

    def rotate(self, tagOrId, x, y, amount, unit = "rad", warn = True):
        '''rotate obj on axis x, y by amount in degrees or radians clockwise'''
        if unit in ("d", "deg", "degree", "degrees"):
            amount *= math.pi/180 #convert to radians
        elif unit in ("r", "rad", "radian", "radians"):
            pass
        else:
            raise InvalidUnitError("Invalid unit \"" + unit + "\"")
        
        angle = cmath.exp(amount*1j)
        offset = complex(x, y)
        newCords = []
        cords = [
            (self.coords(tagOrId)[i], self.coords(tagOrId)[i+1]) for i in range(0, len(self.coords(tagOrId)), 2)
        ]
        for xPt, yPt in cords:
            num = angle * (complex(xPt, yPt) - offset) + offset
            newCords.append(num.real)
            newCords.append(num.imag)
        
        objType = self.tk.call(self._w, 'type', tagOrId)
        if objType == "polygon":
            self.coords(tagOrId, *newCords)
        else:
            if (warn):
                warnings.warn(
                    "WARNING! Canvas element of type " + objType + " is not supported. Rotation may not look as expected. " + 
                    "Use the to_polygon() method to turn the " + objType + " into a polygon.",
                    UnsupportedObjectType
                )
            self.coords(tagOrId, *newCords)
        return newCords

    def flip(self, tagOrId, **eqn):
        '''flips tagOrId on line eqn. eqn should be either {y: val}, {x: val}, or {m: val, b: val} m being slope and b being y-intercept'''
        if len(eqn) == 0: raise InvalidEquation("Empty equation")

        for key, _ in eqn.items():
            if key != "x": eqn[key] = float(eqn[key]) * -1

        if "x" in eqn and "m" not in eqn:
            eqn["m"] = None
        elif "y" in eqn and "m" not in eqn:
            eqn["m"] = 0

        all_cords = self.coords(tagOrId)
        cords = [
            (all_cords[i], all_cords[i+1]) for i in range(0, len(all_cords), 2)
        ]

        #perpendicular slope
        perSlope = AnalyticGeometry.perpendicular_slope(eqn)

        #perpendicular eqnations
        perEqns = [AnalyticGeometry.make_eqn(perSlope, i[0], -i[1]) for i in cords]

        #Points of intersect
        POIs = [AnalyticGeometry.get_poi(eqn, i) for i in perEqns]

        newPts = [] #new points

        for i in range(len(POIs)): #get new points
            newPts.append((
                POIs[i][0]-(cords[i][0]-POIs[i][0]),
                (-(POIs[i][1])-cords[i][1])-POIs[i][1]
            ))
        
        newCords = []
        for i in newPts:
            newCords.append(i[0])
            newCords.append(i[1])
        
        self.coords(tagOrId, *newCords)
        return newPts
        
    reflect = flip

    def resize(self, tagOrId, scale, x, y):
        '''Resizes tagOrId by scale with point x, y'''
        vals = self.coords(tagOrId)
        coords = [(vals[i], vals[i+1]) for i in range(0, len(vals), 2)]
        newCoords = []

        if scale < 1:
            for x1, y1 in coords:
                newCoords.append(x1 + (x - x1)*scale)
                newCoords.append(y1 - (y1 - y)*scale)
        elif scale > 1:
            for x1, y1 in coords:
                newCoords.append(x - (x - x1)*scale)
                newCoords.append(y - (y - y1)*scale)
        
        self.coords(tagOrId, *newCoords)
        return newCoords


class CanvasPlus(Canvas, WidgetWindows, Transformations):
    '''Improved Canvas widget with more functionality to display graphical elements like lines or text.'''

    def clone(self, tagOrId, *args):
        '''clones tagOrId and places is at optional coordinates, or places is on top of the first object'''
        if len(args) == 0:
            args = self.coords(tagOrId)
        
        output = self.get_attributes(tagOrId)
        
        return self._create(
            self.tk.call(self._w, 'type', tagOrId),
            args,
            output
        )
        
    def create_arrow(self, x1, y1, headLength, headWidth, bodyLength, bodyWidth, **kwargs):
        '''Create arrow with x1, y1 as the tip; headWith, headLengh as the length and width of the arrowhead; and bodyLength, bodyWidth as the length and width of the arrow body, as well as direction = val (0 by default)'''
        
        points = [
            x1, y1,
            x1-headWidth//2, y1+headLength,
            x1-bodyWidth//2, y1+headLength,
            x1-bodyWidth//2, y1+bodyLength,
            x1+bodyWidth//2, y1+bodyLength,
            x1+bodyWidth//2, y1+headLength,
            x1+headWidth//2, y1+headLength
        ]
        
        return self._create('polygon', points, kwargs)

    def create_circle(self, x, y, radius, **kwargs):
        '''Create circle with coordinates x, y, radius'''
        return self._create('oval', [x+radius, y+radius, x-radius, y-radius], kwargs)

    def create_round_rectangle(self, x1, y1, x2, y2, radius = 25, **kwargs):
        '''Create circle with coordinates x1, y1, x2, y2, radius = val (default 25)'''
        points = [
            x1+radius, y1,
            x1+radius, y1,
            x2-radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1+radius, y2,
            x1, y2, 
            x1, y2-radius, 
            x1, y2-radius, 
            x1, y1+radius,
            x1, y1+radius, 
            x1, y1
        ]

        kwargs["smooth"] = True
        return self._create('polygon', points, kwargs)

    def get_attributes(self, tagOrId):
        '''Returns all properties of tagOrId'''
        properties = self.itemconfig(tagOrId)
        return {key: properties[key][-1] for key in properties}

    get_attr = get_attributes

    def __iter__(self):
        '''Creates iterator of everything on the canvas'''
        return iter(self.find_all())

    def to_polygon(self, tagOrId):
        '''converts rectangle to polygon'''
        output = self.get_attributes(tagOrId)

        cords = [self.tk.getdouble(x) for x in self.tk.splitlist(self.tk.call((self._w, 'coords') + tuple([tagOrId])))]

        if output["width"] == '0.0':
            output["outline"] = ''

        if self.tk.call(self._w, 'type', tagOrId) == "rectangle":
            newCords = [
                cords[0], cords[1],
                cords[2], cords[1],
                cords[2], cords[3],
                cords[0], cords[3]
            ]
        else:
            raise InvalidObjectType("Invalid canvas element \"" + self.tk.call(self._w, 'type', tagOrId) + "\"")

        self.tk.call((self._w, 'delete') + tuple([tagOrId]))

        return self._create('polygon', newCords, output)

    poly = to_polygon

    def tags_bind(
        self, tagsOrIds, sequences = None, funcs = None, add = False):
        '''Binds either multiple tags to one function, or multiple tags to multiple functions with matching indicies in one function
        
        i.e (tag1, tag2, tag3), func1 will bind tag1, tag2, tag3 into fun1, while (tag1, tag2, tag3), (func1, func2, func3) will bind tag1 to func1, tag2 to func2, tag3 to func3.
        '''
        if type(tagsOrIds) == int and callable(funcs): #normal tag_bind
            return self._bind((self._w, 'bind', tagsOrIds),sequences, funcs, add)
        else:
            bindings = []
            if type(funcs) not in [list, tuple]:
                funcs = tuple([funcs])
            if type(sequences) not in [list, tuple]:
                sequences = tuple([sequences])

            for index, obj in enumerate(tagsOrIds):
                bindings.append(
                        self._bind((self._w, 'bind', obj),
                        sequences[index%len(sequences)],
                        funcs[index%len(funcs)],
                        add
                    )
                )
            return bindings


def _test():
    #Imports
    from tkinter import Tk, StringVar, DoubleVar
    import math

    #set up canvas
    root = Tk()
    canvas = CanvasPlus(root, width=800, height=800, background = "white")
    canvas.pack()
    #create circle function
    canvas.create_circle(300, 600, 100, fill = "black", outline = "green", width = 3)
    
    #create rounded rectangle function
    canvas.create_round_rectangle(
        400, 550, 500, 650, radius = 75, fill = "blue", outline = "orange", width = 5
    )   

    #create arrow function and rotate it to by 310 degrees clockwise
    arrow = canvas.create_arrow(600, 600, 50, 50, 150, 20, fill = "grey", outline = "black")
    canvas.rotate(arrow, 600, 600, 310, unit="deg")

    #create a rectangle and convert it to a polygon; then rotate it by pi/4 radians (45 degrees)
    rect = canvas.create_rectangle(100, 550, 200, 650, fill = "#f7a8c6", width = 0)
    canvas.clone(rect)
    rect = canvas.poly(rect)
    canvas.rotate(rect, 150, 600, math.pi/4)

    #create an entry and set it's default value
    content = StringVar()
    canvas.create_entry(0, 0, anchor = "nw", textvariable = content, fg = "blue", bg = "gold")
    content.set("This is CanvasPlus %s" % _canvasPlusVersion)

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
        5, 75, font = ("Times", "24"), fg = "black", bg = "green", text = "By Luke-zhang-04", anchor = "nw"
    )

    #flip example
    aPrime = canvas.create_polygon(500, 10, 500, 20, 550, 25, 600, 20, 600, 10, fill = "yellow", outline = "black")
    a = canvas.clone(aPrime)
    canvas.flip(a, m = .5, b = -200)

    canvas.update()
    canvas.mainloop()

if __name__ == "__main__":
    _test()