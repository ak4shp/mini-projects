from source_data import hero_hf, swift, volvo, welcome_message

try:
    while True:
        print(welcome_message)
        to_use = int(input("""Please have a look and choose : 
        1 -> Bike
        2 -> Car
        3 -> Commercial Vehicle
        0 -> exit \nI want > """))

        if to_use == 1:
            print(hero_hf.about_bike())
        elif to_use == 2:
            print(swift.about_car())
        elif to_use == 3:
            print(volvo.about_commercial())
        elif to_use == 0:
            print("Thanks for visiting us! Please do come again🤗 ")
            break
        else:
            print("\nInvalid wish! Please type 1, 2, 3 or 0 ")

except ValueError:
    print("\nWARNING...\nYou typed it wrong!! Please choose 1, 2, 3 or 0 next time.")
    