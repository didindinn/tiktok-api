from codecs import open
from os import path

from setuptools import find_packages, setup


setup(
    name="tiktok-api",
    version="0.10.2",
    description="Tiktok Api.",
#    description="tiktok api",
    author="Steffan Jensen",
    author_email="brominercom2@gmail.com",
    license="Apache Software License 2.0",
    url="https://github.com/instabotai/tiktok-api",
    keywords=["tiktok", "bot", "api"],
    install_requires=[
        "requests",
    ],
        entry_points={
        'console_scripts': ['tiktok-api=tiktokapi:api'],
    },
    classifiers=[
        # How mature is this project? Common values are
        "Development Status :: 5 - Production/Stable",
        # Indicate who your project is intended for
        "Intended Audience :: Information Technology",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: Apache Software License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
)
