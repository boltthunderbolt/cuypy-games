# CUPPY GAME
import random

welcome_message = "******************************************\n\n\tWELCOME TO CUPPY GAME!\t\n\n******************************************"
cuypy_position = random.randint(1, 4)
print(welcome_message);

name_of_user_input = input("Kenalan dong, tulis namamu dibawah!\n-> ")
print(f'''
Hi {name_of_user_input}! Coba perhatikan goa dibawah ini
|_| |_| |_| |_|
''')

user_choice = int(input("Menurut kamu di gua nomor berapa CUYPY berada? [1 / 2 / 3 / 4]"))
confirmation_choice = input(f"Apakah kamu yakin memilih nomor {user_choice} [y / n]?")

if confirmation_choice == "y":
	if user_choice == cuypy_position:
		print(f"Betul sekali {name_of_user_input}, jawabannya adalah nomor {cuypy_position}")
	else:
		print(f"Coba lagi {name_of_user_input}")
elif confirmation_choice == "n":
	print("Bye bye...")
	quit()
else:
	print("Silahkan Ulangi Program")