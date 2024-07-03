# Repository QA Automation (practice)
This repository includes framework files for automation testing(SQL, API, UI). 
Documentation using Python.
_____
## Tools:
+ [SqLite](https://www.sqlite.org/)
+ [Selenium](https://www.selenium.dev/)
+ [Pytest](https://docs.pytest.org/)
_____
## Overview
This repository contains the core files of the modular framework for automated testing of objects such as Database, API and UI. 
_____
## Files structure
```
|   .gitignore
|   become_qa_auto.db
|   conftest.py
|   pytest.ini
|
+---config
|       config.py
|
+---modules
|   +---api
|   |   \---clients
|   |       |   github.py
|   |       |   __init__.py
|   |
|   +---common
|   |   |   database.py
|   |   |   __init__.py
|   |
|   \---ui
|       \---page_objects
|           |   base_page.py
|           |   sign_in_page.py
|           |   vsl_book_search.py
|           |   __init__.py
|
\---tests
    +---api
    |   |   test_api.py
    |   |   test_fixtures.py
    |   |   test_github_api.py
    |   |   test_http.py
    |   |
    +---database
    |   |   test_database.py
    |
    \---ui
        |   test_ui.py
        |   test_ui_page_object.py
        |   test_vsl_book_search.py
```    


