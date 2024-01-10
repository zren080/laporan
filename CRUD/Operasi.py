from . import Database
from .Util import random_string
import time
import os
import string

def read_nik(input_nik):
    try:
        with open(Database.DB_NAME,'r') as file:
            while(True):
                content = False
                while (content != input_nik):
                    content = file.readline()
                    if (content == input_nik):
                        break
                return content

    except:
        print('Database error')
        return False

def delete(no_buku):
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0 
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open('data_temp.txt','a',encoding='utf-8') as temp_file:
                        temp_file.write(content)
                
                counter += 1

    except:
        print('Database error')

    os.rename('data_temp.txt',Database.DB_NAME)
    

def update(pk,date_add,nama,alamat,no_buku,nik):
    data = Database.TEMPLATE.copy()

    data['pk'] = pk
    data['date_add'] = date_add 
    data['nama'] = nama + Database.TEMPLATE["nama"][len(nama):]
    data['alamat'] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data['nik'] = str(nik)

    data_str = f"{data['pk']},{data['date_add']},{data['nama']},{data['alamat']},{data['nik']}\n"
    panjang_data = len(data_str)
    try:
        with open(Database.DB_NAME,'r+',encoding='utf-8') as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print('error dalam update data')

# Create Data
def create(nama,alamat,nik):
    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d') 
    data['nama'] = nama + Database.TEMPLATE["nama"][len(nama):]
    data['alamat'] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data['nik'] = str(nik)

    data_str = f"{data['pk']},{data['date_add']},{data['nama']},{data['alamat']},{data['nik']}\n"

    try:
        with open(Database.DB_NAME,'a',encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('hayyyy yukkkkkk')    

# Read Data
def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if 'index' in kwargs:
                index_buku = kwargs['index']-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print('membaca database error')
        return False

# Frist Data
def create_frist_data():
    nama = input('nama : ')
    alamat = input('alamat : ') 
    while(True):
        try:
            nik = int(input("nik\t: "))
            if len(str(nik)) == 16:
                break
            else:
                print("nik tidak boleh ±, masukan lagi")    
        except:
            print("nik harus angka, silahkan masukan nik lagi")

    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d') 
    data['nama'] = nama + Database.TEMPLATE["nama"][len(nama):]
    data['alamat'] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data['nik'] = str(nik)

    data_str = f"{data['pk']},{data['date_add']},{data['nama']},{data['alamat']},{data['nik']}\n"
    print(data_str)

    try:
        with open (Database.DB_NAME,'w',encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('hayyyy yukkkkkk')