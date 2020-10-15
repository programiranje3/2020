# # Hello world: the print() built-in function and the + operator
# print("John Lennon")
# print('John Lennon ' + 'was born in 1940.')
# print('John Lennon', 'was born in 1940.')
# print('John Lennon', 'was born in', 1940, '.')
# print('John Lennon', 'was born in', str(1940) + '.')
# print()
# print('John Lennon', '\nwas born in', str(1940) + '.')


# # The input() built-in function
# # year = input('Read the year when John was born: ')
# # print(year)
# print('Read the year when John was born: ', end='')
# year = input()
# print(year)


# # A simple function and function call
# # def print_year():
# #     print(1940)
# #
# #
# # print_year()
#
#
# # def print_year2(year):
# #     if year:
# #         print(year)
# #     else:
# #         print(None)
# #
# #
# # print_year2('')
#
#
# def f(a, b):
#     if a:
#         return a
#     elif b:
#         return b
#     else:
#         return None
#
#
# print(f(0, ''))


# # A simple loop and the range() built-in function
# print(range(5))
# for i in range(5):
#     print(i)
# print(', '.join(str(i) for i in range(5)))

# # A simple list, accessing list elements, printing lists
# theBeatles = ['John', 'Paul', 'George', 'Ringo']
# print(theBeatles)
# print(theBeatles[0])
# print()
# for i in range(4):
#     print(theBeatles[i])
# print(', '.join(theBeatles))
# print()
#
# # Looping through list elements - for and enumerate()
# print(enumerate(theBeatles))
# print(list(enumerate(theBeatles)))
# print()
# for i, j in list(enumerate(theBeatles)):
#     print(str(i) + ': ', j)
#     # print(i, j)

# # Global variables: __name__, __file__, __doc__,...
# print(__name__)
# print(__file__)
# print(__doc__)

from python import inception
inception.print_year()
# import python.inception
# python.inception.print_year()
print(__name__)


# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
