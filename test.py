# List
hobbies = ["main bola", "berenang", "ngoding"]
start_from = 1
# print(hobbies[1 - start_from])
tmp_hobbies = hobbies
print(f"hobbies -> {hobbies}")

# Temporary Data
# print(f"tmp_hobbies -> {tmp_hobbies}")
tmp_hobbies[2 - start_from] = "biliar"
print(f"tmp_hobbies -> {tmp_hobbies}")

# Search last data from array
# ===========================
# print(len(hobbies) - 1)
# last_data = len(hobbies) - 1
# print(hobbies[last_data])
# print(hobbies[-1])

bentuk_goa = "|_|"
goa = [bentuk_goa] * 4
goa_kosong = goa.copy()

goa_kosong[2] = "DEA"
print(goa)
print(goa_kosong)