try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="pyskip",
    version="0.9.0",
    description="A pure Python skiplist.",
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    long_description=open('README.rst', 'r').read(),
    py_modules=[
        'pyskip',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/toastdriven/pyskip/',
    license='BSD'
)
