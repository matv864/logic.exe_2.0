import os

IGNORED_OBJECTS = [
    "__pycache__",
    ".git",
    "assets"
]

all_sum = 0


def count_lines_in_file(full_name):
    global all_sum
    count = len(open(full_name).readlines())
    print(full_name, count)
    all_sum += count


queue = ["."]

while queue:
    now_dir = queue.pop(0)
    objects = filter(lambda x: x not in IGNORED_OBJECTS, os.listdir(now_dir))
    for obj in objects:
        full_path = f"{now_dir}/{obj}"
        if os.path.isdir(full_path):
            queue.append(full_path)
        else:
            # print(full_path)
            count_lines_in_file(full_path)

print(all_sum)
