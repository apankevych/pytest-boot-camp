import pytest
#import httpx
#from pbc.helpers.rest_client import restcl

#@pytest.mark.xfail
def test_get(rest_request):
	"""
	Test GET method
	
	"""
	rest = rest_request
	response = rest.get(host = '192.168.1.1', port = '80')
	#print(response.text)
	assert response.status_code == 200

