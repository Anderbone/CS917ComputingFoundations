""" This module contains classes that form the basis for part 2 of the assignment

    Refer the the coursework assignment for instructions on how to complete this part.

    Author:Jiyu Yan
    Student ID: 1851015
"""


class Point:

    def __init__(self, x, y):
        self.px = x
        self.py = y

    def set(self, x, y):
        self.px = x
        self.py = y

    def get(self):
        return self.px, self.py

    def equals(self, point):
        if abs(self.px - point.px) < Shape.TOLERANCE and\
                abs(self.py - point.py) < Shape.TOLERANCE:
            return True
        else:
            return False

    def distance(self, point):
        dis = ((self.px-point.px)**2+(self.py-point.py)**2)**0.5
        return dis


class Shape:
    """This class is a convenient place to store the tolerance variable"""
    TOLERANCE = 1.0e-6


class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def get(self):
        return self.centre, self.radius

    def set(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __str__(self) -> str:
        str_c = ('This circle has its centre at (%.2f,%.2f) and a radius of %.2f.'
                 % (self.centre.px, self.centre.py, self.radius))
        print(str_c)

    def area(self):
        return 3.1415926*float(self.radius)**2

    def compare(self, shape):
        if self.area() > shape.area():
            return 1
        elif self.area() < shape.area():
            return -1
        else:
            return 0

    def envelops(self, shape):
        if type(shape) == Circle:
            if self.centre.distance(shape.centre)+shape.radius < self.radius:
                return True
            else:
                return False
        elif type(shape) == Square:
            # If a circle contains a square, the distance of the four point of the square to
            # the circle centre should less than the circle radius.
            if self.centre.distance(shape.top_left) < self.radius and \
                    self.centre.distance(shape.top_right) < self.radius and \
                    self.centre.distance(shape.down_left) < self.radius and \
                    self.centre.distance(shape.down_right) < self.radius:
                return True
            else:
                return False
        else:
            return False

    def equals(self, circle):
        if self.centre.equals(circle.centre) and \
                abs(self.radius - circle.radius) < Shape.TOLERANCE:
            return True
        else:
            return False


class Square:

    def __init__(self, top_left, length):
        self.top_left = top_left
        self.length = float(length)
        self.top_right = Point(self.top_left.px + self.length, self.top_left.py)
        self.down_left = Point(self.top_left.px, self.top_left.py - self.length)
        self.down_right = Point(self.top_right.px, self.top_right.py - self.length)
        self.cen = Point(self.top_left.px + self.length/2, self.top_left.py - self.length/2)

    def get(self):
        return self.top_left, self.length

    def set(self, top_left, length):
        self.top_left = top_left
        self.length = length

    def __str__(self):
        strs = ('This square’s top left corner is at (%.2f,%.2f)  and the side length is %.2f. ' % \
               (self.top_left.px, self.top_left.py, self.length))
        print(strs)

    def area(self):
        return self.length ** 2

    def compare(self, shape):
        if self.area() > shape.area():
            return 1
        elif self.area() < shape.area():
            return -1
        else:
            return 0

    def envelops(self, shape):
        if type(shape) == Circle:
            if self.cen.distance(shape.centre) + shape.radius < self.length/2:
                return True
            else:
                return False
        elif type(shape) == Square:
            if 0 < shape.top_left.px - self.top_left.px < self.length - shape.length and \
                    self.length - shape.length > self.top_left.py - shape.top_left.py > 0:
                return True
            else:
                return False
        else:
            return False

    def equals(self, square):
        if self.top_left.equals(square.top_left) and \
                abs(self.length - square.length) < Shape.TOLERANCE:
            return True
        else:
            return False


class Assignment:
    """ Store all squares and circles of file to squ_list[] and cir_list[]
    """
    squ_list = []
    cir_list = []

    def analyse(self, filename):
        """ Process the file here """

        with open(filename, 'r') as f:
            for line in f:
                line = line.split(' ')
                # print(line)
                if line[0] == 'square':
                    x = float(line[1])
                    y = float(line[2])
                    leng = float(line[3])
                    if leng <= 0:
                        continue
                    self.squ_list.append(Square(Point(x, y), leng))
                elif line[0] == 'circle':
                    x = float(line[1])
                    y = float(line[2])
                    r = float(line[3])
                    if r <= 0:
                        continue
                    self.cir_list.append(Circle(Point(x, y), r))
        return self.squ_list, self.cir_list

    def shape_count(self):
        return self.circle_count() + self.square_count()

    def circle_count(self):
        return len(self.cir_list)

    def square_count(self):
        return len(self.squ_list)

    def max_circle_area(self):
        cmax = 0
        for c in self.cir_list:
            if c.area() > cmax:
                cmax = c.area()
        return cmax

    def min_circle_area(self):
        cmin = 1000000
        for c in self.cir_list:
            if c.area() < cmin:
                cmin = c.area()
        return cmin

    def max_square_area(self):
        smax = 0
        for s in self.squ_list:
            if s.area() > smax:
                smax = s.area()
        return smax

    def min_square_area(self):
        smin = 1000000
        for s in self.squ_list:
            if s.area() < smin:
                smin = s.area()
        return smin

    def mean_circle_area(self):
        csum = 0
        for c in self.cir_list:
            csum += c.area()
        cmean = csum/self.circle_count()
        return cmean

    def mean_square_area(self):
        ssum = 0
        for s in self.squ_list:
            ssum += s.area()
        smean = ssum/self.square_count()
        return smean

    def std_dev_circle_area(self):
        csum2 = 0
        for c in self.cir_list:
            csum2 += (c.area() - self.mean_circle_area())**2
        cstd = (csum2/self.circle_count())**0.5
        return cstd

    def std_dev_square_area(self):
        ssum2 = 0
        for s in self.squ_list:
            ssum2 += (s.area() - self.mean_square_area())**2
        sstd = (ssum2/self.square_count())**0.5
        return sstd

    def median_circle_area(self):
        c_area = []
        for c in self.cir_list:
            c_area.append(c.area())
        c_area.sort()
        if self.circle_count() % 2 == 0:
            return c_area[int(self.circle_count()/2)] + c_area[int(self.circle_count()/2) - 1]
        else:
            return c_area[int((self.circle_count()-1)/2)]

    def median_square_area(self):
        s_area = []
        for s in self.squ_list:
            s_area.append(s.area())
        s_area.sort()
        if self.square_count() % 2 == 0:
            return s_area[int(self.square_count()/2)] + s_area[int(self.square_count()/2) - 1]
        else:
            return s_area[int((self.square_count()-1)/2)]


if __name__ == "__main__":
    # You should add your own code here to test your work
    print("=== Testing Part 2 ===")
    assignment = Assignment()
    # all = assignment.analyse("SmallShapeTest.data")
    assignment.analyse("1000shapetest.data")
    print('1.shape number is ' + str(assignment.shape_count()))
    print('1.max circle area is ' + str('%.2f' % assignment.max_circle_area()))
    print('1.min circle area is ' + str('%.2e' % assignment.min_circle_area()))
    print('1.max square area is ' + str('%.2f' % assignment.max_square_area()))
    print('1.min square area is ' + str('%.2e' % assignment.min_square_area()))
    print('2.mean of circle area is ' + str('%.2f' % assignment.mean_circle_area()))
    print('2.mean of square area is ' + str('%.2f' % assignment.mean_square_area()))
    print('3.std_dev of circle area is ' + str('%.2f' % assignment.std_dev_circle_area()))
    print('3.std_dev of square area is ' + str('%.2f' % assignment.std_dev_square_area()))
    print('4.median circle area is ' + str('%.2f' % assignment.median_circle_area()))
    print('4.median square area is ' + str('%.2f' % assignment.median_square_area()))

