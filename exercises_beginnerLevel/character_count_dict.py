count_dict={}
string=input("Enter a string: ")
for i in string:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict[i]=1
for i in count_dict:
    character=i
    count=count_dict[i]
    print("character",[character],"=>",count)
