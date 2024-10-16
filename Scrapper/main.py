from models.Product import Product
from requestlib.StandardRequester import Requester
from requestlib.CustomRequester import CustomRequester
from scrappers.categories.CategoryMenuScrapper import CategoryMenuScrapper
from serializers.json_serializers.JSONSerializer import JSONSerializer
requester = CustomRequester()
catalogue_response = requester.get_html("https://alcomarket.md/ro/catalog")
category_menu_scrapper = CategoryMenuScrapper(
    catalogue_response, "div", "mini-catalog__wrapper", requests_module=requester)
category_scrappers = category_menu_scrapper.get_category_scrappers()

print("Proceeding on scrapping category pages")

vodka = category_scrappers[4]
print(vodka)
# vodka.get_products(request_module=requester)
# page_urls = vodka.get_pages_urls()
# print(page_urls)
# products = vodka.get_product_urls()
products = vodka.get_products()
# print(products)
vodka_category = vodka.get_model()
processed_products = vodka_category.process_products((100, 200))
serializer = JSONSerializer()
product = processed_products.get("filtered_products")[0]
serialized = serializer.serialize(product)
print(serialized)
deserialized = serializer.deserialize(serialized, Product)
print(deserialized)
# print(processed_products)
