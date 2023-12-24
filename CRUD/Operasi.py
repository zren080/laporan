from . import Database
from .Util import random_string
import time

def update(pk,date_add,judul,penulis,no_buku,tahun):
    data = Database.TEMPLATE.copy()

    data['pk'] = pk
    data['date_add'] = date_add 
    data['judul'] = judul + Database.TEMPLATE["judul"][len(judul):]
    data['penulis'] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"
    panjang_data = len(data_str)
    try:
        with open(Database.DB_NAME,'r+',encoding='utf-8') as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print('error dalam update data')

# Create Data
def create(judul,penulis,tahun):
    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d') 
    data['judul'] = judul + Database.TEMPLATE["judul"]
    data['penulis'] = penulis + Database.TEMPLATE["penulis"]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"

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
    judul = input('judul : ')
    penulis = input('penulis : ') 
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun tidak boleh ±, masukan lagi")    
        except:
            print("tahun harus angka, silahkan masukan tahun lagi")

    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d') 
    data['judul'] = judul + Database.TEMPLATE["judul"]
    data['penulis'] = penulis + Database.TEMPLATE["penulis"]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"
    print(data_str)

    try:
        with open (Database.DB_NAME,'w',encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('hayyyy yukkkkkk')



    