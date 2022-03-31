from math import pi

class Circle:

    def __init__(self, radius):
            self._radius = radius
            self._diameter = radius*2
            self._circle_area = radius**2*pi

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter*0.5)

    @classmethod
    def from_area(cls, area):
        radius=(area/pi)**0.5
        return cls(radius)

    @property
    def radius(self):
        return self._radius
    
    @property
    def circle_diameter(self):
        return self.radius*2
    
    @property
    def circle_area(self):
        return self.radius**2*pi

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = self._radius * 2
        self._circle_area = self.radius**2*pi

    @circle_diameter.setter
    def circle_diameter(self, value):
        self.radius(value/2)
    
    @circle_area.setter
    def circle_area(self, value):
        self.radius((value/ pi)**0.5)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        return self.circle_area < other.circle_area

    def __eq__(self, other):
        return self.circle_area == other.circle_area

    def __str__(self):
            return f"My Circle has a radius of {self._radius} and a diameter of {self._diameter} and an area of {self._circle_area}" 



