# ast_example.py    An example how to extract an Abstract Syntax Tree for a Python expression
#
# 2017 written by Ralf Herbrich

import sys
import ast

# A class that extract the name of all functions
class FuncLister(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(node.name)
        self.generic_visit(node)

# A class that extracts the name of a variable
class NameCollector(ast.NodeVisitor):
    name = None
    def visit_Name(self, node):
        self.name = node.id
        self.generic_visit(node)

# A class that get the name of all constants
class ConstantCollector(ast.NodeVisitor):
    constants = []
    def visit_Num(self, node):
        self.constants.append(str(node.n))
        self.generic_visit(node)
    def visit_Str(self, node):
        self.constants.append(node.s)
        self.generic_visit(node)
    def visit_NameConstant(self, node):
        self.constants.append(str(node.value))
        self.generic_visit(node)


# A class that get the name of all variables that are assigned to
class AssignCollector(ast.NodeVisitor):
    vars = []
    def visit_Assign(self, node):
        for target in node.targets:
            nc = NameCollector()
            nc.visit(target)
            self.vars.append(nc.name)
        self.generic_visit(node)

if len(sys.argv) != 2:
    print("Require the name of Python file as first argument")
    exit(0)
    
with open(sys.argv[1], "r") as source_file:
    source = ''.join(source_file.readlines())
    tree = ast.parse(source, mode='exec')
    
    ac = AssignCollector()
    ac.visit(tree)
    unique_vars = list(set(ac.vars))
    print("Unique variables:\n\t" + "\n\t".join(unique_vars))
    
    cc = ConstantCollector()
    cc.visit(tree)
    unique_consts = list(set(cc.constants))
    print("Unique constants:\n\t" + "\n\t".join(unique_consts))
    
    
