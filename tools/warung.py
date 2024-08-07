import Main

def start():
  while True:
    print("Ini warung apps")
    play_again = input("Kembali ke menu utama? [y / n]")
    if play_again == "y":
      Main.menu()
      break # selalu hentikan dengan syntax break di loop program

if __name__ == '__main__':
  start()