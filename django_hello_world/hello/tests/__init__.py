from .HomePageViewTestCase import *
from .RequestTestCase import *
from .ContextProcessorTestCase import *

  
#starts the test suite
__test__= {  
           'homepage_test': HomePageViewTestCase,
           'request_test': RequestTestCase,
           'processor_test': ContextProcessorTestCase,
           }