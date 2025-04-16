<?php

$x=$_POST["s1"];
$y=$_POST["s2"];
$islemler=$_POST["islem"];


echo "<h3> x:$x y:$y</h3>";
print_r($islemler) ;


echo "<hr>";
foreach($islemler as $islem)
{
    if($islem=="+") echo "$x + $y =" .($x+$y);
    if($islem=="-") echo "$x - $y =".($x-$y);
    if($islem=="*") echo "$x * $y =".($x*$y);
    if($islem=="/") echo "$x / $y =".($×/$y);
    if($islem=="%") echo "$x % $y =".($x%$y);
    echo "<br>";

}

?>