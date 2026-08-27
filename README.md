# 📦Warehouse Manager

A desktop warehouse management application built with Python and PySide6 (Qt for Python), using SQLite as the local database. Originally developed as my Bachelor's degree final project, it covers the core workflow of a small warehouse: registering products, receiving and issuing goods, tracking stock movements, and getting alerted when stock runs low.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)

## Features

- **Add Product** — Register new products with barcode, name, price, stock and minimum-stock threshold.
- **Goods Receiving** — Create receipts for incoming goods and update stock automatically.
- **Goods Issue** — Create receipts for outgoing goods and update stock automatically.
- **Inventory Overview** — Browse every product in a table.
- **Inventory Movement** — Filter and review all receipts (in/out) by date range.
- **Edit Product** — Update a product's details after it has been created.
- **Edit Receipt** — Update the description of an existing receipt.
- **Low Stock Alerts** — The dashboard automatically highlights products at or below their minimum stock level.
- **Print Receipts** — Generate a print preview and print any receipt directly from the app.

## Tech Stack

| Layer      | Technology                          |
|------------|--------------------------------------|
| Language   | Python 3.10+                         |
| GUI        | [PySide6](https://doc.qt.io/qtforpython/) (Qt for Python) |
| Database   | SQLite                               |
| UI Design  | Qt Designer (`.ui` files compiled to Python) |

## Project Structure

```
ProjectCode/
├── main.py                 # Application entry point
├── dbmaker.py               # Creates warehouse.db with the required tables
├── Dashboard.py / .ui       # Main window: navigation + low-stock table
├── Addproduct.py / .ui      # "Good receiving" form
├── Exitproduct.py / .ui     # "Good issue" form
├── ChangeProduct.py / .ui   # "Edit product" form
├── ReceiveForm.py / .ui     # Shared form for goods receiving & goods issue
├── ChangeReceipt.py / .ui   # "Edit receipt description" form
├── Overview.py / .ui        # Full inventory table about all products
├── Movement.py / .ui        # Receipt history with date-range filtering
├── Detail.py / .ui          # Line-item detail
├── newWindow.py / .ui       # "Add new product" form
├── resource.qrc / resource_rc.py  # Compiled Qt resources (icons)
└── icons' sourcesas png or jpg
└── warehouse.db             # SQLite database(created by dbmaker.py)
```

Each screen follows the same pattern: a `.ui` file designed in Qt Designer, compiled into a `*_ui.py` file, and a matching `.py` file that wires up the logic (database queries, signals/slots).

## Database Schema

The app uses three SQLite tables, created by `dbmaker.py`:

- **`products`** — `id`, `barcode` (unique), `name`, `price`, `stock`, `min_stock`
- **`transactions`** — `id`, `receiver`, `sender`, `type` (receive/exit), `date`, `description`, `totalprice`
- **`goodsoftransactions`** — line items linking a transaction to a product: `id`, `transaction_id`, `product_id`, `number`, `totalprice`

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/mahsimaKarami/Warehouse_Manager_app
cd Warehouse_Manager_app

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install PySide6
```

### Set up the database

The app expects a `warehouse.db` SQLite file in the project root. Generate it (once) with:

```bash
python dbmaker.py
```

> ⚠️ Running `dbmaker.py` again on an existing database will fail (tables already exist) — only run it the first time, or delete `warehouse.db` first if you want a clean start.

### Run the app

```bash
python main.py
```

## Usage

1. **Dashboard** — Launch point which shows products currently at or below their minimum stock and it has buttons to every other screen.
2. **Add Product** — Register a new product before receiving or issuing it for the first time.
3. **Goods Receiving / Goods Issue** — Pick a sender/receiver, add one or more products with quantities, and submit to create a receipt.
4. **Inventory Overview** — See stock levels for all products in warehouse.
5. **Inventory Movement** — Filter past receipts by date range and open any of them for details or printing.
6. **Edit Product** — Edit some features of some products after making them.
7. **Edit receipt** — Edit some receipt's description after making them.

## Roadmap for compeleting application

- Custom QSS styling for application
- EXE file for end-user

## Author

**Mahsima Karami** — Bachelor's degree final project.