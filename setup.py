import os
from setuptools import setup, find_packages


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding='utf-8')
    except TypeError:
        file = open(path)
    return file.read()


setup(
    name='django-jet2',
    version=__import__('jet').__version__,
    description='Next Generation of django-jet (Modern template for Django admin interface with improved functionality)',
    long_description=read('README.rst'),
    author='TIK (Technology Innovation Network)',
    author_email='contat@tik.tn',
    url='https://github.com/tikservices/django-jet2',
    packages=find_packages(),
    license='AGPLv3',
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Environment :: Web Environment',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=['Django'],
    long_description_content_type='text/x-rst',
    project_urls={
        'Documentation': 'http://django-jet2.rtfd.io/',
        'Source': 'https://github.com/tikservices/django-jet2',
        'Tracker': 'https://github.com/tikservices/django-jet2/issues',
    },
)
