#!/bin/bash
set -e

# setup.sh - prepare a Frappe bench with the ferum_customs app

echo "\U1F4E6 Installing dependencies..."
pip install -U pip setuptools wheel
pip install frappe-bench

echo "\U1F527 Initializing bench..."
bench init ferum-bench --frappe-branch version-15
cd ferum-bench

# add the ferum_customs app from this repository
APP_PATH="$(cd .. && pwd)"
bench get-app ferum_customs "$APP_PATH"
bench new-site test.local
bench --site test.local install-app ferum_customs

