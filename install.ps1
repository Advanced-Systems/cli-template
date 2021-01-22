$PackageName = Read-Host "Enter package name"
Write-Host "Creating a new virtual environment . . ." -ForegroundColor Yellow
py.exe -3.8 -m venv venv/
venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
Write-Host "Installing $PackageName . . ." -ForegroundColor Yellow 
pip install -e .
Write-Host "Installing additional dev dependencies . . ." -ForegroundColor Yellow
pip install -r .\requirements/dev.txt
Write-Host "Installation is complete!" -ForegroundColor Green
