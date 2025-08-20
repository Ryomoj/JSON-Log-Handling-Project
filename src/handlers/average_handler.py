import json
from collections import defaultdict
from typing import List, Dict, Any

from tabulate import tabulate

from handlers.base import LogHandler


# Класс-обработчик отчётов типа average
class Average(LogHandler):
    def __init__(self, filename: str, date: str = None):
        self.filename = filename
        self.date = date

    def process_log_file(self) -> dict:
        """
        Метод открывает файл(ы), парсит,
        считает количество переходов по url,
        суммирует время отклика и
        создает удобный для обработки словарь
        """

        endpoints_data = defaultdict(lambda: {"count": 0, "response_time": 0.0})

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    log_data = json.loads(line.strip())

                    if "url" in log_data and "response_time" in log_data:
                        if self.date:
                            if self.date in log_data["@timestamp"]:
                                endpoint = log_data["url"]
                                response_time = float(log_data["response_time"])
                                endpoints_data[endpoint]["count"] += 1
                                endpoints_data[endpoint]["response_time"] += (
                                    response_time
                                )

                        else:
                            endpoint = log_data["url"]
                            response_time = float(log_data["response_time"])
                            endpoints_data[endpoint]["count"] += 1
                            endpoints_data[endpoint]["response_time"] += response_time
                    else:
                        print("В файле отсутствует endpoint или response_time")

        except FileNotFoundError:
            print(f"Файл {self.filename} не найден")
        except Exception as e:
            print(f"Ошибка: {e}")

        return endpoints_data

    def calculate_averages(self, processed_data: dict) -> List[Dict[str, Any]]:
        """
        Метод циклом проходится по всем строкам
        и делит общее время отклика url на
        количество переходов по этому url.
        """
        result = []

        for endpoint, data in processed_data.items():
            count = processed_data[endpoint]["count"]
            total_time = processed_data[endpoint]["response_time"]

            average_response_time = total_time / count if count > 0 else 0

            result.append(
                {
                    "endpoint": endpoint,
                    "total": count,
                    "avg_response_time": round(average_response_time, 3),
                }
            )

        result.sort(key=lambda x: x["total"], reverse=True)
        return result

    def generate_report(self):
        """
        Метод generate_report вызывает метод-обработчик process_log_file,
        результат обработки отдает в метод-калькулятор calculate_averages.

        На основе полученных от калькулятора данных собирает отчёт в
        удобном для библиотеки tabulate виде.

        Метод возвращает распечатанную таблицу со средними значениями по
        данным из входного файла(ов)
        """

        processed_data = self.process_log_file()
        if not processed_data:
            return "Нет данных для отчёта"

        processing_results = self.calculate_averages(processed_data)
        if not processing_results:
            return "Не удалось рассчитать статистику"

        table_data = []
        headers = ["endpoint", "total", "avg_response_time"]

        for n, result in enumerate(processing_results):
            table_data.append(
                [n, result["endpoint"], result["total"], result["avg_response_time"]]
            )

        result_table = tabulate(table_data, headers=headers)
        print(result_table)

        return result_table
