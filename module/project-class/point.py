class Point:
    def __init__(self, x_coordinate = -1, y_coordinate = -1, red = 255, green = 255, blue = 255 ) -> None:
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__red = red
        self.__green = green
        self.__blue = blue 
    
    @property
    def x_coordinate(self):
        return self.__x_coordinate
    
    @x_coordinate.setter
    def x_coordinate(self, x_coordinate):
        self.__x_coordinate = x_coordinate
        
    @property
    def y_coordinate(self):
        return self.__y_coordinate
    
    @y_coordinate.setter
    def y_coordinate(self, y_coordinate):
        self.__y_coordinate = y_coordinate
    
    @property
    def red(self):
        return self.__red
    
    @red.setter
    def red(self, red):
        self.__red = red
    
    @property
    def green(self):
        return self.__green
    
    @green.setter
    def green(self, green):
        self.__green = green
    
    @property
    def blue(self):
        return self.__blue
    
    @blue.setter
    def blue(self, blue):
        self.__blue = blue

    def getColor(self):
        return (self.__red, self.__green, self.__blue)
    
    def setColor(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue
        