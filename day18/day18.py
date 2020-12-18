from file_reader import get_file_entries
import re
from collections import defaultdict, deque
from ast import parse, NodeTransformer, Mult, Add, copy_location, NodeVisitor, fix_missing_locations

class ReplaceAst(NodeTransformer):

    def replace(self, node, new_node):
        copy_location(new_node, node)
        NodeVisitor.generic_visit(self, new_node)
        return new_node

    def visit_Div(self, node):
        new_node = Add()
        return self.replace(node, new_node)

    def visit_Sub(self, node):
        new_node = Mult()
        return self.replace(node, new_node)

def calculate(line):
    ast = parse(line, mode='eval')
    visitor = ReplaceAst()
    transformed = visitor.visit(ast)
    transformed = fix_missing_locations(transformed)
    a = compile(transformed, '', 'eval')
    return eval(a)

def sub1():
    print('Attention! The functions of today evaluate any input brought in by input.txt - NEVER run this with arbitrary files! It may cause your device to be compromised!')
    print(sum([calculate(line.replace('*', '-')) for line in get_file_entries('day18/input.txt')]))


def sub2():
    print(sum([calculate(line.replace('*', '-').replace('+', '/')) for line in get_file_entries('day18/input.txt')]))