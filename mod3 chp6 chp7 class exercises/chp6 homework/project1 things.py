## Author: Francisco Bumanglag
## Project: Things.txt Display data
## Assignment: Module 3 Project 1
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 26, 2023


def write_main():                                                   ##define variable

    outfile = open("things.txt", "w")                               ##outfile open file


    #prompt user to imput data for anminal fruit and country
    animal = input("Enter the name of an animal: ")                 #variable / input
    fruit = input("Enter the name of a fruit: ")                   #variable / input
    country = input("Enter the name of a country: ")                #variable / input

    outfile.write (animal + "\n")                                   #write / animal 
    outfile.write (fruit + "\n")                                    #write / fruit
    outfile.write (country + "\n")                                  #write / country

    outfile.close()                                                 #close file
                
    print("The data was written to the file successfully.")         #confirmation

write_main()                                                        #call the fucntion



