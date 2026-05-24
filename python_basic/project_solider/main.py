from solider_manager import add_solider








def show_menu():
    print('0.to exit')
    print('1.to add a new solider')
    print('2.to remove a solider')
    print('3.to show the solider list')
    print('4.to add a new duty')
    print('5.to update duty status')
    print('6. to show a solider duty')






def handle_solider():
    while  True:
     name=input('please enter the solider name:')
     if name=='0':
         print('good bye')
         exit()
     id=int(input('please enter rhe id:'))

     try:
            add_solider(id,name)
            print('solier added ')
            break

     except ValueError as e:
            print(e)
            print('try again or press 0 to exit')











def main():
    show_menu()
    user_choice=input('enter your choice:')
    if user_choice== '0':
        print('good bye')
        exit()
    elif user_choice=='1':
        handle_solider()
    elif user_choice=='2':
        pass
    elif user_choice=='3':
        pass
    elif user_choice=='4':
        pass
    elif user_choice=='5':
        pass
    elif user_choice=='6':
        pass

    else:
        print('invalid input!!')
        main()


main()