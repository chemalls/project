import os
import sys
sys.path.append(os.getcwd())
import pytest
from base.base_driver import init_driver
from base.base_yml import yml_data_with_file
from page.search_page import SearchPage
#导入所需要的模块

def data_with_key(key):
    return yml_data_with_file("shuju")[key]


class TestSearch:
    def setup(self):
        self.driver=init_driver()
        self.search_page=SearchPage(self.driver)

    @pytest.mark.parametrize("content", data_with_key("search"))
    def test_search(self, content):
        #点击放大镜
        self.search_page.click_search()
        #输入文本
        self.search_page.input_content(content)
        #点击返回
        self.search_page.click_back()

    @pytest.mark.parametrize("content", data_with_key("search1"))
    def test_search1(self, content):
        #点击放大镜
        self.search_page.click_search()
        #输入文本
        self.search_page.input_content(content)
        #点击返回
        self.search_page.click_back()
