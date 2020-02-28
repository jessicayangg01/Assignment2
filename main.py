"""
Name: Jessica Yang
Program: Assignment 2, Volume Calculator
Program Description: Calculates the volumes of cubes, pyramids and ellipsoids
"""

# Imports the two other python files: volume and summary
import volume as vl
import summary as sm

# Boolean variable to allow while loop to continue
continueLoop = True

# Lists for the volumes of each shape
cubeVolumeList = []
pyramidVolumeList = []
ellipsoidVolumeList = []


# Formatting the input shape to allow the input of upper/lowercase as well as odd spacing
def format_input(text_line):
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = " ".join(word_list)
    return text_line


# Prompts user for which test number
testNumber = input("What is the test number? ")

# The loop that continuously prompts user for shapes until a q is entered
while continueLoop:
    # prompts user for the shape
    shape = input("What shape would you like to calculate the volume of? Input \"cube\" or \"c\", \"pyramid\" or \"p\", \"ellipsoid\" or \"e\", \"quit\" or \"q\": ")
    # formats the shape string
    shape = format_input(shape)
    # if they chose to quit
    if shape == "q":
        # sorts each list of volumes
        cubeVolumeList.sort()
        pyramidVolumeList.sort()
        ellipsoidVolumeList.sort()
        print("You have reached the end of your session.")
        # checks if arrays are empty so the program can tell user they didn't input anything
        if not cubeVolumeList and not pyramidVolumeList and not ellipsoidVolumeList:
            print("You did not perform any volume calculations.")
        # Otherwise prints out all the volumes entered in this session. If any array does not have a volume, tells user that no volume was input for that given shape
        else:
            print("The volumes calculated for each shape are:")
            if not cubeVolumeList:
                print("Cube: no input")
            elif cubeVolumeList:
                print("Cube: ", end="")
                print(*cubeVolumeList, sep=", ")
            if not pyramidVolumeList:
                print("Pyramid: no input")
            elif pyramidVolumeList:
                print("Pyramid: ", end="")
                print(*pyramidVolumeList, sep=", ")
            if not ellipsoidVolumeList:
                print("Ellipsoid: no input")
            elif ellipsoidVolumeList:
                print("Ellipsoid: ", end="")
                print(*ellipsoidVolumeList, sep=", ")
            # gives the information to summary method in summary file
            sm.summarize(cubeVolumeList, pyramidVolumeList, ellipsoidVolumeList, testNumber)
            # breaks the loop
            break
    # if they chose cube
    elif shape == "cube" or shape == "c":
        # prompts user for dimensions
        a = int(input("what is the length of the cube: "))
        # calculates the volume in python file volume and prints the calculated volume after
        cube_volume = vl.cube_volume(a)
        print("The volume of a cube with length ", a, " is: ", cube_volume)
        # adds the volume to list of volumes
        cubeVolumeList.append(cube_volume)
    # if they choose pyramid
    elif shape == "pyramid" or shape == "p":
        # prompts user for dimensions
        b = int(input("what is the base of the pyramid: "))
        h = int(input("what is the height of the pyramid: "))
        # calculates the volume in python file volume and prints the calculated volume after
        pyramid_volume = vl.pyramid_volume(b,h)
        print("The volume of a pyramid with base ", b, " and height ", h, " is: ", pyramid_volume)
        # adds the volume to list of volumes
        pyramidVolumeList.append(pyramid_volume)
    # if they choose ellipsoid
    elif shape == "ellipsoid" or shape == "e":
        # prompts user for dimensions
        r1 = int(input("what is the first radius of the ellipsoid: "))
        r2 = int(input("what is the second radius of the ellipsoid: "))
        r3 = int(input("what is the third radius of the ellipsoid: "))
        # calculates the volume in python file volume and prints the calculated volume after
        ellipsoid_volume = vl.ellipsoid_volume(r1, r2, r3)
        print("The volume of an ellipsoid with radius of ", r1, ", ", r2, ", and ", r3, "is: ", ellipsoid_volume)
        # adds the volume to list of volumes
        ellipsoidVolumeList.append(ellipsoid_volume)
    # if no valid shape is entered, tells user to enter again
    else:
        print("enter proper value")
