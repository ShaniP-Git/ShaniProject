

class menuPage:

    def __init__(self,page):
        print("into init")
        self.page = page

    def click_on_search_button(self):
        print("clicking on search button")
        search_button = self.page.query_selector_all("[class='swa-link js-search-box']")
        search_button[0].click()

    def searching_product(self):
        print("looking for product")
        search_line = self.page.locator("[id='swa-search-layer-input']")
        search_line.type("Imber bracelet")
        self.page.keyboard.press('Enter')

    def choosing_imber_bracelet(self):
        print("choosing the right bracelet")
        imber_brecelet = self.page.locator("[href='/en-AA/p-M5680094/Imber-bracelet-Round-cut-White-Rose-gold-tone-plated/?variantID=5730677']")
        imber_brecelet.click()

    def set_bracelet_color(self):
        print("choosing bracelet color")
        white_color = self.page.locator("[href='/en-AA/p-M5680094/Imber-bracelet-Round-cut-Scattered-design-White-Gold-tone-plated/?variantID=5680094']")
        white_color.click()

    def click_on_store_finder(self):
        print("clicking on store finder button")
        find_store_button = self.page.locator("[href='/en-AA/store-finder']")
        find_store_button.click()











