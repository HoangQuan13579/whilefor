import math

xtrc = None
ytrc = None
chu_vi_toan_bo = 0

print("Nhập tọa độ điểm đầu tiên trên chu vi đa giác:")
xnhap = input("Nhập giá trị x: ")
while xnhap != "":
    ynhap = input("Nhập giá trị y: ")
    x = float(xnhap)
    y = float(ynhap)
    
    if xtrc is not None and ytrc is not None:
        khoang_cach = math.sqrt((x - xtrc)**2 + (y - ytrc)**2)
        chu_vi_toan_bo += khoang_cach
    
    xtrc = x
    ytrc = y
    
    xnhap = input("Nhập giá trị x (rỗng để kết thúc): ")
    
if xtrc is not None and ytrc is not None:
    khoang_cach = math.sqrt((xtrc - float(xnhap))**2 + (ytrc - float(xnhap))**2)
    chu_vi_toan_bo += khoang_cach

print(f"Chu vi của đa giác là: {chu_vi_toan_bo}")