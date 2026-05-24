# 💸 Expense Tracker

A clean, minimal expense tracking web app built with vanilla HTML, CSS, and JavaScript — no frameworks, no dependencies (except Tabler Icons for UI icons).

---

## 📋 Description

Expense Tracker is a lightweight single-page application that helps you log, view, edit, and delete personal expenses. It shows a live running total and item count, and uses a polished modal for editing — replacing the default browser `prompt()` dialogs.

---

## ✨ Features

- ➕ **Add expenses** with a title/description and amount
- 🗑️ **Delete** any expense instantly
- ✏️ **Edit** expenses via a clean modal popup
- 💰 **Live total** updates automatically
- 🎨 **Auto icons** assigned to each item
- 📱 **Responsive** — works on mobile and desktop
- ⌨️ **Keyboard shortcut** — press `Enter` in amount field to add
- 🪟 **Modal closes** on backdrop click

---

## 📁 Project Structure

```
expense-tracker/
│
├── expense-tracker.html     # Main app (all-in-one: HTML + CSS + JS)
└── README.md                # Project documentation
```

> Everything is in a single `.html` file — just open it in any browser.

---

## 🚀 Getting Started

### 1. Clone or Download
```bash
git clone https://github.com/yoursdevendhar/ExpenseTracker.git
cd ExpenseTracker
```

### 2. Open in Browser
```bash
# Simply open the file — no server needed
open index.html
```

Or double-click `index.html` in your file explorer.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| HTML5 | Page structure |
| CSS3 | Styling & layout |
| Vanilla JavaScript | App logic |

---

## 🧠 Core JavaScript Functions

| Function | Description |
|---|---|
| `addExpense()` | Reads inputs, validates, pushes to array, refreshes UI |
| `displayExpenses()` | Renders the full list and updates total & count |
| `deleteExpense(index)` | Removes item at index, refreshes UI |
| `editExpense(index)` | Opens modal pre-filled with existing values |
| `saveEdit()` | Validates and saves edited values back to array |
| `closeModal()` | Closes the edit modal |

---

## 📸 UI Overview

```
┌─────────────────────────────────┐
│  💸 Expense Tracker             │
│  Track your spending...         │
│                                 │
│  ┌──────────┐  ┌─────────────┐  │
│  │ ₹ Total  │  │  # Items    │  │
│  └──────────┘  └─────────────┘  │
│                                 │
│  ┌─────────────────────────────┐ │
│  │ Description | Amount  (₹)  │ │
│  │         [Add Expense]       │ │
│  └─────────────────────────────┘ │
│                                 │
│  RECENT EXPENSES                │
│  ┌─────────────────────────────┐ │
│  │ 🛒 Groceries   ₹500  ✏️ 🗑️ │ │
│  │ ☕ Coffee      ₹80   ✏️ 🗑️ │ │
│  └─────────────────────────────┘ │
└─────────────────────────────────┘
```

---

## ⚠️ Limitations

- Data is **not persisted** — refreshing the page clears all expenses.
- To add persistence, integrate `localStorage`:
  ```js
  // Save
  localStorage.setItem('expenses', JSON.stringify(expenses));
  // Load
  expenses = JSON.parse(localStorage.getItem('expenses')) || [];
  ```

---
