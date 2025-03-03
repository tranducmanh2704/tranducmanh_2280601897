def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:  # Kiểm tra số chẵn
            tong += num
    return tong

try:
    input_list = input("Nhập danh sách các số (cách nhau bằng dấu phẩy): ")
    number = [int(num.strip()) for num in input_list.split(',')]  # Loại bỏ khoảng trắng thừa và chuyển sang số nguyên
    tong_chan = tinh_tong_so_chan(number)
    print("Tổng các số chẵn trong list là:", tong_chan)
except ValueError:
    print("Vui lòng nhập danh sách số hợp lệ!")
except Exception as e:
    print("Đã xảy ra lỗi:", e)