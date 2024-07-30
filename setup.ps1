Get-ChildItem -Filter *.md -Recurse | Remove-Item

Get-ChildItem -Filter *.py -Recurse | Rename-Item -NewName { $_.Directory.Name+'.py'}
Get-ChildItem -Filter *.py -Recurse | Move-Item -Destination { $_.Directory.Parent.FullName }
