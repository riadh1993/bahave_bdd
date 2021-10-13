import numpy
from selenium.webdriver import ActionChains

from browser import Browser

element1_id = "draggable"
text_id = "dropText"
expected_message = "Dropped!"
link = "https://qavbox.github.io/demo/dragndrop/"
element2_xpath = "//body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]"
message_id = "range"
message = "100"

class DragDrop(Browser):

    def drag(self):
        element1 = self.driver.find_element_by_id(element1_id)
        ActionChains(self.driver).drag_and_drop_by_offset(element1, 145, 32).perform()

    def message(self):
        text = self.driver.find_element_by_id(text_id).text
        return text

    def the_url(self, link):
        self.driver.get(link)


class Slider(Browser):

    def slider(self):
        element_left = self.driver.find_element_by_xpath(element2_xpath)
        ActionChains(self.driver).drag_and_drop_by_offset(element_left, 145, 0).perform()

    def the_message(self):
        message = self.driver.find_element_by_id(message_id).text
        return message

    def the_url(self, link):
        self.driver.get(link)
