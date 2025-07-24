# MiniLang — A Statically Typed Programming Language

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
├── minilang/               # Core interpreter logic
│   ├── __init__.py
│   ├── ast_builder.py      # AST transformer for parse trees
│   ├── interpreter.py      # Interpreter with static type enforcement
│   ├── grammar.lark        # Grammar specification in Lark format
│   └── main.py             # Entry point
│
├── tests/                  # Sample programs for testing
│   └── test_input.txt
│
├── requirements.txt        # Project dependencies
├── .gitignore              # Git exclusions
└── README.md               # Documentation
```

---

## ⚙️ Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/harsh-koushle/MiniLang.git
   cd MiniLang
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the interpreter**:

   ```bash
   python -m minilang.main
   ```

   By default, it reads from `tests/test_input.txt`.

---

## 📝 Language Features

* **Types**: `int`, `bool`, `char`

* **Typed Declarations**:

  ```c
  int x = 5;
  bool flag = true;
  char c = 'A';
  ```

* **Print Statement**:

  ```c
  print x;
  ```

* **Conditionals**:

  ```c
  if x > 0 {
      print x;
  } else {
      print 0;
  }
  ```

* **Loops**:

  ```c
  while x < 10 {
      print x;
      x = x + 1;
  }
  ```

* **Functions**:

  ```c
  def int square(int y) {
      return y * y;
  }

  print square(4); // → 16
  ```

---

## 📦 Requirements

```
lark==1.1.7
```

> Install all dependencies with:
>
> ```bash
> pip install -r requirements.txt
> ```
