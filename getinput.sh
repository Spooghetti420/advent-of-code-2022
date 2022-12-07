daydir="Day $1"
mkdir "$daydir" 2> /dev/null
wget --load-cookies=cookies.txt -O "$daydir/input.txt" https://adventofcode.com/2022/day/$1/input