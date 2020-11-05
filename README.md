## Selenium Python Template with PYTEST to get started with

To automate [Selenium Webdriver](https://docs.seleniumhq.org/projects/webdriver/) binaries management in runtime I am using [webdrivermanager](https://github.com/SergeyPirogov/webdriver_manager), an excellent library by [Sergey Pirogov](https://github.com/SergeyPirogov)

### How to use?
Create the Page Objects of your Web application under **_page_objects_** package and call those Page Objects in your unittests under **_tests_** package (Sample Page Objects, testcase included in this template)

### Install
To install the required dependencies issue the below command in project root directory
```javascript
pipenv install
```

### How to run?
Issue the below commands in project root directory (Remember to activate pipenv)

```javascript
python -m pytest
```

Currently supported browsers are
* chrome
* firefox

> Feel free to modify it to your own needs :)