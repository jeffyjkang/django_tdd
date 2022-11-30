functional test:
deal with the way a user will interact with your project
things the user would know and care about
eg:
(order a pizza)
user goes to homepage, they see restaurant's logo
user goes to order page, they will be able to order pizza
if user wants to change their order, they can

unit tests:
ensure that small pieces of your project are working as they should
things the user would never know about
eg:
(ensure pizza_description() is working properly)
the ability to create a Pizza object from the Pizza class
the function pizza_description() will appropriately tell the size and toppings of a pizza
a specific url loads a specific view

selenium:
pip install selenium

install geckodriver for firefox:

python mange.py test
