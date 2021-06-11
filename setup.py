from setuptools import setup

version = '0.0.1'

setup(
    name = 'pytest_boot_camp',
    description = 'Pytest Boot Camp for pytest classes',
    version = version,
    author = 'Andriy Pankevych',
    author_email = 'a.pankevych@gmail.com',
    install_requires=[
#		'pdb',
		'httpx[http2]',
		'pymongo',	
	],
)
