def save_codes(all_codes):
    with open("codes.txt", "w") as f:
        for code in all_codes:
            f.write(f"{code}\n")