from src.handlers.average_handler import Average


filename = "example_test.log"


def test_process_log_file():
    endpoints_data = Average(filename).process_log_file()

    assert endpoints_data
    assert isinstance(endpoints_data, dict)


def test_calculate_averages():
    mock_data = {
        "/api/homeworks/...": {"count": 55241, "response_time": 5117.5659999996715},
        "/api/context/...": {"count": 43907, "response_time": 849.7039999999848},
    }

    result = Average(filename).calculate_averages(mock_data)

    assert result
    assert isinstance(result, list)


def test_generate_report():
    result = Average(filename).generate_report()

    assert result
    assert isinstance(result, str)
