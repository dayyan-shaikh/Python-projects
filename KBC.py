# def kbc():
#     while(True):
#         print("A:Tiger  B:Lion \nC:Jaguar D:Cheetah")
#         n = (input("What is the national animal of India: ")).lower()
#         if (n == "a" or n == "tiger"):
#             print("7 crore")
#             break
#         else:
#             print("Yeh galat jawab hai")
#             continue
# kbc()

#Using list

l=[["What is the national animal of India","Tiger","A:Tiger  B:Lion \n  C:Jaguar D:Cheetah"],["What is the national animal of India","Peacock","A:Tiger  B:Crocodile \n  C:Peacock  D:Magarmacchh"]]

def game():
    for i in l:
        print("Quesion\n ",i[0])
        print("OPtion\n ",i[2])
        user=input("Enter your anser: ").lower()
        if user==i[1].lower():
            print("Yeg sahi jawab h!!!")
            print("------------------------------------\n")
        else:
            print("Wrong")
            break

d=input("Do you want to play a KBC: ")
if d=="Yes" or d=="yes":
    game()
else:
    print("jaldi yaha niklo")
    
    