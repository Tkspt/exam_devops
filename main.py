import os
from classes.directory_manager import DirectoryManager
from classes.git_manager import GitManager

path = os.getcwd()
directory_manager = DirectoryManager(path)
git_manager = GitManager(path)

second_level_folders = ["data/cleaned", "data/raw",]

directory_manager.createEmptyDirectories(second_level_folders)

git_manager.add_into_local_repos()
git_manager.add_commit('create seconds level folders close #2')
git_manager.push_to_remote()
