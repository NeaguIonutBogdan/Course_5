from itertools import chain
def capitalize_string(my_string1):
    if my_string1[-1] == '.':
        if my_string1 == my_string1.capitalize():
            print(my_string1)
        else:
            my_string1 = my_string1.capitalize()
            print(my_string1)
    else:
        print("proprozitia nu se termina cu '.'")
d = {}
def sting_to_dictionar(my_string2):
    my_string2 = "Sa vedem ce se intampla cu pisica!"
    for x in my_string2:
        global d
        if x not in d:
            d[x] = my_string2.count(x)
    print(d, end=" ")
# def count_letters(string):
#     print( {letter: string.count(letter) for letter in string})
if __name__ == "__main__":
    input_string = input("introduceti o fraza aici: ")# "a vedem ce se intampla cu pisica!"
    capitalize_string(input_string)
    sting_to_dictionar(input_string)
    #count_letters("Sa vedem ce se intampla cu pisica!")

