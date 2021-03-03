from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
	name="Production_Code",
	description="Learning Production Code",
	long_description=long_description,
    long_description_content_type='text/markdown',
	version=0.1,
	author="Skand Upmanyu",
	author_email="upmanyuskand@gmail.com",
	install_requires=required
	)