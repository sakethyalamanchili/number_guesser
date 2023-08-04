print("Welcome to the Interactive Story!")
print("You find yourself in a mysterious forest.")
print("You see three paths ahead. Which one do you take?")

path_choice = input("Enter 'left', 'right', or 'middle': ")

if path_choice.lower() == "left":
    print("You chose the left path.")
    print("You encounter a magical creature. It grants you a wish.")
    print("Here are your options.")
    print("1. Immortality")
    print("2. Endless Wealth")
    print("3. Infinite Knowledge")

    # noinspection PyInterpreter
    wish_choice = input("Enter the number of the wish you want: ")

    if wish_choice == "1":
        print("Congratulations! Your wish Immortality comes true.")
        print("You continue on your journey through the forest.")
    elif wish_choice == "2":
        print("Congratulations! You now have more money than you can imagine.")
        print("You use your newfound wealth to live a life of luxury.")
    elif wish_choice == "3":
        print("Congratulations! Your memory power increases significantly.")
        print("You become incredibly intelligent and gain vast knowledge.")
    else:
        print("You failed to make a wish. The magical creature disappears.")
        print("You continue on your journey through the forest.")

elif path_choice.lower() == "right":
    print("You chose the right path.")
    print("You discover a hidden treasure chest.")
    print("You open the chest and find a valuable treasure.")
    print("You become rich and live happily ever after.")

elif path_choice.lower() == "middle":
    print("You chose the middle path.")
    print("You encounter a friendly group of forest creatures.")
    print("They lead you to a beautiful oasis.")
    print("You rest and enjoy the peaceful surroundings.")
    print("You feel rejuvenated and continue your adventure.")

else:
    print("You are indecisive and can't pick a path.")
    print("You remain stuck in the mysterious forest.")

print("The end. Thanks for playing!")