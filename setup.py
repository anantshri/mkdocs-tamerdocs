from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="tamerdocs",
    version=VERSION,
    url='https://anantshri.github.io/mkdocs-tamerdocs/',
    license='GPL',
    description='AndroidTamer mkdocs theme',
    author='Anant Shrivastava',
    author_email='anant@anantshri.info',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'tamerdocs = mkdocs-tamerdocs',
        ]
    },
    zip_safe=False
)