#Final Project - Basic Python by Alhazmi Yusi Wirawan
#Program untuk mengirimkan email kepada beberapa penerima
#Menggunakan smtp GMAIL, sebelumnya email pengirim di setting untuk menerima low security.

# Imports Library smtplib
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Setup Menu 
while True: 
    print ("-----------------------------")
    print("Selamat datang di Program Pengirim Email!")
    print()
    print("---Menu---")
    print("1. Daftar Email")
    print("2. Tambah Email")
    print("3. Mengirim Email")
    print("4. Keluar")
    print()
    menu = input("Piih Menu: ")
    print()

    if menu == '2':
        print("Masukkan Email Baru ")
        print ("-----------------------------")
        Email = input(str("Email:  "))
        with open('receiver_list.txt', 'a') as filex:
               filex.write(Email)
               filex.write('\n')
        print()
        print("Email berhasil ditambahkan")
    elif menu == '1':
            print("Daftar Email ")
            print ("-----------------------------")
            with open('receiver_list.txt', 'r') as filex:
                 Daftar = filex.read()
                 print(Daftar)

    elif menu == '3':
    # SETUP EMAIL LOGIN 
        print("Silahkan Login Terlebih ")
        gmail_user = input(str("Masukkan akun gmail: "))
        gmail_app_password = gmail_app_password = getpass.getpass("Masukkan Password:")

    # SETUP Pengirim, judul dan isi email (Detail Sumber : https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/ )
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['Subject'] = input("Masukkan Subjek pesan: ")
        body = input("Masukkan Isi pesan: ")

    # SETUP Lampiran, sesuaikan nama filename dengan nama di attachment
        filename = input("Masukkan nama File beserta formatnya: ")
        path = input("Masukkan Path File: ")
        attachment = open(path, "rb") 
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    # SETUP Penerima Email 
        with open('receiver_list.txt', 'r') as filex:
	        penerima = filex.readlines()
       
    # Mengirim Email atau Gagal (Detail Sumber: https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python)
        i = 0
        while i < len(penerima):
            receiver = f"{penerima[i]}"
            msg['To'] = receiver
            msg.attach(MIMEText(body, 'plain'))
           
            try:          
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_app_password)
                text = msg.as_string()
                server.sendmail(gmail_user, receiver, text)
                server.quit()

                print('Email sent!')
            except Exception as exception:
                print("Error: %s!\n\n" % exception)
            i += 1
            if Exception:
                continue
            

    elif menu == '4':
        print ("-----------------------------")
        print("Program selesai, sampai jumpa!")
        break
    else : 
        print ("-----------------------------")
        print("Menu tidak tersedia")

