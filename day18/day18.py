from file_reader import get_file_entries
import re
from collections import defaultdict, deque
from ast import parse, NodeTransformer, Mult, Add, copy_location, NodeVisitor, dump, literal_eval, Expression, fix_missing_locations

class ReplaceAst(NodeTransformer):

    def visit_Div(self, node):
        new_node = Add()
        copy_location(new_node, node)

        NodeVisitor.generic_visit(self, new_node)
        return new_node

    def visit_Sub(self, node):
        new_node = Mult()
        copy_location(new_node, node)

        NodeVisitor.generic_visit(self, new_node)
        return new_node

def calculate(line):
    ast = parse(line, mode='eval')
    visitor = ReplaceAst()
    transformed = visitor.visit(ast)
    transformed = fix_missing_locations(transformed)
    a = compile(transformed, '', 'eval')
    return eval(a)

def sub1():
    print(sum([calculate(line.replace('*', '-')) for line in get_file_entries('day18/input.txt')]))


def sub2():
    print(sum([calculate(line.replace('*', '-').replace('+', '/')) for line in get_file_entries('day18/input.txt')]))