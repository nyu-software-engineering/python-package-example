# 🥠 PyFortuneCookie

A fun Python package that generates your **daily fortune cookie** — complete with a lucky number and color!  
Perfect for learning how to build and run Python packages.

---

## 📦 Installation

Clone or download this repository, then install it locally (in editable mode):

```bash
pipenv install
pipenv run pip install -e .
````

If you don’t have **pipenv**, install it first:

```bash
pip install pipenv
```

---
💻 Run Locally (for teammates)

If you want to run this project on your own machine (e.g., to test or modify it):

# 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/pyfortunecookie.git
cd pyfortunecookie
```

# 2️⃣ Install pipenv and dependencies
```bash
pip install pipenv
pipenv install
```
# 3️⃣ Enter the virtual environment
```bash
pipenv shell
```
# 4️⃣ Run the tests (optional, to verify everything works)
```bash
pipenv run pytest
```bash
# 5️⃣ Run the package
```bash
python3 -m pyfortunecookie
```

💡 You can exit the environment anytime with:

```
exit
```
---

## 🚀 Usage

You can run PyFortuneCookie either from the **command line** or directly as a **Python module**.

### ▶️ Option 1: Run as command-line tool

```bash
pipenv run pyfortunecookie
```

### ▶️ Option 2: Run as a Python module

```bash
pipenv run python -m pyfortunecookie
```

### ▶️ Option 3: Import and use functions in your code

```python
from pyfortunecookie.core import get_fortune, get_lucky_number, get_color

print(get_fortune())
print(get_lucky_number())
print(get_color())
```

---

## 🌟 Example Output

When you run the command:

```bash
pipenv run pyfortunecookie
```

You might see something like this:

```
🥠 Welcome to PyFortune Cookie!

Today's fortune: Your curiosity will lead to something amazing today ✨
Your lucky number: 37
Your lucky color: Lavender
```

Each time you run it, you’ll get a new random fortune, number, and color!

---

## 🧠 Features

| Function             | Description                      |
| -------------------- | -------------------------------- |
| `get_fortune()`      | Returns a random fortune message |
| `get_lucky_number()` | Generates a random lucky number  |
| `get_color()`        | Returns a random lucky color     |

---

## 🧪 Run Tests

Make sure everything works properly with:

```bash
pipenv run pytest
```

All tests are located inside the `tests/` directory.

---

## 🛠 Project Structure

```
pyfortunecookie/
├── src/
│   └── pyfortunecookie/
│       ├── __init__.py
│       ├── __main__.py
│       └── core.py
├── tests/
│   └── test_core.py
├── Pipfile
├── pyproject.toml
└── README.md
```

---

## 👩‍💻 Author

Created by **Sina Liu** (NYU SWE Fall 2025)
-- a practice for SWE Project 3! 🌈


