import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Invoke Browser
        cls.driver = webdriver.Firefox()

    def test01_WebsiteChecker(self):
        # Navigate it to desired URL
        self.driver.get('https://medium.com/')
        self.assertEqual("Medium – a place to read and write big ideas and important stories", self.driver.title,
                         'test01_WebsiteChecker passed')

    def test02_SearchIconChecker(self):
        icon = self.driver.find_element_by_xpath(
            "//span[@class='svgIcon svgIcon--search svgIcon--25px u-baseColor--iconLight']//*[@class='svgIcon-use']").click()
        search = self.driver.find_element_by_xpath("//*[@placeholder='Search Medium']")
        self.assertTrue(search.is_displayed(), 'test02_SearchIconChecker')

    def test03_PredictiveSearchChecker(self):
        self.driver.find_element_by_xpath("//*[@placeholder='Search Medium']").send_keys('IT')
        self.driver.implicitly_wait(5)
        ps = self.driver.find_element_by_xpath("//div[@class='js-predictiveSearchResults u-textAlignLeft u-clearfix']")
        self.assertTrue(ps.is_displayed(), 'test03_PredictiveSearchChecker passed')

    def test04_NullValueSearchChecker(self):
        self.driver.find_element_by_xpath("//*[@placeholder='Search Medium']").clear()
        self.driver.find_element_by_xpath("//*[@placeholder='Search Medium']").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(5)
        search_result = self.driver.find_element_by_xpath("//input[@value='']")
        self.assertTrue(search_result.is_displayed(), 'test04_NullValueSearchCheacker passed')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
