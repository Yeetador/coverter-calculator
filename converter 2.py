########################################################################################################################
import time
########################################################################################################################
print("what you want to convert")
print("1 wheight")
print("2 length")
print("3 lbs kg")
print("4 inch cm")

select1 = input("select 1,2,3 or 4: ")

########################################################################################################################
num3 = 10
########################################################################################################################
if select1 == '1':
    num1 = float(input("select ammount: "))
    print("select what for number in the metric system your number is")
    location_on_the_ladder = input("select from: mm cm dm m dam hm and km: ")

    if location_on_the_ladder == 'mm':
        print("you have chosen", location_on_the_ladder, "you can go up 6 steps.")
        num2 = int(input("How many steps do you want to go up: "))
        yes_or_no = num2 <= 6

        if yes_or_no == bool(True):
            num4 = num1 / (num3 ** num2)
            print(num1, "/ (", num3, "**", num2, ") =", num4)
            time.sleep(60)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'cm':
        print("you have chosen", location_on_the_ladder, "you can go up 5 steps and 1 step down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 1

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 5

            if yes_or_no == bool(True):
                num4 = num1 / (num3*num2)
                print(num1, "/ (", num3, "**", num2, "=", num4,)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'dm':
        print("you have chosen", location_on_the_ladder, "you can go up 4 steps and 2 steps down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 2

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 4

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'm':
        print("you have chosen", location_on_the_ladder, "you can go up 3 steps and 3 seps down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 3

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 3

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'dam':
        print("you have chosen", location_on_the_ladder, "you can go up 2 steps and 4 steps down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 2

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 4

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'hm':
        print("you have", location_on_the_ladder, "you can go up 1 step and 5 steps up.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 1

            if yes_or_no == bool(True):
                num4 = num1 * (num3 * num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 5

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "*", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'km':
        print("you have chosen", location_on_the_ladder, "how many steps would you like to go down")
        num2 = int(input())
        yes_or_no = num2 <= 6

        if yes_or_no == bool(True):
            num4 = num1 * (num3 ** num2)
            print(num1, "* (", num3, "**", num2, ") =", num4,)
            time.sleep(60)

        else:
            print("wrong input")
            time.sleep(5)

    else:
        print("wrong input")
        time.sleep(5)
########################################################################################################################
elif select1 == '2':
    num1 = float(input("select ammount: "))
    print("select what for number in the metric system your number is: ")
    location_on_the_ladder = input("select from: mg cg dg g dag hg and kg: ")

    if location_on_the_ladder == 'mg':
        print("you have chosen", location_on_the_ladder, "you can go up 6 steps.")
        num2 = int(input("How many steps do you want to go up: "))
        yes_or_no = num2 <= 6

        if yes_or_no == bool(True):
            num4 = num1 / (num3 ** num2)
            print(num1, "/ (", num3, "*", num2, ") =", num4)
            time.sleep(60)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'cg':
        print("you have chosen", location_on_the_ladder, "you can go up 5 steps and 1 step down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 1

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'up':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 5

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4,)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'dg':
        print("you have chosen", location_on_the_ladder, "you can go up 4 steps and 2 steps down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 2

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 4

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'g':
        print("you have chosen", location_on_the_ladder, "you can go up 3 steps and 3 seps down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 3

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 3

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'dag':
        print("you have chosen", location_on_the_ladder, "you can go up 2 steps and 4 steps down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 4

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'up':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 2

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'hg':
        print("you have", location_on_the_ladder, "you can go up 1 step and 5 steps down.")
        up_or_down = input("do you want to go up or down?: ")

        if up_or_down == 'up':
            num2 = int(input("How many steps do you want to go up?: "))
            yes_or_no = num2 <= 1

            if yes_or_no == bool(True):
                num4 = num1 * (num3 ** num2)
                print(num1, "* (", num3, "**", num2, ") =", num4)
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        elif up_or_down == 'down':
            num2 = int(input("How many steps do you want to go down?: "))
            yes_or_no = num2 <= 5

            if yes_or_no == bool(True):
                num4 = num1 / (num3 ** num2)
                print(num1, "/ (", num3, "**", num2, ") =", num4, )
                time.sleep(60)

            else:
                print('wrong input')
                time.sleep(5)

        else:
            print('wrong input')
            time.sleep(5)

    elif location_on_the_ladder == 'kg':
        print("you have chosen", location_on_the_ladder, "how many steps would you like to go down")
        num2 = int(input())
        yes_or_no = num2 <= 6

        if yes_or_no == bool(True):
            num4 = num1 / (num3 ** num2)
            print(num1, "/ (", num3, "**", num2, ") =", num4, )
            time.sleep(60)

        else:
            print("wrong input")
            time.sleep(5)

    else:
        print("wrong input")
        time.sleep(5)
########################################################################################################################
elif select1 == '3':
    print("select operation")
    print("type 1 for lbs to kg")
    print("type 2 for kg to lbs")

    select = input("select 1 or 2 :")

    # lbs to kg
    if select == '1':
        num1 = float(input("select ammount :"))
        num2 = float(0.45359237)

        print(num1, "*", 0.45, "=")
        mul = num1 * num2
        print(mul, " kg")

        time.sleep(60)

    # kg to lbs
    elif select == '2':
        num1 = float(input("select ammount :"))
        num2 = float(2.20462262)

        print(num1, "*", 2.21, "=")
        mul = num1 * num2
        print(mul, " lbs")

        time.sleep(60)
########################################################################################################################
elif select1 == '4':
    print("select operation")
    print("type 1 for cm to inches")
    print("type 2 for inches to cm")

    select = input("select 1 or 2 :")

    # inches to cm
    if select == '1':
        num1 = float(input("select ammount :"))
        num2 = float(0.393700787)

        print(num1, "*", num2, "=")
        mul = num1 * num2
        print(mul, " inch")

        time.sleep(60)

    # cm to inches
    elif select == '2':
        num1 = float(input("select ammount :"))
        num2 = float(2.54)

        print(num1, "*", num2, "=")
        mul = num1 * num2
        print(mul, " cm")

        time.sleep(60)
########################################################################################################################
else:
    print("wrong input")
    time.sleep(5)
