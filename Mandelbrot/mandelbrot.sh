#!/bin/bash

while getopts "x:y:w:h:s:n:b:p:f:" opt; do
    case $opt in
        x) export x_coord="$OPTARG" ;;
        y) export y_coord="$OPTARG" ;;
        w) export width="$OPTARG" ;;
        h) export height="$OPTARG" ;;
        s) export step="$OPTARG" ;;
        n) export iters="$OPTARG" ;;
        b) export bound="$OPTARG" ;;
        p) export power="$OPTARG" ;;
        f) export filename="$OPTARG" ;;
        \?) echo "Invalid option: -$OPTARG" ;;
    esac
done

VENV_DIR="./venv"

# Create python venv
python3.11 -m venv $VENV_DIR
echo "Virtual environment created in $VENV_DIR"

# Activate venv
source "$VENV_DIR/bin/activate"

# Install requirements
cd mandelbrotJS
npm install || exit 1
cd ..
python3.11 -m pip install --upgrade pip
pip install -r ./mandelbrotPy/requirements.txt

# Run python script
python3.11 ./mandelbrotPy/mandelbrot.py $filename