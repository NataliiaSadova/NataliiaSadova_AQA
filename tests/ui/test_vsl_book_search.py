import pytest
from modules.ui.page_objects.vsl_book_search import VslBookSearch
import time

@pytest.mark.ui_vsl
def test_check_search_results():
    vsl_book_search = VslBookSearch()
    vsl_book_search.go_to()
    vsl_book_search.enter_search_query("Вірші")
    vsl_book_search.list_search_result
    assert vsl_book_search.check_title("Результати пошуку")
    time.sleep(3)
    vsl_book_search.close()


