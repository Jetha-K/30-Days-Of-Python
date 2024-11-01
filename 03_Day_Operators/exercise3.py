"""4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)."""

# base = int(input('Enter base:'))
# height = int(input('Enter height:'))
# tri_area = 0.5 * base * height
# print('Area of triangle:', tri_area)

"""5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)."""

# a = int(input('Enter side a:'))
# b = int(input('Enter side b:'))
# c = int(input('Enter side c:'))

# tri_peri = a + b + c
# print('Perimeter of Triangle:', tri_peri)

"""6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))"""

# length = int(input('Enter length:'))
# width = int(input('Enter width:'))

# area = length * width
# perimeter = 2 * (length+width)

# print('area:', area)
# print('perimeter', perimeter)

"""7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14."""

# radius = int(input('Enter radius:'))
# circle_area = 3.14 * (radius ** 2)
# circle_circum = 2 * 3.14 * radius
# print(circle_area)
# print(circle_circum)

"""8. Calculate the slope, x-intercept and y-intercept of y = 2x -2"""

# y = 0
# y_intercept = -2
# x_intercept = (y+2)/2

# print(x_intercept, ',', y_intercept)

"""9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)"""

# y1 = 2
# x1 = 2

# y2 = 10
# x2 = 6

# m = (y2 - y1)/(x2 - x1)
# print('slope:', m)


""" Compare the slopes in tasks 8 and 9."""

# slope1 = 2
# slope2 = 2

# print(slope1 == slope2)

""" Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0."""

# import math
# a = 1
# b = 6
# c = 9
# y = 0
# x = (-b + math.sqrt((6**2)-4*a*c))/2*a

# print('(', x, ',', y, ')')

""" Find the length of 'python' and 'dragon' and make a falsy comparison statement."""

# print('python length:', len('python'))
# print('dragon length:', len('dragon'))
# print(len('python') == len('dragon'))

""" Use and operator to check if 'on' is found in both 'python' and 'dragon' """

# print('on' in 'python' and 'on' in 'dragon')

""" I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence. """

# print('jargon' in 'I hope this course is not full of jargon')

""" Find the length of the text python and convert the value to float and convert it to string"""

# length = len('python')
# float = float(length)
# string = str(float)

# print(length, float, type(string))

""" Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python? """

# num = float(input('Enter number:'))

# remainder = num % 2

# if remainder == 0:
#     print('even')
# else:
#     print('odd')

""" Check if the floor division of 7 by 3 is equal to the int converted value of 2.7."""

# print(7 // 3 == int(2.7))

""" Check if type of '10' is equal to type of 10 """

# print('10' == 10)

""" Check if int('9.8') is equal to 10"""

# num = float('9.8')
# print(int(num) == 10)

""" Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?"""

# hours = int(input('Enter hours:'))
# rate = int(input('Enter rate:'))

# print('pay:', hours * rate)

""" Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years"""

# years = int(input('Enter years:'))
# to_seconds = 365.25*24*60*60
# print((years * to_seconds, 's')

""" Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125 """

# for i in range(1, 6):
#     print(f"{i} {1} {i} {i**2} {i**3}")
