# CUPPY GAME
import random
from libs import welcome_message

welcome_message("WELCOME TO CUYPY GAMES")
name_of_user_input = input("Kenalan dong, tulis namamu dibawah!\n-> ")

while name_of_user_input == "":
	name_of_user_input = input("Isi dulu namamu!\n->")

while True:
	start_position, end_position = 1, 4
	cuypy_position = random.randint(start_position, end_position)

	bentuk_goa = "|_|"
	goa_kosong = [bentuk_goa] * 4 # INI TETAP KOSONG
	goa = goa_kosong.copy() # DISINI TEMPAT CUYPY
	goa[cuypy_position - 1] = "|0_0|"

	goa_kosong = ' '.join(goa_kosong)
	goa = ' '.join(goa)

	print(f'''
	Hi {name_of_user_input}! Coba perhatikan goa dibawah ini
	{goa_kosong}
	''')

	user_choice = int(input("Menurut kamu di gua nomor berapa CUYPY berada? [1 / 2 / 3 / 4]\n-> "))
	confirmation_choice = input(f"Apakah kamu yakin memilih nomor {user_choice} [y / n]?")

	if confirmation_choice == "y":
		if user_choice == cuypy_position:
			print(f"Betul sekali {name_of_user_input}, jawabannya adalah nomor {cuypy_position}, posisinya ada di \n{goa}")
		else:
			print(f"Kamu salah, posisinya ada di {goa}\nCoba lagi {name_of_user_input}")
	elif confirmation_choice == "n":
		print("Bye bye...")
		exit()
	else:
		print("Silahkan Ulangi Program")

	play_again = input("\n\nApakah ingin melanjutkan lagi? [y / n]")
	if play_again == "n":
		break;

print("Program selesai")