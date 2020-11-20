#!/bin/bash

CLEAR = $(find ~ -iname lcdClear.py)
MAIN = $(find ~ -iname SpinCoater.py)

echo "Cleaning LCD..."
python $CLEAR

echo "Starting..."
python $MAIN

exit
