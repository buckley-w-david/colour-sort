import setuptools


setuptools.setup(
    name='colour_sort',
    version='0.0.1',
    long_description='',
    author='David Buckley',
    url='https://github.com/buckley-w-david/colour_sort',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    entry_points='''
        [console_scripts]
        colour=colour_sort.cli:main
    '''
)
