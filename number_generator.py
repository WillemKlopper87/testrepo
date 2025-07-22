import random

# Weight distributions
weights_main = {5: 0.15, 13: 0.1, 15: 0.1, 33: 0.15, 38: 0.1, 39: 0.1, 43: 0.1, 45: 0.1, 50: 0.1}
weights_bonus = {2: 0.1, 9: 0.1, 11: 0.1, 12: 0.1, 13: 0.1}  # Adjusted for Bonus numbers
default_weight = 0.02
ranges = [(1, 22), (6, 32), (14, 40), (27, 47), (39, 50)]

# Previous draw for memory
previous_draw = [5, 15, 32, 33, 45]
previous_bonus = 13

# Keep 0–2 numbers from previous draw
keep = random.sample(previous_draw, k=random.randint(0, 2))
draw = keep[:]

# Generate Number 1–5
for i in range(5):
    if i not in [previous_draw.index(x) for x in keep if x in previous_draw]:
        low, high = ranges[i]
        valid = [x for x in range(low, high+1) if x not in draw and (not draw or x > draw[-1])]
        if valid:
            # Encourage small gaps in Number 3–5
            if i >= 2 and draw:
                valid = [x for x in valid if any(abs(x - d) <= 5 for x in draw[-2:]) or random.random() < 0.3]
            draw.append(random.choices(valid, weights=[weights_main.get(x, default_weight) for x in valid], k=1)[0])
draw.sort()

# Generate Bonus (1–20, no overlap with current draw)
valid_bonus = [x for x in range(1, 21) if x not in draw]
# Allow Bonus to echo previous draw numbers
if random.random() < 0.3 and previous_draw[0] in valid_bonus:  # Echo Number 1 or 2
    bonus = previous_draw[0]
else:
    bonus = random.choices(valid_bonus, weights=[weights_bonus.get(x, default_weight) for x in valid_bonus], k=1)[0]

print(f"Draw: {draw}, Bonus: {bonus}")