import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import SMS
import data
import json
from SMS import retrieve_phone_code
from Urban_Routes_Page import UrbanRoutesPage
from data import phone_number


driver = webdriver.Chrome()

class TestUrbanRoutes:
    driver = None



    @classmethod

    def setup_class(cls):# Configurar las opciones del navegador
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(10)
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_click_call_taxi_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        WebDriverWait(self.driver, 10).until(
             expected_conditions.visibility_of_element_located(routes_page.call_taxi_button))
        assert self.driver.find_element(*routes_page.call_taxi_button).is_displayed() == True

    def test_select_comfort_rate(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_rate()
        assert True

    def test_click_phone_number_field(self):
        self.driver.implicitly_wait(5)
        routes_page= UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_field()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(routes_page.phone_number_field))
        assert self.driver.find_element(*routes_page.phone_number_field).is_displayed() == True

    def test_add_phone_number_input(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_phone_number_input()
        assert True

    def test_click_next_button(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_next_button()


    def test_add_code_number(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_code_number()
        assert True

    def test_click_confirm_button(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_confirm_button()


    def test_click_payment_method(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(routes_page.payment_method))
        assert self.driver.find_element(*routes_page.payment_method).is_displayed() == True


    def test_click_card_select(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_card_select()


    def test_add_card_number_input(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_card_number_input()
        assert True


    def test_add_code_card_input(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_code_card_input()
        assert True


    def test_click_summit_button(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_submit_button()


    def test_click_close_button_payment(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_close_button_payment()


    def test_click_message_for_driver_field(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_message_for_driver_field()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(routes_page.message_for_driver_field))
        assert self.driver.find_element(*routes_page.message_for_driver_field).is_displayed() == True


    def test_write_message_for_driver(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_message_for_driver()
        assert self.driver.find_element(*routes_page.message_for_driver).is_displayed() == True


    def test_request_blanket_and_tissues(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_blanket_and_tissues()


    def test_request_ice_cream(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_cream()


    def test_click_taxi_search_button(self):
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_search_button()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()