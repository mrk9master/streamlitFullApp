# for i in range(1,21):
#     if i % 2==0:
#         print(i)


# for i in range(1,50):
#     if i % 3 == 0:
#         print("fizz")
# count=0
# for i in range(1,100):
#     if i % 3==0:
#         if i % 5 ==0:
#          count+=1
# print(count)  
    

# for i in range(1,11):
#     if i % 2 == 0:
#         print("it's even:",i)
#     elif i % 2 != 0:
#         print("it's odd:",i)


# x=0
# for i in range(1,51):
#     if i % 5 !=0:
#         x+=i
# print("sum:",x)
   


# x=0
# for i in range(1,21):
#     x+=i**2
# print(x) 




# x=0
# text = input("enter peragraph to find vowels")
# vowels = "aeiouAEIOU"
# for i in text:
#     if i in vowels:
#         x+=1
# print(x)





# num = [-10,15,-20,25,-5,30]
# ps=0
# nv = 0

# for i in num:
#     if i < 0:
#         nv-=1
#         print("positive are",nv)  
#     elif i > 0:
#         ps+=1
#         print("positive are",ps)





# num = [10,34,56,78,2,89,15]
# min=num[0]
# for i in num:
#     if i<min:
#         min=i
# print(min)
        
# num = [10,34,56,78,2,89,15]
# min=0
# for i in range(1,len(num)):
#     if i < min:
#         min=i
# print(min)


# num=[1,2,3,4,2,1,2,4,5]

# z=num.count(2)
# print(z)



# n=[1,2,3,4,2,1,2,4,5]

# c=0

# for i in n:
#    if i==2:
#     c+=1
# print(c)



# n=[1,2,3,4,5]
# z=3 in n

# print(z)

# n = [1,2,3,4,5]

# for i in n:
#     if i==3:
#         print("True")





# n=[1,2,3,4,5]
# p=1
# for i in range(1,6):
#       p=p*i
#       i+=1
# print(p)
t=2
z=9
n = [1,2,2,4,5]
for i in range(0,len(n)):
    if n[i]==t:
     n[i]=z

    print(n)