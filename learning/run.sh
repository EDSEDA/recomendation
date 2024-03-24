#!/bin/sh

cd ./learning
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install jupyter
jupyter notebook
