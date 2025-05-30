
import os

print(os.system('env'))

print(f"branch: {os.getenv('INPUT_BRANCH')}")
print(f"padrao_branch: {os.getenv('INPUT_PADRAO_BRANCH')}")

if os.getenv("INPUT_BRANCH") in os.getenv("INPUT_PADRAO_BRANCH"):
    print("Branch está no padrão PADRAO_BRANCH")