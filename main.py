import producesyntaxed
from typing import List, Any


#Kinda self explanatory, makes bullet lists
def bulletlist(item):
    splititem=item.split()
    splititem.pop(0)
    render([str("- " + ' '.join(splititem))])

#Processes bold text
def bold(line):
    line=line.split("*")
    bolds = [line[i] for i in range(len(line)) if i % 2 != 0]
    for item in line:
        if item not in bolds:
            print(item, end=' ')
        else:
            producesyntaxed.producesyntaxed(item, 'aqua', True, False)
    print()

#Processes strikethroughs
def strikethrough(line):
    line=line.split("~~")
    tostrike = [line[i] for i in range(len(line)) if i % 2 != 0]
    for item in line:
        if item not in tostrike:
            print(item, end=' ')
        else:
            producesyntaxed.producesyntaxed(item, 'grey', True, False)
    print()

#Processes headings TODO: maybe H6 and H5?
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
    print()

#Run this command to render le text
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
            case x if "~~" in x:
                strikethrough(item)
            case _:
                print(item)
