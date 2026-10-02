print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi n dengan while jika n tidak positif
while n <= 0:
    n = int(input("Banyak suku n harus berupa integer positif. Masukkan ulang n: "))

total = 0.0

# Perulangan for untuk menghasilkan n suku dan menghitung total
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1} = {suku}")

# Menampilkan jumlah akhir dengan dua angka di belakang koma
print(f"Jumlah = {total:.2f}")