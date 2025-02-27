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

        # Configurar la dirección
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(10)
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to


       # Pedir un taxi
    def test_click_call_taxi_button(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi_button()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(routes_page.call_taxi_button))

        assert self.driver.find_element(*routes_page.call_taxi_button).is_displayed() == True


        # Seleccionar la tarifa Comfort
    def test_select_comfort_rate(self):
        self.test_click_call_taxi_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_comfort_rate()

        assert routes_page.get_comfort_rate().text in "Comfort"


        # Rellenar el número de teléfono
    def test_click_phone_number_field(self):
        self.test_select_comfort_rate()
        self.driver.implicitly_wait(5)
        routes_page= UrbanRoutesPage(self.driver)
        routes_page.click_phone_number_field()
        routes_page.add_phone_number_input()
        routes_page.click_next_button()
        routes_page.add_code_number()
        routes_page.click_confirm_button()

        assert self.driver.find_element(*routes_page.phone_number_field).is_displayed() == True


        # Agregar una tarjeta de crédito
    def test_click_payment_method(self):
        self.test_click_phone_number_field()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        routes_page.click_card_select()
        routes_page.add_card_number_input()
        routes_page.add_code_card_input()
        routes_page.click_submit_button()
        routes_page.click_close_button_payment()

        assert self.driver.find_element(*routes_page.payment_method).is_displayed() == True


        # Escribir un mensaje para el controlador
    def test_click_message_for_driver_field(self):
        self.test_click_payment_method()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_message_for_driver_field()
        routes_page.write_message_for_driver()

        assert self.driver.find_element(*routes_page.message_for_driver_field).is_displayed() == True


        # Pedir una manta y pañuelos
    def test_click_blanket_and_tissues(self):
        self.test_click_message_for_driver_field()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_tissues()

        assert routes_page.get_blanket_and_tissues().text in "Blanket_and_tissues"


        # Pedir 2 helados
    def test_request_ice_cream(self):
        self.test_click_blanket_and_tissues()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_ice_cream()

        assert routes_page.request_ice_cream() == routes_page.request_ice_cream()


       # Buscar taxi
    def test_click_taxi_search_button(self):
        self.test_request_ice_cream()
        self.driver.implicitly_wait(5)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_search_button()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()