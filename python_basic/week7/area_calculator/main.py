import rectangle
import square
import circle
import triangle
import hexagon


# r1=rectangle.Rectangle(4,5)
# s1=square.Square(4)
# t1=triangle.Triangle(6,8,6,3,8)
# c1=circle.Circle(4)
# h1=hexagon.Hexagon(5)
#
# shapes_list=[r1,s1,t1,c1,h1]
# for shape in shapes_list:
#     print(shape)
#


def menu():
    print('1.to rectangle ')
    print('2.to square ')
    print('3.triangle ')
    print('4.to circle ')
    print('5.to hexagon ')
    print('0.to exit ')


def validation(*nums):
    for num in nums:
        if num <=0:
            print('invalid number: smaller or equal to 0')
            return False

        return True



def main():
    menu()
    try:
        choice = int(input('please choice:'))
        if choice==0:
            print('good bye')
            exit()
        elif choice== 1:
            width=int(input('enter the width'))
            height=int(input('enter the height'))
            if validation(width,height):
                print(rectangle.Rectangle(width,height))
        elif choice== 2:
            side=int(input('enter the side:'))
            if validation(side):
                print(square.Square(side))
        elif choice== 3:
            base=int(input('enter the base:'))
            height=int(input('enter the heigth'))
            side1=int(input('enter the side1'))
            side2=int(input('enter the side2'))
            side3=int(input('enter the side3'))
            if validation(base,height,side1,side2,side3):
                print(triangle.Triangle(base, height, side1, side2, side3))
        elif choice== 4:
            radius=int(input('enter the radius'))
            if validation(radius):
                print(circle.Circle(radius))
        elif choice== 5:
            side=int(input('enter the side'))
            if validation(side):
                print(hexagon.Hexagon(side))
        else:
            main()
    except ValueError as e:
        print('enter only numbers')
        main()

main()