## A framework I created for practicing Web UI automation testing in Python:

### Packages I use:

* **selenium**: For driver automation
* **webdriver-manager**: For webdriver installation
* **behave**: A testing tool that supports Behaviour Driven Development (BDD). Semi-official Cucumber implementation for Python

---

### Utilities I have created:

* **Driver**: To manage Selenium WebDriver from a central place to use it with ease of config files, preventing repetition of code and duplication of drivers being used
* **ConfigurationReader**: To store values like browser type, testing environment URL, etc.

---

### Website I Test:

[Swag Labs](https://www.saucedemo.com/): A demo website to be tested for learners

---

### To run the test

* Clone the repository:
    ```commandline
    git clone https://github.com/memreyagci/python-bdd-practice
    ```

* Install the required libraries (preferably after switching to a virutal environment):
    ```commandline
    pip install -r requirements.txt
    ```

* Run with behave
    ```commandline
    behave
    ```
  
  - Or running by tags assigned in feature files:
    ```commandline
    behave --tags=tagname
    ```
