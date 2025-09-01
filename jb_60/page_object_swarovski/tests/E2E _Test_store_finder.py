from jb_60.page_object_swarovski.pages.find_store_page import findstorepage


class TestStoreFinder:

    def test_store_finder(self, setup_swarovski):
        print("test start")
        page = setup_swarovski
        find_store_page = findstorepage(page)

        find_store_page.clicking_on_stores_button()
        find_store_page.select_country()
        find_store_page.select_city()
        value = find_store_page.stores_near_you()
        assert len(f'{value}')>0, "no stores were found after search"
