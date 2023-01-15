all_natural_number = set(range(1, 10001));
genarated_number = set();

for i in range(1, 10001):
    for j in str(i):
        i += int(j);
    genarated_number.add(i);
self_number = sorted(all_natural_number - genarated_number);
for k in self_number:
    print(k);

