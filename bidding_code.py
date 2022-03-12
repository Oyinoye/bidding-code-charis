# Bidding code for bidding system

# First set the bidding variable and the bidding to track the while loop

currentBid = 0

bidding = True

while bidding == True:
    userInput = input("Would you like to place a bid? Type 'yes' to continue \nor anything else to end the bidding process: ")
    if (userInput == "Yes" or userInput == "yes"):
        newBid = int(input("Enter amount you would like to bid for( e.g. 50000): "))

        if newBid > currentBid:
            currentBid = newBid
            print("Bid has increased to", str(currentBid))

        else:
            print("Invalid Bid! You must place a higher bid!")
            print("Current Bid: ", str(currentBid))
    
    else:
        bidding = False

print("End of bidding: \nFinal Bid: " + str(currentBid))