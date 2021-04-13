import pytest
#import httpx
from pbc.helpers.rest_client import restcl

#@pytest.mark.xfail
def test_get():
	"""
	Test GET method
	
	"""
	rest = restcl(hostname = '192.168.1.1', port = '80')
	response = rest.get(host = '192.168.1.1', port = '80')
	#print(response.text)
	assert response.status_code == 200

