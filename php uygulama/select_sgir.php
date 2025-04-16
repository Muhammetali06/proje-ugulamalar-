<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>sayı hesapla</title>
</head>
<body>
        <form action="select_shesapla.php" method="post" >
        <p>
        <label for="s1">1. sayi:</label>
        <input type="text" name="s1" id="s1"/>
        </p>
        <p>
        <label for="s2">2. sayi:</label>
        <input type="text" name="s2" id="s2"/> 
         </p>

        <p>
        <label for="islem">1slemi Seçiniz:</label>
    <select name="islem[]" id="islem" size="5" multipte>
        <option value="+">Topla</option>
        <option value="-">cikar</option>
        <option value="*">carp</option>
        <option value="/">Böl</option>
        <option value="%">kalan</option>
    </select>
    </p>
   <p><input type="submit" value="gönder"></p>
</form>
</body>
</html>