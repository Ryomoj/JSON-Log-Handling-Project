
Команды для запуска:

База
python src/main.py --file example1.log --report average

Два файла 
python src/main.py --file example1.log --file example2.log --report average

С датой
python src/main.py --file example2.log --report average --date "2025-06-22"



Для проверки покрытия тестами:
pytest --cov=src tests/