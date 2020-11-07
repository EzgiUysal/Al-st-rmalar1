ezgi = 0
for i in range (100,999,2):
    i=str(i)
    if int(i[0]) == int(i[1]) or int(i[1]) == int(i[2]) or int(i[0]) == int(i[2]): 
        ezgi += 1
        print(i)
print(ezgi)
        

        
