import os
import CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix" : os.system('clear')
        case "nt": os.system('cls')
    
    print('SELAMAT DATANG DI PERPUSTAKAAN BUKU')
    print('DATABASE PERPUSTAKAAN')
    print('='*50+'\n')
    
    CRUD.Database.init_console()

    while(True):
        match sistem_operasi:
            case "posix" : os.system('clear')
            case "nt": os.system('cls')
    
        print('SELAMAT DATANG DI PERPUSTAKAAN BUKU')
        print('DATABASE PERPUSTAKAAN')
        print('='*50+'\n')
        
        print(f'\n1.Read Data')
        print(f'2.Create Data')
        print(f'3.Update Data')
        print(f'4.Delete Data')

        opsi = input('\nPilih Opsi:')
        
        
        match opsi:
            case '1': CRUD.read_console()
            case '2': CRUD.create_console()
            case '3': CRUD.update_console()
            case '4': print('delete data')

        is_done = input('Apakah Selesai(y/n)? : ')
        if is_done == 'y' or is_done == 'Y':
            break
        
    print('Terima Kasih ♡♡')


        
