# Currency Converter

A simple Python script that converts amounts between different currencies.

## Overview

This script uses the `currency_converter` library to convert monetary values from one currency to another. Users are prompted to input the source currency, target currency, and the amount to convert.

## How It Works

1. **askForCurrencyTypeAndAmount()** - Main function that orchestrates the currency conversion process
2. **User Input** - Prompts the user for:
   - Source currency (e.g., USD, EUR, GBP)
   - Target currency (e.g., JPY, CAD, AUD)
   - Amount to convert
3. **Conversion** - Uses the CurrencyConverter library to perform the conversion
4. **Output** - Displays the converted amount

## Dependencies

- `currency_converter` - Library for currency conversion

## Installation

### Linux - Setting up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install currency_converter
pip install currency_converter
```

### Other Systems

```bash
pip install currency_converter
```

## Usage

```bash
python change.py
```

Follow the on-screen prompts to enter the currencies and amounts.

## Future Improvements

- Add tkinter GUI for better user interface
- Enhanced modularity and code organization
- Input validation and error handling
