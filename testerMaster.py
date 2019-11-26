import sys
sys.path.append('src')
sys.path.append('src/classes')
sys.path.append('src/imp')
sys.path.append('src/imp/BoltFuncional.py')


from src.main_test import TestMain
from test.integracion import TestIntegration
from src.imp.BoltFuncional_test import TestBolt
from src.classes.channel_test import TestChannel

#Unitarios
TestMain()
TestBolt()
TestChannel()

#Int
TestIntegration()
