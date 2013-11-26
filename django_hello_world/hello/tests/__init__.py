from django_hello_world.hello.tests.HomePageViewTestCase import *
from django_hello_world.hello.tests.TestHomePageSelenium import *

  
#starts the test suite  
__test__= {  
           'homepage_test': HomePageViewTestCase,
           'selenium_test': TestHomePageSelenium
           }