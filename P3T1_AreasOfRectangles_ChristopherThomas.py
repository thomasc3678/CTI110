# Areas of rectangles tutorial
# 25 June 2019
# CTI-110 P3T1 - Areas of Rectangles
# Christopher Thomas
#
#Input the length and width of rectangle1
#Input the length and width of rectangle2
#Calculate the area of rectangle1
#Calculate the area of rectangle2
#if area1 > area2
#   Display"Rectangle1 has the greatest area."
#else if area2 > area1
#   Display"Rectangle2 has the greatest area.
#else
#   Display"Both rectangles have the same area"

# Get the dimensions of rectangle1.
length1 = int(input('Enter the length of rectangle1: '))
width1 = int(input('Enter the width of rectanglte1: '))

# Get the dimensions of rectangle2.
length2 = int(input('Enter the length of rectangle2: '))
width2 = int(input('Enter the width of rectanglte2: '))

# Calculate the area of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greater area.

if area1 > area2:
    print('Retangle1 has the greater area')
elseif area2 > area1:
    print('Rectangle2 has the greater area')
else:
    print('Both have the same area.'"
