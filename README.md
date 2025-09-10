
# Log Handling Project
Приложение-обработчик файлов логов в формате JSON, разработанное для удобного расширения

## Команды для запуска
### Базовый запуск:
```bash
python src/main.py --file example1.log --report average
# example1.log - название файла
# average - название операции (average - вычисление среднего времени ответа API)
```

### Два файла:
```bash
python src/main.py --file example1.log --file example2.log --report average
```

### С датой:
```bash
python src/main.py --file example2.log --report average --date "2025-06-22"
# --date указывается для просмотра логов за конкретный день
```

#### Для проверки покрытия тестами:
```bash
pytest --cov=src tests/
```
