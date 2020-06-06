from setuptools import (
    find_packages,
    setup,
)

import x_net_color_field


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="x-net-django-color-field",
    version=x_net_color_field.__version__,
    license="MIT",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x-net-services/x-net-django-color-field",
    author="X-Net Services GmbH",
    author_email="support-software@x-net.at",
    packages=find_packages(),
    install_requires=[
        "Django==2.2.13",
    ],
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
    ]
)
