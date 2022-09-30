class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def set_width(self,new_width):
        self.width=new_width

    def set_height(self,new_height):
        self.height=new_height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width+2*self.height

    def get_diagonal(self):
        return (self.width**2+self.height**2)**0.5

    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            raise ValueError("Too big for picture")
        for i in range(1,self.height+1):
            print("*"*self.width)

class Square(Rectangle):
    def __init__(self,side):
        self.width=side
        self.height=side 

    def set_side(self,new_side):
        self.side=new_side

print(Square(7).get_area())
