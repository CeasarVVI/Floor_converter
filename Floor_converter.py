print('Hello this program will convert the floor number between american and european regions')
region = input("what region would like to convert the floor of? ") 
if region == 'america' :
    usf = input("What is the number of the floor you would like to convert? : ")
    euf = int(usf) - 1
    print("Your floor in Europe is" ,euf)
elif region == 'europe' :
    euf = input("What is the number of the floor you would like to convert? : ")
    usf = int(euf) + 1
    print("Your floor in America is",usf)
else:
     print("Sorry we do not support this region ")    

print("Thanks for using this program")
