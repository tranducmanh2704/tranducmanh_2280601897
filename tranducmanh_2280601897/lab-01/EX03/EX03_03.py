def tao_tuple_tu_list(lst):
    return tuple(lst)

try:
    input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ").strip()
    if not input_list:
        raise ValueError("Danh sách không được để trống!")

    numbers = [int(num.strip()) for num in input_list.split(',') if num.strip()]
    
    if not numbers:
        raise ValueError("Danh sách phải chứa ít nhất một số hợp lệ!")

    print("List:", numbers)
    print("Tuple từ List:", tao_tuple_tu_list(numbers))

except ValueError as e:
    print("Lỗi:", e)