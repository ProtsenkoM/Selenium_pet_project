from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, time_out=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, time_out).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, time_out=5):
        return wait(self.driver, time_out).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, time_out=5):
        return wait(self.driver, time_out).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, time_out=5):
        return wait(self.driver, time_out).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, time_out=5):
        return wait(self.driver, time_out).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, time_out=5):
        return wait(self.driver, time_out).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()





