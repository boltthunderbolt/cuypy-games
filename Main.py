# CUPPY GAME
import random

welcome_message = "******************************************\n\n\tWELCOME TO CUPPY GAME!\t\n\n******************************************"
cuypy_position = random.randint(1, 4)
print(welcome_message);

name_of_user_input = input("Kenalan dong, tulis namamu dibawah!\n-> ")

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

user_choice = int(input("Menurut kamu di gua nomor berapa CUYPY berada? [1 / 2 / 3 / 4]"))
confirmation_choice = input(f"Apakah kamu yakin memilih nomor {user_choice} [y / n]?")

if confirmation_choice == "y":
	if user_choice == cuypy_position:
		print(f"Betul sekali {name_of_user_input}, jawabannya adalah nomor {cuypy_position}, posisinya ada di \n{goa}")
	else:
		print(f"Kamu salah, posisinya ada di {goa}\nCoba lagi {name_of_user_input}")
elif confirmation_choice == "n":
	print("Bye bye...")
	quit()
else:
	print("Silahkan Ulangi Program")