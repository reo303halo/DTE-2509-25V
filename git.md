# Git
## **Git Basics**

**Cloning a Repository:**
To clone a repository to your local machine, execute the following command:

```shell
git clone <git repository link>
```

**Checking Local Project Status:**
To obtain an overview of your local project’s current state, utilize this command:

```shell
git status
```

**Adding Changes for Commit:**
To include changes in your commit, execute this command:

```shell
git add .
```

Alternatively, you can specify a specific file to add:

```shell
git add <filename>
```

**Committing Changes and Adding a Comment:**
To finalize your changes and include a comment, execute this command:

```shell
git commit -m “<comment>”
```

**Inspecting Online Changes:**
To retrieve any pending changes from the online repository, execute this command:

```shell
git pull
```

**Handling Merge Conflicts:**
When a merge conflict arises, the initial conflict will display a warning and provide several options. For more control, consider this option:

```shell
git config pull.rebase false
```

**Pushing Commits to the Online Repository:**
To finalize your changes and push them to the online repository, execute this command:

```shell
git push
```


## **Branches:**

**Creating a New Branch:**
To create a new branch, execute the following command:

```shell
git branch <new branch name>
```

**Switching to a Branch:**
To switch to a specific branch, execute this command:

```shell
git checkout <name of branch you want to switch to>
```

**Retrieving a List of All Local Branches:**
To obtain a comprehensive list of all local branches, execute this command:

```shell
git branch
```

**Deleting a Branch:**
To remove a branch, execute the following command:

```shell
git branch -d <branch name>
```

**Renaming a Branch:**
To rename a branch, use the following command with the specified arguments:

```shell
git branch -m <current name> <new name>
```

**Merging from a Branch:**
To merge updates from a branch, switch to the desired branch, execute the following command:

```shell
git merge <branch you want updates from>
```


## **Utilizing Git and Branches in Collaboration:**
1. Switch to your personal branch.
2. Perform edits on your branch.
3. Switch to the main branch, pull updates from the online repository.
4. Return to your personal branch.
5. Merge updates from the main branch into your personal branch.
6. Resolve any conflicts (if any).
7. Switch back to the main branch.
8. Merge updates from your personal branch into the main branch.
9. Commit and push your local changes to the online repository.
