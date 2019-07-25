import sys
import setuptools
from distutils.core import setup


setup(
    name='uk-postcodes',
    version='0.0.1',
    description="Python's library for UK postcodes validation.",
    author='Tulio Cesar',
    author_email='tulicesarpbs@gmail.com',
    url='https://github.com/tuliocpbs/ukpostcodes-lib',
    packages=[
        'postcodes',
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords=['uk', 'postcode', 'validation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests'
)
