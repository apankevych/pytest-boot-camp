import pytest
from pbc.helpers.rest_client import restcl
from pbc.helpers.mongo_client import mongocl


@pytest.fixture(scope="module")
def event_loop():
	loop = get_event_loop()
	yield loop
	
@pytest.fixture(scope="module")
def mongo_connected():
	mongo = mongocl()
	mongo.connect()
	yield mongo

@pytest.fixture(scope="module")
def rest_request():
	rest = restcl()
	rest.connect()
	yield rest

