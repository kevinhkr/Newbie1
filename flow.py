a = str(input("Does it move? (Yes/No) "))

if a == "yes" or a == "Yes":
    b = input("Should it? (Yes/No) ")

    if b == 'Yes' or b == 'yes':
        print("No problem!")
    else:
        print('Use the duct tape!')

else:
    b = input("Should it? (Yes/No) ")

    if b == 'Yes' or b == 'yes':
        print("Use the lubricant!")
    else:
        print('No problem!')
