#!/bin/bash
set -e

# Установка Python-зависимостей
cd backend
pip install -r requirements.txt || exit 1
cd ..

# Установка зависимостей для разработки и pre-commit
pip install -r dev-requirements.txt

# Настройка git-хуков
pre-commit install

# Установка Node-зависимостей
cd frontend
npm install || exit 1
cd ..

echo "Setup completed successfully."
