from . import Operasi

DB_NAME = 'data.txt'

TEMPLATE = {
    'pk':'XXXXXX',
    'date_add':'yyyy-mm-dd',
    'nama':255*" ",
    'alamat':255*" ",
    'nik':'16'
}

def init_console():
    try:
        with open (DB_NAME,'r') as file:
            print('Database tersedia')
    except:
        with open (DB_NAME,'w',encoding='utf-8') as file:
            print('Databe tidak di temukan, Membuat database baru')
            Operasi.create_frist_data()
