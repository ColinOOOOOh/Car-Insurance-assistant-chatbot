#!/bin/bash

pip3 install -r requirements.txt
python3 -m spacy download en_core_web_sm
python3 -m spacy download en
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip3 install -U spacy
