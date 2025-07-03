#!/bin/bash
set -e

# setup.sh - prepare a Frappe bench with the ferum_customs app

echo "\U1F4E6 Installing dependencies..."
pip install -U pip setuptools wheel
pip install -r dev-requirements.txt
pip install frappe-bench
if command -v pre-commit >/dev/null; then
    pre-commit install
else
    echo "⚠️ pre-commit не установлен"
fi

echo "\U1F527 Initializing bench..."
BENCH_DIR="${BENCH_DIR:-ferum-bench}"
SITE_NAME="${SITE_NAME:-test.local}"
ADMIN_PASSWORD="${ADMIN_PASSWORD:-admin}"
MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD:-root}"
FRAPPE_BRANCH="${FRAPPE_BRANCH:-version-15}"

bench init "$BENCH_DIR" --frappe-branch "$FRAPPE_BRANCH"
cd "$BENCH_DIR"

APP_PATH="${APP_PATH:-$(cd .. && pwd)/ferum_customs}"
bench get-app ferum_customs "$APP_PATH"
bench new-site "$SITE_NAME" \
  --admin-password "$ADMIN_PASSWORD" \
  --db-root-password "$MYSQL_ROOT_PASSWORD"
bench --site "$SITE_NAME" install-app ferum_customs

echo "Setup completed."
