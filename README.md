# Journal Entries: Bank & Cash Journals

Odoo 18 module that extends the **Journal** field on manual journal entries so Bank and Cash journals appear alongside Miscellaneous Operations (general) journals.

## Problem

By default, when you create a manual journal entry (**Accounting → Journal Entries**), Odoo only lists journals of type **Miscellaneous Operations** (`general`). Bank and Cash journals are hidden from the dropdown, and selecting one would be reset by the standard compute logic.

## Solution

This module:

1. Extends `_compute_suitable_journal_ids` so the Journal dropdown includes `general`, `bank`, and `cash` journals for manual entries.
2. Extends `_get_valid_journal_types` so a selected Bank or Cash journal is accepted and not cleared by `_compute_journal_id`.

Customer invoices and vendor bills keep their standard sale/purchase journal filtering.

## Requirements

| Item | Value |
|------|--------|
| Odoo version | 18.0 |
| Dependency | `account` |
| License | LGPL-3 |

## Installation

1. Copy the `account_move_journal_bank_cash` folder into your Odoo addons path.
2. Update the apps list.
3. Install **Journal Entries: Bank & Cash Journals**.

## Usage

1. Go to **Accounting → Journal Entries**.
2. Create a new entry.
3. Open the **Journal** field: you can choose Miscellaneous, Bank, or Cash journals.

## Technical notes

- Model inheritance: `account.move`
- Methods overridden:
  - `_get_valid_journal_types`
  - `_compute_suitable_journal_ids`
- No XML data or views; pure Python extension.

## Author

**Charlie Rostant YOSSA**

- Phone: +237 656 95 38 29
- Email: charlieyossa@gmail.com
