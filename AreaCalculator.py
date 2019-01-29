"""This is a calculator"""

print "Starting the calculator...."

option = raw_input (" Enter C for Circle or T for Triangle: ")
if option == 'C':
  print "Area of Circle is: area = phi x R2"
  radius = float(raw_input ("Enter a radius of Circle: "))
  area = 3.14159 * (radius ** 2)
  print "Area of Circle is: %f" %area
elif option == 'T':
  print "Area of Triangle is: area = 1/2 x B x H"
  base = float (raw_input ("Enter a base of Triangle: "))
  height = float (raw_input ("Enter a height of Triangle: "))
  area = 0.5 * base * height
  print "Area of Trinagle is: %f"  %area
else:
  print "You dont input any or false input"
  print "Exiting..."
