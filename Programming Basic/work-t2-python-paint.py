height = float(input('enter the height of your room in metre'))
width = float(input('enter the width of your room in metre'))
length = float(input('enter the length of your room in metre'))
unpaintable_dimension = float(input('enter the total unpaintable area of your house in m^2'))
paint_layers = int(input('enter the layers of paint you want to paint'))

total_dimension = height * width * 2 + height * length * 2 + length * width - unpaintable_dimension

print('you need', round((total_dimension*paint_layers)/11, 2), 'litres of paint')