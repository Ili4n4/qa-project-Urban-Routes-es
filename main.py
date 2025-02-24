import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SMS
import data
import json
from SMS import retrieve_phone_code
from Urban_Routes_Page import UrbanRoutesPage
from data import phone_number



class TestUrbanRoutes:
    driver = None



    @classmethod

    def setup_class(cls):# Configurar las opciones del navegador

        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(),options=options)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(10)
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to


    def test_click_call_taxi_button(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(routes_page.call_taxi_button))
        assert self.driver.find_element(*routes_page.call_taxi_button).is_displayed() == True


    def test_select_comfort_rate(self):
        self.test_click_call_taxi_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_comfort_rate()


    def test_click_phone_number_field(self):
        self.test_select_comfort_rate()
        self.driver.implicitly_wait(5)
        routes_page= UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_field()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(routes_page.phone_number_field))
        assert self.driver.find_element(*routes_page.phone_number_field).is_displayed() == True


    def test_add_phone_number_input(self):
        self.test_click_phone_number_field()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_phone_number_input()


    def test_click_next_button(self):
        self.test_add_phone_number_input()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_next_button()


    def test_add_code_number(self):
        self.test_click_next_button()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_code_number()


    def test_click_confirm_button(self):
        self.test_add_code_number()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_confirm_button()


    def test_click_payment_method(self):
        self.test_click_confirm_button()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(routes_page.payment_method))
        assert self.driver.find_element(*routes_page.payment_method).is_displayed() == True


    def test_click_card_select(self):
        self.test_click_payment_method()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_card_select()


    def test_add_card_number_input(self):
        self.test_click_card_select()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_card_number_input()


    def test_add_code_card_input(self):
        self.test_add_card_number_input()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_code_card_input()



    def test_click_summit_button(self):
        self.test_add_code_card_input()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_submit_button()


    def test_click_close_button_payment(self):
        self.test_click_summit_button()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_close_button_payment()


    def test_click_message_for_driver_field(self):
        self.test_click_close_button_payment()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_message_for_driver_field()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(routes_page.message_for_driver_field))
        assert self.driver.find_element(*routes_page.message_for_driver_field).is_displayed() == True


    def test_write_message_for_driver(self):
        self.test_click_message_for_driver_field()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_message_for_driver()
        assert self.driver.find_element(*routes_page.message_for_driver).is_displayed() == True


    def test_click_blanket_and_tissues(self):
        self.test_write_message_for_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_tissues()


    def test_request_ice_cream(self):
        self.test_click_blanket_and_tissues()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_cream()


    def test_click_taxi_search_button(self):
        self.test_request_ice_cream()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_search_button()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()