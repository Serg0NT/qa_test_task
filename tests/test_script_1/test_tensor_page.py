from pages.tensor_page import TensorPage


def test_block_is_displayed(browser):
    """Find and check the block 'Сила в людях' """
    tensor = TensorPage(browser)
    tensor.open()
    assert tensor.block.is_displayed()


def test_link_about(browser):
    """Find, click and check link in block 'Подробнее'"""
    tensor = TensorPage(browser)
    tensor.open()
    tensor.click_about_people()
    assert tensor.get_url == 'https://tensor.ru/about'
