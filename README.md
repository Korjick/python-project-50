### Hexlet tests and linter status:
[![Actions Status](https://github.com/Korjick/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Korjick/python-project-50/actions)
[![Actions Status](https://github.com/Korjick/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Korjick/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Korjick_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Korjick_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Korjick_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Korjick_python-project-50)

### Демонстрация

[![asciicast](https://asciinema.org/a/740332.svg)](https://asciinema.org/a/740332)

### Описание

`gendiff` — консольная утилита и библиотека для сравнения конфигурационных файлов.
- Поддерживаемые форматы входа: JSON и YAML (`.json`, `.yml`, `.yaml`).
- Форматы вывода: `stylish` (по умолчанию), `plain`, `json`.

### Установка

- Требования: Python 3.13+, установленный `uv`.
- Установка зависимостей:

```bash
uv sync
```

### Запуск (CLI)

- Сравнение JSON:

```bash
uv run gendiff path/to/file1.json path/to/file2.json
```

- Сравнение YAML:

```bash
uv run gendiff path/to/file1.yml path/to/file2.yml
```

- Выбор формата вывода:

```bash
uv run gendiff --format stylish path/to/file1.yml path/to/file2.yml
uv run gendiff --format plain   path/to/file1.yml path/to/file2.yml
uv run gendiff --format json    path/to/file1.yml path/to/file2.yml
```

### Использование как библиотеки

```python
from gendiff import generate_diff
from gendiff.formatters import FormatName

print(generate_diff('file1.json', 'file2.json', FormatName.STYLISH))
print(generate_diff('file1.yml', 'file2.yml',   FormatName.PLAIN))
print(generate_diff('file1.json', 'file2.json', FormatName.JSON))
```

### Тесты и покрытие

```bash
uv run -m pytest -q
make test-coverage
```
