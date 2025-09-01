

class productspage:

    def __init__(self,page):
        print("into init")
        self.page = page
        page.goto("https://www.swarovski.com/en-AA/c-swa-root/Categories/f/product-set/ps-metamorphosis/")


    def heart_ring_selection(self):
        print("looking for the heart ring")
        products = self.page.query_selector_all("[class='swa-product-tile-plp__top']")
        products[4].click()

    def set_color(self):
        print("choosing ring color")
        blue_colored_ring = self.page.get_by_role("link",name="Blue")
        blue_colored_ring.click()

    def set_size(self):
        print("choosing ring size")
        sixty_sized_ring = self.page.get_by_text("60")
        sixty_sized_ring.click()


    def product_availability_checking(self):
        print("product availability checking")
        status = self.page.locator("span[class='swa-product-availability__status']")
        if status:
            text = status.text_content()
            print(f"product availability status: {text}")
            return text










