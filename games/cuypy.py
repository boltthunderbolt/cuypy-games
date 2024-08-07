import random
import Main

def start():
  while True:

    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4 # INI TETAP KOSONG

    start_position, end_position = 1, 4
    cuypy_position = random.randint(start_position, end_position)

    goa = goa_kosong.copy() # DISINI TEMPAT CUYPY
    goa[cuypy_position - 1] = "|0_0|"

    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)

    print(f'Coba perhatikan goa dibawah ini {goa_kosong}')

    user_choice = int(input("Menurut kamu di gua nomor berapa CUYPY berada? [1 / 2 / 3 / 4]\n-> "))
    if user_choice == cuypy_position:
      print(f"Betul sekali, jawabannya adalah nomor {cuypy_position}, posisinya ada di \n{goa}")
    else:
      print(f"Kamu salah, posisinya ada di {goa}\nCoba lagi!")

    play_again = input("\n\nApakah ingin melanjutkan lagi? y(yes) or n(no)")
    if play_again == "n":
     Main.menu()

if __name__ == '__main__':
  start()