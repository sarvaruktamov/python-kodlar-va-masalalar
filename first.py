"""Dunder Metodlari pythonda obektlar bn ishlashda qulaylik bu ikta pastki chiziq double under score yani dunder metodi"""
# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#
#     def __init__(self, make, model, rang, yil, narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
#
#     def __repr__(self):
#         """Obyekt haqida ma'lumot"""
#         return f"Avto: {self.rang} {self.make} {self.model} yii {self.yil},narh,{self.narh}"
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# print(avto1)

"""klasslar"""
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
# talaba2 = Talaba("sarvar","uktamov",2006)
# talaba2.tanishtir()
#
"""obektlar bilan ishlash"""
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-kurs kolejda "
#
# talaba1 = Talaba("sarvar", "uktamov", 2006)
# print(talaba1.get_info())

"""vorislik va polimorfizm """


# class Talaba():
#     """Talaba klassi"""
#
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#
#     def get_id(self):
#
#         return self.idraqam
#
#     def get_bosqich(self):
#
#         return self.bosqich
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
# shaxs1 =("sarvar",'uktamov')
# print(shaxs1.get_info())

# for i in range(1,10):
#     print("{} * {} ={}".format(2,i,2*i))

#
# import datetime as dt
# hozir = dt.datetime.now()
# print(hozir)
#
# print(hozir.date())
# print(hozir.time())
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)


# a = int(input('soni kiriting'))
# b = int(input('soni kiriting'))
# c = int(input('soni kiriting'))
# katta_son=min(a,b,c)
# print=min(a,b,c)

"""superklass"""

# talaba=('Sarvar Uktamov. Passport:FA112299, 2006-yilda tug`ilgan')
#
#
# class Talaba:
#     """Talaba klassi"""
#
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
#
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
# print(talaba)

"""obyekt ichida obyekt"""

# class manzil:
#     def __init__(self,viloyat,tuman,kocha,uy):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.kocha = kocha
#         self.uy = uy
#
#     def get_manzil(self):
#         manzil = f"{self.viloyat},{self.tuman},{self.kocha},{self.uy}"
#         return manzil
#
# class student:
#     def __init__(self,ism,familiya,passport,tyil,):
#         super().__init__(ism,familiya,passport,tyil)
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
#     def get_ism(self):
#         return self.ism
#     def get_familiya(self):
#         return self.familiya
#     def get_passport(self):
#         return self.passport
#     def get_tyil(self):
#         return self.tyil
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_passport()}-F122332F2. tugilgan yili: {self.tyil}"
#         return info
# student_manzil = manzil(12,'toyloq',"Binoiy","Samarqann")
# student1 = student("sarvar","uktamov","FA112299",2006,)

#
# a = int(input('son kiriting'))
# b = int(input('son kiriting'))
# c = int(input('son kiriting'))
# def eng_katta_son(a,b,c):
#     return max(a,b,c)
# print(eng_katta_son(a,b,c))


"""faktorial"""
#
# def faktorial (d):
#      return factorial(d)
#
# from math import *
#
# n = int(input('son kiriting'))
# print("soning faktorial:",faktorial(n))


print()




