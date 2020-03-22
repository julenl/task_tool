from setuptools import setup, find_packages

long_desc = 'Task Tool is a bottle app which implements an extended TODO list.'
long_desc += 'It logs the time spent on each task and generates'
long_desc += 'graphs with statistics.'


setup(
    name = 'task_tool',
    version = '1.0.0.dev1',
    description = 'Extended TODO list with statistics',
    long_description = long_desc,
    license = 'GNU General Public License v2 (GPLv2)',
    author = 'Julen Larrucea',
    author_email = 'code@larrucea.eu',
    url = 'https://github.com/julenl/task_tool',
    download_url = 'https://github.com/julenl/task_tool/archive/0.1.tar.gz',
    keywords = ['config', 'ini', 'raw', 'parser', 'non-interactive'],
    classifiers = [
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2"
        ],
    packages = find_packages()
)
