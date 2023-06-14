#!/usr/bin/env python3


lines = open('rosanswers_tags2.csv').readlines()
out = []
for l in lines:
    elements = l.strip().split(',')
    if len(elements) == 1:
        orig = elements[0]
        lower = orig.lower()
        out.append(f'{orig},{lower},ros')
    else:
        if not 'ros' in elements[1:]:
            elements.append('ros')
        out.append(','.join(elements))

# print(out)
out.sort()
with open('result.csv','w') as outh:
    for l in out:
        outh.write(f'{l}\n')