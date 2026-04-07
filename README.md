# Currency Converter

A Python application with a graphical interface (GUI) that converts amounts between different currencies using the currency_converter library.

## Overview

This app provides a tkinter-based GUI for users to easily convert between different currencies. Users enter the source currency, target currency, and amount, then click a button to see the converted result.

## How It Works

1. **calculateTheCurrency()** - Main function that performs the currency conversion
2. **GUI Interface** - User inputs:
   - Source currency (e.g., USD, EUR, GBP)
   - Target currency (e.g., JPY, CAD, AUD)
   - Amount to convert
3. **Conversion** - Uses the CurrencyConverter library to perform the conversion
4. **Output** - Displays the converted amount in the output field

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

- Enhanced modularity and code organization
- Input validation and error handling
