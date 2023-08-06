Bu kutubxona yordamida CSV fayllardagi datani TXT holatiga o'tkazib beradi.TXT data kelgan faylni esa, CSV
fayliga o'zgartirib beradi.O'zgarayotgan faylga istagan nomni berishingiz mumkin.

Uning uchun:
masalan;

pip install umidstrela    #->pip qilinishi kerak bo'lgan kutubxona.

from umidstrela import csv_txt #-> Ba'zi xollarda bu shart emas!

csv_txt('data.csv', 'data.txt')

from umidstrela import txt_csv

txt_csv('data.txt', 'data.csv')


