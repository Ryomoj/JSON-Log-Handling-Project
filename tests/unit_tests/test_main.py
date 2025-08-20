from src.main import main_function


class MockArgs:
    def __init__(self):
        self.report = "average"
        self.file = "example1.log"
        self.date = None


def test_main_function():
    mock_args = MockArgs()
    result = main_function(mock_args)

    assert not result
