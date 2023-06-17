using namespace System.IO

#region helper function

function Set-VariableInFile([string] $Path, [string] $Variable, [string] $NewValue) {
    $Content = Get-Content -Path $Path
    $Content -replace "^$Variable = (.*?)$", "$Variable = `"$NewValue`"" | Set-Content -Path $Path
}

function Write-Information([string[]] $Messages) {
    $Line = "*" * 80
    Write-Host $Line -ForegroundColor Green
    $Messages | ForEach-Object {
        Write-Host ("* ") -ForegroundColor Green -NoNewline
        Write-Host $_.PadRight(76) -NoNewline
        Write-Host (" *") -ForegroundColor Green
    }
    Write-Host $Line -ForegroundColor Green
}

function Write-Step($Message) {
    Write-Host "[$i/$n] " -ForegroundColor DarkGray -NoNewline
    Write-Host $Message
    $global:i++
}

#endregion

$global:i = 1
$global:n = 4
$Root = git rev-parse --show-toplevel
$DefaultPackage = "clitemplate"
Push-Location -Path $Root

#region meta data

Write-Information @(
    "Copyright (c) $(Get-Date | Select-Object -ExpandProperty Year) Advanced Systems".ToUpper()
    "You are using $DefaultPackage ($(git tag | Select-Object -Last 1))"
    [string]::Empty
    "This work is licensed under the terms of the MIT license."
    "For a copy, see <https://opensource.org/licenses/MIT>."
)

Write-Step "Configure your project, press enter to continue with default settings"

$Package = Read-Host -Prompt "Package"
if ($Package -eq [string]::Empty) { $Package = $DefaultPackage }

$Version = Read-Host -Prompt "Version"
if ($Version -eq [string]::Empty) { $Version = "1.0.0" }

$Author = Read-Host -Prompt "Name"
if ($Author -eq [string]::Empty) { $Author = git config --global user.name }

$Email = Read-Host -Prompt "Email"
if ($Email -eq [string]::Empty) { $Email = git config --global user.email }

$Description = Read-Host -Prompt "Description"
if ($Description -eq [string]::Empty) { $Description = "$Package CLI" }

$Url = Read-Host -Prompt "GitHub Link"
if ($Url -eq [string]::Empty) {
    $Remote = git remote get-url --push origin
    $Tmp = $Remote -split "/" | Select-Object -Last 2
    $Owner = $Tmp[0].Replace("git@github.com:", [string]::Empty)
    $Repository = $Tmp[1].Substring(0, $Tmp[1].IndexOf('.'))
    $Url = "https://github.com/$Owner/$Repository"
}

#endregion

#region main script

Write-Step "Creating a new branch"
git checkout -b dev 2>&1 | Out-Null

Write-Step "Overwriting default meta data . . ."
$PythonFolder = $([Path]::Join($Root, "src", $DefaultPackage))
git mv $([Path]::Join($Root, "src", $DefaultPackage)) $PythonFolder
$InitScript = Get-ChildItem $PythonFolder | Where-Object Name -eq "__init__.py"

Set-VariableInFile -Path $InitScript.FullName -Variable "__version__" -NewValue $Version
Set-VariableInFile -Path $InitScript.FullName -Variable "author_name" -NewValue $Author
Set-VariableInFile -Path $InitScript.FullName -Variable "author_email" -NewValue $Email
Set-VariableInFile -Path $InitScript.FullName -Variable "package_name" -NewValue $Package
Set-VariableInFile -Path $InitScript.FullName -Variable "description" -NewValue $Description
Set-VariableInFile -Path $InitScript.FullName -Variable "url" -NewValue $Url
Set-VariableInFile -Path $InitScript.FullName -Variable "url_documentation" -NewValue "$Url/blob/master/README.md"
Set-VariableInFile -Path $InitScript.FullName -Variable "url_source_code" -NewValue $Url
Set-VariableInFile -Path $InitScript.FullName -Variable "url_bug_reports" -NewValue "$Url/issues"
Set-VariableInFile -Path $InitScript.FullName -Variable "url_changelog" -NewValue "$Url/blob/master/CHANGELOG.md"

$SetupScript = Get-ChildItem -Path $Root | Where-Object Name -eq "setup.py"
$Content = Get-Content -Path $SetupScript
$Content -replace "$DefaultPackage", "$Package" | Set-Content -Path $SetupScript

git add --all
git commit -m "Configure project meta data"

Write-Step "Done. You're all set now!"

Pop-Location

#endregion
