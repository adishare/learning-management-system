= Perhatian 

Ini proyek serius ya , hahahahahahah

== Proses preparasi Development
Untuk dapat membangun aplikasi yang kuat dibutuhkan jiwa yang sehat. Maka dari itu kita perlu mempersiapkan developmen environment yang canggih. Berikut ini adalah langkah-langkah nya.

=== Membuat Virtualenv
Tolong menggunakan python 3 ya. Buat virtualenv dengan perintah 
   ```mkvirtualenv -p /usr/bin/python3 lms```

=== Clone Source code dengan perintah 
Tolong URL nya di sesuaikan ya

=== Install library pendukung
```pip install -r requirements.txt```

== Proses Developmen
 Saatnya kita koding teman-teman

=== Menjalankan skrip init
Pada working directori ketikan perintah 
```make initdev```

=== Menjalankan development server
 Pada working directory ketikan perintah 
```make```

=== Membersihkan / memperbaharui file migrations
Tolong eksekusi perintah ini setiap setelah melakukan perubahan pada models
```make cleanmigrations```
