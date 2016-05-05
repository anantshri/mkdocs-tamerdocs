from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="mkdocs-reloaded",
    version=VERSION,
    url='https://anantshri.github.io/mkdocs-reloaded/',
    license='GPL',
    description='Reloaded: Default theme for MkDocs',
    author='Anant Shrivastava',
    author_email='anant@anantshri.info',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'reloaded = mkdocs-reloaded',
        ]
    },
    zip_safe=False
)