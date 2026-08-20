#!/bin/bash
find . -type d -name "__pycache__" -exec rm -rf {} +
git status