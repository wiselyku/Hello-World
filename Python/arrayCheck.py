def checkArray(input_array):
	print('input array content is ', input_array)
	if 1 not in input_array:
		return False
	if 2 not in input_array:
		return False;
	if 3 not in input_array:
		return False;
	return True



data = [1,2,3,4]
check = checkArray(data)
if check == True:
	print("1, 2, 3 in the list of ", data)

if checkArray([1,2,3]):
	print("True")

if checkArray([1,2,5,6,7]):
	print("True")
else:
	print("False")
