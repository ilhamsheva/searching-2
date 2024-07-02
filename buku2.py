import os

# Inisialisasi daftar buku
books = []

# Fungsi untuk menambah buku
def add_book():
    judul = input("Masukkan judul buku      : ")
    penulis = input("Masukkan penulis buku  : ")
    thn = input("Masukkan tahun terbit buku : ")
    book = {"judul": judul, "penulis": penulis, "tahun": thn}
    books.append(book)
    books.sort(key=lambda x: (x["judul"], x["tahun"]))

# Fungsi binary search yang mengembalikan daftar indeks dengan substring yang cocok
def binary_search(arr, target, key):
    results = []
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid][key]

        if target.lower() in guess.lower():  # Memeriksa apakah substring target ada dalam elemen yang ditebak
            # Cari ke kiri dan ke kanan dari mid untuk semua kemungkinan kecocokan
            left = mid
            right = mid
            while left >= low and target.lower() in arr[left][key].lower():  # Cari ke kiri
                results.append(left)
                left -= 1
            while right <= high and target.lower() in arr[right][key].lower():  # Cari ke kanan
                if right != mid:  # Hindari duplikasi
                    results.append(right)
                right += 1
            break
        elif guess.lower() > target.lower():
            high = mid - 1
        else:
            low = mid + 1

    return results

# Buku ditemukan berdasarkan kriteria
def find_books_by_partial_field(field, value):
    indices = binary_search(books, value, field)
    if indices:
        return [f"Buku ditemukan : '{books[index]['judul']}' oleh {books[index]['penulis']} pada tahun {books[index]['tahun']} pada indeks {index + 1}" for index in indices]
    else:
        return ["Buku tidak ditemukan"]

# Fungsi untuk menampilkan buku
def display_books():
    for index, book in enumerate(books):
        print(f"{index + 1}. {book['judul']} oleh {book['penulis']} ({book['tahun']})")

def clear_console():
    os.system("pause")
    os.system("cls")

def main():
    while True:
        print("======================================")
        print("PROGRAM PENCARIAN BUKU (BINARY SEARCH)")
        print("======================================\n")
        print("1. Input Buku")
        print("2. Tampilkan Buku")
        print("3. Cari Buku Berdasarkan Judul")
        print("4. Cari Buku Berdasarkan Penulis")
        print("5. Cari Buku Berdasarkan Tahun")
        print("6. Keluar")

        choice = input("Pilih Menu : ")

        if choice == '1':
            add_book()
            print("Buku berhasil ditambahkan.")
            clear_console()
        elif choice == '2':
            display_books()
            clear_console()
        elif choice == '3':
            user_input = input("Masukkan judul atau bagian dari judul buku yang dicari: ")
            results = find_books_by_partial_field("judul", user_input)
            for result in results:
                print(result)
            clear_console()
        elif choice == '4':
            user_input = input("Masukkan penulis atau bagian dari nama penulis buku yang dicari: ")
            results = find_books_by_partial_field("penulis", user_input)
            for result in results:
                print(result)
            clear_console()
        elif choice == '5':
            user_input = input("Masukkan tahun terbit atau bagian dari tahun terbit buku yang dicari: ")
            results = find_books_by_partial_field("tahun", user_input)
            for result in results:
                print(result)
            clear_console()
        elif choice == '6':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()