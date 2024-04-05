from pages.sbis_contacts_page import SbisContacts


def test_check_current_region(browser):
    """Check the region and check the list of partners"""
    sbis = SbisContacts(browser)
    sbis.open()
    assert sbis.get_list_partners().is_displayed() and sbis.check_current_region()


def test_change_region(browser):
    """Change region and check it"""
    sbis = SbisContacts(browser)
    sbis.open()
    old_list_partners = sbis.get_list_partners()
    sbis.click_region()
    sbis.click_expected_region()
    assert sbis.check_expected_url_and_title() and sbis.check_expected_region() \
           and old_list_partners is not sbis.get_list_partners()
