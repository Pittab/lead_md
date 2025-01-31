import producesyntaxed
from typing import List, Any

def bulletlist(item):
    producesyntaxed.producesyntaxed("- " + item.strip("*"), 'grey')

def bold(line):
    line=line.split("*")
    bolds = [line[i] for i in range(len(line)) if i % 2 != 0]
    for item in line:
        if item not in bolds:
            producesyntaxed.producesyntaxed(item, 'grey', True, False)
        else:
            print(item, end=' ')
    print()

def heading(line):
    line=line.split()
    if line[0] == "#":
        line.pop(0)
        producesyntaxed.producesyntaxed(' '.join(line), 'blue2', False, True)
    if line[0] == "##":
        line.pop(0)
        producesyntaxed.producesyntaxed(' '.join(line), 'blue', False, True)
    if line[0] == "###":
        line.pop(0)
        producesyntaxed.producesyntaxed(' '.join(line), 'aqua', False, True)
    if line[0] == "####":
        line.pop(0)
        print(' '.join(line))

def render(input_list: List[Any]):
    for item in input_list:
        match item:
            case x if x.split()[0] in ["#", "##", "###", "####"]:
                heading(item)
            case x if x.startswith("*"):
                if item.startswith ("* ") != True:
                    bold(item)
                else:
                    bulletlist(item)
            case x if "*" in x:
                bold(item)
