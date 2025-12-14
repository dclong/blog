Status: published
Date: 2025-11-23 11:06:12
Modified: 2025-11-23 11:06:12
Author: Benjamin Du
Slug: powershell-on-windows-for-github-actions
Title: Powershell on Windows for GitHub Actions
Category: Computer Science
Tags: Computer Science, programming, GitHub Actions, CICD, development, Windows, PowerShell

**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**


## PowerShell on Windows

### Set PATH 

echo "::add-path::./swigwin-4.0.1"

echo %programfiles%
echo ::set-env name=ProgramFilesPath::%programfiles%

https://stackoverflow.com/questions/60169752/how-to-update-the-path-in-a-github-action-workflow-file-for-a-windows-latest-hos

https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions#adding-a-system-path

Prepends a directory to the system PATH variable for all subsequent actions in the current job. The currently running action cannot access the new path variable.