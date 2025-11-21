def menu():
    print("\n===== MENU QUẢN LÝ SẢN PHẨM =====")
    print("1. Thêm sản phẩm mới")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Tìm kiếm sản phẩm theo mã")
    print("4. Cập nhật thông tin sản phẩm")
    print("5. Xóa sản phẩm theo mã")
    print("0. Thoát chương trình")
    print("=================================")


products = []


def add_product():
    id = input("Nhập mã sp : ")

    for p in products:
        if p[0] == id:
            print("Mã sản phẩm đã tồn tại! Không thể thêm.")
            return

    name = input("Nhập tên sản phẩm : ")
    quantity = int(input("Nhập số lượng sản phẩm : "))
    price = float(input("Nhập giá sản phẩm : "))

    products.append((id, name, quantity, price))
    print("Thêm sản phẩm thành công!")


def print_products():
    if not products:
        print("Danh sách sản phẩm trống!")
        return

    print("==============Danh sách sản phẩm==============")
    for p in products:
        print(f"Mã sp: {p[0]}, Tên: {p[1]}, SL: {p[2]}, Giá: {p[3]}")


def search_product():
    id = input("Nhập mã sản phẩm cần tìm: ")
    for p in products:
        if p[0] == id:
            print(f"Mã sp: {p[0]}, Tên: {p[1]}, SL: {p[2]}, Giá: {p[3]}")
            return

    print("Không tìm thấy sản phẩm!")


def update_product():
    print_products()
    id = input("Nhập mã sản phẩm cần cập nhật: ")

    for index, p in enumerate(products):
        if p[0] == id:
            print("Nhập thông tin mới (bỏ trống để giữ nguyên):")

            new_name = input(f"Tên ({p[1]}): ") or p[1]
            new_quantity = input(f"Số lượng ({p[2]}): ")
            new_price = input(f"Giá ({p[3]}): ")

            new_quantity = int(new_quantity) if new_quantity else p[2]
            new_price = float(new_price) if new_price else p[3]

            products[index] = (id, new_name, new_quantity, new_price)

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy sản phẩm!")


def delete_product():
    id = input("Nhập mã sản phẩm cần xóa: ")

    for p in products:
        if p[0] == id:
            products.remove(p)
            print("Xóa sản phẩm thành công!")
            return

    print("Không tìm thấy sản phẩm để xóa!")


while True:
    menu()
    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        print_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ! Vui lòng nhập lại.")
