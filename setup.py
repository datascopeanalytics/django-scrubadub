import glob
import os
from setuptools import setup

import django_scrubadub


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


# read in the dependencies from the virtualenv requirements file
dependencies = []
filename = os.path.join("requirements", "python")
with open(filename, 'r') as stream:
    for line in stream:
        package = line.strip().split('#')[0]
        if package:
            dependencies.append(package)

# get a list of all the packages and package data to include in scr_dir.
# inspiration from django's and django-flux's setup.py
src_dir = 'django_scrubadub'
packages = []
package_data = {src_dir:[]}
for dirpath, dirnames, filenames in os.walk(src_dir):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or dirname == '__pycache__':
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        package_data[src_dir].extend([os.path.join(dirpath, f)
                                      for f in filenames])


github_url='https://github.com/datascopeanalytics/django-scrubadub'
setup(
    name='django_scrubadub',
    version=django_scrubadub.VERSION,
    description="",
    long_description=open('README.md').read(),
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Dean Malmgren',
    author_email='dean.malmgren@datascopeanalytics.com',
    license='MIT',
    install_requires=dependencies,
    packages=packages,
    package_data=package_data,
    include_package_data=True,
    zip_safe=False,
)
