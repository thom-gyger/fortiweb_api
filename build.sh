echo -e "\e[1;33mBuilding the fortiweb_api package...\e[0m"
echo -e "\e[1;33m=============================================\e[0m"
echo -e "\e[1;33mSwitching to directory $REPO_ROOT/packages/fortiweb_api\e[0m"
TEMP_VENV=$(mktemp -d)
echo -e "\e[1;33mCreating temporary virtual environment in $TEMP_VENV...\e[0m"
python3 -m venv "$TEMP_VENV"
source "$TEMP_VENV/bin/activate"

# Check and remove "dist" or "build" directory if it exists
if [ -d "build" ]; then
    echo "Removing 'build' directory..."
    rm -rf build
fi

if [ -d "dist" ]; then
    echo "Removing 'dist' directory..."
    rm -rf dist
fi

echo -e "\e[1;33mInstalling build tools in the temporary environment...\e[0m"
pip install --upgrade pip setuptools wheel build

# building
if [[ -e "setup.py" ]]; then
    echo "Building package using setup.py..."
    python setup.py sdist bdist_wheel
  elif [[ -e "pyproject.toml" ]]; then
    echo -e "\e[1;33mBuilding package using pyproject.toml...\e[0m"
    python -m build
  else
    echo "No setup.py or pyproject.toml found. Exiting."
    deactivate
    rm -rf "$TEMP_VENV"
    exit 1
  fi
deactivate

# Clean up the temporary virtual environment
echo -e "\e[1;33mCleaning up temporary virtual environment...\e[0m"
rm -rf "$TEMP_VENV"

echo -e "\e[1;32mBuild process completed!\e[0m"