
for a in range(1,1000):
    sayac=0
    for sayi in str(a):
        sayac+= int(sayi)
    if sayac < 9 :
        print(a, end=" ")
        

