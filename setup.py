from setuptools import setup, find_packages

setup(
    name='gnome-cats',
    version='0.1.0',
    description='Bring cats to your desktop',
    author='Juanjo Salvador',
    author_email='juanjosalvador@netc.eu',
    packages=find_packages(),
    package_data={'gnomeCats':['application.ui']},
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    scripts=['bin/gnome-cats'],
    install_requires=[
        'PyGObject==3.28.1',
    ],
)
