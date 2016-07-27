from selenium import webdriver
import unittest
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# caps = DesiredCapabilities.FIREFOX
# caps["marionette"] = True
# caps["binary"] = "/usr/bin/firefox"
# browser = webdriver.Firefox(capabilities=caps)

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # check homepage for superlists
        self.browser.get('http://localhost:8000')
        # expect name To-Do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # invite for add item

        # add text "Buy peacock feathers"

        # expect after press enter, page will reload and new item "Buy peacock feathers" available in the list

        # text box invite add new item

        # add new item "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees

        # that the site has generated a unique URL for her -- there is some

        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
