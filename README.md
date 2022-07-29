# Here is my final project from **Python Selenium Automation Course**
https://stepik.org/course/575

[Certificate](https://github.com/NaStenku/Certificates/blob/master/stepik-certificate-575-432aee7%20(1).pdf)

## What we have inside:
### **Pages**:
- **base_page.py** - Here we store methods that apply to the entire project in general, all wrapped up in a class to make it easy to import.

- **main_page.py, basket_page.py, product_page.py, login_page.py**  - Here we store methods for a particular page, wrapped in the class of this page. This class is a conditional MainPage - a descendant of BasePage class, so you can use the methods described in base_page.py

- **locators.py** - Here we store locators as constants. The locators of each individual page are wrapped in a class to make it easy to import

### Files
- **__init__.py** - The file essentially the constructor of  package or directory without it being called such.

- **conftest.py** - is used to define fixtures for static data used by tests.

- **pytest.ini** - is udes for pytest marks

- **requirements.txt** - requirements =)

- **test_main_page.py, test_product_page** - Here we perform the tests ourselves.


![project-structure_by_Павел Кузьмин](https://user-images.githubusercontent.com/58818244/174458904-d5f8c6c9-5282-4f6d-bd17-e30a05029184.jpeg) "img_by_Павел Кузьмин"


>#### Thank you for your time!
