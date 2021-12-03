import sys

gamma = 0
epsilon = 0

bin_status_log = []
max_bit_len = 0
for l in open(sys.argv[1]).readlines():
    l = l.strip()
    if not l:
        continue
    bin_status_log.append(int(l, 2))
    max_bit_len = max(max_bit_len, len(l))

def get_bit(status, n):
    return (status >> max_bit_len - n - 1) & 1

for bit in range(max_bit_len):
    gamma = gamma << 1
    epsilon = epsilon << 1

    gamma_bit = 0
    epsilon_bit = 0
    bitcounts = {0: 0, 1: 0}

    for status in bin_status_log:
        bitcounts[get_bit(status, bit)] += 1
    print(bitcounts, end=' -> ')
    if bitcounts[1] > bitcounts[0]:
        gamma_bit = 1
        epsilon_bit = 0
    else:
        gamma_bit = 0
        epsilon_bit = 1
    print(gamma_bit)

    gamma = (gamma | gamma_bit)
    epsilon = (epsilon | epsilon_bit)

print()
print('---------- First Part -------------')
print(f'gamma: {gamma:0b} {gamma}, epsilon: {epsilon:0b} {epsilon}')
print(f'Result: {gamma * epsilon}')
print()

print('---------- Second Part ------------')

def most_least_common_bit_values(values, bit):
    bitcounts = {0: 0, 1: 0}
    most_common = 0 
    least_common = 0

    for status in values:
        bitcounts[get_bit(status, bit)] += 1

    if bitcounts[1] == bitcounts[0]:
        return 'draw', 'draw'

    if bitcounts[1] > bitcounts[0]:
        most_common = 1
    if bitcounts[0] > bitcounts[1]:
        least_common = 1
    return most_common, least_common

selected_oxy = bin_status_log[:]
selected_co2 = bin_status_log[:]
for bit in range(max_bit_len):
    most, least = most_least_common_bit_values(selected_oxy, bit)
    if most == 'draw':
        selected_oxy = [x for x in selected_oxy if get_bit(x, bit) == 1]
    else:
        selected_oxy = [x for x in selected_oxy if get_bit(x, bit) == most]
    if len(selected_oxy) == 1:
        break

for bit in range(max_bit_len):
    most, least = most_least_common_bit_values(selected_co2, bit)
    if most == 'draw':
        selected_co2 = [x for x in selected_co2 if get_bit(x, bit) == 0]
    else:
        selected_co2 = [x for x in selected_co2 if get_bit(x, bit) == least]
    if len(selected_co2) == 1:
        break

oxy = selected_oxy[0]
co2 = selected_co2[0]

print(f'oxy: {oxy:0b} {oxy}, co2: {co2:0b} {co2}')
print(f'Result: {oxy * co2}')
print()

