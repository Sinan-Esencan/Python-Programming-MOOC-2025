# In the previous part there was an exercise where you implemented the class LunchCard. The card had separate methods for eating a regular and a special lunch, along with a method for depositing money on the card.
# The LunchCard class, as you were asked to implement it, has some problems, however. The card itself had knowledge of the prices of the different lunch options, and knew to subtract the right amount of money from the balance based on these. But imagine the prices changed, or there were new items introduced to the system, but several cards were already registered in the system. This would mean all existing cards would need to be replaced by versions with knowledge of the new prices.
# A better solution would be to make the cards "stupid", ignorant of the prices of different products. The purpose of the card would be to simply keep track of the available balance. All more complicated features should be contained within another class: the payment terminal.
# talimatın devamı icin: advanced course in programming > part 9 > objects and references > LunchCard and PaymentTerminal

# *bu LunchCard'ın diger projedeki LunchCard'dan farkı fiyatları bilmemesi ve sorumlulukların ayrılması ilkesine 
# uygun olması. sorumlulukları ayırarak hem unittesting kolaylaşır ve fiyatlar degisince LunchCard'ı degistirmek 
# zorunda kalmayız hem de "indirimli personel kartı" veya "misafir kartı" gibi yeni kart türleri için yeni sınıflar
# yaratırız ve fiyat degisikliginde her bir classı degistirmek zorunda kalmayız (PaymentTerminal'ı guncellemek 
# yeterli olur). ayrıca birden fazla terminal varsa her birinin kendi farklı fiyat politikasını ve yemek 
# metodlarını belirleme durumumuz olur ve Lunchcard'ı if statementla kirletmeyiz.
# asagıdaki PaymentTerminal sınıfında hem cash hem de karttan odeme kabul ediliyor. karttan odeme icin LunchCard sınıfı
# kullanılırken cash odeme icin dogrudan sayıları PaymentTerminal sınıfındaki metodlara arguman olarak yolluyoruz.
# PaymentTerminal odeme mantıgını yonetirken lunchcard bakiyeyi takip eder. lunchcard fiyatları bilmezken
# paymentterminal bakiye detaylarını bilmez*

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float): #hem kontrol hem de yemek kartını guncelleme
        if self.balance >= amount:
            self.balance -= amount #yemek harcaması kadar launchcarddan cıkarıyor
            return True
        return False


class PaymentTerminal:
    SPECIAL_LUNCH = 4.3 #bunlar class attribute ve constant oldugu icin buyuk harf
    REGULAR_LUNCH = 2.5
    
    def __init__(self):
        self.funds = 1000 #terminal fonu
        self.lunches = 0 #satılan lunch
        self.specials = 0 #satılan specials

    def eat_lunch(self, payment: float):
        if payment >= PaymentTerminal.REGULAR_LUNCH:
            change = payment - PaymentTerminal.REGULAR_LUNCH
            self.funds += PaymentTerminal.REGULAR_LUNCH
            self.lunches += 1
            return change
        return payment

    def eat_special(self, payment: float):
        if payment >= PaymentTerminal.SPECIAL_LUNCH:
            change = payment - PaymentTerminal.SPECIAL_LUNCH
            self.funds += PaymentTerminal.SPECIAL_LUNCH
            self.specials += 1
            return change
        return payment
        
    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >= PaymentTerminal.REGULAR_LUNCH:
            card.subtract_from_balance(PaymentTerminal.REGULAR_LUNCH)
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
# eat_lunch_lunchcard'daki metoda gore bu gosterim daha dogru cunku yukarda gereksiz tekrar var
        if card.subtract_from_balance(PaymentTerminal.SPECIAL_LUNCH):
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount


if __name__ == "__main__":
    # 1
    print("#1")
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)


    # 2
    print("#2")
    terminal = PaymentTerminal()

    change = terminal.eat_lunch(10)
    print("The change returned was", change)

    change = terminal.eat_lunch(5)
    print("The change returned was", change)

    change = terminal.eat_special(4.3)
    print("The change returned was", change)

    print("Funds available at the terminal:", terminal.funds)
    print("Regular lunches sold:", terminal.lunches)
    print("Special lunches sold:", terminal.specials)


    # 3
    print("#3")
    terminal = PaymentTerminal()

    change = terminal.eat_lunch(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = terminal.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = terminal.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = terminal.eat_lunch_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", terminal.funds)
    print("Regular lunches sold:", terminal.lunches)
    print("Special lunches sold:", terminal.specials)


    #4
    print("#4")
    terminal = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = terminal.eat_special_lunchcard(card)
    print("Payment successful:", result)

    terminal.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = terminal.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", terminal.funds)
    print("Regular lunches sold:", terminal.lunches)
    print("Special lunches sold:", terminal.specials)


# ---A. CLAUDE'NUN BAGLANTILARI KOLAYCA HATIRLAMAK ICIN NE YAPMAK LAZIM SORUSUNA VERDIGI CEVAP---
# Önce sınıflar arasındaki ilişkiyi görselleştirelim, sonra hafıza sorununa odaklanalım.Kodun doğru ve iyi yazılmış. Asıl sorun hafızayla değil, **bağlantıları hızlıca inşa etme tekniğinin eksikliğiyle** ilgili. İşte bunu çözmek için somut bir sistem:
# (Burada PaymentTerminal ve Lunchcard icin class diagram cizildi)

# ---

# ## 1. "Neden" sorusunu önce sor, "Nasıl"ı sonra

# Koda başlamadan önce tek bir soru sor: **bu nesne ne bilmeli, ne bilmemeli?**

# Bu egzersizin tüm amacı tek bir tasarım kararından ibaret:

# | Nesne | Sorumluluğu | Bilmediği |
# |---|---|---|
# | `LunchCard` | Bakiyeyi takip et | Fiyatlar |
# | `PaymentTerminal` | Ödeme mantığını yönet | Bakiye detayları |

# Bu iki satırı kafana kazıdıktan sonra, metodlar kendiliğinden yerleşir. Bağlantılar kaybolduğunda bu tabloya dön.

# ---

# ## 2. "Sorumluluk Testi" uygula

# Her method yazarken kendine şunu sor: *"Bu bilgi hangi nesneye ait?"*

# Örneğin `eat_lunch_lunchcard` yazarken:
# - Fiyatı kim bilmeli? → `PaymentTerminal` (class attribute: `REGULAR_LUNCH = 2.5`)
# - Bakiyeden kim düşmeli? → `LunchCard` (kendi metodunu çağırıyoruz: `card.subtract_from_balance(...)`)

# Bu test, nesneye yanlış sorumluluk yüklemeyi engeller.

# ---

# ## 3. Kodu yazmadan önce 3 satır Türkçe yaz

# ```
# # PaymentTerminal: nakit veya kart ödemelerini yöneten, fiyatları bilen terminal.
# # LunchCard: sadece bakiyesini tutan, aptal kart.
# # İlişki: Terminal, kartı argüman olarak alır ve karta iş yaptırır.
# ```

# Senin kodunda zaten bunu yaptığını gördüm (Türkçe yorumlar). Bu alışkanlığı **her yeni sınıf yapısında** uygula.

# ---

# ## 4. Ezberlemek yerine: "Hangi pattern bu?" de

# Bu egzersiz sana **Separation of Concerns** (Endişelerin Ayrılığı) kalıbını öğretiyor. Bu kalıbı bir kez tanırsan, benzer yapıları gördüğünde otomatik olarak tanırsın:

# - Banka kartı ↔ ATM
# - Oyuncu ↔ Oyun motoru
# - Ürün ↔ Alışveriş sepeti

# Hafıza sorunu aslında **kalıp tanıma eksikliği**dir. Detayları ezberlemeye çalışmak yerine, hangi kalıba ait olduğunu anladığında detaylar kendiliğinden gelir.

# ---

# ## 5. Spaced repetition: 1-3-7 kuralı

# Bugün çözdüğün egzersizi:
# 1. **1 gün sonra**: Notlara bakmadan aynı şeyi sıfırdan yaz
# 2. **3 gün sonra**: Kalıbı farklı bir örneğe uygula (ATM + BankCard gibi)
# 3. **7 gün sonra**: Birine anlat veya comment'siz versiyonunu yaz

# ---

# ## Short Answer

# Kodun doğru ve mantıklı — sorun hafıza değil, teknik. Üç şey yap:

# 1. **Her yeni sınıf yapısında önce sor:** *"Bu nesne ne bilmeli, ne bilmemeli?"* — bu soruyu cevaplamak, metodların nereye gideceğini otomatik belirler.
# 2. **Kalıpları tanı:** Bu egzersiz "Separation of Concerns" kalıbıdır. Kalıbın adını bilmek, detayları ezberlemenin önüne geçer.
# 3. **1-3-7 kuralını uygula:** Bugün çözdüğün kodu 1, 3 ve 7 gün sonra notlara bakmadan tekrar yaz — hafıza sorunu değil, tekrar eksikliği sorunu bu.


#############################################################################
# ---B. BU DA KIMI'NIN NEDEN LUNCHCARD'I AYIRMAK LAZIM SORUSUNA VERDIGI ORNEK:---
# class LunchCard:
#     def __init__(self, balance: float):
#         self.balance = balance
#         self.card_type = "student"  # Kart sadece "kim olduğunu" söyler
    
#     def deposit_money(self, amount: float):
#         self.balance += amount
    
#     def subtract_from_balance(self, amount: float):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         return False


# class TeacherCard:
#     def __init__(self, balance: float):
#         self.balance = balance
#         self.card_type = "teacher"  # Aynı interface, farklı tip
    
#     def deposit_money(self, amount: float):
#         self.balance += amount
    
#     def subtract_from_balance(self, amount: float):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         return False


# class PaymentTerminal:
#     # Fiyatlar hâlâ burada (tek merkez)
#     BASE_REGULAR = 2.50
#     BASE_SPECIAL = 4.30
    
#     # İNDİRİM POLİTİKASI da burada! (İşte kritik nokta)
#     DISCOUNTS = {
#         "student": 0.00,
#         "teacher": 0.20,   # %20 indirim
#         "staff": 0.15,
#         "loyalty": 0.10
#     }

#     def __init__(self):
#         self.funds = 1000
#         self.lunches = 0
#         self.specials = 0

#     def _get_price(self, base_price, card):
#         """Terminal, kartın tipine bakarak fiyatı hesaplar."""
#         discount = self.DISCOUNTS.get(card.card_type, 0)
#         return base_price * (1 - discount)

#     def eat_lunch_lunchcard(self, card):
#         # Hangi kart olursa olsun, terminal fiyatı belirler!
#         price = self._get_price(self.BASE_REGULAR, card)
        
#         if card.subtract_from_balance(price):
#             self.lunches += 1
#             return True
#         return False

#     def eat_special_lunchcard(self, card):
#         price = self._get_price(self.BASE_SPECIAL, card)
        
#         if card.subtract_from_balance(price):
#             self.specials += 1
#             return True
#         return False

#     def deposit_money_on_card(self, card, amount: float):
#         card.deposit_money(amount)
#         self.funds += amount


# --- Test ---
# terminal = PaymentTerminal()

# ogrenci_karti = LunchCard(10)
# ogretmen_karti = TeacherCard(10)

# # Öğrenci: 2.50 öder
# print(terminal.eat_lunch_lunchcard(ogrenci_karti))  # True
# print(f"Öğrenci bakiye: {ogrenci_karti.balance}")   # 7.50

# # Öğretmen: 2.00 öder (%20 indirimli!)
# print(terminal.eat_lunch_lunchcard(ogretmen_karti)) # True
# print(f"Öğretmen bakiye: {ogretmen_karti.balance}") # 8.00


# KISACA:
# Bir yazılım tasarımında fiyatlandırma mantığının nerede yönetileceği, sistemin uzun vadeli bakım kolaylığını
# ve esnekliğini doğrudan belirler. Kartlar akıllı yaklaşımında her kart tipi (örneğin TeacherCard, StudentCard)
# kendi indirim kurallarını ve fiyat mantığını içinde barındırır. Bu durumda bir öğretmen indirimini %20’den %30’a
# çıkarmak için TeacherCard sınıfına girip ilgili fiyat attribute’larını elle değiştirmeniz gerekir.
# Aynı şekilde yeni bir SeniorCard tipi eklemek istediğinizde, baştan yeni bir sınıf oluşturmanız, tüm fiyat
# mantığını ve metodları yazmanız zorunlu hale gelir. Kampanya uygulamak ise daha da zahmetlidir; mevcut tüm kart
# sınıflarına kampanya fiyatı ekleme veya override etme işlemi yapılması gerekir. Kantin B gibi farklı 
# lokasyonlarda fiyatların değişmesi durumunda ise kartlar kantin bilgisini taşımadığından bu yaklaşım oldukça 
# sınırlı ve karmaşık kalır.
# Öte yandan Terminal akıllı yaklaşımı (mevcut kodunuz), fiyatlandırma sorumluluğunu PaymentTerminal sınıfına
# ve onun alt sınıflarına verir. Bu modelde öğretmen indirimini %30 yapmak için tek bir satır yeterlidir: 
# DISCOUNTS["teacher"] = 0.30. Yeni bir SeniorCard eklemek sadece DISCOUNTS["senior"] = 0.25 satırını eklemekle
# tamamlanır. Bugün herkese %10 kampanya uygulamak için Terminal’de self.active_campaign = 0.10 
# tanımlayıp _get_price() metodunda bu değeri kullanmanız yeterlidir. Kantin B’de farklı fiyatlandırma 
# gerektiğinde ise KantinBTerminal adında bir alt sınıf oluşturarak fiyat mantığını sadece orada 
# özelleştirebilirsiniz. Bu yaklaşım, değişikliklerin çok daha az çabayla ve minimum riskle yapılmasını sağlar.
