from math import pi

class MyCircle:
    _radius=0
    _diameter = 0
    _circle_area=0


    def __init__(self, radius=None, diameter=None,circle_area=None):
        if radius is not None:
            self._radius = radius
            self._diameter = radius*2
            self._circle_area = radius**2*pi
        elif diameter is not None:
            self._diameter = diameter
            self._radius = diameter/2
            self._circle_area = self.radius**2*pi
        elif circle_area is not None:
            self._circle_area = circle_area
            self._radius =  (circle_area/pi)**0.5
            self._diameter = self._radius*2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = self._radius * 2
        self._circle_area = self.radius**2*pi


    @property
    def circle_diameter(self):
        return self._diameter
    
    @circle_diameter.setter
    def circle_diameter(self, value):
        self._diameter = value
        self._radius = self._diameter / 2
        self._circle_area = self.radius**2*pi 
    
    @property
    def circle_area(self):
        return self._circle_area

    @circle_area.setter
    def circle_area(self, value):
        self._circle_area = value
        self._radius = (self._circle_area / pi)**0.5
        self._diameter = self._radius * 2

    def __add__(self, other):
        return self.circle_area + other.circle_area

    def __lt__(self, other):
        return self.circle_area < other.circle_area

    def __eq__(self, other):
        return self.circle_area == other.circle_area

    def __str__(self):
            return f"My Circle has a radius of {self._radius} and a diameter of {self._diameter} and an area of {self._circle_area}" 



