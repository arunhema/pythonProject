# # Give me the discount
# # Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# #
# # The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.
#
# print ("Enter the full price")
# price = int(input())
# print ("Enter the discount price")
# discount = int(input())
#
# print("Final price:", price-(price*discount/100))
#
# #now
# #nnooww
#
#
# op_str=""
# inp_str = input()
# for c in inp_str:
#     op_str=op_str+(c*2)
# print(op_str)
#
#
# str1 = "abcdefg"
# print(str1[::-1])
#
# pset_time = 15
# sleep_time = 8
# print(sleep_time > pset_time)
# derive = True
# drink = False
# both = drink and derive
# print(both)
#
# x = 1
# print(x)
# x_str = str(x)
# print("my fav num is", x, ".", "x =", x)
# print("my fav num is " + x_str + ". " + "x = " + x_str)
#
# text = input("Type anything... ")
# print(5*text)
#
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x / y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
# print("thanks!")


def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
#    print ("factorial",x)
    if x == 1:
        return 1

    else:
        res=(x * factorial(x-1))
 #       print("factorial res", res)
        return (res)

num = 10
print("The factorial of", num, "is", factorial(num))