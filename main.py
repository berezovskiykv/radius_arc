import math

def radius(lengh, height):
	# Расчитаем центральный угол α, т.е. угол между радиусами, проведенными из начала и конца сегмента
	alpha = 4 * (math.atan(2 * height / lengh))
	# Рачитаем радиуса
	R = height / (1 - math.cos(alpha / 2))
	return R
	
in_lengh = input("Введите длину хорды ")

in_height = input("Введите высоту сегмента ")

print("Радиус равен ")
print(radius(int(in_lengh), int(in_height)))
