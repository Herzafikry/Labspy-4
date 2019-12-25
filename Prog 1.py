data=[]
while(True):
    Nim=input("Nim : ")
    Nama=input("Nama : ")
    Tugas=int(input("Nilai Tugas : "))
    UTS=int(input("Nilai UTS : "))
    UAS=int(input("Nilai UAS : "))
    Akhir = (30 * Tugas / 100) + (35 * UTS / 100) + (35 * UAS / 100)
    data.append([Nim, Nama, Tugas, UTS, UAS, Akhir])
    ulangi=input("tambah data (y/t)?")
    if ulangi.lower() == 't':
        break;

print("\ndaftar nama\n")
print("==============================================================================================================")
print("|      Nim       |       Nama        |       Tugas       |       UTS     |       UAS     |       Akhir       |")
print("==============================================================================================================")
for x in data:
    print("|    {0:7s}  |   {1:13s}    |    {2:6d}  |   {3:5d}  |   {4:4d}  |   {5:4.2f}    |".format(x[0], x[1], x[2], x[3], x[4], x[5]))