while True:
    loop = True
    test = 0
    while loop == True :
        number = input('yo gimme a number so I can tell you if its prime : ')
        if number.isdigit() == True :
            loop = False
        else :
            print(number + ' isnt a number, try again')
            print(' ')

    if int(number) % 2 == 0 and number != '2' :
        test = test + 1

    if int(number) % 3 == 0 and number != '3' :
        test = test + 1
    
    if int(number) % 5 == 0 and number != '5' :
        test = test + 1
   
    if int(number) % 7 == 0 and number != '7' :
        test = test + 1

    if int(number) % 11 == 0 and number != '11' :
        test = test + 1

    if int(number) % 13 == 0 and number != '13' :
        test = test + 1

    if test == 0:
        if number == '1' :
            print( number + ' is not prime')
        else:
            print( number + ' is prime')
    else:
        print( number + ' is not prime')
    print(' ')
  
