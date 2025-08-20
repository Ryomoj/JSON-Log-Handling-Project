import argparse

from handlers.average_handler import Average


def get_argparse_config():
    parser = argparse.ArgumentParser(
        description="Анализатор лог-файлов: статистика по эндпоинтам",
        epilog="Пример использования: python main.py --file access.log --report average",
    )
    parser.add_argument("--file", type=str, required=True, help="Путь к log-файлу")
    parser.add_argument("--report", type=str, required=True, help="Тип отчёта")
    parser.add_argument(
        "--date", type=str, required=False, help="Дата отчёта (Опционально)"
    )
    args = parser.parse_args()

    return args


def main_function(args):
    if args.report == "average":
        average = Average(args.file, args.date)
        average.generate_report()
    else:
        print("Выбран неверный тип отчёта")


def main():
    args = get_argparse_config()

    return main_function(args)


if __name__ == "__main__":
    main()
