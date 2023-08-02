import pytest

import pytest


# def test_option1(pytestconfig):
#     print('host: %s' % pytestconfig.getoption('host'))
#     # print('port: %s' % pytestconfig.getoption('port'))


#
# def test_answer(cmdopt):
#     if cmdopt == 'type1':
#         print("first")
#     elif cmdopt == "type2":
#         print('second')
#     else:
#         print('10.58.144.96')
#     assert 0

#
#
#
# def f():
#     raise SystemExit(1)
#
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

#
# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "check")

# class MyPlugin:
#     def pytest_sessionfinish(self):
#         print("*** test run reporting finishing")
#
#
# pytest.main(["-qq"], plugins=[MyPlugin()])


# def test_set_comparison():
#     set1 = set("1308")
#     set2 = set("8035")
#     assert set1 == set2



# class Foo:
#     def __init__(self,val):
#         self.val = val
#
#
#     def __eq__(self, other):
#         return self.val == other.val
#
#
# def test_compare():
#     f1 = Foo(1)
#     f2 = Foo(2)
#     assert f1 == f2


# content of test_foocompare.py
# class Foo:
#     def __init__(self, val):
#         self.val = val
#     def __eq__(self, other):
#         return self.val == other.val
#
# def test_compare():
#     f1 = Foo(1)
#     f2 = Foo(2)
#     assert f1 == f2


# def test_needsfiles(tmpdir):
#     print(tmpdir)
#     assert 0

# def test_option1(pytestconfig):
#     print('host: %s' % pytestconfig.getoption('host'))
#     # print('port: %s' % pytestconfig.getoption('port'))


#
# def test_answer(cmdopt):
#     if cmdopt == 'type1':
#         print("first")
#     elif cmdopt == "type2":
#         print('second')
#     else:
#         print('10.58.144.96')
#     assert 0


#
# @pytest.fixture()
# def postcode():
#     return '010'
#
#
# def test_postcode(postcode):
#     assert postcode == '020'


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6+9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

def test_valid_string(stringinput):
    assert stringinput.isalpha()