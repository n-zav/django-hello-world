from .HomePageViewTestCase import *
from .RequestTestCase import *
from .ContextProcessorTestCase import *
from .EditTestCase import *
from .AuthTestCase import *

  
#starts the test suite
__test__= {  
           'homepage_test': HomePageViewTestCase,
           'request_test': RequestTestCase,
           'processor_test': ContextProcessorTestCase,
           'edit_form_test': EditTestCase,
           'auth_test': AuthTestCase
           }