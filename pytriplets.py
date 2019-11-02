#Pythagorean Triplets 1.0 (By: BladeSides)
x=int(input()) #Max value of result
j=0 #Loop Value 1
k=0 #Loop Value 2
for i in range(1,x+1): #Goes from 1 to x
    for j in range(1,x+1): #Same as above
        for k in range(j,x+1): #Goes from j to x
            if(j**2+k**2==i**2): #Compares to see if it is a triplet
                print(j,"²","+",k,"² = ",i,"²") #Prints output if true
