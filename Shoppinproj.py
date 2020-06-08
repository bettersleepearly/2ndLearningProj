currency = 'USD' 
pricecruiser = {'CB1':"139" + currency,
'CB2':"149" + currency,
'CB3':"139" + currency,
'CB4':"139" + currency,
'CB5':"169" + currency,
'CB6':"139" + currency,
'CB7':"139" + currency,
'CB8':"139" + currency,
'CB9':"139" + currency,
'CB10':"149" + currency,
'CB11':"134" + currency,
'CB12':"129" + currency}

pricelongboard = {'LB1':"174" + currency,
'LB2':"174" + currency,
'LB3':"174" + currency,
'LB4':"199" + currency,
'LB5':"199" + currency,
'LB6':"199" + currency,
'LB7':"189" + currency,
'LB8':"189" + currency,
'LB9':"179" + currency,
'LB10':"244" + currency,
'LB11':"244" + currency,
'LB12':"244" + currency}

cb1 = 'Dinghy Tiger:'
cb2 = 'Dinghy FG Watercolor:'
cb3 = 'Dinghy Crown Peak:'
cb4 = 'Dinghy BK:'
cb5 = 'Gordito Pantera:'
cb6 = 'Ditchlife:'
cb7 = 'Wrecktangle Lighthouse:'
cb8 = 'Tugboat Captain:'
cb9 = 'Tugboat Chill Cat:'
cb10 = 'Tugboat Midnight Snek:'
cb11 = 'Dinghy Arctic Fox:'
cb12 = 'Mighty Mite:'

lb1 = 'Super Chief Watercolor:'
lb2 = 'Ripper Humanoid:'
lb3 = 'Ripper Watercolor:'
lb4 = 'Drop Carve 40 Fox:'
lb5 = 'Drop Cat 33 Illuminacion:'
lb6 = 'Drop Cat 38 Seeker:'
lb7 = 'Pinner Night Moves:'
lb8 = 'Totem Blaze:'
lb9 = 'Chief Eyes:'
lb10 = 'Switchblade 38 Tropic:'
lb11 = 'Nine Two Five Horror:'
lb12 = 'Hollowtech Switchblade 36 Lizard:'


print("\n _____________")
print("|             |")
print("|   L A N D   |")
print("| Y A T C H Z |")
print("|_____________|")

print('\nWE EXPLORE THE WORLD ON SKATEBOARDS \nWe make vehicles for seeking out adventure, finding joy in self-expression and improving our interactions with the world around us.')

print('\nInterested in our products? Wanna dive in?')

question = input('\nIf yes, type Y. \nType N to exit.')

if question == "N":
    print('___________________________________________________________________________________________________________________________________________________')
    print('\nWell then... Fuck off mate.')
if question == "Y":
    print('___________________________________________________________________________________________________________________________________________________')
    print("\nBefore finding you a perfect skateboard, \nLet's create a account")
 
    username = input('\nMay I have your username:')
    
    print("\nOkay" + " " + username + ",")

    print("May I have your age? (since our branding and products are not suited for ages under 18):")
    age = int(input())

    if age < 18:
        print('___________________________________________________________________________________________________________________________________________________')
        print("\nI am sorry that you can not countinue" + " " + username)
        print("\nUnderage usage of our products and contents is illegal...\nSo fuck off kid!")


    if age >= 18:
        print('___________________________________________________________________________________________________________________________________________________')
        print("\nRequirement reached,\nYour access is now granted")
        print("\nEnjoy shopping skateboards!")
        print("\nWe own a large varieties of skateboards and longboards with different styles and uses.")
        print("\nOur 2 main lines are recommended the most,")
        boards = input("\n(1) Cruiser boards\n(2) Longboards\nPick one (type a number):")

           
        if boards == "1":
            print('___________________________________________________________________________________________________________________________________________________')
            print("\nThe most fun and capable boards in our line-up, these boards are the best bang for your buck available today.")
            print('Whether it’s your first board or your tenth, there’s always room in your quiver for a good cruiser and you’ll quickly find it becoming your go-to in all sorts of situations.')
            print('So...Pick one (by typing "CB" + the number of the board):')

            print('___________________________________________________________________________________________________________________________________________________')
            print('\n1.'+cb1+ " "+ pricecruiser.get('CB1') + '\n(No Picture LMAO)')
            print('\n2.'+cb2+ " "+ pricecruiser.get('CB2') + '\n(No Picture LMAO)')
            print('\n3.'+cb3+ " "+ pricecruiser.get('CB3') + '\n(No Picture LMAO)')
            print('\n4.'+cb4+ " "+ pricecruiser.get('CB4') + '\n(No Picture LMAO)')
            print('\n5.'+cb5+ " "+ pricecruiser.get('CB5') + '\n(No Picture LMAO)')
            print('\n6.'+cb6+ " "+ pricecruiser.get('CB6') + '\n(No Picture LMAO)')
            print('\n7.'+cb7+ " "+ pricecruiser.get('CB7') + '\n(No Picture LMAO)')
            print('\n8.'+cb8+ " "+ pricecruiser.get('CB8') + '\n(No Picture LMAO)')
            print('\n9.'+cb9+ " "+ pricecruiser.get('CB9') + '\n(No Picture LMAO)')
            print('\n10.'+cb10+ " "+ pricecruiser.get('CB10') + '\n(No Picture LMAO)')
            print('\n11.'+cb11+ " "+ pricecruiser.get('CB11') + '\n(No Picture LMAO)')
            print('\n12.'+cb12+ " "+ pricecruiser.get('CB12') + '\n(No Picture LMAO)')
            print('___________________________________________________________________________________________________________________________________________________')

        if boards == "2":
            print('___________________________________________________________________________________________________________________________________________________')
            print('Our Longboards are designed to get you out exploring your environment, no matter what kind of terrain you have surrounding you.\nThe boards in this category come in two deck styles; Top mounted or Drop-through.')
            print('\nTop mount boards give you tons of leverage over your trucks, giving you a deeper carving, surfy feel and a lively ride underfoot.')
            print('Drop-through boards are lower to the ground, making them driftier, more stable and blurring the lines between longboarding and freeriding.')
            print('\n1.'+lb1+ " "+ pricelongboard.get('LB1') + '\n(No Picture LMAO)')
            print('\n2.'+lb2+ " "+ pricelongboard.get('LB2') + '\n(No Picture LMAO)')
            print('\n3.'+lb3+ " "+ pricelongboard.get('LB3') + '\n(No Picture LMAO)')
            print('\n4.'+lb4+ " "+ pricelongboard.get('LB4') + '\n(No Picture LMAO)')
            print('\n5.'+lb5+ " "+ pricelongboard.get('LB5') + '\n(No Picture LMAO)')
            print('\n6.'+lb6+ " "+ pricelongboard.get('LB6') + '\n(No Picture LMAO)')
            print('\n7.'+lb7+ " "+ pricelongboard.get('LB7') + '\n(No Picture LMAO)')
            print('\n8.'+lb8+ " "+ pricelongboard.get('LB8') + '\n(No Picture LMAO)')
            print('\n9.'+lb9+ " "+ pricelongboard.get('LB9') + '\n(No Picture LMAO)')
            print('\n10.'+lb10+ " "+ pricelongboard.get('LB10') + '\n(No Picture LMAO)')
            print('\n11.'+lb11+ " "+ pricelongboard.get('LB11') + '\n(No Picture LMAO)')
            print('\n12.'+lb12+ " "+ pricelongboard.get('LB12') + '\n(No Picture LMAO)')
            print('___________________________________________________________________________________________________________________________________________________')
             
            print('___________________________________________________________________________________________________________________________________________________')


pick = str(input())
cart = print("Your Cart:" + " " + str(pricecruiser.get(pick)))
print(cart)