# KHOI TAO CAC BIEN
so_du = 0
muc_tieu = 10_000_000_000
tien_gui = 60_000_000
lai_suat = 0.10
tang_tien_gui = 0.08
tuoi = 25
nam = 0

print("=== MO PHONG KE HOACH TICH LUY HUU TRI ===")
print(f"Muc tieu: {muc_tieu:,.0f} VND")
print(f"Lai suat dau tu: {lai_suat * 100:.0f}%/nam")
print("-" * 75)

print(
    f"{'Nam':<6}{'Tuoi':<7}"
    f"{'Tien gui':>18}{'Tien lai':>18}"
    f"{'So du cuoi nam':>22}"
)
print("-" * 75)

# LAP DEN KHI DAT MUC TIEU
while so_du < muc_tieu:
    nam += 1
    tuoi_hien_tai = tuoi + nam - 1

    # Tinh lai tren so du dau nam
    tien_lai = so_du * lai_suat

    # Cap nhat so du cuoi nam
    so_du = so_du + tien_lai + tien_gui

    print(
        f"{nam:<6}{tuoi_hien_tai:<7}"
        f"{tien_gui:>18,.0f}"
        f"{tien_lai:>18,.0f}"
        f"{so_du:>22,.0f}"
    )

    # Tang tien gui cho nam tiep theo
    tien_gui = tien_gui * (1 + tang_tien_gui)

print("-" * 75)
print(f"So nam can thiet: {nam} nam")
print(f"Tuoi khi dat muc tieu: {tuoi + nam - 1} tuoi")
print(f"Tong tai san cuoi ky: {so_du:,.0f} VND")
print("KET LUAN: Da dat muc tieu huu tri!")
