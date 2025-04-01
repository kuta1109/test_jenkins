import pytest
import requests
from config.config import *

class Testapi():
    def test_baidu(self):
        """测试百度."""
        res = requests.get(url1)
        assert res.status_code == 200