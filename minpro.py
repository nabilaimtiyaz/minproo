print("Nama : Nabila Imtiyaz Agustin")
print("NIM  : 2409116011")
print("kelas: A")
print("-----MinPro Praktikum DDP-----")
print("\n")

# Nama dan NIM sebagai syarat berhasil login
NIM = "011"
kata_sandi = "2508" 

#login 
NIM_1 = input("NIM Akhir: ")
password_2 = input("Kata Sandi: ")

#perulangan jika NIM dan password benar atau salah
while True:
    if NIM_1 == NIM and password_2 == kata_sandi :
        print("\n˚ ༘♡ ⋆｡˚ Anda Berhasil Masuk, Selamat Datang! ˚ ༘♡ ⋆｡˚ ")
        break
    else :
        print("NIM dan/atau kata sandi anda salah")
        opsi1 = input("\napakah anda ingin mengulang? \n(Iya/Tidak): ")
        if opsi1.lower != "Iya":
            NIM = str(input("NIM akhir: "))
            kata_sandi = int(input("Kata Sandi: "))
        else:
            exit()  

while True:
    jam_kerja = int(input("\nSilahkan masukkan jumlah jam kerja: "))
    tarif = int(input("Silahkan masukkan tarif per jam: "))

    gaji_anda = jam_kerja * tarif

    if jam_kerja > 160:
        bonus  = 0.1 * gaji_anda
        total_gaji = gaji_anda + bonus
        print("Gaji anda ditambah bonus adalah sebesar: " + str(bonus))
    else:
        print("Gaji anda adalah sebesar: " + str(gaji_anda))

    opsi2 = input("\napakah anda ingin menghitung ulang? \n(Iya/Tidak): ").lower()
    if opsi2 == "tidak":
        print("Terima Kasih")
        break
    else:
        continue  