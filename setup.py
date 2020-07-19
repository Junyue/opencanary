from setuptools import setup, find_packages

import os
import opencanary

setup(
    name='opencanary',
    version=opencanary.__version__,
    url='http://www.thinkst.com/',
    author='Thinkst Applied Research',
    author_email='info@thinkst.com and p1r06u3@gmail.com',
    description='OpenCanary daemon',
    long_description='A low interaction honeypot intended to be run on internal networks.',
    install_requires=[
        'Twisted==14.0.2',
        'pyasn1==0.4.4',
        'pycrypto==2.6.1',
        'simplejson==3.16.0',
        'wsgiref==0.1.2',
        'zope.interface==4.5.0',
        'PyPDF2==1.26.0',
        'fpdf==1.7.2',
        'passlib==1.7.1',
        'Jinja2==2.10',
        'ntlmlib==0.72',
        'APScheduler==3.5.3',
        'service-identity==17.0.0',
        'scapy==2.4.0',
        'pcapy==0.11.4',
        'rdpy==1.3.2',
        'pyinotify==0.9.6',
        'rsa==4.5'
    ],
    setup_requires=[
        'setuptools_git'
    ],
    license='BSD',
    packages = find_packages(exclude='test'),
    scripts=['bin/opencanaryd','bin/opencanary.tac'],
    platforms='any',
    include_package_data=True
)

