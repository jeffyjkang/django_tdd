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

deployment testing:
run your functional and unit tests locally
deploy your code to staging server
have a custom domain for that
run your functional tests against the staging site and unit tests against the staging server
automate the process or you will get burned out

testing after:
tests can be exhausting
when project is new, it changes too much for testing
you'll often delete features and the tests associated with them
if others aren't using it, why test
wait until you have version 1.0
create tests for those things you find crucial
provide freedom and security that your code is working
