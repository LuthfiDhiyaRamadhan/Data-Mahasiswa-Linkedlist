import json
from tabulate import tabulate

class Node: #class node
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList: #class linkedlist
    def __init__(self): # awal list
        self.awal=None

    def isEmpty(self): # list kosong
        return self.awal is None

    def display(self): # tampil list
        with open("mydata.json","r")as f:
            temp=json.load(f)
            if temp==self.isEmpty(): #jika list kosong maka tampilkan data kosng
                print("[Data Kosong]")
            else:# jika tidak,tampilkan list
                bantu=self.awal
                while bantu is not None:
                    
                    bantu= bantu.next
                print(tabulate(temp, headers=["NIM","NAMA","KELAS","TEMPAT LAHIR","TANGGAL LAHIR","JURUSAN","FAKULTAS","NO HP"],tablefmt="fancy_grid"))
                #import pandas untuk menampilkan data tabel                
        print() 
    def addFirts(self):
        temp={
            "nim": [],
            "nama": [],
            "kelas": [],
            "tempatLahir": [],
            "tanggalLahir": [],
            "jurusan": [],
            "fakultas": [],
            "nohp": []
             }
        
        print("tambah awal")
        nim     =int(input("Masukan nim                           : "))
        nama    = input   ("Masukan nama                          : ")
        kelas   = input   ("Masukan kelas                         : ")
        tempatL = input   ("Masukan Tempat Lahir                  : ")
        tanggalL= input   ("Masukan Tanggal Lahir (16/11/2003)    : ")   
        jurusan = input   ("Masukan Jurusan                       : ")
        fakultas= input   ("Masukan Fakultas                      : ")
        nohp    =int(input("Masukan NO Hp (62)                    : "))
        #data=nim,nama,kelas,tempatL,tanggalL,jurusan,fakultas,nohp
        #print(dataa)
        temp["nim"].append(nim)
        temp["nama"].append(nama)
        temp["kelas"].append(kelas)
        temp["tempatLahir"].append(tempatL)
        temp["tanggalLahir"].append(tanggalL)
        temp["jurusan"].append(jurusan)
        temp["fakultas"].append(fakultas)
        temp["nohp"].append(nohp)
        
        print("DATA TELAH TERSIMPAN")
        with open ("mydata.json","w")as f:
            json.dump(temp,f,indent=2)
            newNode=Node(temp)
            newNode.next= self.awal
            self.awal=newNode
        
            
    def addLast(self):
        with open("mydata.json","r")as f:
            temp=json.load(f)

        print("tambah akhir")
        nim     =int(input("Masukan nim                           : "))
        nama    = input   ("Masukan nama                          : ")
        kelas   = input   ("Masukan kelas                         : ")
        tempatL = input   ("Masukan Tempat Lahir                  : ")
        tanggalL= input   ("Masukan Tanggal Lahir (16/11/2003)    : ")   
        jurusan = input   ("Masukan Jurusan                       : ")
        fakultas= input   ("Masukan Fakultas                      : ")
        nohp    =int(input("Masukan NO Hp (62)                    : "))
        #data=nim,nama,kelas,tempatL,tanggalL,jurusan,fakultas,nohp
        #print(dataa)
        temp["nim"].append(nim)
        temp["nama"].append(nama)
        temp["kelas"].append(kelas)
        temp["tempatLahir"].append(tempatL)
        temp["tanggalLahir"].append(tanggalL)
        temp["jurusan"].append(jurusan)
        temp["fakultas"].append(fakultas)
        temp["nohp"].append(nohp)

        with open ("mydata.json","w")as f:
            json.dump(temp,f,indent=2)
            newNode = Node(temp)
            last = self.getLast()
            last.next = newNode
                
    def add(self):# tambah data pertama        
        if self.isEmpty():
            self.addFirts()
        else:
            self.addLast()
    def getFirst(self): #ambil data pertama
        return self.awal

    def getLast(self): # ambil d1ata terakhir
        if self.isEmpty():
            return None
        else:
            bantu = self.awal
            while bantu.next is not None:
                bantu = bantu.next
            return bantu
        
    def update(self): # update data
        newData=[]
        with open("mydata.json","r")as f:
            temp=json.load(f)
            nim=temp["nim"]
            nama=temp["nama"]
            kelas=temp["kelas"]
            tempatL=temp["tempatLahir"]
            tanggalL=temp["tanggalLahir"]
            jurusan=temp["jurusan"]
            fakultas=temp["fakultas"]
            nohp=temp["nohp"]
            panjang=len(nim)-1
            if panjang<0:
                print("[ DATA KOSONG ]")
            else:
                index= int(input(f"pilih data berdasaarkan index0-{panjang}"))
                if index>panjang:
                    print("Data yang akan diupdate tidak ditemukan")
                else:
                    i=0
                    for entry in temp:
                        if i == int(index):
                            print(f" Ganti nim           : {nim[index]} ")
                            print(f" Ganti nama          : {nama[index]}")
                            print(f" Ganti kelas         : {kelas[index]}")
                            print(f" Ganti Tempat Lahir  : {tempatL[index]}")
                            print(f" Ganti Tanggal Lahir : {tanggalL[index]}")
                            print(f" Ganti Jurusan       : {jurusan[index]}")
                            print(f" Ganti Fakultas      : {fakultas[index]}")
                            print(f" Ganti No Hp         : {nohp[index]}")
                            print()
                            #inputan untuk mengganti data dari setiap index
                            nimbaru     =int(input  (" Masukan Nim Baru              : "))
                            namabaru    =input      (" Masukan Nama Baru             : ")
                            kelasbaru   =input      (" Masukan Kelas Baru            : ")
                            tempatLbaru =input      (" Masukan Tempat Lahir Baru     : ")
                            tanggalLbaru=input      (" Masukan Tanggal Lahir Baru    : ")
                            jurusanbaru =input      (" Masukan Jurusan Baru          : ")
                            fakultasbaru=input      (" Masukan Fakultas Baru         : ")
                            nohpbaru    =int(input  (" Masukan No Hp Baru            : "))
                            #ganti index dari setiap data dari inputan baru
                            nim[index]      =nimbaru
                            nama[index]     =namabaru
                            kelas[index]    =kelasbaru
                            tempatL[index]  =tempatLbaru
                            tanggalL[index] =tanggalLbaru
                            jurusan[index]  =jurusanbaru
                            fakultas[index] =fakultasbaru
                            nohp[index]     =nohpbaru
                            
                            i=i+1   
                        else:
                            newData.append(entry)
                            i=i+1
                with open("mydata.json","w")as f:
                    json.dump(temp,f, indent=2)
    def remove(self): # hapus data berdasarkan index
        newData=[]
        with open("mydata.json","r")as f:
            temp=json.load(f)
            nim=temp["nim"]
            nama=temp["nama"]
            kelas=temp["kelas"]
            tempatL=temp["tempatLahir"]
            tanggalL=temp["tanggalLahir"]
            jurusan=temp["jurusan"]
            fakultas=temp["fakultas"]
            nohp=temp["nohp"]
            panjang=len(nim)-1
            if panjang<0:
                print("[ DATA KOSONG ]")
            else:
                hapus= int(input(f"pilih data berdasarkan index 0-{panjang}"))
                i=0
                
                for entry in temp:
                    if i == int(hapus):
                       
                        del nim[hapus]
                        del nama[hapus]
                        del kelas[hapus]
                        del tempatL[hapus]
                        del tanggalL[hapus]
                        del jurusan[hapus]
                        del fakultas[hapus]
                        del nohp[hapus]

                        i=i+1
                        
                    else:
                        newData.append(entry)
                        i=i+1
        with open("mydata.json","w")as f:
            json.dump(temp,f,indent=4)
    
    def menu(self):
        print("="*112)
        print("="*30+"SELAMAT DATANG DI APLIKASI PENGOLAHAN DATA MAHASISWA"+"="*30)
        print("="*112)
        print("!"+"-"*110+"!")
        print("silahkan pilih :")
        print("1. INPUT DATA")
        print("2. TAMPIL DATA")
        print("3. UPDATE DATA")
        print("4. HAPUS DATA")
        print("5. CREDIT ")
        pilih=int(input("Masukan pilihan    : "))
        print("="*112)
        print()
        if pilih==1:
            self.add()
            self.loop()
        elif pilih==2:
            self.display()
            self.loop()
        elif pilih ==3:
            self.update()
            self.loop()
        elif pilih ==4:
            self.remove()
            self.loop()
        elif pilih==5:
            self.credit()
            self.loop()
        else:
            print("Pilihan tidak ada")
    def credit(self):
        print("="*112)
        print("="*52+" CREDIT "+"="*52)
        print("="*112)
        print("TENTANG APLIKASI")
        print("="*112)
        print("PROGRAM INI DIBUAT UNTUK PROSES PENGELOLAAN DATA MAHASISWA")
        print("KEMUDIAN SETIAP DATA YANG DIINPUTKAN AKAN TERSIMPAN DALAM FILE JSON")
        print("DATA YANG DAPAT DIOLAH ANTARA LAIN   : ")
        print("1) NIM MAHASISWA")
        print("2) NAMA MAHASISWA ")
        print("3) KELAS")
        print("4) TEMPAT LAHIR")
        print("5) TANGGAL LAHIR ")
        print("6) JURUSAN ")
        print("7) FAKULTAS ")
        print("8) NO HP ")
        print("="*112)
        print("*CATATAN")
        print("-UNTUK NO HP HARUS DI INPUT DENGAN 62 KARENA NO HP BERTIPE DATA INTEGER (TIDAK BOLEH DIAWALI DENGAN 0/NOL)")
        print("-TANGGAL LAHIR BERTIPE STRING JADI BOLEH (16/11/2003) ATAU (16 NOVEMBER)")
        print("="*112)
        print("CREATED BY")
        print("="*112)
        print("NIM          : 101221221                 ")
        print("NAMA         : LUTHFI DHIYA RAMADHAN     ")
        print("KELAS        : IF-6                      ")
        print("JURUSAN      : TEKNIK INFORMATIKA        ")
        print("="*112)

    def loop(self):
        print("="*112)
        print("1) [ KEMBALI ]")
        print("2) [ KELUAR  ]")
        back = int(input("Pilih                 :"))
        if back == 1:
            self.menu()
        elif back == 2:
            print("="*50+"TERIMA KASIH"+"="*50)

list1 = LinkedList()  # membuat/menginisialisasi linked list
list1.menu()
#list1.display()
#list1.addFirst()
#list1.addFirst()
#list1.update()
#list1.remove()

