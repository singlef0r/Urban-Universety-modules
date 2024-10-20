my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
id = 0
while id != len(my_list):
	if my_list[id] > 0:
		print(my_list[id])
		id += 1
	elif my_list[id] == 0:
		id += 1
		continue
	else:
		break
