import re
import itertools

size_extracter = re.compile("print-type-size\stype:\s`(.+)`:\s(\d+)\sbytes")

def build(path):
    with open(path) as f:
        text = f.read()
        ret = dict()
        for i in size_extracter.findall(text):
            name, size = (i[0], int(i[1]))
            ret[name] = size
    return ret

sizes_nightly = build("type_sizes_nightly.txt")
sizes_optimized = build("type_sizes_optimized.txt")
types_in_both = {i for i in sizes_nightly.keys()}.intersection({i for i in sizes_optimized.keys()})

optimized = dict()
pessimized = dict()
for i in types_in_both:
    delta = sizes_nightly[i]-sizes_optimized[i]
    if delta > 0:
        optimized[i] = delta
    elif delta < 0:
        pessimized[i] = delta

print("Maximum improvement", max(optimized.values()))
print("Number of optimized types", len(optimized))
print("")

for i, j in optimized.items():
    print(i, "optimized by", j, "bytes")
    print("")
