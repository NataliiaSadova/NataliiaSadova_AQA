from modules.ui.page_objects.W3S_python_practice import W3S_PYTHON
import pytest

@pytest.mark.ui_w3s
def test_block_try_it_yourself():
    python_pract = W3S_PYTHON()
    python_pract.go_to()
    python_pract.try_practice()
    python_pract.close()
