$bin_path = "bin"
$cache_path = "$bin_path\cache"
$dist_path = "$bin_path\dist"

if (Test-Path $bin_path)
{
    Remove-Item -Recurse -Force $bin_path
}
New-Item $bin_path -ItemType Directory
New-Item $cache_path -ItemType Directory
New-Item $dist_path -ItemType Directory

pyinstaller --onefile --clean --workpath $cache_path --distpath $dist_path --specpath $dist_path "image_utils.py"
Copy-Item "$dist_path\image_utils.exe" $bin_path