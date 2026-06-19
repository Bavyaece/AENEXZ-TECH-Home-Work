AENEXZ TECH HOMEWORK

A set of three Python mini-projects covering core fundamentals: variables, data types, conditionals, loops, functions, and the often-misunderstood topic of **mutable vs immutable** objects in Python.

## 📂 Files

| File | Topic | Difficulty |
|------|-------|------------|
| `q1_result_analyzer.py` | Student Result Analyzer — grading logic, loops, lists 
| `q2_library_system.py` | Library Book Management System — dict, list, set, tuple 
| `q3_shopping_cart.py` | Shopping Cart — default arguments & mutable default pitfall 

## 📝 Overview

**Q1 — Student Result Analyzer**
Takes a student's name, roll number, and 5 subject marks, then calculates total, average, assigns a grade (A/B/C/D/Fail), and flags any subjects scored below 40.

**Q2 — Library Book Management System**
Models a simple library using the right data structure for each job — a `dict` for the book catalog (fast lookups), `tuple` values for immutable book details, a `list` for borrowed-book history (order matters), and a `set` for unique member IDs.

**Q3 — Shopping Cart with Default & Mutable Pitfall**
Explores one of Python's classic gotchas: mutable default arguments. Includes:
- Part A: identifying the bug in a function using `cart=[]` as a default
- Part B: the correct fix using `cart=None`
- Part C: a full shopping cart system demonstrating independent customer carts and tuple immutability
- Discussion comments on rebinding vs. mutating, and which built-in types are mutable

## ▶️ Running

Each file is self-contained and can be run directly:

```bash
python q1_result_analyzer.py
python q2_library_system.py
python q3_shopping_cart.py
```

## 🎯 Concepts Covered

Variables · Data Types · Lists / Sets / Tuples / Dicts · Conditionals · Loops (`for`/`while`) · Functions · Default Parameters · Mutable vs Immutable Objects

