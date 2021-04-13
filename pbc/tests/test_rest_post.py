import pytest
#import httpx
from pbc.helpers.rest_client import restcl


def test_post():
	"""
	Test POST method
	"""
	
	response = httpx.post('http://192.168.1.1', data={'password': 'tp-pa55'})
	#print(response.text)
	assert response.status_code == 201
