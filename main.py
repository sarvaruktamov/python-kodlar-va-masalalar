# import random
#
#
# def sontop(x=10):
#     tasodifiy_son = random.randint(1, x)
#     print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         taxmin = int(input(">>>"))
#         if taxmin < tasodifiy_son:
#             print("Kattaroq son ayting:", end="")
#         elif taxmin > tasodifiy_son:
#             print("Kichikroq son ayting:", end="")
#         else:
#             print("Yutdingiz!")
#             break
#
#     print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
#     return taxminlar
#
#
# def sontop_pc(x=10):
#     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         if quyi != yuqori:
#             taxmin = random.randint(quyi, yuqori)
#         else:
#             taxmin = quyi
#         javob = input(
#             f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
#             f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
#         )
#         if javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f"Men {taxminlar} ta taxmin bilan topdim!")
#     return taxminlar
#
#
# def play(x=10):
#     yana = True
#     while yana:
#         taxminlar_pc = sontop_pc(x)
#         taxminlar_user = sontop(x)
#
#         if taxminlar_user > taxminlar_pc:
#             print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
#         elif taxminlar_user < taxminlar_pc:
#             print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
#         else:
#             print("Durrang!")
#         yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
#
#
# play()
# Samandar Mahmudov, [13.10.2022 16:58]
#  from telegram.ext import *
# import keys
#  import kalitlar
# print('Starting up bot...')
# def start_command(update, context):
#     update.message.reply_text("Salom hammaga! Men botman. Qalaysiz?")
#
# def help_command(update, context):
#     update.message.reply_text("Sizga qanaqa yordam bera olaman")
#
# def help_command(update, context):
#     update.message.reply_text("Bu yerda siz italgan narsangizni yozishingiz mumkun")
#
# def handle_response(text) -> str:
#
#     if 'hello' in text:
#         return "Salom hammaga!"
#     if 'Qandaysan?' in text:
#         return 'Men yaxshiman'
#     return "Men sizni tushunmadim"
# def handle_message( update, context):
#     message_type = update.message.chat.type
#     text = str(update.message.text).lower()
#     response = ' '
#     print(f"User ({update.message.chat.id}) says: '{text}' in: {message_type}")
#
#     if message_type == 'group':
#         if '@bot19292bot' in text:
#             new_text = text.replace('@bot19292bot', ' ').strip()
#             response = handle_response(new_text)
#         else:
#             response= handle_response(text)
#         update.message.reply_text(response)
#
#
#
# def error(update, context):
#     print(f"Update {update} caused error {context.error}")
#
#
# #run programm
# if name == 'main':
#     updater = Updater(kalitlar.token, use_context=True)
#     dp - updater.dispatcher
#
#     #Comandalar
#     dp.add_handler(CommandHandler('start', start_command))
#     dp.add_handler(CommandHandler('help', help_command))
#     dp.add_handler(CommandHandler('custom', custom_command))
#
#     #habarlar
#     dp.add_handler(MessageHandlar(Filters.text, handle_message))
#
#     dp.add_error_handler(error)
#
#     updater.start_polling(1.0)
#     updater.iddle()
# ism = input("ismingiz nima?")
#
# a = 565465
# print(type(a))
#
#
# def hi():
#     print(type(hi))
#
#
# class laptop:
#     def __init__(self,name,model,rangi,xotira,):
#         self.name = name
#         self.model = model
#         self.rangi = rangi
#         self.xotira = xotira
#
#
#         laptop1 = laptop("acer","12gen","metalika","1trb")
#         print(laptop1.name)
#         print(laptop1.model)
#         print(laptop1.rangi)
#         print(laptop1.xoti
#         ra)


# class planets:
#     def __init__(self, nomi, vazni, ulchami, harorati):
#         self.nomi = nomi
#         self.vazni = vazni
#         self.ulchami = ulchami
#         self.harorati = harorati
#     def tasvirlash(self):
#         print(f"Nomi: {self.nomi}, vazni:{self.vazni}, ulchami:{self.ulchami}, harorati: {self.harorati}")
# planets1 = planets("Mars","654547567 kub", 56655755667, "7986543456789 C")
# planets1.tasvirlash()

# class classmates:
#     def__init__(self,name,surname,born)
#     self.name = name
#     self.surname = surname
#     self.born = born
#
#     def get_name(self):
#         return self.name
#     def get_lastname(self):
#         return self.surname
#
#     def get_fullname(self):
#         return f"{self.name} {self.surname}"
#     def get_age(self,yil):
#         return yil-self.born
#     def introduction(self):
# print(f'my name is{selfname} , my surname is{self.surname},i was born in{self.born})
# classmates1 = classmates("sarvar","uktamov",2006)
# classmates1.introduction()
# print(classmates1.get_age(2022))
# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda
# ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
#
# class foydalanuvchi:
#     def __init__(self,nomi,email,raqami,yoshi)
#     self.nomi = nomi
#     self.email = email
#     self.raqami = raqami
#     self.yosh = yoshi
#     def get_foydalanuvchi(self)
#     return nomi-self
#     def introduction(self):

#
#
#
# class user:
#  def __init__(self, nomi, yoshi, email, nickname):
#         self.nomi = nomi
#         self.yoshi = yoshi
#         self.email = email
#         self.nickname = nickname
# def tasvirlash(self):
#             print(f"Nomi: {self.nomi}, yoshi:{self.yoshi}, email:{self.email}, nickname: {self.nickname}")
# user1 = user("sarvar","16","sarvaruktamov", "not")
#
# def get_name(self):
#          return self.nomi
# def get_self.nomi(self):
#         return self.yoshi
# def get_yoshi(self):
#     return self.yoshi

#
# class user:
#      def __init__(self, ism, foydalanuvchi, email):
#         self.ism = ism
#         self.foydalanuvchi = foydalanuvchi
#         self.email = email
#      def get_ism(self):
#         return self.ism
#      def get_foydalanuvchi(self):
#         return self.foydalanuvchi
#      def get_email(self):
#         return self.email
#      def description(self):
#         print(f' mening ism{self.ism}foydalanuvchi: {self.foydalanuvchi} email:{self.email}')
#
# user1 = user("sarvar", "uktamov", "sarvaruktamov6@gmail.com")
# user1.description()

#
#
# class Talaba:
#  def __init__(self, ism, familiya, tyil):
#
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#  def get_name(self):
#         return self.ism
#  def get_lastname(self):
#         return self.familiya
#  def get_fullname(self):
#         return f"{self.ism} {self.familiya}"
#  def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yil")
# talaba1 = Talaba("sarvar", "uktamov", 2006)
# print(talaba1.get_fu

#  """funksiya katta son chiqaradigan"""
# son=int(input("birinchi sonni kiriting"))
# son1=int(input("ikkinchi sonni kiriting"))
# son2=int(input("uchinchi sonni kiriting"))
# def katta(a,b,c):
#     aa =max(a,b,c)
#     return aa
# print(katta(son,son1,son2))



















































































































































































