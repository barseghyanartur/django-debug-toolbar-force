import os
from setuptools import find_packages, setup

try:
    readme = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
except:
    readme = ""

version = "0.2"

install_requires = [
    "django-nine>=0.2.3",
]

tests_require = [
    "beautifulsoup4",
    "factory_boy",
    "Faker",
    "Pillow",
    "pytest",
    "pytest-django",
    "pytest-cov",
    "pytest-pythonpath",
    "tox",
]

setup(
    name="django-debug-toolbar-force",
    version=version,
    description="Force debugging of partial- or non-HTML views in "
    "django-debug-toolbar.",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords="django, django-debug-toolbar",
    author="Artur Barseghyan",
    author_email="artur.barseghyan@gmail.com",
    url="https://github.com/barseghyanartur/django-debug-toolbar-force/",
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/"
        "django-debug-toolbar-force/",
        "Documentation": "https://django-debug-toolbar-force.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/"
        "django-debug-toolbar-force/",
        "Changelog": "https://django-debug-toolbar-force.readthedocs.io/"
        "en/latest/changelog.html",
    },
    package_dir={"": "src"},
    packages=find_packages(where="./src"),
    license="GPL-2.0-only OR LGPL-2.1-or-later",
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
)
