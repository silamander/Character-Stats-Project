#Character Stats 4.0
#define game Functions
#-add points
def point_addition():
    print("You have", skills["Points"], "points to use.")
    print("Out of your S.P.E.C.I.A.L. skill list,")
    skill_name=input("which skill would you like to add points to? ")
    skill_name=skill_name.capitalize()
    #if skill exists
    if skill_name in skills.keys():
        point_num=(input("How many points would you like to add to it? "))
        point_num=int(float(point_num))
        #if enough points exist
        if (point_num>skills["Points"]):
            print("\nWoah, hold on. You don't have enough points to add.")
            #option to retry or to return
            cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
            cont=cont.capitalize()
            if cont == "Again":
                print("\n")
                point_addition()
            elif cont == "":
                print("\n")
            else:
                print("That is not a valid option. We're just gunna send you back to the menu.")
                pass
        #add points when all is valid
        else:
            skills[skill_name]+=point_num
            skills["Points"]-=point_num
            print("You have", skills[skill_name], "points in your", skill_name, "now.")
            print("And", skills["Points"], "points left!\n")
            #option to retry or to return
            cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
            cont=cont.capitalize()
            if cont == "Again":
                print("\n")
                point_addition()
            elif cont == "":
                print("\n")
            else:
                print("That is not a valid option. We're just gunna send you back to the menu.")
                pass
    else:
        print("\nThat's not a listed skill")
        #option to retry or to return
        cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
        cont=cont.capitalize()
        if cont == "Again":
            print("\n")
            point_addition()
        elif cont == "":
            print("\n")
        else:
            print("That is not a valid option. We're just gunna send you back to the menu.")
            pass
                   
#-remove points
def point_subtraction():
    print("Out of your S.P.E.C.I.A.L. skill list,")
    skill_name=input("which skill woud you like to remove points from? ")
    skill_name=skill_name.capitalize()
    #if skill exists
    if skill_name in skills.keys():
        point_num=(input("How many points would you like to remove from it? "))
        point_num=int(float(point_num))
        #if enough points exist
        if (point_num>skills[skill_name]):
            print("\nWoah, hold on. If you took that many points away you'd have negative points in that skill.")
            #option to retry or to return
            cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
            cont=cont.capitalize()
            if cont == "Again":
                print("\n")
                point_subtraction()
            elif cont == "":
                print("\n")
            else:
                print("That is not a valid option. We're just gunna send you back to the menu.")
                pass
        #add points when all is valid
        else:
            skills[skill_name]-=point_num
            skills["Points"]+=point_num
            print("You have", skills[skill_name], "points in your", skill_name, "now.")
            print("And", skills["Points"], "points left!\n")
            #option to retry or to return
            cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
            cont=cont.capitalize()
            if cont == "Again":
                print("\n")
                point_addition()
            elif cont == "":
                print("\n")
            else:
                print("That is not a valid option. We're just gunna send you back to the menu.")
                pass
    else:
        print("\nThat's not a listed skill.")
        #option to retry or to return
        cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
        cont=cont.capitalize()
        if cont == "Again":
            print("\n")
            point_addition()
        elif cont == "":
            print("\n")
        else:
            print("That is not a valid option. We're just gunna send you back to the menu.")
            pass              
#-list stat details
def skill_details():
    for skill in skills.keys():
        if skill !="Points":
            print(skill)
    skillName=input("Which skill would you like to know more about? ")
    skillName=skillName.capitalize()
    if skillName in skills.keys():
        print(skillName, "-", skills[skillName])
        print(skillDetail[skillName])
        print("\n")
        #option to retry or to return
        cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
        cont=cont.capitalize()
        if cont == "Again":
            print("\n")
            skill_details()
        elif cont == "":
            print("\n")
        else:
            print("That is not a valid option. We're just gunna send you back to the menu.")
            pass    
    else:
        print("\nThat's not a listed skill.")
        #option to retry or to return
        cont=input("Press Enter to go back to the menu or type in 'Again' to try again. " )
        cont=cont.capitalize()
        if cont == "Again":
            print("\n")
            skill_details()
        elif cont == "":
            print("\n")
        else:
            print("That is not a valid option. We're just gunna send you back to the menu.")
            pass    
    
#setup configurations
#-config stats and points
skillDetail={"Strength": "Effects your max carry weight \nand satisfies the Strength requirement on weapons. \nEach point of Strength adds 25 lbs \nto your max carry weight." ,
             "Perception": "Effects how well you notice things \nand allows you to open up new dialouge options sometimes." ,
             "Endurance": "Determines your environmental resistance, \nhit points, and healing rate.",
             "Charisma": "Effects your social influence \nand number of companion slots you have.",
             "Intelligence": "Allows you to gain extra experience \npoints from learning more about skills.",
             "Agility": "Determines the success of combat moves \nand how successful dodging will be.",
             "Luck": "Effects how good the items you'll find in containers will be \nand how many coins you'll find." }

skills={"Strength": 5, "Perception": 5, "Endurance": 5, "Charisma": 5, "Intelligence": 5, "Agility": 5, "Luck": 5, "Points":20}
#-config menu
on=True

while on:
    print("Character Skill Builder\nBuild up your character's skills.\n")
    for skill in skills.keys():
        if skill !="Points":
            print(skill)
    print("\n")
    print("1. Add points to your skills\n2. Remove points from your skills\n3.List details about your skills\n4.Exit")
    selection=input("\nChoice: ")
    print("\n")
    #selections
    if selection == "1":
        point_addition()
    elif selection == "2":
        point_subtraction()
    elif selection == "3":
        skill_details()
    elif selection == "4":
        input("Good-Bye!")
        on=False
    else:
        pass
