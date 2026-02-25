list=[(),(1,),(1,2,3),(4,5,6),(7,8,9),(10,11,12),(),]
res=[]
for i in list:    
    if len(i)!=0:
        res.append(i)
print(res)
