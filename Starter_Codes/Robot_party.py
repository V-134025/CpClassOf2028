# ROBOT RESCUE DATABASE - STARTER CODE
# Your task: complete the binary search and menu system.
# Data structure robots[ID,"name","sector", "battery", "status" ]
import math
import time

robots = [
    [101, "Scout-1", "Sector A", 92, "AVAILABLE"],
    [108, "Medic-2", "Sector B", 67, "BUSY"],
    [115, "Rover-3", "Sector A", 45, "CHARGING"],
    [121, "Drone-4", "Sector C", 88, "AVAILABLE"],
    [128, "Carrier-5", "Sector B", 73, "BUSY"],
    [134, "Scout-6", "Sector D", 56, "AVAILABLE"],
    [142, "Atlas-7", "Sector D", 81, "AVAILABLE"],
    [149, "Medic-8", "Sector A", 39, "CHARGING"],
    [157, "Drone-9", "Sector C", 95, "AVAILABLE"],
    [164, "Rover-10", "Sector B", 62, "BUSY"],
    [172, "Atlas-11", "Sector E", 76, "AVAILABLE"],
    [181, "Scout-12", "Sector E", 51, "CHARGING"],
    [193, "Carrier-13", "Sector C", 84, "AVAILABLE"],
    [205, "Medic-14", "Sector D", 69, "BUSY"],
    [218, "Drone-15", "Sector A", 97, "AVAILABLE"],
    [231, "Atlas-16", "Sector E", 42, "CHARGING"]
]

search_history = []
menu=("PRESS ENTER TO RETURN TO THE MENU")


def show_all_robots():
    print("\n--- ROBOT DATABASE ---")


def linear_search_robot(target_id):
    comparisons = 0

    # TODO: use a for loop to match each entry with a target_ID.
    # TODO: add +1 to the counter of comparisons.
    
    return None, comparisons
def binary_search_robot(target_id):
    print("\n\n")
    low = 0
    high = len(robots) - 1
    comparisons = 0

    Low = 0
    High = len(robots)-1
    Mid = int((Low+High)/2)
    FOUND_ID=0

    while Low < High:
        if ENT_ID == (Mid):
            comparisons=comparisons+1
            FOUND_ID=Mid
            Low=High
            print(robots[FOUND_ID-1][1]+" --ROBOT FOUND\n")
            print("COMPARISONS MADE: ", comparisons)
            return FOUND_ID
        elif ENT_ID < Mid:
            comparisons=comparisons+1
            High = Mid
            print(Mid, " --ROBOT NOT FOUND")
            Mid=int((Low+High)/2)
        elif ENT_ID > Mid:
            comparisons=comparisons+1
            Low=Mid
            print(Mid, " --ROBOT NOT FOUND")
            Mid=math.ceil((Low+High)/2)

    return None, comparisons


def show_robot(robot):
    print("\n-----------------------------")
    print("ROBOT FOUND")
    print("-----------------------------")
    print("ID:      ", robot[0])
    print("Name:    ", robot[1])
    print("Location:", robot[2])
    print("Battery: ", str(robot[3]) + "%")
    print("Status:  ", robot[4])
    input("\n"+menu)

    # TODO CHALLENGE: classify battery as GOOD / LOW / CRITICAL
    # TODO CHALLENGE: say whether the robot is ready to deploy


def search_robot():
    target_id = int(input("Enter Robot ID: "))
    search_history.append(target_id)

    robot, comparisons = binary_search_robot(target_id)

    if robot is not None:
        show_robot(robot, comparisons)
    else:
        print("Robot", target_id, "was not found.")
        print("Search completed after", comparisons, "comparisons.")


def show_ready_robots():
    print("\n--- READY FOR EMERGENCY DEPLOYMENT ---")
    # TODO: Use a for loop to display robots that are AVAILABLE
    #       and have a battery level of at least 70%


running = True
while running:
    print("\n=================================")
    print("   RESCUE ROBOT CONTROL SYSTEM")
    print("=================================")
    print("1 - Search robot using binary search")
    print("2 - Display robot database")
    print("3 - Show robots ready for deployment")
    print("4 - deploy first available robot")
    print("5 - deploy robot by ID")
    print("6 - Exit")
    choice = int(input("select option: "))
    if choice == 1:
        ENT_ID = int(input("Enter robot binary ID: "))
        (binary_search_robot(target_id=ENT_ID))
        input(menu)

    elif choice == 2:
        for i in robots:
            print (i)
        input(menu)

    elif choice == 6:
        running = False
        print("\n\nSHUTTING DOWN")
        time.sleep(0.2)
        print(".")
        time.sleep(0.25)
        print("..")
        time.sleep(0.15)
        print("...\n")
        time.sleep(0.5)
        print("SHUTDOWN SUCCESSFUL")