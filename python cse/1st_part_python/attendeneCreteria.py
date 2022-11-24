from ast import If


TotalClass=int(input("Enter the total number classes held: "))
TotalHeld=int(input("Enter total number of classes attended: "))
percent=(TotalClass/TotalHeld)*100
print("percent of class attended: ",percent)
if(percent>75):
    print("You can give exam")
else:
    print("You can not attend exam")