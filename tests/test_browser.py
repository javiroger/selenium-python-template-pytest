import pytest

from page_objects.google_search_pom import GoogleSearchPage
from page_objects.search_results_pom import SearchResultsPage


class TestBrowser:

    def test_example(self, browser):
        googlesearchpage = GoogleSearchPage(browser)
        searchresultspage = SearchResultsPage(browser)
        googlesearchpage.searchfor("Selenium")
        searchresultspage.link_selenium_present()
