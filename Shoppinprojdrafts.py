print("May I have your age? (since our branding and products are not suited for ages under 18):")
age = input()

Limit = {age >= 18}

if age != Limit:
    print("\nI am sorry that you can not countinue" + username) 
    print("\nUnderage usage of our products and contents is illegal...\nSo fuck off kid!")
if age == Limit:
    print("\nRequirement reached,\nYour access is now granted")
    print("\nEnjoy shopping skateboards!")