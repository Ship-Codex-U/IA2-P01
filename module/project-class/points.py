from point import Point

class Points:
    def __init__(self):
        self.__points = []

    def insert_point(self, point:Point):
        self.__points.append(point)
    
    def get_points(self):
        return self.__points
    
    def __str__(self):
        result = ""
        for p in self.__points:
            result += f"({p.x_coordinate}, {p.y_coordinate})\n"
        return result
    
    def __len__(self):
        return len(self.__points)
    
    def __iter__(self):
        self.__iter = 0
        return self
    
    def __next__(self):
        if self.__iter < len(self.__points):
            result = self.__points[self.__iter]
            self.__iter += 1
            return result
        else:
            raise StopIteration
        
    def __getitem__(self, key):
        return self.__points[key]
    
    def __setitem__(self, key, value):
        self.__points[key] = value

    def __delitem__(self, key):
        del self.__points[key]

    def __contains__(self, item):
        return item in self.__points
    
    def __add__(self, other):
        new_points = Points()
        new_points.__points = self.__points + other.__points
        return new_points
    
    def __iadd__(self, other):
        self.__points += other.__points
        return self
    
    def __mul__(self, scalar):
        new_points = Points()
        new_points.__points = self.__points * scalar
        return new_points
    
    def __imul__(self, scalar):
        self.__points *= scalar
        return self
    
    def __eq__(self, other):
        return self.__points == other.__points
    
    def __ne__(self, other):
        return self.__points != other.__points
    
    def __lt__(self, other):
        return self.__points < other.__points
    
    def __le__(self, other):
        return self.__points <= other.__points
    
    def __gt__(self, other):
        return self.__points > other.__points
    
    def __ge__(self, other):
        return self.__points >= other.__points
    
    def __reversed__(self):
        return reversed(self.__points)
    
    def __add__(self, other):
        return self.__points + other.__points
    
    def __sub__(self, other):
        return self.__points - other.__points   
    
    def __mul__(self, other):
        return self.__points * other.__points  
    
    def __truediv__(self, other):
        return self.__points / other.__points
    
    
