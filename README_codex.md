# Установка и тестирование Codex

Codex запускает `./setup.sh` для подготовки Frappe Bench и установки приложения
`ferum_customs`. Скрипт выполняет `bench init`, устанавливает зависимости из
`dev-requirements.txt` и настраивает `pre-commit`, поэтому ставить `frappe`
напрямую через `pip` не требуется.

Перед запуском создайте файл `.env` на основе `.env.example` и укажите 
`SITE_NAME`, `ADMIN_PASSWORD`, `MYSQL_ROOT_PASSWORD`, а также при
необходимости `BENCH_DIR`, `FRAPPE_BRANCH` и `APP_PATH`.
Codex копирует `.env.example` в `.env` автоматически.

Для доступа к PyPI убедитесь, что в `.codexrc` включён параметр `network = true`.

## Зависимости
- Python >= 3.10
- Frappe (устанавливается через bench)
- Pre-commit
- Pytest

## Задачи
- Прогон тестов: `pytest`
- Проверка кода: `pre-commit`

## Запуск вручную

1. Скопируйте `.env.example` в `.env` и при необходимости измените значения.
2. Установите зависимости Python и Node:
   ```bash
   pip install -r dev-requirements.txt
   (cd frontend && npm install)
   ```
3. Инициализируйте Bench и приложение:
   ```bash
   bash setup.sh
   ```
4. Запустите проверки локально:
   ```bash
   pre-commit run --all-files
   pytest -q
   ```

### Makefile команды

Для удобства используйте цели из `Makefile`:

```bash
make lint   # запустить pre-commit
make test   # подготовить тестовое окружение и выполнить pytest
make bench  # запустить bench start
```


