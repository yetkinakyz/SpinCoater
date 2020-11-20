#!/bin/bash

echo "Cleaning LCD..."
python $(find ~ -iname lcdClear.py)

echo "Starting..."
python $(find ~ -iname SpinCoater.py)

exit
