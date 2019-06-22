from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Baseaction:
    def __init__(self,driver):
        self.driver = driver

    def click(self,loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, loc):
        key, value = loc[0], loc[1]
        #return self.driver.
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(key, value))

    def find_elements(self,loc):
        key, value = loc[0], loc[1]
        if key == By.XPATH:
            value = self.make_xpath_with_feature(value)
        #return self.driver.
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_elements(key, value))

    def make_xpath_with_unite_feature(self,loc):
        args = loc.split(",")
        feature = ""
        key_index = 0
        value_index = 1
        option_index = 1
        if len(args) == 2:
            feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "
        elif len(args) == 3:
            if args[option_index] == "1":
                feature = "@" + args[key_index] + "='" + args[value_index] + "'" + " and "
            else:
                feature = "contains(@" + args[key_index] + ",'" + args[value_index] + "')" + " and "
        print(feature)
        return feature

    def make_xpath_with_feature(self,loc):
        feature_start = "//*["
        feature_end = "]"
        feature = ""
        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            feature = self.make_xpath_with_unite_feature(loc)
        else:
            for i in loc:
                feature += self.make_xpath_with_unite_feature(i)
        feature = feature.rstrip(" and ")
        print(11111111111)
        print(feature)
        print(22222222222)
        loc = feature_start + feature + feature_end
        print(loc)
        return loc
    #
    # def main():
    #     # loc="text,设置,1"
    #     loc = ["text,设置,1", "text,设置,0"]
    #     a = make_xpath_with_feature(loc)
    #     print(a)
    #
    # if __name__ == "__main__":
    #     main()
