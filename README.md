# Ferum Customs для Frappe

## Описание

`Ferum Customs` — модуль к ERPNext, который автоматизирует работу с сервисными заявками, отчётами и начислениями. Приложение расширяет стандартный функционал Frappe, добавляя удобные роли и механизмы контроля заявок.

## Требования

* Python 3.10+
* Node.js и Yarn
* MariaDB и Redis
* Linux/Unix‑подобная система (рекомендуется)

Перед запуском скрипта `dev_bootstrap.sh` убедитесь, что Redis установлен и запущен. Его можно установить следующей командой:

```bash
sudo apt update && sudo apt install -y redis-server
redis-server --version
sudo systemctl status redis
sudo systemctl enable redis
sudo systemctl start redis
```

После установки и запуска Redis повторно выполните `./dev_bootstrap.sh`.

Полная пошаговая инструкция по настройке окружения доступна в файле
[`docs/INSTALL_FULL.md`](docs/INSTALL_FULL.md).

## Быстрый старт

```bash
# загрузите репозиторий
git clone https://github.com/Dmitriyrus99/ferum_customs_main.git
cd ferum_customs_main

# скопируйте шаблон настроек окружения
cp .env.example .env

# установите системные пакеты (Ubuntu 22.04)
sudo apt-get update && sudo apt-get install -y \
  git build-essential python3-dev libffi-dev libmysqlclient-dev \
  mariadb-server redis-server xvfb libfontconfig wkhtmltopdf
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

# установка Python зависимостей
./install-dev.sh

# автоматическое развёртывание Bench и сайта
./dev_bootstrap.sh
```

После запуска `dev_bootstrap.sh` каталог `ferum-bench` будет инициализирован,
создан сайт `dev.localhost` и установлено приложение `ferum_customs`. Сервер
Bench запустится автоматически и будет доступен по адресу
`http://localhost:8000` (пользователь **Administrator**, пароль `admin`).

Для ручного развертывания тестового сайта Bench:

```bash
pip install frappe-bench
export CI=true  # позволяет запускать bench под root
sudo bench init ferum-bench --frappe-branch version-15
cd ferum-bench
sudo bench new-site test_site
bench get-app erpnext --branch version-15
bench --site test_site install-app erpnext
bench set-config allow_tests true

pytest --maxfail=1 -q
```

## Работа с репозиторием

В проекте используется [pre-commit](https://pre-commit.com/) для запуска форматирования, линтера и тестов. Установите хуки один раз:

```bash
pre-commit install
```

Перед коммитом будет автоматически выполняться `black`, `ruff`, `mypy` и `pytest`. Вы также можете запустить их вручную:
Ruff заменяет Flake8, поэтому отдельный запуск Flake8 не требуется.

```bash
pre-commit run --all-files
```

## Структура репозитория

```
ferum_customs/
├── custom_logic/          # хуки и дополнительная логика
├── doctype/               # определения DocType
├── patches/               # скрипты миграций
├── ferum_customs/tests/   # autotests
install-dev.sh             # создание виртуального окружения
dev_bootstrap.sh           # автоматическое развёртывание Bench
Makefile                   # часто используемые команды
ferum_customs/fixtures/ # демонстрационные данные
```

## Команды Makefile

Основные задачи автоматизированы через `make`:

| Цель      | Описание                                                  |
|-----------|-----------------------------------------------------------|
| `setup`   | Установка приложения и миграция базы на тестовом сайте    |
| `start`   | Запуск сервера разработки (`bench start`)                 |
| `update`  | Применение миграций, сборка бандлов и перезапуск Bench    |
| `fixtures`| Экспорт текущих фикстур                                   |
| `test`    | Подготовка тестового сайта и запуск `pytest`               |
| `lint`    | Проверка стиля кода через `pre-commit`                     |
| `bench`   | Запуск `bench start`                                      |

Для локальной отладки можно создать файл `ferum_customs/dev_hooks.py` и
дополнить или переопределить стандартные хуки приложения. Этот файл игнорируется
если отсутствует.

## Разработка и тесты

```bash
./install-dev.sh
./dev_bootstrap.sh
pre-commit run --all-files
# запуск unit-тестов с отчётом покрытия
coverage run -m pytest
coverage report -m
```

## Установка и настройка Codex

Codex CLI помогает автоматизировать работу с репозиторием. Установите утилиту и создайте конфигурационный файл на конечном сервере.

```bash
npm install -g @openai/codex
```

Пример `~/.codex/config.yaml`:

```yaml
model: o4-mini
approvalMode: suggest
fullAutoErrorMode: ask-user
notify: true
providers:
  - name: OpenAI
    baseURL: https://api.openai.com/v1
    envKey: OPENAI_API_KEY
```

Экспортируйте API-ключ:

```bash
export OPENAI_API_KEY="<ваш-ключ>"
```

## Backup

Scripts in the `scripts` directory simplify creation and restoration of backups.
Run `./scripts/backup.sh` to create an archive and `./scripts/restore.sh` with a
backup file to restore. Systemd unit files inside `scripts/systemd` can automate
daily backups. A cron job example is available in `scripts/cron` for systems
where systemd is not used. Detailed instructions are available in
[docs/backup.md](docs/backup.md).

После настройки запустите `codex` в каталоге проекта. Подробности в [docs/CODEX_SETUP.md](docs/CODEX_SETUP.md).
## Поддержка

Вопросы и предложения можно оставлять в [issue‑трекере](https://github.com/Dmitriyrus99/ferum_customs_main/issues).

---
Дополнительные материалы доступны в [docs/OUTLINE.md](docs/OUTLINE.md).
