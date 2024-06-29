import pytest
from modules.ui.page_objects.vsl_book_search import VslBookSearch

@pytest.mark.ui
def test_check_valid_search_results():
    vsl_book_search = VslBookSearch()
    vsl_book_search.go_to()
    vsl_book_search.enter_search_query('Вірші')

    assert vsl_book_search.list_search_result != 0
    
    vsl_book_search.close()


@pytest.mark.ui_vsl
def test_check_empty_search_result():
    vsl_book_search = VslBookSearch()
    vsl_book_search.go_to()
    vsl_book_search.enter_search_query('Ві')

    assert vsl_book_search.empty_search_result("На жаль, за вашим запитом нічого не знайдено.")

    vsl_book_search.close()