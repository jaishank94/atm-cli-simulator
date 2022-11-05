print("Welcome to Our Banking System")
print("\t\t* `login [name]` - Logs in as this customer and creates the customer if not exist")
print("\t\t* `deposit [amount]` - Deposits this amount to the logged in customer")
print("\t\t* `withdraw [amount]` - Withdraws this amount from the logged in customer")
print("\t\t* `transfer [target] [amount]` - Transfers this amount from the logged in customer to the target customer")
print("\t\t* `logout` - Logs out of the current customer")
choice = 0
Dict = {}

while (True):
    choice = input("> ").split()
    print("\n\n")

    if choice[0] == "login":
        print("Hello, ", choice[1],"!")
        
        if choice[1] in Dict.keys():
            print("Your balance is $", Dict[choice[1]]["balance"])
            
            x1 = list(Dict[choice[1]]["own"].keys())
            x2 = list(Dict[choice[1]]["owe"].keys())

            if(len(x1)>0):
                print("Owed $",Dict[choice[1]]["own"][x1[0]]," from ", x1[0])
                
            if(len(x2)>0):
                print("Owed $",Dict[choice[1]]["owe"][x2[0]]," to ", x2[0])
                
        else:
            Dict[choice[1]] = {"balance":0, "owe": {}, "own":{}}
            print("Your balance is $", 0)
            
        while (True):
            OpChoice = input("> ").split()
            
            if OpChoice[0] == "deposit":
                x = list(Dict[choice[1]]["owe"].keys())
                
                if(len(x)>0):
                    if(Dict[choice[1]]["owe"][x[0]] > int(OpChoice[1])):
                        Dict[choice[1]]["owe"][x[0]] = Dict[choice[1]]["owe"][x[0]] - int(OpChoice[1])
                        Dict[x[0]]["own"][choice[1]] = Dict[choice[1]]["owe"][x[0]]
                        Dict[x[0]]["balance"] = int(Dict[x[0]]["balance"]) + int(OpChoice[1])
                        print("Transferred $", OpChoice[1]," to ", x[0])
                        print("Your balance is $",0)
                        print("Owed $",Dict[choice[1]]["owe"][x[0]]," to ", x[0])
                        continue
                    else:
                        Dict[x[0]]["balance"] = int(Dict[x[0]]["balance"]) + Dict[choice[1]]["owe"][x[0]]
                        Dict[choice[1]]["balance"] = int(Dict[choice[1]]["balance"]) + int(OpChoice[1]) - Dict[choice[1]]["owe"][x[0]]
                        print("Transferred $", Dict[choice[1]]["owe"][x[0]]," to ", x[0])
                        print("Your balance is $",Dict[choice[1]]["balance"])
                        Dict[choice[1]]["owe"][x[0]] = {}
                        Dict[x[0]]["own"] = {}
                        continue
                else:
                    Dict[choice[1]]["balance"] = int(Dict[choice[1]]["balance"]) + int(OpChoice[1])
                    print("Your balance is $", Dict[choice[1]]["balance"])
                    continue
            
            elif OpChoice[0] == "transfer":
                
                if OpChoice[1] in Dict.keys():
                    print("")
                else:
                    Dict[OpChoice[1]] = {"balance":0, "owe": {}, "own":{}}
                    
                x = list(Dict[choice[1]]["own"].keys())
                
                if(len(x) > 0 and x[0] == OpChoice[1]):
                    if(Dict[choice[1]]["own"][x[0]] >= int(OpChoice[2])):
                        Dict[choice[1]]["own"][x[0]]  = Dict[choice[1]]["own"][x[0]] - int(OpChoice[2])
                        Dict[x[0]]["owe"][choice[1]] = Dict[choice[1]]["own"][x[0]]
                        # Dict[x[0]]["balance"] = int(Dict[x[0]]["balance"]) + int(OpChoice[1])
                        print("Your balance is $",Dict[choice[1]]["balance"])
                        print("Owed $",Dict[choice[1]]["own"][x[0]]," from ", x[0])
                        
                elif(int(OpChoice[2]) > int(Dict[choice[1]]["balance"])):
                    Dict[choice[1]]["owe"] = { OpChoice[1]: int(OpChoice[2]) - int(Dict[choice[1]]["balance"]) }
                    Dict[OpChoice[1]]["own"] = { choice[1]: int(OpChoice[2]) - int(Dict[choice[1]]["balance"]) }
                    Dict[OpChoice[1]]["balance"] = int(Dict[OpChoice[1]]["balance"]) + int(Dict[choice[1]]["balance"])
                    print("Transferred $",Dict[choice[1]]["balance"]," to ", OpChoice[1])
                    print("Your balance is $", 0)
                    print("Owed $", int(OpChoice[2]) - int(Dict[choice[1]]["balance"]) ," to ", OpChoice[1])
                    Dict[choice[1]]["balance"] = 0
                else:
                    Dict[OpChoice[1]]["balance"] = int(Dict[OpChoice[1]]["balance"]) + int(OpChoice[2])
                    Dict[choice[1]]["balance"] = int(Dict[choice[1]]["balance"]) - int(OpChoice[2])
                    print("Transferred $",OpChoice[2]," to ", OpChoice[1])
                    print("Your balance is $", Dict[choice[1]]["balance"])
                continue
            
            if OpChoice[0] == "logout":
                print("Goodbye,", choice[1], "!")
                break
            else:
                break
                
    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit!")
        break