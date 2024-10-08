# Online Shop

## Description

Online Shop is an object-oriented program that represents a core for an online store. Though it does not provide 
payment services, it can still be used as a basic for a website to a Telegram bot.

## Installation

1. Clone the repository:
```
git clone https://github.com/obladishka/online_shop.git
```
2. Install project dependencies:
```commandline
poetry intall
```

## Usage

The project consists of 2 classes: Product and Category. There are 2 types of products: smartphones and loan grass.

1. Creating product :
```commandline
product = Product(name="product name", description="product description", price=10.0, quantity=1)

smartphone = Smartphone(name="Iphone 15", desctiption="512GB, Gray space", 
price=210000.0, quantity=8, efficiency=98.2, model="15", memory=512, color="Gray space")

grass = LawnGrass(name="Газонная трава", desctiption="Элитная трава для газона", 
price=500.0, quantity=20, country="Россия", germination_period="7 дней", color="Зеленый")
```
Information about all newly created products is printed out to console.
2. Adding new product:
```commandline
product = {name: "product name", description: "product description", price: 10.0, quantity: 1}
new_product = Product.new_product(product: dict)
```
In case a product with the same name already exists and there is no price conflict, its quantity will be increased 
by the quantity of a newly added product. In case of price conflict, the higher price will be set and quantity will be 
increased accordingly.
3. Price setting:
```commandline
product.price = new price (float)
```
In case a new price is lower than the current one, additional confirmation is needed.
4. Calculating total price of 2 products:
```commandline
product_1 = Product("product_1 name", "product_1 description", 10.0, 1)
product_2 = Product("product_2 name", "product_2 description", 20.0, 2)
print(product_1 + product_2)
>>> 50.0
```
**NOTE!** Only products of the same type can be summed up.

Same products can be grouped in a Category.
1. Creating category:
```commandline
category = Category(name="categoty name", description="category description", products=[product_1, product_2])
```
2. Adding new products to a products list:
```commandline
category.add_product(product: Product)
```
**NOTE!** Only objets of Product class can be added.
3. Getting information about products in the list in a convenient format:
```commandline
print(category.products)
>>> Product name, 10 руб. Остаток: 1 шт.
```
4. Getting statistics information:
```commandline
print(category.category_count) # returns the number of all existing categories
print(category.product_count) # returns the number of products in all categories (not counting quantity of each product)
```
5. Dispaying information about category in a convenient format:
```commandline
print(category)
>>> Category name, количество продуктов: 20 шт. # number of products in the category (counting quantity of each product)
```
6. With a supportive class ProductIterator it's possible to iterate through products in products list:
```commandline
iterator = ProductIterator(category)
for product in iterator:
    print(product)
    
>>> product_1 name, 10 руб. Остаток: 1 шт.
    product_2 name, 20 руб. Остаток: 2 шт.
    ...
```

## Testing

The code is 97% covered by Pytest unit tests. To run it write the following commands in your terminal:
```
poetry add --group dev pytest # install pytest in the application's virtual environment
pytest # run the tests
```
A detailed coverage report can be found in the *index.html* file in the *htmlcov* folder after running the command:
```commandline
pytest --cov=src --cov-report=html
```
in the terminal.