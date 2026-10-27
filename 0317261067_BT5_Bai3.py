# KHOI TAO DU LIEU
von_goc = 20.0  # Don vi: ty VND

ty_gia_shocks = [-0.03, 0.00, 0.03]
lai_suat_shocks = [-0.02, -0.01, 0.01, 0.02]

print("=== MA TRAN PHAN TICH DO NHAY GIA TRI DANH MUC (TY VND) ===")
print(f"Von danh muc ban dau: {von_goc:.2f} Ty VND")
print()

# IN TIEU DE MA TRAN
print(f"{'Thay doi lai suat (Dong) / Ty gia (Cot)':<43}", end="")
for fx in ty_gia_shocks:
    print(f"{fx * 100:>10.1f}%", end="")
print()

print("-" * 73)

# VONG LAP LONG NHAU
for ir in lai_suat_shocks:
    print(f"Lai suat: {ir * 100:+.1f}%".ljust(43), end="")

    for fx in ty_gia_shocks:
        gia_tri_moi = von_goc * (1 + 1.5 * fx - 2.0 * ir)
        print(f"{gia_tri_moi:>10.2f}", end="")

    print(" Ty")

print("-" * 73)
