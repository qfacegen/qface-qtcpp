from setuptools import setup, find_packages

setup(
    name='qface-qtcpp',
    version='1.1',
    description='Qt CPP generator based on the QFace library',
    url='https://github.com/Pelagicore/qface-qtcpp',
    author='jryannel',
    author_email='juergen@ryannel.org',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='qt cpp generator',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.h', '*.cpp', '*.pro', '*.pri', '*.qml', '*.js', '*.j2', '*.qdocconf', '*.conf', 'CMakeLists.txt', 'qmldir']
    },
    install_requires=[
        'qface>=1.7',
    ],
    entry_points={
        'console_scripts': [
            'qface-qtcpp = qtcpp.qtcpp:app'
        ],
    },
)
