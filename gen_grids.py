import random


def gen_html(arr, s):
    for i in range(1, 6):
        for j in range(1, 6):
            s = s.replace(f"r{i}s{j}", arr[(i - 1) * 5 + j - 1])
    return s


with open("grid.html", "r") as f:
    html = f.read()

with open("tehtavat.txt", "r") as f:
    tehtavat_raw = f.readlines()

tehtavat = list(map(lambda x: x.strip(), tehtavat_raw))

for i in range(1, 201):
    random.shuffle(tehtavat)
    with open(f"outputs/{i:03}.html", "w") as f:
        f.write(
            gen_html(
                tehtavat,
                html,
            )
        )
