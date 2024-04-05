from pages.about_page import AboutPage


def test_equal_size(browser):
    """Check equal size of foto in the block 'Работаем' """
    about = AboutPage(browser)
    about.open()
    about.scroll_to()
    assert about.check_size_images()
