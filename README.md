# playwright-pytest-bdd



[Playwright Python](https://github.com/Microsoft/playwright-python) BDD framework using
pytest pytest-bdd page-object allure cucumber-report

## setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install

## How to run

1. Run tests `execute_tests_bdd.sh`
2. or pytest -v tests/step_definition/swag_labs/test_swag_labs.py

## Docker

Execute tests - `docker-compose run tests`

Rebuild container - `docker-compose build --no-cache setup`

## Cucumber Html Report

- This requires using node, which is not ideal especially in a python environment like docker.
- Better to use allure reports or pytest reports, but if you must have BDD reports:
  npm i cucumber-html-reporter
  node generate-html-report.js

npm install multiple-cucumber-html-reporter
node generate-multiple-cucumber-html-report.js

## Pytest BDD

pytest-bdd generate features/shop/shop_order_t_shirt.feature > step_definition/shop/test_shop.py

Can Generate only missing steps, or generate all.

pytest --generate-missing --feature features tests/functional

pytest-bdd generate tests/features/swag_labs.feature > tests/step_definition/swag_labs/test_swag_labs.py

###python venv etc.

pytest -v tests/step_definition/swag_labs/test_swag_labs.py --alluredir=allure-results

- will save allure results.
- allure serve allure-results
  allure generate --clean

allure open allure-report
