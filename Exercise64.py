tongtienpenny=0
while True:
    gia = input("Nhập giá (nhập để kết thúc): ")
    if gia == "":
        break
    tongtienpenny+= float(gia) * 100  
tong_tien = tongtienpenny / 100  
print(f"Tổng số tiền mặt hàng là: {tong_tien:.2f}")
so_tien_penny_tra = round(tongtienpenny)  
phan_du = so_tien_penny_tra % 5  
if phan_du < 2.5:
    tienmucduoi = so_tien_penny_tra - phan_du
else:
    tienmucduoi = so_tien_penny_tra + (5 - phan_du)
tienmucduoi = tienmucduoi / 100 
print(f"Số tiền phải trả nếu trả bằng tiền mặt là: {tienmucduoi:.2f}")