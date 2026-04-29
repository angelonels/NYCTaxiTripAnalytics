#!/bin/bash

# NYC Taxi Trip Analytics - Project Setup Script
# This script automates the creation of the project structure and data directories.

echo " Starting project setup..."

# 1. Create directory structure
echo " Creating directories..."
mkdir -p data/raw data/processed notebooks scripts docs reports/figures tableau/screenshots assets

# 2. Create .gitkeep files for empty directories
touch data/raw/.gitkeep
touch data/processed/.gitkeep

# 3. Check for uv installation
if command -v uv &> /dev/null
then
    echo " uv is installed."
else
    echo " uv not found. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# 4. Sync environment
echo " Syncing Python environment..."
uv sync

echo " Setup complete! You can now run the notebooks in order."
echo " Raw data can be downloaded using the links in README.md or notebooks/01_extraction.ipynb"
