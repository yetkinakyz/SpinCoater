#!/bin/bash

echo "Cleaning LCD..."
find ~ -iname lcdClear.py
python $(find ~ -iname lcdClear.py)

echo "Starting..."
find ~ -iname SpinCoater.py
python $(find ~ -iname SpinCoater.py)

exit
