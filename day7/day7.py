from file_reader import get_file_entries
import re
from graphviz import Digraph
from collections import defaultdict

rule_first = re.compile(r'^(\w+\s\w+).*contain\s(.*).$')
rule_second = re.compile(r'(\d+)\s(.*)\sbag.*')

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self._amounts = {}
        self.calculated_amount = - 1

    def amounts(self):
        if self.calculated_amount > 0:
            return self.calculated_amount
        _sum = 1
        for child in self.children:
            _sum += self._amounts[child] * child.amounts()
        self.calculated_amount = _sum
        return _sum

    def add_child(self, child, amount=0):
        self.children.append(child)
        self._amounts[child] = amount

    def generate_dot_names(self, dot):
        dot.node(self.name, self.name)
        for child in self.children:
            child.generate_dot_names(dot)

    def generate_dot_edges(self, dot):
        for child in self.children:
            label = ''
            if child in self._amounts.keys():
                label = str(self._amounts[child])
            dot.edge(self.name, child.name, label=label)
            child.generate_dot_edges(dot)

    def generate_dot(self, dot):
        self.generate_dot_names(dot)
        self.generate_dot_edges(dot)


    def get_all_subnodes(self):
        subtree = []
        for child in self.children:
            subtree.append(child)
            subtree.extend(child.get_all_subnodes())
        return subtree

    def __str__(self):
        string = f'+ {self.name} ->'
        string += ', '.join([str(child) for child in self.children])
        return string

def parse_rule(rule):
    if (m := rule_first.match(rule)):
        parent = m.group(1)
        children = m.group(2)
        children_parsed = []
        if not 'no other bags' in children:
            splits = children.split(', ')
            for split in splits:
                if (m := rule_second.match(split)):
                    amount = m.group(1)
                    colour = m.group(2)
                    children_parsed.append((amount, colour))
        return parent, children_parsed
    else:
        print(f'Can\'t parse rule: {rule}')

already_generated_nodes = {}

def build_tree(node, rules):
    global already_generated_nodes
    children = rules[node.name]
    for child in children:
        if child not in already_generated_nodes:
            new_node = Node(child)
            already_generated_nodes[child] = new_node
            build_tree(new_node, rules)
        node.add_child(already_generated_nodes[child])

def sub1():
    global already_generated_nodes
    already_generated_nodes = {}
    rules = get_file_entries('day7/input.txt')
    rules_parsed = defaultdict(list)
    for rule in rules:
        parent, children = parse_rule(rule)
        for child in children:
            rules_parsed[child[1]].append(parent)

    root = Node('shiny gold')
    build_tree(root, rules_parsed)
    dot = Digraph(comment='BAGGAGE 1')
    root.generate_dot(dot)
    dot.render('day7/out/1.graph', format='png')
    print(len(set(root.get_all_subnodes())))

def build_tree_with_weights(node, rules):
    global already_generated_nodes
    children = rules[node.name]
    newly_generated_nodes = []
    for child in children:
        if child[1] not in already_generated_nodes:
            new_node = Node(child[1])
            already_generated_nodes[child[1]] = new_node
            newly_generated_nodes.append(new_node)
        node.add_child(already_generated_nodes[child[1]], amount=int(child[0]))
    for child in newly_generated_nodes:
        build_tree_with_weights(child, rules)

def sub2():
    global already_generated_nodes
    already_generated_nodes = {}
    rules = get_file_entries('day7/input.txt')
    rules_parsed = defaultdict(list)
    for rule in rules:
        parent, children = parse_rule(rule)
        for child in children:
            rules_parsed[parent].append((child[0], child[1]))

    root = Node('shiny gold')
    build_tree_with_weights(root, rules_parsed)
    dot = Digraph(comment='BAGGAGE 2')
    root.generate_dot(dot)
    dot.render('day7/out/2.graph', format='png')
    print(root.amounts() - 1)
