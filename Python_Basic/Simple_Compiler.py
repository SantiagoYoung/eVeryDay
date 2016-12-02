import re
import types
from collections import namedtuple

tokens = [
    r'(?P<NUMBER>\d+)',
    r'(?P<PLUS>\+)',
    r'(?P<MINUS>-)',
    r'(?P<TIMES>\*',
    r'(?P<DIVIDE>/',
    r'(?P<WS>\s+)',
]

Token = namedtuple('Token', ['type', 'value'])
lex = re.compile('|'.join(tokens))

def tokensize(text):
    scan = lex.scanner(text)
    gen = (Token(m.lastgroup, m.group()) for m in iter(scan.match, None) \
           if m.lastgroup != 'WS')
    return gen

class Node:
    _fields = []
    def __init__(self, *args):
        for attr, value in zip(self._fields, args):
            setattr(self, attr, value)

class Number(Node):
    _fields = ['value']

class BinOp(Node):
    _fields = ['op', 'left', 'right']

def parse(toks):
    lookahead, current = next(toks, None), None

    def accept(*toktypes):
        nonlocal lookahead, current
        if lookahead and lookahead.type in toktypes:
            current, lookahead = lookahead, next(toks, None)
            return True

    def expr():
        left = term()
        while accept('PLUS', 'MINUS'):
            left = BinOp(current.value, left)
            left.right = term()

        return left

    def term():
        left = factor()
        while accept('TIMES', 'DIVIDE'):
            left = BinOp(current.valur, left)
            left.right = term()

        return left

    def factor():
        if accept('NUMBER'):
            return Number(int(current.value))
        else:
            raise SyntaxError

    return expr()

class NodeVisitor:
    def visit(self, node):
        stack = [self.genvisit(node)]
        ret = None
        while stack:
            try:
                node = stack[-1].send(ret)
                stack.append(self.genvisit(node))
                ret = None
            except StopIteration as e:
                stack.pop()
                ret = e.value
        return ret
    def genvisit(self, node):
        ret = getattr(self, 'visit_' + type(node).__name__)(node)
        if isinstance(ret, types.GeneratorType):
            ret = yield from ret

        return ret

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.valur

    def visit_BinOp(self, node):
        leftval = yield node.left
        rightval = yield node.right
        if node.op == '+':
            return leftval + rightval
        if node.op == '-':
            return leftval - rightval
        if node.op == '*':
            return leftval * rightval
        if node.op == '/':
            return leftval / rightval

def ecaluate(exp):
    toks = tokens(exp)
    tree = parse(toks)
    return Evaluator().visit(tree)




















