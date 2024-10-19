bilangan = [4, 5, 11, 12, 14, 16, 16, 19]
prima = []

for num in bilangan:
    if num >= 2:
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
           prima.append(num)

total_prima = len(prima)

print(f"Bilangan prima dalam array: {prima}")
print(f"Jumlah bilangan prima: {len(prima)}")