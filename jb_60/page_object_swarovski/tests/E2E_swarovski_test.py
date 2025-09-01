from jb_60.page_object_swarovski.pages.menu_page import menuPage
from jb_60.page_object_swarovski.pages.products_page import productspage
from jb_60.page_object_swarovski.pages.find_store_page import findstorepage



class TestSwarovskiE2E:

    def test_shop_now_button(self, setup_swarovski):
        print("test start")
        page = setup_swarovski
        products_page = productspage(page)

        products_page.heart_ring_selection()
        products_page.set_color("Blue")
        products_page.set_size()
        status = products_page.product_availability_checking()
        assert status == "Unfortunately this product is currently not available.", "product is in stock"



    def test_store_finder(self, setup_swarovski):
        print("test start")
        page = setup_swarovski
        find_store_page = findstorepage(page)

        find_store_page.clicking_on_stores_button()
        find_store_page.select_city()
        value = find_store_page.stores_near_you()
        assert len(f'{value}')>0, "no stores were found after search"



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











