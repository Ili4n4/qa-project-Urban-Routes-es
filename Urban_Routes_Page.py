from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import data
import pytest
from selenium.webdriver.support import expected_conditions
from SMS import retrieve_phone_code
from data import phone_number

detail_route_XPATH= None


class UrbanRoutesPage:
    from_address = (By.ID, 'from')
    to_address = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_rate = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    phone_number_field = (By.CLASS_NAME, "np-button")
    phone_number_input = (By.ID, "phone")
    phone_number_section = (By.XPATH, 'section active"><button class')
    close_button = (By.CLASS_NAME, 'close-button')
    number = (By.XPATH, '//*[@id="phone"]')
    next_button = (By.XPATH, '//*[text()="Siguiente"]')
    click_code = (By.ID, 'code_input')
    phone_code = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    phone_send_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    select_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    payment_method = (By.CLASS_NAME, 'pp-text')
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')
    card_select = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_number_input = (By.ID, "number")
    code_card_input = (By.NAME, "code")
    click_add_card = (By.CLASS_NAME, "card-wrapper")
    summit_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_button_payment = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    message_for_driver_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label')
    message_for_driver = (By.ID, 'comment')
    reqs_body = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]')
    request_button = (By.CLASS_NAME, "reqs-head")
    blanket_and_tissues = (By.XPATH,  '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    switch_button = (By.CLASS_NAME, "switch-input")
    ice_cream = (By.CLASS_NAME, 'counter-plus')
    counter_value = (By.CLASS_NAME, 'counter-value')
    quantity_2 = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    order_number = (By.ID, "number>h_180")
    taxi_search_button = (By.CLASS_NAME, "smart-button")
    Button_x = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[2]/div')

    def __init__(self, driver):
        self.driver = driver
        self.imput_add_card_code = None
        self.imput_add_card_number = None
        self.comfort_rate_button_locator = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
        self.phone_number_field_locator = (By.ID, "np-text")
        self.phone_number_input_locator = (By.ID, "phone")
        self.request_button_locator = (By.CLASS_NAME, "reqs-head")




    def set_from(self, from_address):
        self.driver.find_element(*self.from_address).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_address).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_address).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_address).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    def select_comfort_rate(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_rate_button_locator)).click()

    def click_phone_number_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).click()

    def add_phone_number_input(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.number).send_keys(data.phone_number)

    def click_next_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.next_button))
        self.driver.find_element(*self.next_button).click()

    def add_code_number(self):
        self.driver.implicitly_wait(5)
        phone_code = retrieve_phone_code(driver=self.driver)
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.phone_code).send_keys(phone_code)

    def click_confirm_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.confirm_button))
        self.driver.find_element(*self.confirm_button).click()

    def click_payment_method(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.payment_method))
        self.driver.find_element(*self.payment_method).click()

    def click_card_select(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.card_select))
        self.driver.find_element(*self.card_select).click()

    def add_card_number_input(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.card_number_input).send_keys('1234 5678 9100')

    def add_code_card_input(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.code_card_input).click()
        self.driver.find_element(*self.code_card_input).send_keys("111" + Keys.TAB)

    def click_submit_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.summit_button))
        self.driver.find_element(*self.summit_button).click()

    def click_close_button_payment(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.close_button_payment))
        self.driver.find_element(*self.close_button_payment).click()


    def click_message_for_driver_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.message_for_driver_field))
        self.driver.find_element(*self.message_for_driver_field).click()


    def write_message_for_driver(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.message_for_driver).send_keys(data.message_for_driver)


    def click_request_button(self):
        return self.request_button_locator


    def request_blanket_and_tissues(self):
        button = self.driver.find_element(By.CLASS_NAME, "switch-input")
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.blanket_and_tissues))

    def request_ice_cream(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.ice_cream).click()
        self.driver.find_element(*self.counter_value)
        self.driver.find_element(*self.quantity_2).click()


    def click_taxi_search_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.taxi_search_button).click()


    def get_taxi(self):
        return self.driver.find_element(*self.taxi_search_button).get_property('value')


    def close_window(self):
        self.driver.implicitly_wait(0)

