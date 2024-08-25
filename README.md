## **QARF GUI Automation**

This project automates the E2E testing for QARF Application using BDD(Behave) with Selenium,Python. Currently it covered
Smoke Test. Framework Features

Page Object Model is followed in this framework

**pages** folder contains the elements and corresponding actions of the pages.
**features**folder contains steps folder which has all the test files and also the feature files.
**configuration**directory contains the configuration files.
**utils** directory contains the utility functions.
**tests** contains test related files.
**requirements.txt**file contains all the python packages needed to run this framework.

**gitignore** This file contains all ignored files.


### **Commands to run the tests**

**To run the test with allure report**
`behave -f allure_behave.formatter:AllureFormatter -o reports/ features/login.feature`

**To run the test without allure report** `behave features/login.feature`

**To generate the html allure report from the json files inside reports folder**
`allure serve reports/`

**To run the test Cases one by one**
`behave --tags=TC01`

**Executing Behave Tests Tagged with @smoke**
`behave --tags=@smoke   `

**To run the all text cases using pytest**
`pytest`
