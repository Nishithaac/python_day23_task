"""
Using Python Selenium Automation and ACtion Chains visit the URL
https://jqueryui.com/droppable/ and do a Drag and Drop operatin of the white rectangular Box
into the Yellow Rectangular Box?
"""

# Importing necessary modules from selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

# Creating class for performing Drag and Drop operation
class DragDrop:
    def __init__(self,url):
        # Initializing the URL of the webpage
        self.url=url
        # Initializing Firefox WebDriver using GeckoDriverManager
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Method to peforme drag and drop operation
    def drag_drop(self):
        try:
            # Maximizing the browser window
            self.driver.maximize_window()
            # Opening the specified URL in the browser
            self.driver.get(self.url)
            # Sleeping for 3 seconds to ensure elements are loaded
            sleep(3)
            # Switching to the first iframe on the page (index 0)
            self.driver.switch_to.frame(0)
            # Creating an ActionChains object for performing actions
            action=ActionChains(self.driver)

            # Finding the draggable and droppable elements by their IDs
            draggable=self.driver.find_element(by=By.ID,value="draggable")
            droppable=self.driver.find_element(by=By.ID,value="droppable")

            # Checking if both source and target elements are visible and enabled before performing the action
            if draggable.is_displayed() and droppable.is_displayed():
                if draggable.is_enabled() and droppable.is_enabled():
                    # Performing the drag and drop action
                    action.drag_and_drop(draggable,droppable).perform()


        except (NoSuchElementException,ElementNotVisibleException) as e:
            # Handling specific exceptions that may occur
            print("ERROR :",e)
        finally:
            # Quitting the WebDriver session once done
            self.driver.quit()
            # Printing completion message
            print("Drag and Drop completed")

# URL of the webpage to perform the Drag and Drop operation on
url="https://jqueryui.com/droppable/"
# Creating an instance of the DragDrop class
dragdrop=DragDrop(url)
# Calling the drag_drop method to execute the drag and drop operation
dragdrop.drag_drop()
