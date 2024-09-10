from choice import first_choice, second_choice

def menu():
    while True:
        print("\nMENU PILIHAN:")
        print("1. MENGETAHUI SERVICE DAN PROTOKOL PADA JARINGAN")
        print("2. MENGETAHUI ALAMAT IP DARI SEBUAH WEBSITE")
        print("3. KELUAR")

        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            first_choice()
        elif choice == '2':
            second_choice()
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        repeat = input("ANDA INGIN MENGULANG (Y/T)? ").strip().upper()
        if repeat != 'Y':
            print("Keluar dari program.")
            break

if __name__ == "__main__":
    menu()
