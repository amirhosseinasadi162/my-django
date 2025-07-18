from library import Library, Book

def main():
    library = Library()

    while True:
        print("\n📚 Library CLI 📚")
        print("1.add books")
        print("2.show list books")
        print("3.search the books")
        print("4.remove books")
        print("5.exite")

        choice = input("select the number (1-5): ")

        if choice == "1":
            title = input("title book: ")
            author = input("author book: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            library.list_books()

        elif choice == "3":
            title = input("title books for search: ")
            library.search_book(title)

        elif choice == "4":
            title = input("title books for remove")
            library.delete_book(title)

        elif choice == "5":
            print("✅ خروج از برنامه. موفق باشی!")
            break

        else:
            print("گزینه نامعتبر. لطفا دوباره تلاش کنید.")

if __name__ == "__main__":
    main()
