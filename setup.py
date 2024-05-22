from setuptools import setup, find_packages

setup(
    name='pushoverwrap',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    author='plutotree',
    author_email='plutotreetree@gmail.com',
    description='A simple Pushover API wrapper.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/plutotree/pushovewrap',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
