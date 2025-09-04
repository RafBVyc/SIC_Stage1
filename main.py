import konversi

print("==== Program Konversi Suhu ====")
nilai_suhu = float(input("Masukkan nilai suhu: "))
awal = input("Masukkan satuan awal (c/f/k):").lower()
akhir = input("Masukkan satuan akhir (c/f/k):").lower()

nilai = None

if awal == "c":
    if akhir == "f":
        hasil = konversi.celsius_to_fahrenheit(nilai_suhu)
    elif akhir == "k":
        hasil = konversi.celsius_to_kelvin(nilai_suhu)
    else:
        hasil = nilai_suhu
elif awal == "f":
    if akhir == "c":
        hasil = konversi.fahrenheit_to_celsius(nilai_suhu)
    elif akhir == "k":
        hasil = konversi.fahrenheit_to_kelvin(nilai_suhu)
    else:
        hasil = nilai_suhu
elif awal == "k":
    if nilai_suhu < 0:
        print("Nilai Kelvin tidak boleh negatif!")
    elif akhir == "c":
        hasil = konversi.kelvin_to_celsius(nilai_suhu)
    elif akhir == "f":
        hasil = konversi.kelvin_to_fahrenheit(nilai_suhu)
    else:
        hasil = nilai_suhu
else:
    print("satuan tidak valid... mohon pilih diantara (c/f/k)")

if hasil is not None:
    print(f"hasil konversi = {hasil:.2f} {akhir.upper()}")