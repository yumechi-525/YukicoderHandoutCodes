<?php
$arr = explode(' ', trim(fgets(STDIN)));
echo ($arr[1] > $arr[0] ? "+" : "") . ($arr[1] - $arr[0]) . PHP_EOL;
