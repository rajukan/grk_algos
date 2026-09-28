from collections import defaultdict

nums = [14, 142,41, 72, 214, 421, 99, 142]

groups=defaultdict(list)

for num in nums:
    s=str(num)
    key=min(s[i:] + s[:i] for i in range(len(s)))
    groups[key].append(num)
    # print(f"Number: {num}, Key: {key}, Groups: {groups[key]}")
    # print(groups)

print([grp for grp in groups.values() if len(grp) > 1])
print(len([grp for grp in groups.values() if len(grp) > 1]))
