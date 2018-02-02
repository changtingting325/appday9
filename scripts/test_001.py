import pytest,allure
class Test_allure:
    def setup(self):
        pass

    def teardown(self):
        pass
    @allure.step(title="第一个测试")
    def test_al(self):
        assert 1
# if __name__ == '__main__':
