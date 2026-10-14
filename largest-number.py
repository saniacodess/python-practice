l1 = [56,89,234,677]
if(l1[0]>l1[1] and l1[0]>l1[2] and l1[0]>l1[3]):
    print(l1[0])
elif(l1[1]>l1[0] and l1[1]>l1[2] and l1[1]>l1[3]):
    print(l1[1])
elif(l1[2]>l1[1] and l1[2]>l1[0] and l1[2]>l1[3]):
    print(l1[2])
else:
    print(l1[3])