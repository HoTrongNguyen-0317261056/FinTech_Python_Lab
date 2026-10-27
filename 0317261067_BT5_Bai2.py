# THONG SO TRAI PHIEU
F = 1_000_000
c = 0.09
N = 10
y = 0.085

# 1. Tinh tien lai coupon hang nam
C = F * c

# 2. Tinh gia tri hien tai cua cac khoan coupon
tong_pv_coupon = 0.0

print("=== DINH GIA TRAI PHIEU DOANH NGHIEP ===")
print(f"Menh gia trai phieu: {F:,.0f} VND")
print(f"Lai coupon hang nam: {C:,.0f} VND")
print(f"Loi suat thi truong: {y * 100:.1f}%/nam")
print("-" * 65)

print(f"{'Nam':<10}{'Tien coupon':>18}{'Gia tri hien tai':>25}")
print("-" * 65)

for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c

    print(f"{t:<10}{C:>18,.0f}{pv_c:>25,.2f}")

# 3. Tinh gia tri hien tai cua menh gia
pv_f = F / ((1 + y) ** N)

# 4. Tinh gia trai phieu
gia_trai_phieu = tong_pv_coupon + pv_f

print("-" * 65)
print(f"Tong PV tien coupon: {tong_pv_coupon:,.2f} VND")
print(f"PV menh gia trai phieu: {pv_f:,.2f} VND")
print(f"Gia tri trai phieu: {gia_trai_phieu:,.2f} VND")

# 5. Phan loai trai phieu
if gia_trai_phieu > F:
    print("Ket luan: TRAI PHIEU CO GIA CAO HON MENH GIA (PREMIUM)")
elif gia_trai_phieu < F:
    print("Ket luan: TRAI PHIEU CO GIA THAP HON MENH GIA (DISCOUNT)")
else:
    print("Ket luan: TRAI PHIEU DUNG MENH GIA (PAR)")
