currency = 'USD' 
price = {'CB1':139,
'CB2':149,
'CB3':139,
'CB4':139,
'CB5':169,
'CB6':139,
'CB7':139,
'CB8':139,
'CB9':139,
'CB10':149,
'CB11':134,
'CB12':129,
'LB1':174,
'LB2':174,
'LB3':174,
'LB4':199,
'LB5':199,
'LB6':199,
'LB7':189,
'LB8':189,
'LB9':179,
'LB10':244,
'LB11':244,
'LB12':244}

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
        boards = "\n(1) Cruiser boards\n(2) Longboards\nPick one (type a number):"
        print(boards)
        boardpick = str(input())

           
        if boardpick == "1":
            print('___________________________________________________________________________________________________________________________________________________')
            print("\nThe most fun and capable boards in our line-up, these boards are the best bang for your buck available today.")
            print('Whether it’s your first board or your tenth, there’s always room in your quiver for a good cruiser and you’ll quickly find it becoming your go-to in all sorts of situations.')
            

            print('___________________________________________________________________________________________________________________________________________________')
            print('\n1.'+cb1+ " "+ str(price.get('CB1')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n2.'+cb2+ " "+ str(price.get('CB2')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n3.'+cb3+ " "+ str(price.get('CB3')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n4.'+cb4+ " "+ str(price.get('CB4')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n5.'+cb5+ " "+ str(price.get('CB5')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n6.'+cb6+ " "+ str(price.get('CB6')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n7.'+cb7+ " "+ str(price.get('CB7')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n8.'+cb8+ " "+ str(price.get('CB8')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n9.'+cb9+ " "+ str(price.get('CB9')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n10.'+cb10+ " "+ str(price.get('CB10')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n11.'+cb11+ " "+ str(price.get('CB11')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n12.'+cb12+ " "+ str(price.get('CB12')) +" "+ currency+'\n(No Picture LMAO)')
            
            print('\nSo...Pick one (by typing "CB" + the number of the board):')
            action = str(input('To return to the menu,\nType "menu"\nType "mycart" to go to your cart and further check-out there.'))
            print(action)
            print('___________________________________________________________________________________________________________________________________________________')

        if boardpick == "2":
            print('___________________________________________________________________________________________________________________________________________________')
            print('Our Longboards are designed to get you out exploring your environment, no matter what kind of terrain you have surrounding you.\nThe boards in this category come in two deck styles; Top mounted or Drop-through.')
            print('\nTop mount boards give you tons of leverage over your trucks, giving you a deeper carving, surfy feel and a lively ride underfoot.')
            print('Drop-through boards are lower to the ground, making them driftier, more stable and blurring the lines between longboarding and freeriding.')
            print('\n1.'+lb1+ " "+ str(price.get('LB1')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n2.'+lb2+ " "+ str(price.get('LB2')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n3.'+lb3+ " "+ str(price.get('LB3')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n4.'+lb4+ " "+ str(price.get('LB4')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n5.'+lb5+ " "+ str(price.get('LB5')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n6.'+lb6+ " "+ str(price.get('LB6')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n7.'+lb7+ " "+ str(price.get('LB7')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n8.'+lb8+ " "+ str(price.get('LB8')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n9.'+lb9+ " "+ str(price.get('LB9')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n10.'+lb10+ " "+ str(price.get('LB10')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n11.'+lb11+ " "+ str(price.get('LB11')) +" "+ currency+'\n(No Picture LMAO)')
            print('\n12.'+lb12+ " "+ str(price.get('LB12')) +" "+ currency+'\n(No Picture LMAO)')
            
            print('\nPick one (by typing "LB" + the number of the board):')
            action = str(input('To return to the menu,\nType "menu"\nType "mycart" to go to your cart and further check-out there.'))
            print(action)
            print('___________________________________________________________________________________________________________________________________________________')
             
instore = True      

while action == "menu":
    instore = True
    print("O U R  B O A R D S")
    print(boards)
    boardpick
    print('___________________________________________________________________________________________________________________________________________________')

            #if action == "mycart":
                #print(AHHA)

if action != "menu":
    cart = [int(price.get(action))]
    visualcart = ("Your Cart:" + " " + str(cart) +" "+ currency)
    print(visualcart) 
    print('___________________________________________________________________________________________________________________________________________________')
    instore = True
    while action:
        instore = True
        action = str(input('Anymore sellection? my friend :)\nType here:'))
        print(visualcart)
    




