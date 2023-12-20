import re

with open('./day_19/input.txt', 'r') as file:
    workflows, inputs = map(lambda x: x.splitlines(),
                            file.read().split('\n\n'))


workflows = {workflow.split('{')[0]: workflow.split(
    '{')[1][:-1].split(',') for workflow in workflows}

total = 0

for item in inputs:
    exec('\n'.join(item[1:-1].split(',')))

    currentWorkflow = 'in'
    while currentWorkflow not in 'AR':
        conditions = workflows[currentWorkflow]
        for condition in conditions:
            if '>' not in condition and '<' not in condition:
                currentWorkflow = condition
                break
            if eval(condition.split(':')[0]):
                currentWorkflow = condition.split(':')[1]
                break
    if currentWorkflow == 'A':
        total += x + m + a + s

print(total)
