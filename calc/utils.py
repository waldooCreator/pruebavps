import ast
import operator as op

# Supported operators
_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError('Only numeric constants are allowed')
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        if op_type in _operators:
            return _operators[op_type](left, right)
        raise ValueError('Operator not supported')
    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        op_type = type(node.op)
        if op_type in _operators:
            return _operators[op_type](operand)
        raise ValueError('Unary operator not supported')
    raise ValueError('Unsupported expression')


def safe_eval(expr: str):
    """Safely evaluate a simple arithmetic expression containing numbers and + - * / % and **"""
    parsed = ast.parse(expr, mode='eval')
    return _eval(parsed)
