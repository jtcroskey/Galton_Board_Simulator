#This script simulates a Galton board. User can adjust the number of slots on the simulated Galton board and the number of balls used in the simulation. 
#Prints a list containing the results of the simulation to the terminal.
#Prints a visual output to the terminal (so long as the number of slots and balls are below an upper limit described below). 

def Main():
    
    #########################################################################################################################################################################################
    #########################################################################################################################################################################################

    #User inputs

    #Choose how many balls will be used in the simulation
    #Must be a positive integer
    number_of_balls = 140

    #Choose the number of slots on the Galton board
    #Must be a positive integer 
    number_of_slots = 17

    #Chance a ball bounces right when it hits a peg
    #Value of 100 means the ball bounces right 100% of the time when it hits a peg
    #Value of 50 means the ball bounces right 50% of the time when it hits a peg
    #Value of 0 means the ball bounces right 0% of the time when it hits a peg
    #Must be an integer value between 0 and 100 (inclusive)
    bounce_chance_right = 50

    #########################################################################################################################################################################################
    #########################################################################################################################################################################################

    #Checks if user inputs are valid

    if (number_of_balls % 1 != 0) or (number_of_balls <= 0):
        print('ERROR: correct the number of balls and rerun program')
        return

    if (number_of_slots % 1 != 0) or (number_of_slots <= 0):
        print('ERROR: correct the number of slots and rerun program')
        return
    
    if (number_of_balls % 1 != 0) or (bounce_chance_right < 0) or (bounce_chance_right > 100):
        print('ERROR: correct the chance of ball bouncing right and rerun program')
        return

    #On physical Galton boards and on this simulated Galton board, there is always one more slot for the balls than there is rows of pegs 
    
    number_of_rows_of_pegs = number_of_slots - 1 

    #Below section runs the simulation

    results = [0]*(number_of_slots) #initialize list of results
    for counter1 in range(0,number_of_balls,1):
        left_or_right = 0

        if number_of_rows_of_pegs % 2 == 0: #even number of rows of pegs
            position = 0
            for counter2 in range(1,number_of_slots,1):
                left_or_right = random.randrange(1,101,1)
                if left_or_right <= bounce_chance_right:
                    position = position + .5
                else:
                    position = position - .5
            #print(position) #test - end position of every ball
            results[int(number_of_rows_of_pegs*.5)+int(position)] = results[int(number_of_rows_of_pegs*.5)+int(position)] + 1
        if number_of_rows_of_pegs % 2 == 1: #odd number of rows of pegs
            position = .5
            for counter2 in range(1,number_of_slots,1):
                left_or_right = random.randrange(1,101,1)
                if left_or_right <= bounce_chance_right:
                    position = position + .5
                else:
                    position = position - .5
            #print(position) #test - end position of every ball
            results[int((number_of_rows_of_pegs-1)*.5)+int(position)] = results[int((number_of_rows_of_pegs-1)*.5)+int(position)] + 1
        #print(results) #test - shows distribution after every new ball drops
    
    #Print graphical representation of results to terminal if number of balls is less than or equal to 500 and number of slots is less than or equal to 80
    #These limits are put in place for the sake of keeping the output reasonably sized in the terminal
    #If you have a larger screen, you can adjust these limits. You can also adjust these limits down if you have a small screen. 

    if (number_of_slots <= 80) and (number_of_balls <= 2000): #Adjust limits here. If user input number_of_slots or number_of_balls are outside of these limits, 
                                                              #then the results will not be output to terminal as a visual representation of the distribution.
                                                              #However, the list showing the numerical distribution will still print to terminal regardless.

        graph = list() #initialize list for the graphical representation
        height = max(results) #finds height of the output so as to not waste space in the terminal
        #height = number_of_balls #uncomment this line and comment out the above line if you want the graphical output to the terminal to be the same size from simulation to simulation

        #creates list for the visual output of the Galton board
        for counter in range(0,number_of_slots,1):
            graph.append([" - "]*height)
        for y_value in range(0,height,1):
            for x_value in range(0,number_of_slots,1):
                if results[x_value] > y_value:
                    graph[x_value][y_value] = " O "
                #print(graph[x_value][y_value], end = "") #prints Galton board upside down
            #print("\n")                                  #prints Galton board upside down
        #Prints out the visual representation of the Galton board to the terminal
        print("\n"*2)
        for y_value in range(height - 1,-1,-1):
            for x_value in range(0,number_of_slots,1):                        
                print(graph[x_value][y_value], end = "")
            print()
        #print(graph) #test - prints the entire contents of the list called graph

    #Print user inputs and results of simulation

    print("Number of balls: ",number_of_balls)
    print("Number of slots: ",number_of_slots)
    #print("Number of rows of pegs: ",number_of_rows_of_pegs) #optional output to terminal
    print("Height of the tallest stack: ",max(results)) #optional output to terminal
    print("Height of the shortest stack: ",min(results)) #optional output to terminal
    print("Number of balls per slot: ", results, "\n")


import random
print("\n"*50)
Main()


