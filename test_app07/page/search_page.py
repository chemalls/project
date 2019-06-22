from selenium.webdriver.common.by import By
from base.base_action import Baseaction


class SearchPage(Baseaction):
    #display_button = By.XPATH, "//*[contains(@text,'显示')]"
    display_button = By.XPATH, "//*[@text='显示']"
    search_button = By.ID, "com.android.settings:id/search"
    text_button = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_search(self):
        self.click(self.search_button)

    def input_content(self, text):
        self.input_text(self.text_button,text)

    def click_back(self):
        self.click(self.back_button)

