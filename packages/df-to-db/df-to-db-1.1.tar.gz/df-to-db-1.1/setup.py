"""Package write dataframe to database module"""

from setuptools import find_packages, setup

setup(
    name="df-to-db",
    version="1.1",
    author="Masum Billal",
    author_email="billalmasum93@gmail.com",
    packages=find_packages(),
    scripts=[],
    url="https://github.com/proafxin/df_to_db",
    license="LICENSE",
    description="An awesome package that does something",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "pandas",
        "pymysql",
        "pytest",
        "cryptography",
        "pymongo",
        # "pyodbc",
        "sqlalchemy",
        "mysqlclient",
        "coverage",
        "sphinx",
        "sphinx-rtd-theme",
        "psycopg2-binary",
        "sqlalchemy-utils",
        "dnspython",
        "pymssql",
        "tox",
        "tox-gh-actions",
    ],
)
