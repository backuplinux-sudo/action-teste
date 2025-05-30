
import os

print(os.system('env'))

branch = os.getenv('INPUT_BRANCH')
padrao_branch = os.getenv('INPUT_PADRAO_BRANCH').split(", ")

for padrao in padrao_branch:
    if branch.startswith(padrao):
        print(f"Branch '{branch}' está no padrão '{padrao}'")
        exit(0)