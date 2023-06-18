using namespace System.IO

#region helper function

function Set-VariableInFile([string] $Path, [string] $Variable, [string] $NewValue) {
    $Content = Get-Content -Path $Path
    $Content -replace "^$Variable = (.*?)$", "$Variable = `"$NewValue`"" | Set-Content -Path $Path
}

function Set-StringInFile([string] $Path, [string] $Name, [string] $OldString, [string] $NewString) {
    $File = Get-ChildItem -Recurse -Path $Path | Where-Object Name -eq $Name | Select-Object -First 1
    $Content = Get-Content -Path $File.FullName
    $Content -replace "$OldString", "$NewString" | Set-Content -Path $File.FullName
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
$MetaData = @{}
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
if ($Package -eq [string]::Empty) { $Package = "package" }
$MetaData.Add("package_name", $Package)

$Version = Read-Host -Prompt "Version"
if ($Version -eq [string]::Empty) { $Version = "1.0.0" }
$MetaData.Add("__version__", $Version)

$Author = Read-Host -Prompt "Name"
if ($Author -eq [string]::Empty) { $Author = git config --global user.name }
$MetaData.Add("author_name", $Author)

$Email = Read-Host -Prompt "Email"
if ($Email -eq [string]::Empty) { $Email = git config --global user.email }
$MetaData.Add("author_email", $Email)

$Description = Read-Host -Prompt "Description"
if ($Description -eq [string]::Empty) { $Description = "$Package CLI" }
$MetaData.Add("description", $Description)

$Url = Read-Host -Prompt "GitHub Link"
if ($Url -eq [string]::Empty) {
    $Remote = git remote get-url --push origin
    $Tmp = $Remote -split "/" | Select-Object -Last 2
    $Owner = $Tmp[0].Replace("git@github.com:", [string]::Empty)
    $Repository = $Tmp[1].Substring(0, $Tmp[1].IndexOf('.'))
    $Url = "https://github.com/$Owner/$Repository"
}
$MetaData.Add("url", $Url)
$MetaData.Add("url_documentation", "$Url/blob/master/README.md")
$MetaData.Add("url_source_code", $Url)
$MetaData.Add("url_bug_reports", "$Url/issues")
$MetaData.Add("url_changelog", "$Url/blob/master/CHANGELOG.md")

#endregion

#region main script

Write-Step "Creating a new branch"
git checkout -b development

Write-Step "Overwriting default meta data . . ."
$PythonFolder = $([Path]::Join($Root, "src", $Package))
git mv $([Path]::Join($Root, "src", $DefaultPackage)) $PythonFolder 2>&1 | Out-Null
$InitScript = Get-ChildItem $PythonFolder | Where-Object Name -eq "__init__.py"

$MetaData.GetEnumerator() | ForEach-Object {
    Set-VariableInFile -Path $InitScript.FullName -Variable $_.Key -NewValue $_.Value
}

@("setup.py", "test_commands.py") | ForEach-Object {
    Set-StringInFile -Path $Root -Name $_ -OldString $DefaultPackage -NewString $MetaData["package_name"]
}

git add --all
git commit -m "Configure project meta data"

Write-Step "Done. You're all set now!"

Pop-Location

#endregion
