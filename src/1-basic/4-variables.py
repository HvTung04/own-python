# Biến = tên cho vùng nhớ dùng để lưu trữ dữ liệu -> đặt tên biến = đặt tên cho nơi chứa dữ liệu
# Các kí tự trong tên biến: a-z, A-Z, 0-9, _,... (Unicode)
a = None
print(a, type(a)) # = print(None, type(None))

print(True, type(True))
print(67, type(67))
print(3.6, type(3.6))
print(2+3j, type(2+3j))
print("Hello World", type("Hello World"))
print('Hello World', type('Hello World'))
print(b'Hello', type(b'Hello'))
print(("Hello", 3), type(("Hello", 3)))
print([1,2,3,4], type([1,2,3,4]))
print({'name': 'Tung', 'age': 22}, type({'name': 'Tung', 'age': 22}))

# Quy tắc đặt tên (naming conventions): ưu tiên viết thường, ngăn cách bởi '_' khi có nhiều từ, dùng '_' ở đâu cho các biến private