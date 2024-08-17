import  pytest

@pytest.fixture(params=["数据1","数据2"],ids=[])
def params_fixture(request):
    return request.param   #####request和param必须这么写

def test_params(params_fixture):
    print(params_fixture)