from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.drag_drop import DragDrop, Slider


def before_scenario(context, scenario):
    option = webdriver.ChromeOptions()
    #option.add_argument("--start-maximized")
    option.add_argument("headless")
    context.browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option)
    browser = context.browser
    browser.maximize_window()
    browser.implicitly_wait(30)
    context.dd = DragDrop(context.browser)
    context.dd = Slider(context.browser)


def after_scenario(context, scenario):
    context.browser.close()



def after_step(context, step):
    if step.status == "failed":
        context.browser.save_screenshot('c://b/screenshot.png')
        attach(
            context.browser.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG)
