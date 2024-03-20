from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='pranab',
    author_email='dasp70578@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
