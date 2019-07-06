import unittest

def suite():
    return unittest.TestLoader().discover("TheBlueAlliance.tests", pattern="*.py")
