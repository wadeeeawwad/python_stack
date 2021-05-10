
print("name:wadee_awwad.93")
print("welcome in  for_loop_basic1 assignment")
 

  #//1
for x in range(151):
  print(x)
for x in range(3):
  print(x)

#//2
for x in range(5,1000,5):
    
 print(x)

#//3 
for x in range (1,100):
     if x%5==0:
         print("coding")
     if x%10==0:
        print("codingdojo")    

#//4 odd num &sum we replace 50001 by 101 in order to saver time of sum process
sum=0
for x in range(1,101):
  if x%2!=0:
    sum=sum+x
    print(sum)
#//5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
  if x%2==0:
   print(x)


#//6 Flexible Counter - Set three variables: lowNum, highNum, mult.
low=2
high=9
mult=3
for mult in range(low+1,high+1,mult):
  
   print(mult)


print("the end of the process Thank you <3 :)")







