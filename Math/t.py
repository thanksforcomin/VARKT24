start = 10_000
end = 50_000
step = 500
end_d = 75_000
count = 0

for _ in range(start, end, step):
    for __ in range(_ + 5000, end_d, step):
        count += 1

print(count * 3 / 3600)
