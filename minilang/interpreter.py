class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.vars = {}
        self.types = {}
        self.functions = {}

    def eval_expr(self, node):
        if isinstance(node, tuple):
            tag = node[0]
            if tag in ('int', 'char', 'bool'): return node[1]
            elif tag == 'var':
                name = node[1]
                if name not in self.vars:
                    raise NameError(f"Variable '{name}' not defined")
                return self.vars[name]
            elif tag == 'add': return self.eval_expr(node[1]) + self.eval_expr(node[2])
            elif tag == 'sub': return self.eval_expr(node[1]) - self.eval_expr(node[2])
            elif tag == 'mul': return self.eval_expr(node[1]) * self.eval_expr(node[2])
            elif tag == 'div': return self.eval_expr(node[1]) // self.eval_expr(node[2])
            elif tag == 'eq': return self.eval_expr(node[1]) == self.eval_expr(node[2])
            elif tag == 'ne': return self.eval_expr(node[1]) != self.eval_expr(node[2])
            elif tag == 'lt': return self.eval_expr(node[1]) < self.eval_expr(node[2])
            elif tag == 'le': return self.eval_expr(node[1]) <= self.eval_expr(node[2])
            elif tag == 'gt': return self.eval_expr(node[1]) > self.eval_expr(node[2])
            elif tag == 'ge': return self.eval_expr(node[1]) >= self.eval_expr(node[2])
            elif tag == 'func_call':
                name = node[1]
                arg_val = self.eval_expr(node[2])
                return self.call_function(name, arg_val)
        raise Exception(f"Invalid expression: {node}")

    def check_type(self, name, value):
        expected = self.types.get(name)
        if expected == 'int' and isinstance(value, int): return
        if expected == 'char' and isinstance(value, str) and len(value) == 1: return
        if expected == 'bool' and isinstance(value, bool): return
        raise TypeError(f"Type mismatch for variable '{name}': expected {expected}, got {type(value).__name__}")

    def execute(self, stmts):
        for stmt in stmts:
            tag = stmt[0]
            if tag == 'assign':
                _, name, expr = stmt
                val = self.eval_expr(expr)
                if name in self.types:
                    self.check_type(name, val)
                self.vars[name] = val
            elif tag == 'typed_assign':
                _, typename, name, expr = stmt
                val = self.eval_expr(expr)
                self.types[name] = typename
                self.check_type(name, val)
                self.vars[name] = val
            elif tag == 'print':
                print(self.eval_expr(stmt[1]))
            elif tag == 'if':
                _, cond, then_body, else_body = stmt
                if self.eval_expr(cond):
                    self.execute(then_body)
                else:
                    self.execute(else_body)
            elif tag == 'while':
                _, cond, body = stmt
                while self.eval_expr(cond):
                    self.execute(body)
            elif tag == 'func_def':
                _, ret_type, name, param_type, param_name, body = stmt
                self.functions[name] = (ret_type, param_type, param_name, body)
            elif tag == 'func_call_stmt':
                _, name, arg = stmt
                self.call_function(name, self.eval_expr(arg))
            elif tag == 'return':
                raise ReturnValue(self.eval_expr(stmt[1]))

    def call_function(self, name, arg_val):
        if name not in self.functions:
            raise NameError(f"Function '{name}' not defined")
        
        ret_type, param_type, param_name, body = self.functions[name]
        
        # Save current scope
        old_vars = self.vars.copy()
        old_types = self.types.copy()
        
        # Inherit global scope and set function param
        self.vars = old_vars.copy()
        self.vars[param_name] = arg_val
        self.types = old_types.copy()
        self.types[param_name] = param_type

        try:
            self.execute(body)
        except ReturnValue as rv:
            result = rv.value
            self.vars = old_vars
            self.types = old_types
            return result

        # Restore outer scope
        self.vars = old_vars
        self.types = old_types

