def main():
    print("Welcome to my game")
    player_name=input("What is yor name? ")
    print("Hello " + player_name)

    lives = 3
    print(f"You have {lives} lives remaining")
    
    direction = input("Where do you want to go? North, South, East or West? ")
    if direction == "North":
        print("You went North")
    elif direction == "South":
        print("You went South")
    elif direction == "East":
        print("You went East")
    elif direction == "West"
        print("You went West")
    Else:
        print("Sorry not recognised")

main()
    
