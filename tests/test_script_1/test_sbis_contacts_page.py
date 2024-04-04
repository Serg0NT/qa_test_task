from pages.sbis_contacts_page import SbisContacts


def test_script_1_sbis(browser):
    """Find and click on the banner 'Tensor' """
    contacts = SbisContacts(browser)
    contacts.open()
    contacts.click_button()
