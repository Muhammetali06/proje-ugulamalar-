print("Merhaba ben kişisel asistanınızım") 
print("Lütfen giriş yapınız")


kullanici_adi = {'ALİ', 'ali', 'ELİF', 'elif'}
sifre_1 = {'123', '1905', '0000'}


while True:
    KULLANICI = input('Kullanıcı adı: ')
    if KULLANICI in kullanici_adi:
        while True:
            SİFRE = input('Lütfen şifrenizi girin: ') 
            if SİFRE in sifre_1:
                print("Giriş başarılı!") 
                while True:
                    CEVAP_1 = input('Size nasıl yardımcı olabilirim: ') 
                    if CEVAP_1 == '': 
                        print("Değer alınamadı.")
                        continue
                    if 'merhaba' in CEVAP_1.lower():
                        print("Size de merhaba efendim.")
                    elif 'nasılsın' in CEVAP_1.lower():
                        nsoru=input("İyiyim efendim, siz nasılsınız:") 
                        if 'iyi' in nsoru : 
                            print('iyi olmanıza sevindim efendim.')   
                        elif 'normal' in nsoru : 
                            print('moodunuzu yükselticek bişeyler yapabilirsiniz')  
                        elif 'kötü' in nsoru :
                            print('kötü olmanıza üzüldüm kitap okuyabilirsiniz' '/n' 'müzik dinleyebilir veya film izleyebilirsiniz ')                 
                    else:
                        print("Üzgünüm, sizi anlayamadım.")
                        continue
                break  
            else:
                print("Şifre yanlış. Lütfen tekrar deneyin.")
        break  
    else:
        print("Kullanıcı adı hatalı. Lütfen tekrar deneyin.")
