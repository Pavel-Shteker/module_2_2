print ("В этом упражнении требуется ввести три целых числа. Погнали: ")
first = int(input ("Первое - "))
second = int(input ("Второе - "))
third = int(input("Третье - "))
# print ("Для наглядности:", '1)', first, "2)", second, "3)", third)
if first == second == third:
    print (3)
elif first == second or first == third or second == third:
    print (2)
else:
    print (0)