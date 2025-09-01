from jb_60.page_object_swarovski.pages.products_page import productspage


class TestShopNow:

    def test_shop_now_button(self, setup_swarovski):
        print("test start")
        page = setup_swarovski
        products_page = productspage(page)

        products_page.heart_ring_selection()
        products_page.set_color()
        products_page.set_size()
        status = products_page.product_availability_checking()
        assert status == "Unfortunately this product is currently not available.", "product is in stock"











