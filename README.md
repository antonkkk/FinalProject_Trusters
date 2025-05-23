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
- Allure Reports
- Jenkins
- Docker
  
---
## Project structure

```text
.
├── .gitignore
├── Dockerfile
├── README.md
├── conftest.py
├── helper
│   ├── __init__.py
│   └── utils.py
├── main.py
├── pages
│   ├── __init__.py
│   ├── add_contact_page.py
│   ├── base_page.py
│   ├── contact_details_page.py
│   ├── contact_list_page.py
│   ├── edit_contact_details_page.py
│   ├── login_page.py
│   └── signup_page.py
├── pipeline_jobs
│   ├── job_acceptance
│   │   └── Jenkinsfile
│   ├── job_all
│   │   └── Jenkinsfile
│   ├── job_api
│   │   └── Jenkinsfile
│   ├── job_feature
│   │   └── Jenkinsfile
│   ├── job_regression
│   │   └── Jenkinsfile
│   ├── job_smoke
│   │   └── Jenkinsfile
│   └── job_ui
│       └── Jenkinsfile
├── pytest.ini
├── requirements.txt
├── test_data
│   ├── __init__.py
│   ├── add_contact_template.json
│   ├── config.json
│   ├── contact_fields_locators.py
│   ├── contact_template.py
│   ├── env.py
│   ├── signup.json
│   ├── user_creds.json
│   └── user_creds.py
└── tests
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   ├── test_api_add_contact.py
    │   ├── test_api_delete_contact.py
    │   ├── test_api_edit_contact_details.py
    │   ├── test_api_login.py
    │   ├── test_api_logout.py
    │   ├── test_api_signup.py
    │   └── test_api_view_contact_details.py
    └── ui
        ├── __init__.py
        ├── test_ui_add_contact.py
        ├── test_ui_edit_contact_details.py
        ├── test_ui_login.py
        ├── test_ui_signup.py
        └── test_ui_view_contact_details.py
```

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
1. UI, API tests:
   * login - All login tests
   * sign_up - All sign up tests
   * logout - All logout tests
   * add_contact - Tests adding new contact to the contact list
   * edit_contact -Tests editing existing contact
   * delete_contact -Tests deletion existing contact
   * contact_details -Tests view contact details

2. Common:
   * regression - Run the regression test suite
   * smoke - Run the smoke test suite
   * acceptance - Run the acceptance test suite
  
3. Allure markers:
   * "Login functionality" - Tests related to login functionality
   * "Signup functionality" - Tests related to Signup functionality
   * "Logout functionality" - Tests related to Logout functionality
   * "Add contact functionality" - Tests related to Add contact functionality
   * "Edit functionality" - Tests related to Edit contact functionality
   * "Delete functionality" - Tests related to Delete contact functionality
   * "View contact functionality" - Tests related to View contact details functionality

---
## Contacts and support
If you have any questions or suggestions, create an issue or write to email:
trusters_test@gmail.com

---

