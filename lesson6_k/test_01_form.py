from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService

b_path = r"C:\Users\simon\Downloads\edgedriver_win64\msedgedriver.exe"
browser = webdriver.Edge(service=EdgeService(b_path))


def test_buttons():
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    browser.implicitly_wait(10)

    f_name = browser.find_element(By.CSS_SELECTOR, "[name='first-name']")
    f_name.click()
    f_name.send_keys("Иван")

    l_name = browser.find_element(By.CSS_SELECTOR, "[name='last-name']")
    l_name.click()
    l_name.send_keys("Петров")

    adress = browser.find_element(By.CSS_SELECTOR, "[name='address']")
    adress.click()
    adress.send_keys("Ленина, 55-3")

    email = browser.find_element(By.CSS_SELECTOR, "[name='e-mail']")
    email.click()
    email.send_keys("test@skypro.com")

    phone_number = browser.find_element(By.CSS_SELECTOR, "[name='phone']")
    phone_number.click()
    phone_number.send_keys("+7985899998787")

    city = browser.find_element(By.CSS_SELECTOR, "[name='city']")
    city.click()
    city.send_keys("Москва")

    country = browser.find_element(By.CSS_SELECTOR, "[name='country']")
    country.click()
    country.send_keys("Россия")

    job_position = browser.find_element(
        By.CSS_SELECTOR, "[name='job-position']")
    job_position.click()
    job_position.send_keys("QA")

    company = browser.find_element(By.CSS_SELECTOR, "[name='company']")
    company.click()
    company.send_keys("SkyPro")

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

    zip_code = browser.find_element(By.CSS_SELECTOR, "#zip-code"
                                    ).value_of_css_property("background-color")
    assert zip_code == "rgba(248, 215, 218, 1)"

    f_name_color = browser.find_element(
        By.ID, "first-name").value_of_css_property("background-color")
    assert f_name_color == "rgba(209, 231, 221, 1)"

    l_name_color = browser.find_element(
        By.ID, "last-name").value_of_css_property("background-color")
    assert l_name_color == "rgba(209, 231, 221, 1)"

    adress_color = browser.find_element(
        By.ID, "address").value_of_css_property("background-color")
    assert adress_color == "rgba(209, 231, 221, 1)"

    email_color = browser.find_element(
        By.ID, "e-mail").value_of_css_property("background-color")
    assert email_color == "rgba(209, 231, 221, 1)"

    phone_number_color = browser.find_element(
        By.ID, "phone").value_of_css_property("background-color")
    assert phone_number_color == "rgba(209, 231, 221, 1)"

    city_color = browser.find_element(
        By.ID, "city").value_of_css_property("background-color")
    assert city_color == "rgba(209, 231, 221, 1)"

    country_color = browser.find_element(
        By.ID, "country").value_of_css_property("background-color")
    assert country_color == "rgba(209, 231, 221, 1)"

    job_position_color = browser.find_element(
        By.ID, "job-position").value_of_css_property("background-color")
    assert job_position_color == "rgba(209, 231, 221, 1)"

    company_color = browser.find_element(
        By.ID, "company").value_of_css_property("background-color")
    assert company_color == "rgba(209, 231, 221, 1)"

    browser.quit()
