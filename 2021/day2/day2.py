import sys

x = 0
depth = 0
# first half: for line in open(sys.argv[1]).readlines():
# first half:     line = line.strip()
# first half:     if not line:
# first half:         continue
# first half:     movement, delta = line.strip().split()
# first half:     delta = int(delta)
# first half: 
# first half:     # move
# first half:     if movement == 'forward':
# first half:         x += delta
# first half:     elif movement == 'down':
# first half:         depth += delta
# first half:     elif movement == 'up':
# first half:         depth -= delta

aim = 0
for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if not line:
        continue
    movement, delta = line.strip().split()
    delta = int(delta)

    # move
    if movement == 'forward':
        x += delta
        depth += aim * delta
    elif movement == 'down':
        aim += delta
    elif movement == 'up':
        aim -= delta

print(f'x: {x}, depth: {depth}')
print(f'Result: {x * depth}')

