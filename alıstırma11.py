kalan=[]
bolen=[]
for x in range(1,125):
    a=125%x
    b=200%x
    c=350%x
    if a==b==c:
        kalan.append(b)
        bolen.append(x)
konum= kalan.index(max(kalan))
print(bolen[konum])




