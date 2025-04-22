LONG=15
INDENT=38
left_I = INDENT-1
right_I = INDENT
print(" "*INDENT, "*", sep='') #Top of triangle
for i in range(LONG-1): #Long of triangle side
    print(" "*left_I, "*", " "*(right_I - left_I), "*", sep='')
    right_I+= 1
    left_I -= 1
#Triangle base (i==LONG)
print(" "*left_I, "*"*(right_I - left_I + 2), sep='')
