import pytest
import sys

if __name__ == "__main__":
    sys.exit(pytest.main(["--alluredir=allure-results", "--cucumberjson=reports/cucumber.json", "--tb=short"]))
