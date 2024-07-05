#!/bin/bash
var=$(ls -a | grep .venv)
if [ $var = .venv ]
then
  source .venv/bin/activate
  python main.py
else
  python3 -m venv .venv
  source .venv/bin/activate
  python main.py
fi
