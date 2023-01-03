# """masala 1"""
# son = int(input("Son kirting"))
# royhat = [2,3,4,5,6,7,8,9,10]
# print("qolganlarga qushilmaydi")
# for raqam in royhat:
#     if son+raqam:
#         print(f"{raqam} ga qushiladi")

 # """masala 2"""
#
# def tubmi(n):
#     bolovchilar = 0
# for i in range(1, n+1):
#     if n % i ==0:
#         bolovchilar +=1
#         return bolovchilar ==2
#     gcha = int(input("qaysi songacha"))
# for i in range (1,gacha + 1):
#         if tubmi(i):
#             print(i, end='')

# """masala 3"""
# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi +=son
#         return yigindi
# #     print(summa(1,2,3,4,5,6,7,8,9))
# """5-masala"""
# a=int(input('uch xonali son kiriting:'))
# d=a%10
# c=a//10
# s=c%10
# a=c%10
# k=c//10
# n=d+s+k
# print("yig'indi",n)

# """9 masala"""
# # def son(natural):
# #    sonlar = 1,2,3,4,5,
# #    for son in sonlar:
# #     reverse.sonlar():
# print(sonlar)

# son = int(input("Son kirting"))
# royhat = [7]
# print("qolganlarga qushilmaydi")
# for raqam in royhat:
#     if son+raqam:
#         print(f"{raqam} ga qushiladi")

"""9-MASALA"""
# a = [1,2,3,4,5]
# a.sort()
# print(a)
# a.reverse()
# print(a)


# """10-masala"""
# sonlar = []
# print("raqam kirit")
# for n in range(5):
#     sonlar.append(input(f"{n+1}"))

# """16-masala"""
# a=2
# b=6
# print(a**b)

# # """17-masala"""
# a=4
# n=5
# print(a+n)
#
# # """14-masala"""
# # a=5
# # b=6
# # print(a*b)
# def summa(*sonlar):
#     kupaytma = 1
#     for son in sonlar:
#         kupaytma *=son
#         return kupaytma
#     print(summa(5,3,8,))

# """13-masala"""
# def summa(*sonlar):
#     kupaytma = 1
#     for son in sonlar:
#         kupaytma+=son
#         return kupaytma
#     print(summa(1,2,3,))
# """22-misol"""
# son =int(input('son kiriting'))
# if son<=10:
#     print('togri 3ni darajasi')
# elif son(*3):
#     print('3ning darajasi emas')

# """21-misol"""
#
# x = lambda a, b : a*b
# print(x(19,9))
# y = lambda a,b, : a/b
# print(y(19,9))
#
# 25-masala
# a=int(input("son kiriting="))
# d=a%10
# c=a//10
# s=d%a
# print("bulinma=",s)
#11-Masala

# def oraliq(min,max):
#     sonlar=[]
#     while min < max:
#         sonlar.append(max)
#         max -= 1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))


#12-masala
# def oraliq(min,max):
#     sonlar=[]
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))
# 28 -misol
# def ekuk(a,b):
#     n=a*b
#     while a!=0 and b!=0:
#         if a>b:
#             a%=b
#         else:
#             b%=a
#     return n//(a+b)
# a=int(input('a='))
# b=int(input('b='))
# print('EKUK:',ekuk(a,b))
# """18-misol"""
#
# print("N natural son kiriting")
# from math import*
# n=int(input("n="))
# s=0
# for i in range(n):
#     s +=i
#     print("yigindi qiymat=",s)

# savol = int(input("son kirit"))
# for a in range(2,50):
#     b=0
#     c=[x for x in range(1,a+1)if a%x==0]
#     if len(c)==2:
#         print(a,'tub son')
# else:
#     print('bu tub son emas')

# """8-masala"""
# def almashtirish():
#     b=''
#     for i in 'son':
#         if i =='k':
#             i='q'
#         elif i=='t':
#             i='m'
#             b+=i
#             print(b)
#             son=input('soni kiriting')
#             almashtirish()
