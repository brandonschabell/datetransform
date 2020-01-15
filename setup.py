from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


test_requirements = [
    'pytest'
]

setup(
    name='datetransform',
    version='0.1.0',
    packages=find_packages(),
    url='https://www.github.com/brandonschabell/datetransform',
    download_url='https://github.com/brandonschabell/datetransform/archive/v0.1.0.tar.gz',
    license='MIT',
    author='Brandon Schabell',
    author_email='brandonschabell@gmail.com',
    description='Feature engineering for dates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities'
    ],
    python_requires='~=3.5',
    install_requires=[
        'pandas',
        'numpy'
    ],
    tests_require=test_requirements,
    setup_requires=[
        'pytest-runner'
    ],
    extras_require={
        'tests': test_requirements
    }
)
