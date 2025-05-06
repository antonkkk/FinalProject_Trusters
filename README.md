# Final project of Trusters team
This repository contains a set of automated tests for "Thinking Tester Contact List" web application, created using the 'pytest' framework.

---
## About the application
"Thinking Tester Contact List" is a simple web application for managing contacts: adding, editing, deleting contacts.
Application link: [https://thinking-tester-contact-list.herokuapp.com/](https://thinking-tester-contact-list.herokuapp.com/)

---
## Technology stack
- Python 3.x
- pytest
- Selenium WebDriver
- Allure Reports **???**
  
---
## Project structure
**???**

---
## Installation and configuration
1. Clone repository:
```
git clone https://github.com/antonkkk/FinalProject_Trusters.git
cd FinalProject_Trusters
```

2. Create virtual environment, activate it:
```
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv/Scripts/activate.bat     # Windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Install Allure package:
```
pip install allure-pytest
```

5. Make sure you have a browser driver (e.g. ChromeDriver) installed and it is available in your PATH.

---
## Test run
1. To execute all tests:
```
pytest tests/
```

2. To run tests with verbose output:
```
pytest -sv tests/
```

3. To execute ALL smoke test suite:
```
pytest . -m smoke
```

4. To execute ALL acceptance test suite:
```
pytest . -m acceptance
```

5. To execute ALL regression test suite:
```
pytest . -m regression
``` 

6. To generate html report:
```
pytest --html=report.html --self-contained-html tests/
```

7. To run tests with Allure report generation:
```
pytest --alluredir=allure-results
```

8. To generate Allure html report:
```
allure serve allure-results
```

---
## Fixtures
The conftest.py file describes fixtures for configuring the browser, login, and other reusable actions.

---
## Available markers
1. UI tests:
   * login - All login tests
   * sign_up - All sign up tests
   * logout - All logout tests
   * add_contact - Tests adding new contact to the contact list
   * edit_contact -Tests editing existing contact
   * delete_contact -Tests deletion existing contact
   * contact_details -Tests view contact details
   **???**

2. Common:
   * regression - Run the regression test suite
   * smoke - Run the smoke test suite
   * acceptance - Run the acceptance test suite

---
## Additional arguments
**???**

---
## Contacts and support
If you have any questions or suggestions, create an issue or write to email:
trusters_test@gmail.com

---
## License
**???**
