a,b,c,d = [int(input()) for _ in range (4)]
stringi = ''

for j in range (c,d+1):
    stringi += str(j) + '\t'
print ('\t'+stringi)
for i in range (a,b+1) :
    stringi = ''
    for j in range (c,d+1):
        stringi += str(j*i) + '\t'
        k=(j*i)
    print(str(i) + '\t' + stringi, end ='')
        
    print()
