def calculate_emi(principal, annual_rate, months):
    r = annual_rate / 12                      # lãi suất tháng
    if r == 0:                                # tránh chia cho 0 khi lãi = 0%
        emi = principal / months
    else:
        factor = (1 + r) ** months
        emi = principal * r * factor / (factor - 1)
    total_interest = emi * months - principal
    return emi, total_interest                # trả về tuple (emi, total_interest)


# Test: unpacking
emi, interest = calculate_emi(1_000_000_000, 0.12, 12)
print(f"Trả mỗi tháng: {emi:,.0f} VNĐ | Tổng lãi phải trả: {interest:,.0f} VNĐ")
