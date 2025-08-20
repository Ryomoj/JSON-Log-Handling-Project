from abc import ABC, abstractmethod


# Абстрактный класс "Обработчик логов"
class LogHandler(ABC):
    # Метод для обработки файлов логов
    @abstractmethod
    def process_log_file(self):
        pass

    # Метод для генерации отчёта
    @abstractmethod
    def generate_report(self):
        pass
