from . import Operasi

# Delete Data
def delete_console():
    read_console()
    print('Silahkan masukan no buku yang akan di delete')
    while(True):
        no_buku = int(input('pilih no buku : '))
        data_buku = Operasi.read(index=no_buku)
        

        if data_buku:
            break
        else:
            print('nomor tidak valid')
    while(True):
        if data_buku:
            data_break = data_buku.split(",")                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            pk = data_break[0]
            date_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]

            print('-'*100+'\n')
            print(f'1.judul   : {judul:.40}')
            print(f'2.penulis : {penulis:.40}')
            print(f'3.tahun   : {tahun:4}')
        
            is_done = input('Apakah Yakin Di Hapus (y/n)? : ')
            if is_done == 'y' or is_done == 'Y':
                Operasi.delete(no_buku)
                break
        else:
            print('Data Berhasil Di hapus')



# Update Data
def update_console():
    read_console()
    print('Silahkan masukan no buku yang akan di update')
    while(True):
        no_buku = int(input('pilih no buku : '))
        data_buku = Operasi.read(index=no_buku)
        

        if data_buku:
            break
        else:
            print('nomor tidak valid')

    
    data_break = data_buku.split(",")                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]
    
    while(True):
        print('-'*100+'\n')
        print(f'1.judul   : {judul:.40}')
        print(f'2.penulis : {penulis:.40}')
        print(f'3.tahun   : {tahun:4}')

        user_option = (input('\npilih opsi [1,2,3] :'))
        match user_option:
            case '1': judul = input('\njudul : ')
            case '2': penulis = input('penulis : ')
            case '3': 
                while(True):
                    try:
                        tahun = int(input("Tahun : "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("tahun tidak boleh ±, masukan lagi")    
                    except:
                        print("tahun harus angka, silahkan masukan tahun lagi")
            case _: print('index tidak cocok')

        is_done = input('Apakah Selesai Update (y/n)? : ')
        if is_done == 'y' or is_done == 'Y':
            break

    Operasi.update(pk,date_add,judul,penulis,no_buku,tahun)

# Create Data
def create_console():
    print('-'*100)
    print('\nSilahkan tambahkan buku\n')
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
    
    Operasi.create(judul,penulis,tahun)
    print('\ndata yang anda tambahkan...')
    read_console()  

# Read Data
def read_console():
    data_file = Operasi.read()
    
    index = 'No'
    judul = 'judul'
    penulis = 'penulis'
    tahun = 'tahun'

    # Header
    print('='*100)
    print(f'{index:^4} | {judul:^40} | {penulis:^40} | {tahun:^4}')
    print('-'*100+'\n')

    # Body
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")


    # Flooer
    print('\n'+'='*100)
        

    
    
    