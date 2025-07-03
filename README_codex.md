# Установка и тестирование Codex

Codex должен запускать `setup.sh` для установки Frappe и приложения `ferum_customs`.

Перед запуском создайте файл `.env` на основе `.env.example` и задайте
`SITE_NAME`, `ADMIN_PASSWORD` и `MYSQL_ROOT_PASSWORD`.

## Зависимости
- Python >= 3.10
- Frappe (устанавливается через bench)
- Pre-commit
- Pytest

## Задачи
- Прогон тестов: `pytest`
- Проверка кода: `pre-commit`


