from setuptools import setup, find_packages

# @see https://github.com/pypa/sampleproject/blob/master/setup.py
setup(
    name='monolog-python',
    version='0.1.0',
    author='Maciej Brencz',
    author_email='maciej.brencz@gmail.com',
    description='Python\'s logging formatter compatible with https://github.com/macbre/monolog-utils',
    url='https://github.com/macbre/monolog-python',
    keywords='logging json syslog monolog php',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ]
)
