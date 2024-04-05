from pages.sbis_download_page import SbisDownload


def test_sbis_download_plugin(browser):
    sbis = SbisDownload(browser)
    sbis.open()
    sbis.click_plugin()
    sbis.download_file()
    assert sbis.get_file_size() == sbis.get_element_size()
