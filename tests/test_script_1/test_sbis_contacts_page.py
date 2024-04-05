from pages.sbis_contacts_page import SbisContacts


def test_sbis_contacts_page(browser):
    """Find and click on the banner 'Tensor' """
    contacts = SbisContacts(browser)
    contacts.open()
    contacts.click_banner_tensor()
