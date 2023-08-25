import os
from classes.directory_manager import DirectoryManager
from classes.git_manager import GitManager

path = os.getcwd()
directory_manager = DirectoryManager(path)
git_manager = GitManager(path)

files = ['requirements.txt', 'notebooks/main.ipynb', 'src/utils.py']

for file in files:
    directory_manager.createFile(file)

git_manager.add_into_local_repos()
git_manager.add_commit('create files close #3')
git_manager.push_to_remote()
