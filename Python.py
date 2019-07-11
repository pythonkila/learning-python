None
if type(varA) == str or type(varB) == str:
    print ('string involved')
elif varA > varB:
    print ('bigger')
elif varA == varB:
    print ('equal')
else:
    print ('smaller')
	
	
	

n = 2
while n <= 10 :
    print (n)
    n = n + 2 
print ('Goodbye!')


t= 12
while t > 11 :
    print ('Hello!')
    t -=2
    
while t >= 2:
    print (t)
    t -=2

counter=0
gbogbo= 0
end = 6
while  counter < end :
    counter +=1
    gbogbo +=counter
    #print (gbogbo)
print (gbogbo)
    


for n in range (0 , 10, 2):
    n+=2
    print (n)
print ('Goodbye!')


rof= 1
for rof in range (1):
    print ('Hello')

for raf in range (0, 10, 2):
    raf=10 - raf
    print (raf)
    
	
#Counting bob.	
s = 'azcbobobegghakl'
start= 0
end = 3
ncount= 0
count = s[start:end]
while len(s) >= end:
    count = s[start:end]
    end +=1
    start +=1
    if count == 'bob':
        ncount +=1
print ('Number of times bob occurs is: ' + str(ncount))