# Data structure robots[ID,"name","sector", "battery", "status" ]
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

menu=("\nPRESS ENTER TO RETURN TO THE MENU")

def show_all_robots():
    print("\n--- ROBOT DATABASE ---")
    for i in robots:
        print (i)


def binary_search_robot(target_id):
    print("\n\n")
    comparisons = 0

    Low = 0
    High = len(robots)-1
    FOUND_ID=0

    while Low <= High:
        Mid = (Low+High)//2
        if ENT_ID == (Mid):
            comparisons += 1
            FOUND_ID=Mid
            Low=High
            print(robots[FOUND_ID-1][1]+" --ROBOT FOUND\n")
            print("COMPARISONS MADE: ", comparisons)
            return FOUND_ID
        elif robots[Mid] < ENT_ID:
            comparisons=comparisons+1
            Low = Mid +1
            print(Mid, " --ROBOT NOT FOUND")
        else:
            comparisons=comparisons+1
            High = Mid -1
            print(Mid, " --ROBOT NOT FOUND")
            Mid=(Low+High)//2

    return None, comparisons


def show_robot(robot):
    ready=False
    if robots[robot][3] >= 70:
        BAT=("GOOD")
    elif robots[robot][3] >=40:
        BAT=("LOW")
    else:
        BAT=("CRITICAL")

    if robots[robot][4] == "AVAILABLE":
        if robots[robot][3] >= 70:
            ready=True
    print("\n-----------------------------")
    print("ROBOT FOUND")
    print("-----------------------------")
    print("ID:      ", robots[robot][0])
    print("Name:    ", robots[robot][1])
    print("Location:", robots[robot][2])
    print("Battery: ", str(robots[robot][3]) + "%", BAT)
    print("Status:  ", robots[robot][4])
    if ready is True:
        print("ROBOT IS SUFFICIENTLY CHARGED AND IS READY TO DEPLOY")


def search_robot():
    target_id = int(input("Enter Robot ID: "))
    
    robot, comparisons = binary_search_robot(target_id)

    if robot is not None:
        show_robot(robot, comparisons)
    else:
        print("Robot", target_id, "was not found.")
        print("Search completed after", comparisons, "comparisons.")


def show_ready_robots():
        print("\n--- READY FOR EMERGENCY DEPLOYMENT ---")
        CALCULATING=0
        for i in robots:
            if robots[CALCULATING][3] >= 70:
                if robots[CALCULATING][4] != "BUSY":
                    print (robots[CALCULATING][1], " is ready for deployment, battery at", robots[CALCULATING][3], "percent")
            CALCULATING=CALCULATING+1

def QUICK_DEPLOY():
    CALCULATING=0
    loop = True
    while loop is True:
        if CALCULATING == 16:
            print("THERE ARE NO AVAILABLE ROBOTS")
            loop = False
        elif robots[CALCULATING][3] >= 70:
            if robots[CALCULATING][4] is "AVAILABLE":
                robot=robots[CALCULATING]
                robot.pop(4)
                robot.append("BUSY")
                print(robot[1], " HAS BEEN DEPLOYED AND IS NOW BUSY")
                loop = False
            else:
                CALCULATING=CALCULATING+1
        else:
            CALCULATING=CALCULATING+1

def DEPLOY(DEPLOY_BOT):
    CALCULATING=0
    for i in robots:
        if robots[CALCULATING][0] == DEPLOY_BOT:
            robot=robots[CALCULATING]
            robot.pop(4)
            robot.append("BUSY")
            print(robot[1], " HAS BEEN DEPLOYED AND IS NOW BUSY")
        CALCULATING=CALCULATING+1


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
        ENT_ID = int(input("Enter robot's designated number: "))
        found_robot=(binary_search_robot(target_id=ENT_ID))
        CALCULATING=0
        show_robot(robot=found_robot -1)
        input(menu)


    elif choice == 2:
        show_all_robots()
        input(menu)

    elif choice == 3:
        (show_ready_robots())
        input(menu)

    elif choice == 4:
        QUICK_DEPLOY()
        input(menu)

    elif choice == 5:
        DEPLOY(DEPLOY_BOT=int(input("INPUT ID OF THE ROBOT YOU DESIRE TO DEPLOY: ")))
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