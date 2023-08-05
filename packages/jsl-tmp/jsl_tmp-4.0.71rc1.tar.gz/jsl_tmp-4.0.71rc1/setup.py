from setuptools import setup, find_packages
from codecs import open
from os import path
import johnsnowlabs.settings

# johnsnowlabs.settings.
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

REQUIRED_PKGS = [
    f'pyspark=={johnsnowlabs.settings.raw_version_pyspark}',
    f'spark-nlp=={johnsnowlabs.settings.raw_version_nlp}',
    f'nlu=={johnsnowlabs.settings.raw_version_nlu}',
    f'spark-nlp-display=={johnsnowlabs.settings.raw_version_nlp_display}',
    'numpy',
    'dataclasses',
    'requests',
    'databricks-api',
    'pydantic',
    'colorama'
]

setup(
    version=johnsnowlabs.settings.raw_version_jsl_lib,
    # scrirpts=['bin/myscript.py'],
    # entry_points={
    #     'console_scripts': [
    #         'hello-world = custom_lib:hi.hello_world ',
    #         'hello = custom_lib:hi.hello'
    #     ]
    # },# ! pip install jsl_tmp==4.0.25
    name='jsl_tmp',
    description='TODO',
    long_description=long_description,
    install_requires=REQUIRED_PKGS,
    long_description_content_type='text/markdown',
    url='https://nlu.johnsnowlabs.com',
    author='John Snow Labs',
    author_email='christian@johnsnowlabs.com',
    classifiers=[
        # Optional
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='NLP spark development NLU ',
    packages=find_packages(exclude=['test*', 'tmp*']),  # exclude=['test']
    include_package_data=True
)
