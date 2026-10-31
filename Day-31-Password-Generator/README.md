# Day 31 – Password Generator

## Overview
A configurable password generator that creates passwords using
selected character types and a user-defined length.

## Features
- Configurable password length
- Lowercase character option
- Uppercase character option
- Digit option
- Special character option
- Secure random generation using `secrets`
- Ensures each selected character type is included
- Does not save generated passwords

## Technologies Used
- Python 3
- secrets module
- string module

## How to Run

```bash
python password_generator.py