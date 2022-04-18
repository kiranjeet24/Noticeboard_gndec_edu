from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in noticeboard/__init__.py
from noticeboard import __version__ as version

setup(
	name="noticeboard",
	version=version,
	description="Noticeboard for student",
	author="SDC",
	author_email="sdc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
