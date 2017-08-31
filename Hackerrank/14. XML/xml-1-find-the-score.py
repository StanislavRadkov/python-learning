import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = 0
    children = []
    
    children.extend(node)
    score += len(node.attrib)

    while children:
        child = children.pop()
        score += len(child.attrib)
        children.extend(child)

    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))