import time

# fungsi untuk mencari nilai sebuah permutasi
def permutasi (elemen_list):
    # best case mengembalikan elemen tunggal
    if len(elemen_list) == 1:
        return [elemen_list]
    # rekurens
    else :
        temp =[]
        # melanjutkan ke elemen berikutnya
        for i in range (len(elemen_list)):
            a = elemen_list[i]
            sisaList = elemen_list[:i] + elemen_list[i+1:]
            for j in permutasi (sisaList):
                temp.append([a]+j)
        return temp

# fungsi main
print("###########################################################")
print("#           --    --           --            --           #")
print("#          |  |  |  |         |  |          |  |          #")
print("#          |  |  |  |         |  |          |  |          #")
print("#          |   --   |         |  |          |  |          #")
print("#          |   --   |         |  |          |  |          #")
print("#          |  |  |  |         |  |           --           #")
print("#          |  |  |  |         |  |           /\           #")
print("#           --    --           --            \/           #")
print("###########################################################")
print("#                                                         #")
print("#                 CRYPTARITHMETIC SOLVER                  #")
print("#                                                         #")
print("#      ARJUNA MARCELINO         13519021        K01       #")
print("#                                                         #")
print("###########################################################")
print("")
print("File yang diterima hanya dengan ekstensi \".txt\"")

# menerima masukan nama file
soal = input("Masukkan nama file teks (dengan ekstensi) : ")

# buka file
file_soal = open("../test/"+soal,"r")

# baca isi file
baca_soal = file_soal.read()

# mulai menghitung waktu
start = time.time()

# membersihkan karakter '+', '-', '\n'
car_bersih = baca_soal
car_bersih = car_bersih.replace('+','')
car_bersih = car_bersih.replace('-','')
car_bersih = car_bersih.replace('\n','')

# menyimpan kata
kata = car_bersih.split()

# menyimpan huruf berbeda
huruf = car_bersih.replace(' ','')
huruf = list(dict.fromkeys(huruf))

# menentukan banyaknya operan
n_operan = len(kata)-1


cek = 0
# mencari solusi yang benar dengan mencoba semua kemungkinan permutasi
found = False
data = list('1234567890') 
for p in permutasi(data): 
    sum = 0
    nilai_hasil = 0
    nilai_operan = [0 for i in range (n_operan)]
    nol = False
    for i in range (n_operan) :
        digit = len(kata[i])-1
        for curr in kata[i] :
            idx = huruf.index(curr)
            nilai_operan[i] += int(p[idx])*(10**digit)
            digit-=1
        sum += nilai_operan[i]
        if (int(p[huruf.index(kata[i][0])])==0):
            nol = True

    digit_hasil = len(kata[n_operan])-1  
    for curr in kata[n_operan] :
        indx = huruf.index(curr)
        nilai_hasil += int(p[indx])*(10**digit_hasil)
        digit_hasil-=1
    if (int(p[huruf.index(kata[n_operan][0])])==0):
            nol = True

    if (sum == nilai_hasil) and (not (nol)) :
            found = True
            break
     
    cek +=1
        
end = time.time()
# menampilkan output
print("")
print(baca_soal)

if (not(found)):
    print("\nTidak ada solusi untuk menyelesaikan permasalahan Cryptarithmetic ini")
else :
    print("\nSolusi : \n")
    for i in range (n_operan-1):
        spasi = len(kata[n_operan])-len(kata[i])
        print(' '*spasi+str(nilai_operan[i]))

    spasi = len(kata[n_operan])-len(kata[n_operan-1])
    print(' '*spasi+str(nilai_operan[n_operan-1])+' +')
    print('-'*(len(kata[n_operan])+2))
    print(nilai_hasil)
    print("\nWaktu eksekusi program : "+ str(end - start),"detik")
    print("\nJumlah tes yang dilakukan untuk menemukan substitusi angka yang benar untuk setiap huruf : ",cek,"kali")
    
# tutup file
file_soal.close()
