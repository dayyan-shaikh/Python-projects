n=int(input("Enter number of people: "))
vote=[]
for i in range(n):
    voting=input("Enter vote for jack or jill: ")
    vote.append(voting)
if vote.count("jack")>vote.count("jill"):
    print("Jack wins")
elif vote.count("jill")>vote.count("jack"):
    print("jill wins")
else:
    print("Draw")