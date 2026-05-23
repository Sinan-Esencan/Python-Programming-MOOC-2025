# In the previous part there was an exercise where you implemented the class LunchCard. The card had separate methods for eating a regular and a special lunch, along with a method for depositing money on the card.
# The LunchCard class, as you were asked to implement it, has some problems, however. The card itself had knowledge of the prices of the different lunch options, and knew to subtract the right amount of money from the balance based on these. But imagine the prices changed, or there were new items introduced to the system, but several cards were already registered in the system. This would mean all existing cards would need to be replaced by versions with knowledge of the new prices.
# A better solution would be to make the cards "stupid", ignorant of the prices of different products. The purpose of the card would be to simply keep track of the available balance. All more complicated features should be contained within another class: the payment terminal.
# talimatın devamı icin: advanced course in programming > part 9 > objects and references > LunchCard and PaymentTerminal

# *bu LunchCard'ın diger projedeki LunchCard'dan farkı fiyatları bilmemesi ve sorumlulukların ayrılması ilkesine uygun 
# olması. sorumlulukları ayırarak hem unittesting kolaylaşır ve fiyatlar degisince LunchCard'ı degistirmek zorunda kalmayız
# hem de "indirimli personel kartı" veya "misafir kartı" gibi yeni kart türleri için yeni sınıflar yaratırız ve fiyat
# degisikliginde her bir classı degistirmek zorunda kalmayız (PaymentTerminal'ı guncellemek yeterli olur). eat_soup() gibi 
# yeni metodları da sadece PaymentTerminal'a koyarız ve bunlarla ilgili guncelleme olursa (fiyat bazlı veya kod akısında)
# sadece PaymentTerminal'den isimizi halletmis oluruz. bir indirim olacagı zaman discount degiskenini PaymentTerminal icinde
# tanımlamak ve tek bir paymentterminal objesi uzerinden bu degiskeni degistirmek daha pratiktir.
# asagıdaki PaymentTerminal sınıfında hem cash hem de karttan odeme kabul ediliyor. karttan odeme icin LunchCard sınıfı
# kullanılırken cash odeme icin dogrudan sayıları PaymentTerminal sınıfındaki metodlara arguman olarak yolluyoruz.
# PaymentTerminal odeme mantıgını yonetirken lunchcard bakiyeyi takip eder. lunchcard fiyatları bilmezken paymentterminal 
# bakiye detaylarını bilmez*
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
    special_lunch = 4.3 #bunlar class attribute (java'daki statik)
    regular_lunch = 2.5
    
    def __init__(self):
        self.funds = 1000 #terminal fonu
        self.lunches = 0 #satılan lunch
        self.specials = 0 #satılan specials

    def eat_lunch(self, payment: float):
        if payment >= PaymentTerminal.regular_lunch:
            change = payment - PaymentTerminal.regular_lunch
            self.funds += PaymentTerminal.regular_lunch
            self.lunches += 1
            return change
        return payment

    def eat_special(self, payment: float):
        if payment >= PaymentTerminal.special_lunch:
            change = payment - PaymentTerminal.special_lunch
            self.funds += PaymentTerminal.special_lunch
            self.specials += 1
            return change
        return payment
        
    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >= PaymentTerminal.regular_lunch:
            card.subtract_from_balance(PaymentTerminal.regular_lunch)
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
# eat_lunch_lunchcard'daki metoda gore bu gosterim daha dogru cunku yukarda gereksiz tekrar var
        if card.subtract_from_balance(PaymentTerminal.special_lunch):
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


#Claude'nun baglantıları kolayca hatırlamak icin ne yapmak lazım sorusuna verdigi cevap:

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
# - Fiyat kim bilmeli? → `PaymentTerminal` (class attribute: `regular_lunch = 2.5`)
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
