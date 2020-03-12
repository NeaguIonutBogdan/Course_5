import math

x_is_prim = 0
y_not_prim = 0
z_is_patrat = 0
w_not_patrat = 0
counter = 0


def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            global y_not_prim
            y_not_prim += 1
            global counter
            counter += 1
            return False
        else:
            global x_is_prim
            x_is_prim += 1
            # global counter
            counter += 1
            return True


# print("nr prim de {} ori.".format(x_is_prim))
# print("nr Nu e  prim de {} ori.".format(y_not_prim))

def patrat_perfect(a):
    if math.sqrt(a) * math.sqrt(a) == a:
        global z_is_patrat
        z_is_patrat += 1
        global counter
        counter += 1
        return True
    else:
        global w_not_patrat
        w_not_patrat += 1
        counter += 1
        return False
        print()


if __name__ == "__main__":
    loop = True
    int_choice = -1
    while loop:
        choice = input("daca vrei sa te joci introdu '1', pt Exit introdu 'q': ")
        if choice == '1':
            # print("buna")
            nr1 = int(input("introdu nr: "))
            print(is_prime(nr1))
            print("nr prim de {} ori.".format(x_is_prim))
            print("nr Nu e  rim de {} ori.".format(y_not_prim))
            print(patrat_perfect(nr1))
            print("nr e patrat perfect de {} ori.".format(z_is_patrat))
            print("nr Nu e patrat perfect de {} ori.".format(w_not_patrat))
            print("cate nr s-au verificat pan acum: {}".format(counter//2))
        if choice == 'q':
            loop = False
