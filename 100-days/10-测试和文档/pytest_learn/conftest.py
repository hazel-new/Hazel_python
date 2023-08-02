import pytest

# from projects.auto_change_password_on_all_devices.tests.test_try import Foo

#
# def pytest_addoption(parser):
#     parser.addoption("--cmdopt", action="store",
#                      default="tyfe",
#                      help="将自定义命令行参数 ’--cmdopt' 添加到 pytest 配置中")
#
#
# # 从配置对象获取 ip 的值
# @pytest.fixture()
# def cmdopt(request):
#     return request.config.getoption('--cmdopt')


# def pytest_assertrepr_compare(op, left, right):
#     if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
#         return [
#             "Comparing Foo instances:",
#             "  vals: {} != {}".format(left.val, right.val)
#         ]
#
#
#
# def pytest_assertrepr_compare(op, left, right):
#     if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
#         return [
#             "Comparing Foo instances:",
#             " vals: {} != {}".format(left.val, right.val),
#             ]



def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))