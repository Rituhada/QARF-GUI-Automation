## **QARF GUI Automation**

This project automates the E2E functional and non-functional testing for QARF Application using BDD(Behave) with Selenium,Python.
## Framework Features
- Page Object Model is followed in this framework.
- Pages folder contains the elements and corresponding actions of the pages.
- Features folder contains steps folder which has all the test files and also the feature files.
- Configuration directory contains the configuration files.
- Utils directory contains the utility functions.
- Tests contains test related files.
- Requirements.txt file contains all the python packages needed to run this framework.
- Gitignore This file contains all ignored files.

### **Commands to run the test cases**

**To run the test cases with allure report**
`behave -f allure_behave.formatter:AllureFormatter -o reports/ features/login.feature`

**To run the test cases without allure report** `behave features/login.feature`

**To generate single html allure report from the json files inside reports folder**
`allure serve reports/`

**To run the test cases one by one**
`behave --tags=TC01`

**Executing Behave test cases Tagged with @smoke**
`behave --tags=@smoke`

**To run the all test cases using pytest**
`pytest`