## A framework I created for practicing Web UI automation testing in Python:

### Packages I use:

* **selenium**: For driver automation
* **webdriver-manager**: For webdriver installation
* **behave**: A testing tool that supports Behaviour Driven Development (BDD). Semi-official Cucumber implementation for Python

---

### Utilities I have created:

* **Driver**: To manage Selenium WebDriver from a central place to use it with ease of config files, preventing repetition of code and duplication of drivers being used
* **ConfigurationReader**: To store values like browser type, testing environment URL, etc.
