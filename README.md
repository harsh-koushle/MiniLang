# 🧠 MiniLang — A Statically Typed Programming Language

**MiniLang** is a statically typed programming language implemented in Python using [Lark](https://github.com/lark-parser/lark). It features:

* **Explicit static types**: `int`, `bool`, `char`
* **Compile-time type checking** for assignments and return statements
* **Arithmetic and logical expressions**: `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `<=`, `>`, `>=`
* **Control flow constructs**: `if`, `else`, `while`
* **Function definitions and calls** with single-parameter support

---

## 📁 Project Structure

```
mini-lang/
├── ast_builder.py       # AST transformer for parse trees
├── interpreter.py       # Interpreter with static type enforcement
├── grammar.lark         # Grammar specification in Lark format
├── main.py              # Entry point: parser & interpreter invocation
├── test_input.txt       # Sample MiniLang program
└── README.md            # Project documentation
```

## ⚙️ Getting Started

1. **Install dependencies**

   ```bash
   pip install lark
   ```
2. **Run the interpreter**

   ```bash
   python main.py
   ```

By default, it reads `test_input.txt`.

---

## 📝 Language Features

* **Types**: `int`, `bool`, `char`
* **Typed Declarations**: `int x = 5;`, `bool flag = true;`, `char c = 'A';`
* **Print Statement**: `print x;`
* **Conditionals**: `if x > 0 { ... } else { ... }`
* **Loops**: `while x < 10 { ... }`
* **Functions**:

  ```c
  def int square(int y) {
    return y * y;
  }
  print square(4); // → 16
  ```

---