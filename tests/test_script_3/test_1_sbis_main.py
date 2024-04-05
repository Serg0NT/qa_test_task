from pages.sbis_page import SbisMain


def test_sbis_footer(browser):
    sbis = SbisMain(browser)
    sbis.open()
    sbis.scroll_to()
    sbis.click_footer_element()
    assert browser.current_url == 'https://sbis.ru/download'