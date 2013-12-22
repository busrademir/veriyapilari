   

def agda_ara():   
    
        iller={"Edirne":"Kirklareli Tekirdag",
        "Kirklareli":"Edirne Tekirdag Istanbul",
        "Tekirdag":"Edirne Kirklareli Istanbul",
        "Istanbul":"Tekirdag Kirklareli Kocaeli",
        "Kocaeli":"Istanbul Yalova Sakarya Bursa",
        "Sakarya":"Kocaeli Duzce Bursa Bilecik Bolu",
        "Duzce":"Sakarya Bolu Zonguldak",
        "Bolu":"Sakarya Duzce Zonguldak Karabuk Ankara Bilecik Eskisehir",
        "Zonguldak":"Duzce Bolu Karabuk Bartin",
        "Karabuk":"Zonguldak Bartin Kastamonu Cankiri Ankara Bolu",
        "Bartin":"Zonguldak Karabuk Kastamonu",
        "Kastamonu":"Bartin Karabuk Cankiri Corum Sinop",
        "Cankiri":"Karabuk Kastamonu Corum Kirikkale Ankara",
        "Corum":"Kastamonu Sinop Samsun Amasya Yozgat Kirikkale Cankiri",
        "Sinop":"Kastamonu Corum Samsun",
        "Samsun":"Sinop Corum Amasya Tokat Ordu",
        "Amasya":"Samsun Corum Tokat Yozgat",
        "Tokat":"Samsun Amasya Ordu Sivas Yozgat",
        "Ordu":"Samsun Tokat Sivas Giresun",
        "Sivas":"Tokat Ordu Giresun Erzincan Malatya Kahramanmaras Kayseri Yozgat",
        "Giresun":"Ordu Sivas Erzincan Gumushane Trabzon",
        "Gumushane":"Giresun Erzincan Bayburt Trabzon",
        "Erzincan":"Sivas Giresun Gumushane Bayburt Erzurum Tunceli Malatya",
        "Rize":"Trabzon Bayburt Erzurum Artvin",
        "Erzurum":"Rize Bayburt Erzincan Bingol Mus Agri Kars Ardahan Artvin",
        "Artvin":"Rize Erzurum Ardahan",
        "Ardahan":"Artvin Erzurum Kars",
        "Kars":"Ardahan Erzurum Agri Igdir",
        "Igdir":"Kars Agri",
        "Agri":"Erzurum Kars Igdir Mus Van",
        "Van":"Agri Bitlis Siirt Sirnak Hakkari",
        "Bitlis":"Mus Agri Van Siirt Batman",
        "Siirt":"Bitlis Batman Mardin Sirnak Van",
        "Batman":"Diyarbakir Mardin Siirt Bitlis Mus",
        "Mus":"Bingol Erzurum Agri Bitlis Batman Diyarbakir",
        "Sirnak":"Mardin Siirt Hakkari Van",
        "Hakkari":"Van Sirnak",
        "Mardin":"Sanliurfa Diyarbakir Batman Siirt Sirnak",
        "Diyarbakir":"Bingol Mus Batman Mardin Sanliurfa Adiyaman Elazig Malatya",
        "Bingol":"Tunceli Erzurum Erzincan Mus Diyarbakir Elazig",
        "Bayburt":"Gumushane Trabzon Rize Erzurum Erzincan",
        "Elazig":"Tunceli Bingol Diyarbakir Malatya",
        "Tunceli":"Erzincan Bingol Elazig Malatya",
        "Malatya":"Sivas Erzincan Elazig Tunceli Adiyaman Kahramanmaras",
        "Adiyaman":"Kahramanmaras Malatya Diyarbakir Sanliurfa Gaziantep",
        "Kahramanmaras":"Kayseri Sivas Malatya Adiyaman Gaziantep Osmaniye Adana",
        "Sanliurfa":"Gaziantep Adiyaman Diyarbakir Mardin",
        "Gaziantep":"Kilis Hatay Osmaniye Kahramanmaras Adiyaman Sanliurfa",
        "Adana":"Mersin Nigde Kayseri Kahramanmaras Osmaniye Hatay",
        "Osmaniye":"Adana Kahramanmaras Gaziantep Hatay",
        "Kilis":"Hatay Osmaniye Gaziantep",
        "Hatay":"Adana Osmaniye Kilis Gaziantep",
        "Kayseri":"Yozgat Sivas Kahramanmaras Adana Nigde Nevsehir",
        "Nigde":"Aksaray Nevsehir Kayseri Adana Mersin Konya",
        "Nevsehir":"Kirsehir Yozgat Kayseri Nigde Aksaray Kayseri",
        "Aksaray":"Ankara Konya Nigde Nevsehir",
        "Mersin":"Antalya Karaman Konya Nigde Adana",
        "Karaman":"Antalya Konya Mersin",
        "Konya":"Antalya Isparta Afyon Eskisehir Ankara Aksaray Nigde Karaman Mersin",
        "Kirsehir":"Ankara Kirikkale Yozgat Nevsehir",
        "Kirikkale":"Ankara Cankiri Corum Yozgat Kirsehir",
        "Ankara":"Eskisehir Bolu Karabuk Cankiri Kirikkale Kirsehir Aksaray Konya",
        "Eskisehir":"Afyon Kutahya Bilecik Bolu Ankara Konya",
        "Afyon":"Denizli Usak Kutahya Eskisehir Konya Isparta Burdur",
        "Kutahya":"Usak Manisa Balikesir Bursa Bilecik Eskisehir Afyon",
        "Bilecik":"Bursa Kocaeli Sakarya Bolu Eskisehir Kutahya",
        "Denizli":"Mugla Aydin Manisa Usak Afyon Burdur",
        "Usak":"Denizli Manisa Kutahya Afyon",
        "Isparta":"Burdur Afyon Konya Antalya",
        "Burdur":"Mugla Denizli Afyon Isparta Antalya",
        "Manisa":"Izmir Balikesir Kutahya Usak Denizli Aydin",
        "Balikesir":"Canakkale Bursa Kutahya Manisa Izmir",
        "Bursa":"Balikesir Yalova Kocaeli Bilecik Kutahya Sakarya",
        "Mugla":"Aydin Denizli Burdur Antalya",
        "Izmir":"Balikesir Manisa Aydin",
        "Aydin":"Izmir Manisa Denizli Mugla",
        "Canakkale":"Balikesir Tekirdag"
               
        }

        
        islem = 'true'
        
        while islem=='true':
                girdi=raw_input('Lutfen ili giriniz:')
                if girdi=="end":
                        break
                        
                        
                elif girdi!='end':
                        ikinci_girdi=raw_input('Lutfen komsulugu aranacak ili giriniz:')
                        x=iller[girdi]
                        y=x.split()

                        
                        
                        if ikinci_girdi in y:
                                print"Evet,baglidir."
                                
                        else:
                                print"Hayir,bagli deðildir."
                                
                                
                                
                

               
