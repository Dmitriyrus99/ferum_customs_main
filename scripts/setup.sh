#!/bin/bash
set -e

# Установка Python-зависимостей
cd backend
pip install -r requirements.txt || exit 1
cd ..

# Установка Node-зависимостей
cd frontend
npm install || exit 1
cd ..

echo "Setup completed successfully."
