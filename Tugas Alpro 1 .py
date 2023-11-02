print("SELAMAT DATANG DI PIZZA HUT!!!")

#Pilih Topping 
print('//// Berikut Pilihan Topping ////')
print('''-Frankuter
-Meat Monsta
-Super Supreme
-Supeer Supreme Chicken''')

Pilih_Topping = str(input("Pilih Menu Topping: "))
if Pilih_Topping == 'Frankuter':
    Harga_Topping = 43637
    
elif Pilih_Topping == 'Meat Monsta':
    Harga_Topping = 43637

elif Pilih_Topping == "Super Supreme": 
    Harga_Topping = 43637
    
elif Pilih_Topping == "Super Supreme Chicken":
    Harga_Topping = 43637
    
else :
    print("Pilihan Menu Anda Tidak Valid")

#Pilih crust
print('/////Untuk Pilihan Crust/////')
print('''-Pan Pizza
-StuffedCrust Cheese
-StuffedCrust Sausage
-Cheesy Bites
-Crown Crust''')

pilih_crust = str(input("pilih  crust yang anda inginkan: "))
if pilih_crust == 'Pan Pizza' :
    harga_crust = 0
    
elif pilih_crust == 'StuffedCrust Cheese':
    harga_crust = 11818
    
elif pilih_crust == "StuffedCrust Sausage":
    harga_crust = 9101
    
elif pilih_crust == "Cheesy Bites":
    harga_crust = 13636

elif pilih_crust == 'Crown Crust':
    harga_crust = 11818
else:
    print("Pilihan Crust anda tidak valid")

#pilih  ukuran pizza
print('/////Untuk Pilihan Ukuran/////')
print('''-Personal
-Reguler
-Large''')

pilih_ukuran = str(input("pilih ukuran: "))
if pilih_ukuran == "Personal":
    harga_ukuran = 0
elif pilih_ukuran == "Reguler":
    harga_ukuran = 57273
elif pilih_ukuran == "Large":
    harga_ukuran = 89091
else:
    print("Ukuran anda tidak ada")

#Tambah Keju
tambah_keju = str(input("apakah anda ingin menambah extra keju? yes/no: "))
if tambah_keju == "yes":
    harga_keju = 16364
elif tambah_keju == "no":
    harga_keju = 0
else :
    print("jawaban anda tidak valid")

total_harga = harga_toping + harga_crust + harga_ukuran + harga_keju

print("thank you for choosing Pizza Hut deliveries!")
print("Your final bill is: Rp", total_harga )

