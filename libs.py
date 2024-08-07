import socket
from time import sleep
PC_NAME = socket.gethostname()
countdown = 3

def welcome_message():
	style = "*" * (len(PC_NAME) + 6)
	print(style)
	print(f"** {PC_NAME} **")
	print(style)

def exit_program():
	global countdown
	while countdown >= 1:
		print(100 * "\n" + f"Program akan dihentikan dalam {countdown}")
		countdown -= 1
		sleep(1)
	print("Program berhasil dihentikan")

if __name__ == '__main__':
	welcome_message()
	exit_program()