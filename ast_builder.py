from lark import Transformer

class ASTBuilder(Transformer):
    def start(self, items): return items
    def number(self, items): return ('int', int(items[0]))
    def char(self, items): return ('char', items[0][1])
    def var(self, items): return ('var', str(items[0]))
    def true(self, _): return ('bool', True)
    def false(self, _): return ('bool', False)

    def add(self, items): return ('add', items[0], items[1])
    def sub(self, items): return ('sub', items[0], items[1])
    def mul(self, items): return ('mul', items[0], items[1])
    def div(self, items): return ('div', items[0], items[1])

    def eq(self, items): return ('eq', items[0], items[1])
    def ne(self, items): return ('ne', items[0], items[1])
    def lt(self, items): return ('lt', items[0], items[1])
    def le(self, items): return ('le', items[0], items[1])
    def gt(self, items): return ('gt', items[0], items[1])
    def ge(self, items): return ('ge', items[0], items[1])

    def expr(self, items): return items[0]
    def term(self, items): return items[0]
    def sum_expr(self, items): return items[0]
    def factor(self, items): return items[0]

    def block(self, items): return items

    def assign_stmt(self, items): return ('assign', str(items[0]), items[1])
    def typed_assign_stmt(self, items): return ('typed_assign', str(items[0]), str(items[1]), items[2])
    def print_stmt(self, items): return ('print', items[0])

    def if_stmt(self, items):
        cond = items[0]
        true_block = items[1]
        false_block = items[2] if len(items) > 2 else []
        return ('if', cond, true_block, false_block)

    def while_stmt(self, items): return ('while', items[0], items[1])
    def return_stmt(self, items): return ('return', items[0])

    def func_call_expr(self, items): return ('func_call', str(items[0]), items[1])
    def func_call_stmt(self, items): return ('func_call_stmt', str(items[0]), items[1])

    def type_int(self, _): return 'int'
    def type_bool(self, _): return 'bool'
    def type_char(self, _): return 'char'

    def typed_param(self, items): return (str(items[0]), str(items[1]))

    def func_def(self, items):
        typename = str(items[0])
        name = str(items[1])
        param_type, param_name = items[2]
        body = items[3]
        return ('func_def', typename, name, param_type, param_name, body)
