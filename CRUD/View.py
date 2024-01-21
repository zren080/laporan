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
            nama = data_break[2]
            alamat = data_break[3]
            nik = data_break[4][:-1]

            print('-'*100+'\n')
            print(f'1.nama   : {nama:.40}')
            print(f'2.alamat : {alamat:.40}')
            print(f'3.nik   : {nik:16}')
        
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
    nama = data_break[2]
    alamat = data_break[3]
    nik = data_break[4][:-1]
    
    while(True):
        print('-'*100+'\n')
        print(f'1.nama   : {nama:.40}')
        print(f'2.alamat : {alamat:.40}')
        print(f'3.nik   : {nik:16}')

        user_option = (input('\npilih opsi [1,2,3] :'))
        match user_option:
            case '1': nama = input('\nnama : ')
            case '2': alamat = input('alamat : ')
            case '3': 
                while(True):
                    try:
                        nik = int(input("nik : "))
                        if len(str(nik)) == 16:
                            break
                        else:
                            print("nik tidak boleh ±, masukan lagi")    
                    except:
                        print("nik harus angka, silahkan masukan nik lagi")
            case _: print('index tidak cocok')

        is_done = input('Apakah Selesai Update (y/n)? : ')
        if is_done == 'y' or is_done == 'Y':
            break

    Operasi.update(pk,date_add,nama,alamat,no_buku,nik)

# Create Data
def create_console():
    print('-'*100)
    print('\nSilahkan tambahkan buku\n')
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
    
    Operasi.create(nama,alamat,nik)
    print('\ndata yang anda tambahkan...')
    read_console()  

# Read Data
def read_console():
    data_file = Operasi.read()

    index = 'No'
    nama = 'nama'
    alamat = 'alamat'
    nik = 'nik'

    # Header
    print('='*109)
    print(f'{index:^4} | {nama:^40} | {alamat:^40} | {nik:^16}')
    print('-'*109+'\n')

    # Body
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        nama = data_break[2]
        alamat = data_break[3]
        nik = data_break[4]
        print(f"{index+1:4} | {nama:.40} | {alamat:.40} | {nik:16}",end="")


    # Flooer
    print('\n'+'='*109)
        

    
    
    