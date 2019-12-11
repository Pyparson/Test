import pytest
import mock


@pytest.fixture(scope='function', params=[1, 2, 3])    # multiple test cases
def mock_data_params(request):
    return request.param

def test_not_2(mock_data_params):
    print('test_data: %s' % mock_data_params)
    assert mock_data_params != 2

##################

def _call(x):
    return '{} _call'.format(x)

def func(x):
    return '{} func'.format(_call(x))

def test_func_normal():
    for x in [11, 22, 33]:                          # multiple test cases
        print('{i} - {n}'.format(i=x, n=func(x)))
        assert func(x) == '{} _call func'.format(x)

@mock.patch('pytest2._call', return_value='None')   # set mock 'pytest2._call'.return_value is 'None', also could use mock_call.return_value='None'
def test_func_mock(mock_call):
    for x in [11, 22, 33]:
        # print '{} - {}'.format(x, func(x))
        ret = func(x)
        assert mock_call.called                 # True or False
        assert mock_call.call_args == ((x,),)   # This is either None (if the mock hasn’t been called), or the arguments that the mock was last called with
        assert ret == 'None func'               # because mock_call.return_value is 'None', so the result here is 'None func'
