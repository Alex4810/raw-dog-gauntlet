import random
def encounter():
    choices = ["combat", "tavern", "NPC"]
    weights = [75, 12.5, 12.5]
    result = random.choices(choices, weights)[0]
    match result:
        case "combat":
            combat()
        case "tavern":
            tavern()
        case "NPC":
            NPC()


def combat():
    choices = ["Goblin", "Skeleton", "Hobgoblin", "Crusader", "The People's Republic of Waterdeep"]
    weights = [50, 20, 15, 14, 1]
    result = random.choices(choices, weights)[0]
    match result:
        case "Goblin":
            print("You encountered a Goblin!")
            goblin()
        case "Skeleton":
            print("You encountered a Skeleton!")
            skeleton()
        case "Hobgoblin":
            print("You encountered a Hobgoblin!")
            hobgoblin()
        case "Crusader":
            print("You encountered a Crusader!")
            crusader()
        case "The People's Republic of Waterdeep":
            print("You encountered The People's Republic of Waterdeep!")
            the_peoples_republic_of_waterdeep()



def goblin():
    print("goblin")
def skeleton():
    print("skeleton")
def hobgoblin():
    print("hobgoblin")
def crusader():
    print("crusader")
def the_peoples_republic_of_waterdeep():
    print("the people's republic of Waterdeep")



def tavern():
    print("tavern")
def NPC():
    print("NPC")

def clear_screen():
    input("\nPress Enter to continue...")
    print("\n" * 20)




print("\nWelcome to the Dankest Dungeon!\n"+
"Your adventure awaits!\n"+
"Are you ready?")
result = input("y or n")
match result:
    case "y":
        print("Your adventure awaits!")
    case "n":
        print("Too bad! Your adventure begins anyways!")
    case _:
        print("You're gonna have to figure out how to input properly on the road! Your adventure beins!")
clear_screen()
encounters_num = random.randint(10,20)
for x in range(encounters_num):
    encounter()
    clear_screen()
print("You finished your adventure!\n"
      +"You will never be the same...")