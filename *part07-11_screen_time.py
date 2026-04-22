# Please write a program for recording the amount of time the user has spent in front of a television, computer or mobile device screen over a 
# specific period of time.
# The program should work as follows:
# Filename: late_june.txt
# Starting date: 24.6.2020
# How many days: 5
# Please type in screen time in minutes on each day (TV computer mobile):
# Screen time 24.06.2020: 60 120 0
# Screen time 25.06.2020: 0 0 0
# Screen time 26.06.2020: 180 0 0
# Screen time 27.06.2020: 25 240 15
# Screen time 28.06.2020: 45 90 5
# Data stored in file late_june.txt

# The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, representing minutes.
# With the above input, the program should store the data in a file named late_june.txt. The contents should look like this:

# Time period: 24.06.2020-28.06.2020
# Total minutes: 780
# Average minutes: 156.0
# 24.06.2020: 60/120/0
# 25.06.2020: 0/0/0
# 26.06.2020: 180/0/0
# 27.06.2020: 25/240/15
# 28.06.2020: 45/90/5

# bu versiyon mooc.fi ve biraz modifiye ettim:
from datetime import datetime, timedelta
 
def format(time): #dosyaya yazdıracakken formatlamak icin
    return time.strftime("%d.%m.%Y")

# her seferinde input girmemek icin once input() yerine hard-coded kod kullan:
if False:
    file = input("Filename: ")
    day, month, year = input("Starting date (dd.mm.yyyy): ").split('.') #list unpacking okunaklı kılar
    # *split() kullanmak yerine strptime() kullanılabilirdi:*
    # starting_date = input("Starting date (dd.mm.yyyy): ")
    days = int(input("How many days: "))
else:
    file = "denemelik.txt"
    day, month, year = "19.2.1999".split(".")
    days = 2
    
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
# her gune karsılık gelen tv, pc ve mobil suresini tuple olarak saklıyoruz
screen_times = []
total_time = 0
start = datetime(int(year), int(month), int(day))
# start = datetime.strptime(starting_date, "%d.%m.%Y") #yukarki alternatifin devamı
 
for i in range(days):
    day = start + timedelta(days=i) #tarih + sure = tarih
    tv, pc, mobile = input(f"Screen time {format(day)}: ").split(' ')
    total_time += int(tv) + int(pc) + int(mobile)
    screen_times.append((day, tv, pc, mobile) )

with open(file, "w") as my_file:
    my_file.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    my_file.write(f"Total minutes: {total_time}\n")
    my_file.write(f"Average minutes: {total_time/days:.1f}\n")
    for day, tv, pc, mob in screen_times:
        my_file.write(f"{format(day)}: {tv}/{pc}/{mob}\n")
 
print(f"Data stored in file {my_file.name}")



# *alt1 - claude: bu kodun daha duzgunu ve try-catch kullanılmıs hali:*
from datetime import datetime, timedelta

def format(time):
    return time.strftime("%d.%m.%Y")

try: #asagıdaki 3 tane raise ile hatanın hangi inputtan kaynaklı oldugu belli oluyor
    file = input("Filename: ").strip()
    if not file: #erkenden operasyonu sonlandırıyoruz
        raise ValueError("Filename cannot be empty.")

    raw_date = input("Starting date (dd.mm.yyyy): ").strip()
    parts = raw_date.split('.')
    if len(parts) != 3: #bu kısım opsiyonel olsa da acıklayıcı hata mesajı veriyor
        raise ValueError("Date must be in dd.mm.yyyy format.")
    day, month, year = parts

    days = int(input("How many days: "))
    if days <= 0: #onlenebilir hatalar icin if sta kullanılmalı ve kaynagında onlenmeli 
        # (try/except ZeroDivisionError kullanmak yerine)
        raise ValueError("Number of days must be a positive integer.")

    start = datetime(int(year), int(month), int(day))  # ValueError burada da olabilir
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

print("Please type in screen time in minutes on each day (TV computer mobile):")
screen_times = []
total_time = 0

for i in range(days):
    current_day = start + timedelta(days=i)
    try:
        parts = input(f"Screen time {format(current_day)}: ").strip().split(' ')
        if len(parts) != 3: #bu kısım da opsiyonel olsa da acıklayıcı hata mesajı veriyor
            raise ValueError("Please enter exactly 3 values separated by spaces.")
        tv, pc, mobile = parts
        total_time += int(tv) + int(pc) + int(mobile)
        screen_times.append((current_day, tv, pc, mobile))
    except ValueError as e:
        print(f"Invalid screen time entry: {e}")
        exit(1)

try:
    with open(file, "w") as my_file:
        my_file.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
        my_file.write(f"Total minutes: {total_time}\n")
        my_file.write(f"Average minutes: {total_time/days:.1f}\n")
        for day, tv, pc, mob in screen_times:
            my_file.write(f"{format(day)}: {tv}/{pc}/{mob}\n")
    print(f"Data stored in file {my_file.name}")
except (OSError, PermissionError) as e: #OSError, FileNotFoundError'u kapsar
    print(f"File error: {e}")
    exit(1)
    


# *alt2 - z.ai: kodun en duzgun hali*
from datetime import datetime, timedelta
 
def format(time): 
    return time.strftime("%d.%m.%Y")

# 1. DOSYA ADI KONTROLÜ
while True:
    file = input("Filename: ").strip()
    if file == "":
        print("Hata: Dosya adı boş olamaz!")
    else:
        # İsteğe bağlı: Dosya adında geçersiz karakter var mı kontrol edebilirsiniz
        break

# 2. TARİH KONTROLÜ (strptime kullanarak hem bölme hem int'a çevirme hem tarih mantığını kontrol ederiz)
while True:
    date_str = input("Starting date (dd.mm.yyyy): ")
    try:
        start = datetime.strptime(date_str, "%d.%m.%Y")
        break # Hata yoksa döngüden çık
    except ValueError:
        print("Hata: Geçersiz tarih formatı veya olmayan bir tarih girdiniz. Lütfen gg.aa.yyyy formatında girin.")
# *strptime() yerine split() kullansaydık:*
# while True:
#     date_input = input("Starting date (dd.mm.yyyy): ")
#     try:
#         # 1. Bölme (Split) işlemi
#         day, month, year = date_input.split('.')
#         # 2. İnt'e çevirme (int) işlemi
#         start = datetime(int(year), int(month), int(day))
#         # Eğer yukarıdaki satırlardan hiçbiri hata vermezse buraya ulaşır ve döngüden çıkar
#         break 
#     except ValueError:
#         # 3. Tarih mantığı (datetime ile obje olustururken fırlatılır) kontrolü de burada yakalanır
#         print("Hata: Lütfen gg.aa.yyyy formatında ve geçerli bir tarih girin!")

# 3. GÜN SAYISI KONTROLÜ
while True:
    days_str = input("How many days: ")
    try:
        days = int(days_str) #int dısındakilerde hata fırlatır
        if days <= 0:
            print("Hata: Gün sayısı 0 veya negatif olamaz!")
            # *alt: raise ValueError("Gün sayısı 0'dan büyük olmalıdır.")*
        else:
            break # Hata yoksa döngüden çık
    except ValueError:
        print("Hata: Lütfen sadece sayı girin!")
 
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
screen_times = []
total_time = 0
 
# 4. EKRAN SÜRESİ GİRDİSİ KONTROLÜ
for i in range(days):
    current_day = start + timedelta(days=i) 
    
    while True:
        time_str = input(f"Screen time {current_day}: ")
        try:
            # Boşlukla ayırıp 3 parça olup olmadığını kontrol ediyoruz
            tv, pc, mobile = time_str.split()
            
            # Sayıya çevirmeyi dene, metin girilirse ValueError fırlatır
            tv_int = int(tv)
            pc_int = int(pc)
            mobile_int = int(mobile)
            
            # Süre negatif olmamalı (isteğe bağlı kontrol)
            if tv_int < 0 or pc_int < 0 or mobile_int < 0:
                print("Hata: Süreler negatif olamaz!")
                continue
                
            total_time += tv_int + pc_int + mobile_int
            screen_times.append((current_day, tv, pc, mobile))
            break # Bu günün verisi doğru girildi, bir sonraki güne geç
        except ValueError:
            print("Hata: Lütfen 3 adet sayıyı boşlukla ayırarak girin (Örn: 10 20 30)")
        except Exception as e: #sadece uygulama hatalarını yakalaması icin Exception as e denmeli
            print("Hata: Beklenmeyen bir hata oluştu. Lütfen formatı kontrol edin.")

# 5. DOSYAYA YAZMA KONTROLÜ
try:
    with open(file, "w") as my_file:
        my_file.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
        my_file.write(f"Total minutes: {total_time}\n")
        my_file.write(f"Average minutes: {total_time/days:.1f}\n") # days <= 0 kontrolü yukarıda yapıldığı için burada ZeroDivisionError almazsın
        for day, tv, pc, mob in screen_times:
            my_file.write(f"{format(day)}: {tv}/{pc}/{mob}\n")
    print(f"Data stored in file {my_file.name}")
except OSError as e:
    print(f"Dosya yazma hatası! Dosya adını veya yazma izinlerinizi kontrol edin. (Hata Detayı: {e})")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")
