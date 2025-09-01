import time


class findstorepage:

    def __init__(self,page):
        print("into init")
        self.page = page

    def clicking_on_stores_button(self):
        print("clicking on stores button")
        stores_button = self.page.query_selector_all("[class='swa-link__icon swa-link__icon--left-locator']")
        stores_button[0].click()

    def select_country(self):
        print("select country")
        country_combobox = self.page.locator("[class='swa-form-input__field swa-label-sans--medium']")
        print("setting 'Isreal' as defult")

    def select_city(self):
        print("select city")
        city_line = self.page.locator("[class='swa-form-input__field swa-label-sans--medium js-location-autocomplete-input-field js-swa-store-finder-search ui-autocomplete-input']")
        city_line.click()
        city_line.type("Petah Tikva")
        time.sleep(3)
        self.page.keyboard.press("Enter")
        time.sleep(3)


    def stores_near_you(self):
        print("looking for stores near you")
        result = self.page.locator("[class='swa-text-sans--small swa-store-view__location-title']")
        result_text = result.text_content()
        value = int(result_text.split()[0])
        print(f"{value} stores found near you")

