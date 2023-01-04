from setuptools import find_packages, setup

with open('README/md', 'r') as f:
    long_description = f.read()

setup(
    name='mypgbackup',
    version='0.1.0',
    author='Dukuze',
    author_email = 'dukuze.dorna@outlook.com',
    description= 'An utility for backup a PostgreSQL databases',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Savimbi/mypgbackup',
    packages = find_packages('src')
)
