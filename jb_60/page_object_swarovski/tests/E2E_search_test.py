from jb_60.page_object_swarovski.pages.menu_page import menuPage


class TestSearchButton:

    def test_search_button(self, setup_swarovski):
        print("test start")
        page = setup_swarovski
        menu_Page = menuPage(page)

        menu_Page.click_on_search_button()
        menu_Page.searching_product()
        menu_Page.choosing_imber_bracelet()
        menu_Page.set_bracelet_color()
        menu_Page.click_on_store_finder()
        assert page.url == "https://www.swarovski.com/en-AA/store-finder/", "store finder is not working as expected"