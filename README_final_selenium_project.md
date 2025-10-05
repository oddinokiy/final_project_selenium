
# Final Selenium Automation Project

This is a UI test automation project developed using **Python**, **Selenium**, and **Pytest**.  
It tests the functionality of the [Restful Booker](https://restful-booker.herokuapp.com) web application, focusing on booking-related scenarios.

## 📌 Features
- Token-based login automation
- Create a new booking
- Update existing booking
- Delete booking
- Automated setup and teardown with Pytest fixtures
- Modular structure using the Page Object Model

## 🧰 Tech Stack
- Python 3.10+
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- RESTful API testing concepts

## 🚀 How to Run Tests

1. Clone the repository:
   ```bash
   git clone https://github.com/oddinokiy/final_project_selenium.git
   cd final_project_selenium
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

## 📂 Project Structure

```
final_project_selenium/
│
├── pages/              # Page Object Models for Login and Booking
├── tests/              # Pytest-based test scripts
├── conftest.py         # Fixtures and setup
├── pytest.ini          # Pytest configuration
├── requirements.txt    # List of required packages
└── README.md           # Project documentation
```

## ✅ Example Test Scenarios
- ✅ Create a booking and validate the response
- ✅ Authenticate using token and perform authorized actions
- ✅ Update a booking with new data
- ✅ Delete a booking and check the result

## 👨‍💻 Author
**Nikita Sharoiko-Shakhrai**  
Final project for QA Automation (Python + Selenium)

---

This project helped me understand the full cycle of UI test automation, including interaction with REST APIs, handling assertions, structuring reusable test code, and debugging failures effectively.
