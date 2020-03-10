import math
x_is_prim = 0
y_not_prim = 0
z_is_patrat = 0
w_not_patrat = 0
counter = 0

def is_prime(a):
	if a <= 1:
		return False
	for i in range(2,a):
		if a % i == 0 :
			global y_not_prim
			y_not_prim += 1
			return False
		else:
			global x_is_prim
			x_is_prim+=1
			return True
#print(is_prime(2))
print(is_prime(3))
print(is_prime(7))
print(is_prime(14))
print(is_prime(14))
print("nr prim de {} ori.".format(x_is_prim))
print("nr Nu e  rim de {} ori.".format(y_not_prim))
# def patrat_perfect(a):
# 	if math.sqrt(a)*math.sqrt(a) == a:
# 		global z_is_patrat
# 		z_is_patrat += 1
# 		return True
# 	else:
# 		global w_not_patrat
# 		w_not_patrat += 1
# 		return False
# 		print()
# # print(patrat_perfect(16))
# # print(patrat_perfect(7))
# # print(patrat_perfect(4))
# print(z_is_patrat)
# print(w_not_patrat)
# print()
# password = ''

# while password != 'password':
#     print('What is the password?')
#     password = input()

# print('Yes, the password is ' + password + '. You may enter.')
# loop = True
# int_choice = -1
# #n=input("Introduceti un nr intreg: ")
# while loop:
# 	choice = int(input("Enter your choice [1-4]: "))
# 	if choice == '1':
# 		int_choice = 1
# 		print("buna")
# 	# print("Finish.")
# 	# nr1 = input("introdu nr: ")
# 	# is_prime(nr1)
# 	# patrat_perfect(nr1)
# 	# print("nr prim de {} ori.".format(x_is_prim))
# 	# print("nr Nu e  rim de {} ori.".format(y_not_prim))
# 	# print(z_is_patrat)
# 	# print(w_not_patrat)
# 	loop = False