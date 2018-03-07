
user1=(str(input("Rocks!,Papers!,Scissors!: ")))
user2=(str(input("Rocks!,Papers!,Scissors!: ")))


def compare(user1, user2):
    if user1 == user2:
        return "Its a tie"
    
    elif user1 == "rock":
        if user2 == "scissors":
            return "rock wins"
        else:
            return "paper wins"

    elif user1 == "scissors":
        if user2 == "paper":
            return "scissor wins"
        else:
            return "rock wins"

    elif user1 == "paper":
        if user2 == "rock":
            return "paper wins"
        else:
            return "scissor wins"

    else:
        return "Invalid user input"



print(compare(user1,user2))
        
        
     
        
        
        
