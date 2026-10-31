def credit_score(income, credit_history_years, has_bad_debt=False):
    if has_bad_debt:
        return "Reject"
    if income < 10_000_000 or credit_history_years < 1:
        return "High Risk"
    if income >= 20_000_000 and credit_history_years >= 3:
        return "VIP"
    return "Standard"


# Test thử
print(credit_score(25_000_000, 5))                    # VIP
print(credit_score(15_000_000, 2))                    # Standard
print(credit_score(8_000_000, 5))                     # High Risk
print(credit_score(30_000_000, 10, has_bad_debt=True))  # Reject
