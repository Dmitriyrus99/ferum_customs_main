#!/bin/bash
set -e

# setup.sh - prepare a Frappe bench with the ferum_customs app

echo "\U1F4E6 Installing dependencies..."
pip install -U pip setuptools wheel
pip install frappe-bench

echo "\U1F527 Initializing bench..."
BENCH_DIR="ferum-bench"
SITE_NAME="${SITE_NAME:-test.local}"
ADMIN_PASSWORD="${ADMIN_PASSWORD:-admin}"
MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD:-root}"

bench init "$BENCH_DIR" --frappe-branch version-15
cd "$BENCH_DIR"

APP_PATH="$(cd .. && pwd)"
bench get-app ferum_customs "$APP_PATH"
bench new-site "$SITE_NAME" --admin-password "$ADMIN_PASSWORD" --db-root-password "$MYSQL_ROOT_PASSWORD"
bench --site "$SITE_NAME" install-app ferum_customs

echo "Setup completed."
