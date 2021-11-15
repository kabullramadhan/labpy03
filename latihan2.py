print("MENAMPILKAN BILANGAN TERBESAR DARI N BUAH DATA YANG DIINPUTKAN, ANGKA 0 UNTUK BERHENTI")

max=0
while True:
    a=int(input("MASUKAN BILANGAN : "))
    if max < a :
        max = a
    if a==0:
        break
print("BILANGAN TERBESAR ADALAH = ",max)
