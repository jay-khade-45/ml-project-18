from setuptools import find_packages, setup

# it will find package inside this project dir.
from typing import List


HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """This function will return list of requirements.

    Args:
        file_path (str): path of requirements.txt

    Returns:
        List[str]: list of dependencies.
    """

    requirements = []

    with open(file_path) as file_obj:
        # reading each line.
        requirements = file_obj.readlines()
        # replacing "/n" with blank
        requirements = [req.replace("\n", "").strip() for req in requirements]

        # dont want to run -e .
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="jay",
    author_email="jaykhade2023@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
