from libs import welcome_message, exit_program
from games import cuypy
from tools import warung
## CUPPY GAME

def main():
	welcome_message()
	menu()

def menu():
	options = ["cuypy games", "warung mini", "keluar"]
	print("Menu Program\n============")
	for i, option in enumerate(options, start = 1):
		print(f"{i}. {option.title()}")

	user_option = int(input("Silahkan pilih: "))
	if user_option == 1:
		cuypy.start()
	elif user_option == 2:
		warung.start()
	elif user_option == 3:
		exit_program()
	else: print("Hanya boleh pilih yang tersedia di menu");

if __name__ == '__main__':
	main()