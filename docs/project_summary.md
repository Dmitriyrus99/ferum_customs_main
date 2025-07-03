# Сводка по текущей реализации
Конфигурация DocType и их событий хранится в `docs/doctype_config.yaml`.

## Набор DocType

На данный момент в приложении `ferum_customs` определены следующие DocType:

- `Service Request`
- `Service Report`
- `Service Report Work Item`
- `Service Report Document Item`
- `Service Object`
- `Service Project`
- `Assigned Engineer Item`
- `Payroll Entry Custom`
- `Custom Attachment`
- `Audit Log`
- `Service Contract`
- `Invoice`
- `Site`
- `Maintenance Plan`
  
Полный перечень DocType и краткое описание доступен в файле
[`docs/doctype_list.csv`](doctype_list.csv).

## Хуки (custom_hooks)

Файл `ferum_customs/custom_hooks.py` задаёт обработчики событий DocType:

- **Service Request** – `validate`, `on_update_after_submit`, `on_trash`, `after_insert`, `on_cancel`
- **Service Report** – `validate`, `on_submit`, `after_insert`, `on_cancel`
- **Service Object** – `validate`
- **Payroll Entry Custom** – `validate`, `before_save`
- **Custom Attachment** – `on_trash`

## API

В `ferum_customs/api.py` реализованы whitelisted‑методы:

- `validate_service_request`
- `on_submit_service_request`
- `cancel_service_request`
- `validate_service_report`
- `on_submit_service_report`
- `create_invoice_from_report`
- `get_request_status`
- `get_report_status`
- `generate_pdf`
- `create_pdf_attachment`

Они доступны через `frappe.call` и могут использоваться для интеграций.

## Автоматизация и вспомогательные сценарии

- Скрипты `scripts/backup.sh` и `scripts/restore.sh` создают и восстанавливают резервные копии.
- В каталоге `scripts/systemd` присутствуют юнит‑файлы `ferum_backup.service` и `ferum_backup.timer` для ежедневного запуска резервного копирования.
- В каталоге `scripts/cron` есть пример cron‑задания `ferum_backup`.
- Модуль `ferum_customs/custom_logic/automation.py` содержит функции автоматического назначения инженеров по зоне, напоминаний о сроках и проверки SLA.


## Тесты

Подробные тесты расположены в `ferum_customs/tests/` и покрывают логику хуков, API и утилит.
Дополнительные сценарии проверяют цепочку от `Service Request` до создания `Invoice`.

## Конфигурационный файл

Сводка DocType и соответствующих хуков приведена в `docs/doctype_config.yaml`.
