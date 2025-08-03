@echo off
REM Run pytest with allure reporting
python -m pytest --alluredir=allure-results --cucumberjson=reports/cucumber.json
if exist allure-results (
    allure serve allure-results
)
