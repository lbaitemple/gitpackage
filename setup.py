from setuptools import setup

setup(
    name='biology',
    version='1.0.0',
    packages=['biology', 'biology.plants', 'biology.animals'],
    url='',
    license='',
    author='Li Bai',
    author_email='',
    description='package example',
    install_requires=['pandas'],
    package_data={
        'biology': ['conf/*.csv']
    }
)
