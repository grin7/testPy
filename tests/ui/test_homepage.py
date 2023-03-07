import pytest

from ui.pages.homepage import HomePage


@pytest.mark.usefixtures('setup')
class TestHomePage:

    def test_google_search(self):
        google_home = HomePage(self.driver, 'https://google.com.ua')
        google_home.do_search()
        expected_links_count = 10
        actual_links_count = len(google_home.get_result_links())
        assert expected_links_count == actual_links_count
