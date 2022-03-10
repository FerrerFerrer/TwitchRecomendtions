import sys
sys.path.append('src')
sys.path.append('src/classes')
sys.path.append('src/imp')
sys.path.append('src/imp/BoltFuncional.py')


from src.main_test import TestMain
from test.integracion import TestIntegration
from src.imp.BoltFuncional_test import TestBolt
from src.classes.channel_test import TestChannel
from src.imp.APIfuncional_test import TestApi

#Unitarios
TestMain()
TestBolt()
TestChannel()
TestApi()


#Int
TestIntegration()

# A change to trigger build on travis
