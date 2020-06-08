print("\n _____________")
print("|             |")
print("|   L A N D   |")
print("| Y A T C H Z |")
print("|_____________|")

print('\nWE EXPLORE THE WORLD ON SKATEBOARDS \nWe make vehicles for seeking out adventure, finding joy in self-expression and improving our interactions with the world around us.')

print('\nInterested in our products? Wanna dive in?')

question = input('\nIf yes, type Y. \nType N to exit.')

if question == "N":
    print('__________________________________________________________________________________________________________________')
    print('\nWell then... Fuck off mate.')
if question == "Y":
    print('__________________________________________________________________________________________________________________')
    print("\nBefore finding you a perfect skateboard, \nLet's create a account")
 
    username = input('\nMay I have your username:')
    
    print("\nOkay" + " " + username + ",")

    print("May I have your age? (since our branding and products are not suited for ages under 18):")
    age = int(input())

    if age < 18:
        print('__________________________________________________________________________________________________________________')
        print("\nI am sorry that you can not countinue" + " " + username)
        print("\nUnderage usage of our products and contents is illegal...\nSo fuck off kid!")


    if age >= 18:
        print('__________________________________________________________________________________________________________________')
        print("\nRequirement reached,\nYour access is now granted")
        print("\nEnjoy shopping skateboards!")
        print("\nWe own a large varieties of skateboards and longboards with different styles and uses.")
        print("\nOur 2 main lines are recommended the most,\nPick one (type a number):")
        boards = input("\n1.Cruiser boards\n2.Longboards")

        currency = ('USD')    
        if boards == "1":
            print('__________________________________________________________________________________________________________________')
            print("\nThe most fun and capable boards in our line-up, these boards are the best bang for your buck available today.")
            print('Whether it’s your first board or your tenth, there’s always room in your quiver for a good cruiser and you’ll quickly find it becoming your go-to in all sorts of situations.')
            print('So...Pick one (by typing "cruiser + the number of the board):')


        pricecruiser = {'cruiser1':'139' +currency,
        'cruiser2':'149' +currency,
        'cruiser3':'139' +currency,
        'cruiser4':'139' +currency,
        'cruiser5':'169' +currency,
        'cruiser6':'139' +currency,
        'cruiser7':'139' +currency,
        'cruiser8':'139' +currency,
        'cruiser9':'139' +currency,
        'cruiser10':'149' +currency,
        'cruiser11':'134' +currency,
        'cruiser12':'129' + currency}
            

        cartmoney = input(pricecruiser)
        while input(pricecruiser):
            print("\n                                                             Your Cart:" + " " + cartmoney + currency) 
            continue

       






    
