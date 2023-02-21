# number = int(input('Enter the number: '))
## Positive or negetive
# if number >0:
#     print('It is a positive number')
# elif number == 0:
#     print('This is zero')
# else:
#     print('This is negetive number')

## Even or odd
# if number % 2 ==0:
#     print('Number is even')
# else:
#     print('Number is odd')

## Leap year
# if number % 100 != 0: 
#     if number % 4 ==0:
#         print("It is a leap year")
#     else:
#         print('Not a leap year')
# elif number % 400 == 0:
#     print('It is a leap year')
# else:
#     print('Not a leap year')

## Area of sqare or circle
# choice = int(input('Please enter 1 for Square 2 for Circle: '))
# if choice == 1:
#     side = int(input('Please tell me side of Square: '))
#     area = side * side
#     print('Area of Square: ', area)
# elif choice == 2:
#     rad = int(input('Please tell me radius of Circle: '))
#     area = 3.14 * rad * rad
#     print('Area of Circle: ', area)
# else:
#     print("Input correct choice")

## vowel or not
# charector = str(input('Please input a charector: ')).lower()
# vowels = ['a','e','i','o','u']
# if charector in vowels:
#     print(charector, ': is vowel')
# else:
#     print(charector, ': is consonent')

## input 3 number to sum > 1000
# n1 = int(input('Enter first number: '))
# n2 = int(input('Enter second number: '))
# n3 = int(input('Enter third number: '))
# if(n1+n2+n3)>1000:
#     print('You Won!')
# else:
#     print('Try again')

## Armstrong number

## Print number series incresing order
# def shasha(start, stop, step):
#     for i in range(start, stop, step):
#         print(i)
# a = int(input('Enter number as start point: '))
# b = int(input('Enter number as stop point: '))
# c = int(input('Enter number for step up or down: '))
# shasha(a, b, c)

## Print numbers 1 to 100 using while loop
def siya(i,n):
    sum = 0
    while i <= n:
        sum = sum + i
        print(sum)
        i = i + 1
start = int(input('Enter start number: '))
end = int(input('Enter end number: '))
siya(start, end)

i = 1
n = 1
sum = 0
while i <= n:
    #sum = sum + i
    print(sum)
    i = i + 1




