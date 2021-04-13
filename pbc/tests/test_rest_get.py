import pytest
#import httpx
from helpers.rest_client import restcl

#@pytest.mark.xfail
def test_get():
	"""
	Test GET method
	
	"""
	rest = restcl(hostname = '192.168.1.1', port = '80')
	response = rest.get(host = '192.168.1.1', port = '80')
	#print(response.text)
	assert response.status_code == 200


def test_post():
	"""
	Test POST method
	"""
	
	response = httpx.post('http://192.168.1.1', data={'password': 'tp-pa55'})
	#print(response.text)
	assert response.status_code == 201
