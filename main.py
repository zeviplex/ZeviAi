import telebot
import telegram
import re
import random
import schedule
import threading
import time
from datetime import datetime
from telebot import types
from telegram.constants import ParseMode


bot = telebot.TeleBot('6437402376:AAEnpZt8oFZ7FIGNxhamEj-FOmo2FtLSLH4')




# Ayurvedic drug list with extended information

ayurvedic_drugs = {
    "ahipena": {
    "english_name": "Opium",
    "tamil_name": "à®•à®š à®•à®šà®¾",
    "sanskrit_name": "à¤…à¤¹à¤¿à¥žà¥‡à¤¨  (à¤®à¤¦à¤•à¤¾à¤°à¥€)",
    "botanical_name": "Papaver somniferum",
    "family_name": "Papaveraceae",
    "chemical_composition": "Morphine, Codeine, Papaverine",
    "rasa": "Tikta",
    "guna": "Laghu,Ruksha,",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Pacifies Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Pain management, Cough suppression (under medical supervision), Diarrhea treatment (under medical supervision)",
    "dose": "As prescribed by a qualified healthcare professional But 30-125 mg is adviceable",
    "uses":  [
        "Pain management",
        "Cough suppression (under medical supervision)",
        "Diarrhea treatment (under medical supervision)",
        "Derived opioid medications for severe pain"
        ],
        "image_url": 'https://www.flickr.com/search/show/?q=Papaver+somniferum' # Replace with actual image URL
    },
    "agnimantha": {
    "english_name": "Premna",
    "tamil_name": "à®ªà¯à®°à¯‡à®£à®¾",
    "sanskrit_name": " à¤…à¤—à¥à¤¨à¤¿à¤®à¤¨à¥à¤¥ (à¤¶à¥‹à¤¥à¤¹à¤°)",
    "botanical_name": "Premna mucronata",
    "family_name": "Lamiaceae",
    "chemical_composition": "Iridoids, Flavonoids, Triterpenes",
    "rasa": "Tikta, Katu",
    "guna": "Laghu,Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Anti-inflammatory, Diuretic, Fever management, Respiratory support",
    "dose": "1 to 3 grams per day (as directed by an Ayurvedic practitioner)",
    "uses": [
        "Anti-inflammatory",
        "Diuretic",
        "Fever management",
        "Respiratory support"
        ],
        "image_url": 'https://www.flickr.com/photos/dinesh_valke/5928846965/'  # Replace with actual image URL
    },
    "agaru": {
    "english_name": "Agarwood",
    "tamil_name": "à®…à®•à®¿à®²à¯",
    "sanskrit_name": " à¤…à¤—à¤°à¥  (à¤¶à¥€à¤¤à¤ªà¥à¤°à¤¶à¤®à¤¨)",
    "botanical_name": "Aquilaria spp.",
    "family_name": "Thymelaeaceae",
    "chemical_composition": "Aquilarin, Essential Oils (sesquiterpenes)",
    "rasa": "Katu,Tikta,Madhura",
    "guna": "Tiksna,Laghu,Snigdha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Aromatic, Calming, Spiritual practices, Respiratory support",
    "dose": "As incense or in the form of essential oil (1-2 Bindu)(as directed by a qualified practitioner)",
    "uses": [
        "Aromatic purposes",
        "Calming and relaxation",
        "Spiritual practices",
        "Respiratory support"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Aquilaria+agallocha'  # Replace with actual image URL
  },
  "amalaki": {
    "english_name": "Indian Gooseberry",
    "tamil_name": "à®¨à¯†à®²à¯à®²à®¿à®•à¯à®•à®¾à®¯à¯",
    "sanskrit_name": "à¤†à¤®à¤²à¤•à¥€ (à¤°à¤¸à¤¾à¤¯à¤¨)",
    "botanical_name": "Emblica officinalis",
    "family_name": "Phyllanthaceae",
    "chemical_composition": "Vitamin C, Tannins, Flavonoids",
    "rasa": "AmlaPradhana Except Lavana",
    "guna": "Laghu,Ruksha,Sara",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances all three doshas",
    "prayoga": "Antioxidant, Immune support, Digestive aid, Hair care",
    "dose": "1 to 3 grams per day (as directed by an Ayurvedic practitioner)",
    "uses": [
        "Antioxidant properties",
        "Immune system support",
        "Digestive aid",
        "Hair care and rejuvenation"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Emblica+officinalis'
  },
  "apamarga": {
    "english_name": "Prickly Chaff Flower",
    "tamil_name": "à®¨à®¾à®¯à¯à®°à¯à®µà®¿",
    "sanskrit_name": "à¤…à¤ªà¤¾à¤®à¤¾à¤°à¥à¤— (à¤¯à¤•à¥„à¤¤à¥à¤¯)",
    "botanical_name": "Achyranthes aspera",
    "family_name": "Amaranthaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Saponins",
    "rasa": "Tikta, Katu",
    "guna": "Sara,Tiksna,Ruksa",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Anti-inflammatory, Antipyretic, Diuretic, Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (Ksara=0.5-2g,Swarasa=10-20ml,Curna=3g)",
    "uses": [
        "Anti-inflammatory properties",
        "Fever management",
        "Diuretic effect",
        "Wound healing"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Achyranthes+aspera'
   },
   "aragwadha": {
    "english_name": "Indian Laburnum",
    "tamil_name": "à®•à¯Šà®©à¯à®±à¯ˆ à®…à®²à¯à®²à®¤à¯ à®šà®°à®•à¯à®•à¯Šà®©à¯à®±à¯ˆ ",
    "sanskrit_name": "à¤†à¤°à¤—à¥à¤µà¤§ (à¤•à¥à¤·à¥à¤ à¤˜à¥à¤¨)",
    "botanical_name": "Cassia fistula",
    "family_name": "Fabaceae",
    "chemical_composition": "Anthraquinones, Flavonoids, Saponins",
    "rasa": "Madhura,Tikta",
    "guna": "Guru,Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Kapha doshas, increases Vata dosha",
    "prayoga": "Laxative, Antipyretic, Blood purifier, Skin conditions",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Laxative properties",
        "Antipyretic (fever-reducing) effects",
        "Blood purification",
        "Treatment of skin conditions"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Cassia+fistula'
  },
  "ardraka": {
    "english_name": "Ginger",
    "tamil_name": "à®‡à®žà¯à®šà®¿",
    "sanskrit_name": "à¤†à¤°à¥à¤¦à¥à¤°à¤•/à¤¶à¥à¤£à¥à¤ à¥€ (à¤¤à¥„à¤ªà¥à¤¤à¤¿à¤˜à¥à¤¨)",
    "botanical_name": "Zingiber officinale",
    "family_name": "Zingiberaceae",
    "chemical_composition": "Gingerol, Shogaol, Zingerone",
    "rasa": "Katu, Madhura",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Digestive aid, Anti-inflammatory, Immune support, Nausea relief",
    "dose": "Up to 4 grams per day (as directed by a healthcare professional)",
    "uses": [
        "Digestive aid",
        "Anti-inflammatory properties",
        "Immune system support",
        "Relief from nausea and motion sickness"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Zingiber+officinale'
  },
  "arjuna": {
    "english_name": "Arjuna",
    "tamil_name": "à®®à®°à¯à®¤à®®à¯",
    "sanskrit_name": "Arjuna",
    "botanical_name": "Terminalia arjuna",
    "family_name": "Combretaceae",
    "chemical_composition": "Arjunolic acid, Tannins, Flavonoids",
    "rasa": "Kasaya",
    "guna": "Laghu,Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, increases Vata dosha",
    "prayoga": "Cardiovascular support, Anti-inflammatory, Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=60-100ml,Curna=3-6g,Ksirapaka=20-30ml)",
    "uses": [
        "Cardiovascular support",
        "Anti-inflammatory properties",
        "Wound healing",
        "Support for respiratory health"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Terminalia+arjuna'
  },
  "arka": {
    "english_name": "Calotropis",
    "tamil_name": "à®¨à¯€à®² à®Žà®°à¯à®•à¯à®•à¯",
    "sanskrit_name": "à¤…à¤°à¥à¤• (à¤¤à¥€à¤•à¥à¤·à¥à¤£à¤µà¤¿à¤°à¥‡à¤šà¤¨)",
    "botanical_name": "Calotropis procera",
    "family_name": "Apocynaceae",
    "chemical_composition": "Calotropin, Uscharin, Calotropagenin",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, increases Pitta dosha",
    "prayoga": "Anti-inflammatory, Antimicrobial, Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (Mula twak curna=500-750mg,Ksira1/4-1/2g)",
    "uses": [
        "Anti-inflammatory properties",
        "Antimicrobial effects",
        "Wound healing",
        "Traditionally used for skin conditions"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Calotropis+procera'
  },
  "ashwagandha": {
    "english_name": "Ashwagandha",
    "tamil_name": "à®…à®šà¯à®µà®•à®¾à®¨à¯à®¤à®¾  or à®…à®®à¯à®•à¯à®•à®¿à®°à®¾",
    "sanskrit_name": "à¤…à¤¶à¥à¤µà¤—à¤¨à¥à¤§à¤¾ (à¤°à¤¸à¤¾à¤¯à¤¨)",
    "botanical_name": "Withania somnifera",
    "family_name": "Solanaceae",
    "chemical_composition": "Withanolides, Alkaloids, Sitoindosides",
    "rasa": "Tikta, Kasaya, Madhura",
    "guna": "Laghu, snigdha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Adaptogen, Stress reduction, Immune support, Stamina and vitality",
    "dose": "3 to 5 grams per day (as directed by an Ayurvedic practitioner)",
    "uses": [
        "Adaptogenic properties",
        "Stress reduction",
        "Immune system support",
        "Enhanced stamina and vitality"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Withania+somnifera'
   },
   "asoka": {
    "english_name": "Ashoka",
    "tamil_name": "à®…à®šà¯‹à®•à®®à¯ or à®†à®¯à®¿à®²",
    "sanskrit_name": "à¤…à¤¶à¥‹à¤•  (à¤†à¤°à¥à¤¤à¤µà¤¸à¤‚à¤—à¥à¤°à¤¹à¤£à¥€à¤¯)",
    "botanical_name": "Saraca indica",
    "family_name": "Caesalpiniaceae",
    "chemical_composition": "Tannins, Flavonoids, Alkaloids",
    "rasa": "Astringent, Bitter",
    "guna": "Light, Dry",
    "virya": "Cooling",
    "vipaka": "Pungent",
    "amayoga": "Balances Pitta and Kapha doshas, increases Vata dosha",
    "prayoga": "Uterine tonic, Menstrual health, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Uterine tonic",
        "Supports menstrual health",
        "Anti-inflammatory properties",
        "Traditionally used for gynecological issues"
    ],
    "image_url": 'https://www.flickr.com/search/?q=Saraca+asoca'
   },
   "ativisa": {
    "english_name": "Indian Ativisa",
    "tamil_name": "à®…à®¤à®¿à®µà®¿à®Ÿà®¯à®®à¯",
    "sanskrit_name": "à¤…à¤¤à¤¿à¤µà¤¿à¤·à¤¾   (à¤¦à¥€à¤ªà¤¨ ",
    "botanical_name": "Aconitum heterophyllum",
    "family_name": "Ranunculaceae",
    "chemical_composition": "Alkaloids (Aconitine, Pseudaconitine), Tannins",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksa",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, increases Pitta dosha",
    "prayoga": "Antipyretic, Analgesic, Respiratory support, Digestive aid (under medical supervision)",
    "dose": "As prescribed by an Ayurvedic practitioner (Mula Curna=1-3g)",
    "uses": [
        "Antipyretic properties",
        "Analgesic (pain-relieving) effects",
        "Respiratory support",
        "Digestive aid (under medical supervision)"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Aconitum+heterophyllum'
   },
   "bakuchi": {
    "english_name": "Bakuchi",
    "tamil_name": "à®•à®¾à®°à¯à®ªà¯‹à®• à®…à®°à®¿à®šà®¿",
    "sanskrit_name": "à¤¬à¤¾à¤•à¥à¤šà¥€ (à¤•à¥à¤·à¥à¤ à¤˜à¥à¤¨)",
    "botanical_name": "Psoralea corylifolia",
    "family_name": "Fabaceae",
    "chemical_composition": "Psoralen, Isopsoralen, Bakuchiol",
    "rasa": "Tikta, Madhura",
    "guna": "Laghu, Ruksha, Sara",
    "virya": "Ushna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, increases Pitta dosha",
    "prayoga": "Skin disorders, Vitiligo, Antifungal, Antioxidant",
    "dose": "As directed by an Ayurvedic practitioner (Curna=1-3gm)",
    "uses": [
        "Treatment of skin disorders",
        "Used in conditions like Vitiligo",
        "Antifungal properties",
        "Antioxidant effects"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Psoralea+corylifolia'
   },
   "bala": {
    "english_name": "Country Mallow",
    "tamil_name": "à®šà®¿à®¤à¯à®¤à®¾à®®à¯à®Ÿà¯à®Ÿà®¿ à®…à®²à¯à®²à®¤à¯ à®šà®¿à®±à¯à®±à®¾à®®à¯à®Ÿà¯à®Ÿà®¿",
    "sanskrit_name": "à¤¬à¤²à¤¾à¤¦à¥à¤µà¤¯   à¤¬à¤²à¤¾ (à¤¬à¤²à¥à¤¯)",
    "botanical_name": "Sida cordifolia",
    "family_name": "Malvaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Tannins",
    "rasa": "Madhura, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Rejuvenative, Anti-inflammatory, Aphrodisiac, Immune support",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=50-100ml,Curna=3-6g,Swarasa=10-20ml)",
    "uses": [
        "Rejuvenative properties",
        "Anti-inflammatory effects",
        "Aphrodisiac qualities",
        "Immune system support"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Sida+cordifolia'
   },
   "abutilon_indicum": {
    "english_name": "Indian Mallow",
    "tamil_name": "à®¤à¯à®¤à¯à®¤à®¿à®•à¯à®•à¯€à®°à¯ˆ à®…à®²à¯à®²à®¤à¯ à®µà®Ÿà¯à®Ÿà®¤à¯à®¤à¯à®¤à¯à®¤à®¿",
    "sanskrit_name": " à¤¬à¤²à¤¾à¤¦à¥à¤µà¤¯   à¤…à¤¤à¤¿à¤¬à¤²à¤¾ (à¤¬à¤²à¥à¤¯)",
    "botanical_name": "Abutilon indicum",
    "family_name": "Malvaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Tannins",
    "rasa": "Madhura",
    "guna": "Guru, Snigdha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Rejuvenative, Anti-inflammatory, Diuretic",
    "dose": "As directed by an Ayurvedic practitioner (Curnaa=1-3g)",
    "uses": [
        "Rejuvenative properties",
        "Anti-inflammatory effects",
        "Diuretic action",
        "Traditional use for urinary issues"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Abutilon+indicum'
   },
   "bhallataka": {
    "english_name": "Marking Nut",
    "tamil_name": "à®¤à¯‡à®©à¯à®•à¯Šà®Ÿà¯à®Ÿà¯ˆ à®®à®°à®®à¯",
    "sanskrit_name": "à¤­à¤²à¥à¤²à¤¾à¤¤à¤• (à¤•à¥à¤·à¥à¤ à¤˜à¥à¤¨)",
    "botanical_name": "Semecarpus anacardium",
    "family_name": "Anacardiaceae",
    "chemical_composition": "Anacardic acid, Bhilawanols",
    "rasa": "Katu, Madhura",
    "guna": "Laghu, Snigdha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Kapha and Vata doshas, increases Pitta dosha",
    "prayoga": "Anti-rheumatic, Laxative (under medical supervision), Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (Taila=10-20drops,Ksirapaka=30ml)",
    "uses": [
        "Anti-rheumatic properties",
        "Laxative effects (under medical supervision)",
        "Wound healing",
        "Traditional use in joint disorders"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Semecarpus+anacardium'
   },
   "bharangi": {
    "english_name": "Bharangi",
    "tamil_name": "à®•à®¾à®µà®¾à®²à®¿, à®ªà®°à®™à¯à®•à®¿à®ªà¯à®ªà®Ÿà¯à®Ÿà¯ˆ",
    "sanskrit_name": "à¤­à¤¾à¤‚à¤°à¤—à¥€  (à¤¶à¥à¤µà¤¾à¤¸à¤¹à¤°)",
    "botanical_name": "Clerodendrum serratum",
    "family_name": "Lamiaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Tannins",
    "rasa": "Katu,Tikta,Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Respiratory support, Anti-inflammatory, Immunomodulator",
    "dose": "As directed by an Ayurvedic practitioner (Mula Curna=3-6gm)",
    "uses": [
        "Respiratory support",
        "Anti-inflammatory effects",
        "Immunomodulatory properties",
        "Traditional use in respiratory disorders"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Clerodendrum+serratum'
   },
   "bhringaraja": {
    "english_name": "Bhringaraja",
    "tamil_name": "à®•à®°à®¿à®šà®²à®™à¯à®•à®©à®¿",
    "sanskrit_name": "à¤­à¥ƒà¤‚à¤—à¤°à¤¾à¤œ (à¤•à¥‡à¤¶à¥à¤¯)",
    "botanical_name": "Eclipta alba",
    "family_name": "Asteraceae",
    "chemical_composition": "Ecliptine, Wedelolactone, Triterpenoids",
    "rasa": "Katu,Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Kapha doshas, increases Vata dosha",
    "prayoga": "Hair care, Liver support, Anti-inflammatory, Immunomodulator",
    "dose": "As directed by an Ayurvedic practitioner (Swarasa=5-10ml,Curna=3-6g)",
    "uses": [
        "Hair care and rejuvenation",
        "Liver support",
        "Anti-inflammatory effects",
        "Immunomodulatory properties"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Eclipta+alba'
   },
   "bibhitaki": {
    "english_name": "Bibhitaki",
    "tamil_name": "	à®¤à®¾à®©à¯à®±à®¿à®•à¯à®•à®¾à®¯à¯",
    "sanskrit_name": "à¤¬à¤¿à¤­à¥€à¤¤à¤• (à¤›à¥‡à¤¦à¤¨)",
    "botanical_name": "Terminalia bellirica",
    "family_name": "Combretaceae",
    "chemical_composition": "Gallic acid, Ellagic acid, Tannins",
    "rasa": "Astringent",
    "guna": "Light, Dry",
    "virya": "Cooling",
    "vipaka": "Astringent",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Digestive support, Respiratory health, Detoxification",
    "dose": "1 to 2 grams per day (as directed by an Ayurvedic practitioner)",
    "uses": [
        "Digestive support",
        "Respiratory health",
        "Detoxification",
        "Balancing all three doshas"
    ],
    "image_url": 'https://www.flickr.com/search/?q=Terminalia+bellirica'
   },
   "bijaka": {
    "english_name": "Indian Kino Tree",
    "tamil_name": "à®µà¯‡à®™à¯à®•à¯ˆ",
    "sanskrit_name": "à¤¬à¥€à¤œà¤• (à¤®à¥‚à¤¤à¥à¤°à¤¸à¤‚à¤—à¥à¤°à¤¹à¤£à¥€à¤¯)",
    "botanical_name": "Pterocarpus marsupium",
    "family_name": "Fabaceae",
    "chemical_composition": "Pterostilbene, Marsupin, Epicatechin",
    "rasa": "Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, increases Pitta dosha",
    "prayoga": "Blood sugar support, Antioxidant, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner (50-100ml)",
    "uses": [
        "Blood sugar support",
        "Antioxidant properties",
        "Anti-inflammatory effects",
        "Traditionally used for diabetes management"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Pterocarpus+marsupium'
   },
   "bilva": {
    "english_name": "Bael",
    "tamil_name": "à®µà®¿à®²à¯à®µà®®à¯",
    "sanskrit_name": "à¤¬à¤¿à¤²à¥à¤µ (à¤—à¥à¤°à¤¾à¤¹à¥€)",
    "botanical_name": "Aegle marmelos",
    "family_name": "Rutaceae",
    "chemical_composition": "Tannins, Alkaloids, Flavonoids",
    "rasa": "kasaya",
    "guna": "Guru, Ruksha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, increases Pitta dosha",
    "prayoga": "Digestive aid, Respiratory health, Antidiarrheal",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Digestive aid",
        "Respiratory health",
        "Antidiarrheal properties",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Aegle+marmelos'
   },
   "brahmi": {
    "english_name": "Brahmi",
    "tamil_name": "à®¨à¯€à®°à¯à®ªà¯à®ªà®¿à®°à®®à®¿ or à®µà®²à¯à®²à®¾à®°à¯ˆ",
    "sanskrit_name": "Brahmi",
    "botanical_name": "Bacopa monnieri",
    "family_name": "Plantaginaceae",
    "chemical_composition": "Bacosides, Alkaloids, Flavonoids",
    "rasa": "Tikta,Kasaya,Madhura",
    "guna": "Laghu, Sara, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Pitta doshas, increases Kapha dosha",
    "prayoga": "Memory and cognitive support, Stress reduction, Nervine tonic",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Memory and cognitive support",
        "Stress reduction",
        "Nervine tonic",
        "Traditionally used for enhancing mental clarity"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Bacopa+monnieri'
   },
   "brhati": {
    "english_name": "Brhati",
    "tamil_name": "à®šà¯à®£à¯à®Ÿà¯ˆà®•à¯à®•à®¾à®¯à¯",
    "sanskrit_name": "à¤¬à¥ƒà¤¹à¤¤à¥€ (à¤•à¤¾à¤¸à¤¹à¤°) ",
    "botanical_name": "Solanum indicum",
    "family_name": "Solanaceae",
    "chemical_composition": "Saponins, Alkaloids, Flavonoids",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksha, Tiksna",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, increases Pitta dosha",
    "prayoga": "Expectorant, Anti-inflammatory, Respiratory support",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Expectorant properties",
        "Anti-inflammatory effects",
        "Respiratory support",
        "Traditionally used for respiratory conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Solanum+indicum'
   },
   "chandana": {
    "english_name": "Sandalwood",
    "tamil_name": "à®šà®¨à¯à®¤à®©à®®à¯",
    "sanskrit_name": "à¤šà¤¨à¥à¤¦à¤¨ (à¤¦à¤¾à¤¹à¤ªà¥à¤°à¤¶à¤®à¤¨)",
    "botanical_name": "Santalum album",
    "family_name": "Santalaceae",
    "chemical_composition": "Santalol, Santalenes, Terpenes",
    "rasa": "Tikta, Madhura",
    "guna": "Guru, Sita",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta dosha, pacifies Vata dosha, may increase Kapha dosha in excess",
    "prayoga": "Aromatic, Cooling, Anti-inflammatory, Skin care",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Aromatic properties",
        "Cooling effects",
        "Anti-inflammatory properties",
        "Traditionally used for skin care"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Santalum+album'
   },
   "rakta_chandana": {
    "english_name": "Red Sandalwood",
    "tamil_name": "à®°à®•à¯à®¤ à®šà®¨à¯à®¤à®©à®®à¯",
    "sanskrit_name": "à¤°à¤•à¥à¤¤à¤šà¤¨à¥à¤¦à¤¨ (à¤¦à¤¾à¤¹à¤ªà¥à¤°à¤¶à¤®à¤¨)",
    "botanical_name": "Pterocarpus santalinus",
    "family_name": "Fabaceae",
    "chemical_composition": "Santalol, Santalenes, Tannins",
    "rasa": "Tikta, Madhura",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Kapha doshas, increases Vata dosha",
    "prayoga": "Skin care, Anti-inflammatory, Cooling",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Skin care",
        "Anti-inflammatory effects",
        "Cooling properties",
        "Traditionally used for various skin conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Pterocarpus+santalinus'
   },
   "citraka": {
    "english_name": "Citraka",
    "tamil_name": "à®šà®¿à®¤à¯à®°à®•à®®à¯",
    "sanskrit_name": "à¤šà¤¿à¤¤à¥à¤°à¤• (à¤¦à¥€à¤ªà¤¨)",
    "botanical_name": "Plumbago zeylanica",
    "family_name": "Plumbaginaceae",
    "chemical_composition": "Plumbagin, Resins, Tannins",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, increases Pitta dosha",
    "prayoga": "Digestive stimulant, Respiratory support, Anti-parasitic",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Digestive stimulant",
        "Respiratory support",
        "Anti-parasitic properties",
        "Traditionally used for digestive disorders"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Plumbago+zeylanica'
   },
   "dadima": {
    "english_name": "Pomegranate",
    "tamil_name": "à®®à®¾à®¤à¯à®³à®®à¯",
    "sanskrit_name": "à¤¦à¤¾à¤™à¤¿à¤®  (à¤°à¥‹à¤šà¤¨)",
    "botanical_name": "Punica granatum",
    "family_name": "Lythraceae",
    "chemical_composition": "Ellagic acid, Punicalagins, Anthocyanins",
    "rasa": "Kasaya, Madhura, Amla",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta dosha, may increase Vata and Kapha in excess",
    "prayoga": "Antioxidant, Astringent, Cardioprotective, Digestive support",
    "dose": "As directed by an Ayurvedic practitioner (Phala rasa=20-50ml,Phala kwatha=40-80ml)",
    "uses": [
        "Antioxidant properties",
        "Astringent taste",
        "Cardioprotective effects",
        "Digestive support",
        "Traditionally used for various health benefits"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Punica+granatum'
   },
   "devadaru": {
    "english_name": "Himalayan Cedar",
    "tamil_name": "à®¤à¯‡à®µà®¤à®¾à®°à¯",
    "sanskrit_name": "Devaadaru",
    "botanical_name": "Cedrus deodara",
    "family_name": "Pinaceae",
    "chemical_composition": "Deodarone, Deodarol, Resins",
    "rasa": "Tikta, Kasaya, Katu",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta dosha, may increase Kapha and Vata in excess",
    "prayoga": "Respiratory support, Anti-inflammatory, Sedative",
    "dose": "As directed by an Ayurvedic practitioner (Curna=1-3g,Taila=20-40drops)",
    "uses": [
        "Respiratory support",
        "Anti-inflammatory effects",
        "Sedative properties",
        "Traditionally used for respiratory and inflammatory conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Cedrus+deodara'
   },
   "dhataki": {
    "english_name": "Dhataki",
    "tamil_name": "à®¤à®¾à®¤à®¾à®°à®¿ à®œà®¾à®°à¯à®•à®¿",
    "sanskrit_name": "à¤§à¤¾à¤¤à¤•à¥€  (à¤¸à¥à¤¤à¤®à¥à¤­à¤¨)",
    "botanical_name": "Woodfordia fruticosa",
    "family_name": "Lythraceae",
    "chemical_composition": "Tannins, Flavonoids, Gallic acid",
    "rasa": "Kasaya, Katu",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Hemostatic, Uterine tonic, Antioxidant",
    "dose": "As directed by an Ayurvedic practitioner (Curna=1-3g)",
    "uses": [
        "Hemostatic properties",
        "Uterine tonic",
        "Antioxidant effects",
        "Traditionally used for women's health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Woodfordia+fruticosa'
   },
   "durva": {
    "english_name": "Bermuda Grass",
    "tamil_name": "à®…à®°à¯à®•à®®à¯à®ªà¯à®²à¯",
    "sanskrit_name": "à¤¦à¥‚à¤°à¥à¤µà¤¾ (à¤ªà¥à¤°à¤œà¤¾",
    "botanical_name": "Cynodon dactylon",
    "family_name": "Poaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Tannins",
    "rasa": "Tikta, Kasaya, Madhura",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta dosha, may increase Kapha and Vata in excess",
    "prayoga": "Anti-inflammatory, Detoxification, Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (Swarasa=10-20ml,Kwatha=500-100ml,Kalka=1-3g)",
    "uses": [
        "Anti-inflammatory properties",
        "Detoxification",
        "Wound healing",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Cynodon+dactylon'
   },
   "ela": {
    "english_name": "Cardamom",
    "tamil_name": "à®à®²à®•à¯à®•à®¾à®¯à¯",
    "sanskrit_name": "à¤à¤²à¤¾ (à¤¦à¤¾à¤¹à¤ªà¥à¤°à¤¶à¤®à¤¨)",
    "botanical_name": "Elettaria cardamomum",
    "family_name": "Zingiberaceae",
    "chemical_composition": "Essential oils (mainly cineole, terpinyl acetate)",
    "rasa": "Madhura, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Respiratory support, Cardioprotective",
    "dose": "As directed by an Ayurvedic practitioner (Curna=0.5-1g)",
    "uses": [
        "Digestive aid",
        "Respiratory support",
        "Cardioprotective effects",
        "Traditionally used as a culinary spice"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Elettaria+cardamomum'
   },
   "eranda": {
    "english_name": "Castor",
    "tamil_name": "à®†à®®à®£à®•à¯à®•à¯",
    "sanskrit_name": "à¤à¤°à¤£à¥à¤¡ (à¤µà¥‡à¤¦à¤¨à¤¾à¤¸à¥à¤¥à¤¾à¤ªà¤¨)",
    "botanical_name": "Ricinus communis",
    "family_name": "Euphorbiaceae",
    "chemical_composition": "Ricinoleic acid, Palmitic acid, Stearic acid",
    "rasa": "Tikta, Katu, Madhura",
    "guna": "Guru, Snigdha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Laxative, Anti-inflammatory, Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=50-100ml,Kalka=3-6g,Curna=3-6g)",
    "uses": [
        "Laxative properties",
        "Anti-inflammatory effects",
        "Wound healing",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Ricinus+communis'
   },
   "gambhari": {
    "english_name": "Gambhari",
    "tamil_name": "à®•à¯à®®à®¿à®´à¯ à®®à®°à®®à¯ à®…à®²à¯à®²à®¤à¯ à®•à¯à®®à¯à®²à¯",
    "sanskrit_name": "à¤—à¤®à¥à¤­à¤¾à¤°à¥€ (à¤¶à¥‹à¤¥à¤¹à¤°)",
    "botanical_name": "Gmelina arborea",
    "family_name": "Lamiaceae",
    "chemical_composition": "Gmelinol, Phenolic compounds, Flavonoids",
    "rasa": "Tikta, Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Pitta doshas, increases Kapha dosha",
    "prayoga": "Anti-inflammatory, Analgesic, Antipyretic",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=50-100ml,Curna=36g)",
    "uses": [
        "Anti-inflammatory effects",
        "Analgesic properties",
        "Antipyretic (fever-reducing) effects",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Gmelina+arborea'
   },
   "gokshura": {
    "english_name": "Tribulus",
    "tamil_name": "à®¨à¯†à®°à¯à®žà¯à®šà®¿à®²à¯",
    "sanskrit_name": "à¤—à¥‹à¤•à¥à¤·à¥à¤° (à¤®à¥‚à¤¤à¥à¤°à¤µà¤¿à¤°à¥‡à¤šà¤¨à¥€à¤¯)",
    "botanical_name": "Tribulus terrestris",
    "family_name": "Zygophyllaceae",
    "chemical_composition": "Saponins, Alkaloids, Flavonoids",
    "rasa": "Madhura, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
    "prayoga": "Diuretic, Aphrodisiac, Immunomodulator",
    "dose": "As directed by an Ayurvedic practitioner (Curna=3-6g,Kwatha=50-100ml)",
    "uses": [
        "Diuretic properties",
        "Aphrodisiac effects",
        "Immunomodulatory properties",
        "Traditionally used for reproductive health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Tribulus+terrestris'
   },
   "guduchi": {
    "english_name": "Guduchi",
    "tamil_name": "à®šà®¿à®±à¯à®•à¯à®±à®¿à®žà¯à®šà®©à¯",
    "sanskrit_name": "à¤—à¥à¤¡à¥‚à¤šà¥€ (à¤°à¤¸à¤¾à¤¯à¤¨)",
    "botanical_name": "Tinospora cordifolia",
    "family_name": "Menispermaceae",
    "chemical_composition": "Alkaloids, Diterpenoid lactones, Glycosides",
    "rasa": "Tikta, Kasaya",
    "guna": "Laghu, Snigdha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances all three doshas",
    "prayoga": "Immunomodulator, Antioxidant, Liver support",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=50-100ml,Curna=1-3g,Ssatva=0.5-2g)",
    "uses": [
        "Immunomodulatory properties",
        "Antioxidant effects",
        "Liver support",
        "Traditionally used for overall health and well-being"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Tinospora+cordifolia'
   },
   "guggulu": {
    "english_name": "Guggul",
    "tamil_name": "à®•à¯à®™à¯à®•à¯à®²à¯ à®ªà®¿à®šà®¿à®©à¯",
    "sanskrit_name": "à¤—à¥à¤—à¥à¤—à¥à¤²à¥‚  (à¤µà¥‡à¤¦à¤¨à¤¾à¤¸à¥à¤¥à¤¾à¤ªà¤¨)",
    "botanical_name": "Commiphora wightii",
    "family_name": "Burseraceae",
    "chemical_composition": "Guggulsterones, Flavonoids, Essential oils",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha dosha, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Cholesterol management, Joint support",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Anti-inflammatory effects",
        "Cholesterol management",
        "Joint support",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Commiphora+wightii'
   },
   "haridra": {
    "english_name": "Turmeric",
    "tamil_name": "à®®à®žà¯à®šà®³à¯",
    "sanskrit_name": "à¤¹à¤°à¤¿à¤¦à¥à¤°à¤¾  (à¤•à¥à¤·à¥à¤ à¤˜à¥à¤¨)",
    "botanical_name": "Curcuma longa",
    "family_name": "Zingiberaceae",
    "chemical_composition": "Curcuminoids (mainly curcumin), Essential oils",
    "rasa": "Tikta, Katu, Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances all three doshas",
    "prayoga": "Anti-inflammatory, Antioxidant, Digestive aid",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Anti-inflammatory effects",
        "Antioxidant properties",
        "Digestive aid",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Curcuma+longa'
   },
   "daruharidra": {
    "english_name": "Indian Barberry",
    "tamil_name": "à®®à®°à®®à®žà¯à®šà®²à¯",
    "sanskrit_name": "Daruharidra",
    "botanical_name": "Berberis aristata",
    "family_name": "Berberidaceae",
    "chemical_composition": "Berberine, Berbamine, Oxyacanthine",
    "rasa": "Tikta, Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Anti-inflammatory, Antimicrobial, Digestive support",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=50-100ml,Rasanjana=0.5-1g)",
    "uses": [
        "Anti-inflammatory effects",
        "Antimicrobial properties",
        "Digestive support",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Berberis+aristata'
   },
   "haritaki": {
    "english_name": "Haritaki",
    "tamil_name": "à®•à®Ÿà¯à®•à¯à®•à®¾à®¯à¯",
    "sanskrit_name": "à¤¹à¤°à¥€à¤¤à¤•à¥€ (à¤°à¤¸à¤¾à¤¯à¤¨)",
    "botanical_name": "Terminalia chebula",
    "family_name": "Combretaceae",
    "chemical_composition": "Chebulagic acid, Chebulinic acid, Tannins",
    "rasa": "Madhura, Kasaya",
    "guna": "Guru, Ruksha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata, Pitta, and Kapha doshas",
    "prayoga": "Laxative, Rejuvenative, Detoxification",
    "dose": "As directed by an Ayurvedic practitioner (Curna=1g,Kwatha=30-50ml)",
    "uses": [
        "Laxative properties",
        "Rejuvenative effects",
        "Detoxification",
        "Traditionally used for digestive health and overall well-being"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Terminalia+chebula'
   },
   "hingu": {
    "english_name": "Asafoetida",
    "tamil_name": "à®ªà¯†à®°à¯à®™à¯à®•à®¾à®¯à®®à¯",
    "sanskrit_name": "à¤¹à¤¿à¤‚à¤—à¥ (à¤¦à¥€à¤ªà¤¨)",
    "botanical_name": "Ferula assa-foetida",
    "family_name": "Apiaceae",
    "chemical_composition": "Resin, Gum, Volatile oils",
    "rasa": "Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata dosha, may increase Pitta and Kapha in excess",
    "prayoga": "Digestive aid, Anti-flatulent, Respiratory support",
    "dose": "As directed by an Ayurvedic practitioner (Curna=125-500mg)",
    "uses": [
        "Digestive aid",
        "Anti-flatulent properties",
        "Respiratory support",
        "Traditionally used as a culinary spice"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Asafoetida'
   },
   "jambu": {
    "english_name": "Java Plum",
    "tamil_name": "à®¨à®¾à®µà®²à¯",
    "sanskrit_name": "à¤œà¤®à¥à¤¬à¥‚  (à¤®à¥‚à¤¤à¥à¤°à¤¸à¤‚à¤—à¥à¤°à¤¹à¤£à¥€à¤¯)",
    "botanical_name": "Syzygium cumini",
    "family_name": "Myrtaceae",
    "chemical_composition": "Anthocyanins, Ellagic acid, Tannins",
    "rasa": "Kasaya, Madhura",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Antidiabetic, Antioxidant, Digestive aid",
    "dose": "As directed by an Ayurvedic practitioner (Swarasa=10-20ml,Curna=3-6gm)",
    "uses": [
        "Antidiabetic properties",
        "Antioxidant effects",
        "Digestive aid",
        "Traditionally used for managing diabetes"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Syzygium+cumini'
   },
   "jatamansi": {
    "english_name": "Spikenard",
    "tamil_name": "à®œà®Ÿà®¾à®®à®žà¯à®šà®²à¯",
    "sanskrit_name": "à¤œà¤Ÿà¤¾à¤®à¤¾à¤‚à¤¸à¥€  (à¤¸à¤‚à¤œà¥à¤žà¤¾à¤¸à¥à¤¥à¤¾à¤ªà¤¨)",
    "botanical_name": "Nardostachys jatamansi",
    "family_name": "Valerianaceae",
    "chemical_composition": "Valeranone, Jatamansone, Sesquiterpenes",
    "rasa": "Tikta, Madhura",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
    "prayoga": "Calmative, Nervine tonic, Anti-anxiety",
    "dose": "As directed by an Ayurvedic practitioner (Curna=3-6g)",
    "uses": [
        "Calmative properties",
        "Nervine tonic",
        "Anti-anxiety effects",
        "Traditionally used for promoting mental well-being"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Nardostachys+jatamansi'
   },
   "jatiphala": {
    "english_name": "Nutmeg",
    "tamil_name": "à®œà®¾à®¤à®¿à®•à¯à®•à®¾à®¯à¯",
    "sanskrit_name": "à¤œà¤¾à¤¤à¤¿à¤«à¤²  (à¤—à¥à¤°à¤¾à¤¹à¥€)",
    "botanical_name": "Myristica fragrans",
    "family_name": "Myristicaceae",
    "chemical_composition": "Myristicin, Elemicin, Eugenol",
    "rasa": "Tikta, Katu, Madhura",
    "guna": "Laghu, Snigdha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Carminative, Mild sedative",
    "dose": "As directed by an Ayurvedic practitioner (Curna=250mg-1g,Taila=7-15drops)",
    "uses": [
        "Digestive aid",
        "Carminative properties",
        "Mild sedative effects",
        "Traditionally used for culinary and medicinal purposes"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Myristica+fragrans'
   },
   "sweta_jiraka": {
    "english_name": "White Cumin Seeds",
    "tamil_name": "à®µà¯†à®³à¯à®³à¯ˆ à®œà¯€à®°à®•à®®à¯",
    "sanskrit_name": "à¤œà¥€à¤°à¤• (à¤¦à¥€à¤ªà¤¨)",
    "botanical_name": "Cuminum cyminum",
    "family_name": "Apiaceae",
    "chemical_composition": "Cuminaldehyde, Cumic acid, Essential oils",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Carminative, Appetizer",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Digestive aid",
        "Carminative properties",
        "Appetizer",
        "Traditionally used for culinary and medicinal purposes"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Carum+carvi'
   },
   "Krsna Jiraka302": {
    "english_name": "Black Seed",
    "tamil_name": "à®•à®°à¯à®žà¯à®šà¯€à®°à®•à®®à¯",
    "sanskrit_name": "Kalonji",
    "botanical_name": "Nigella sativa",
    "family_name": "Ranunculaceae",
    "chemical_composition": "Thymoquinone, Nigellone, Essential oils",
    "rasa": "Bitter, Pungent",
    "guna": "Light, Dry",
    "virya": "Heating",
    "vipaka": "Pungent",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Antioxidant, Immune support",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Anti-inflammatory effects",
        "Antioxidant properties",
        "Immune support",
        "Traditionally used for culinary and medicinal purposes"
    ],
    "image_url":'https://www.flickr.com/search/?text=BLACK%20CARAWAY'
   },
   "jyotismati": {
    "english_name": "Malkangani",
    "tamil_name": "à®•à¯à®µà®°à®¿à®•à¯à®£à¯à®Ÿà®²à¯",
    "sanskrit_name": "Jyotismati",
    "botanical_name": "Celastrus paniculatus",
    "family_name": "Celastraceae",
    "chemical_composition": "Sesquiterpenes, Triterpenes, Alkaloids",
    "rasa": "Tikta, Kkasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Ssita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Nervine tonic, Memory enhancer, Anti-anxiety",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Nervine tonic properties",
        "Memory enhancement",
        "Anti-anxiety effects",
        "Traditionally used for cognitive health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Celastrus+paniculatus'
   },
   "kalamegha": {
    "english_name": "Andrographis",
    "tamil_name": "à®¨à®¿à®²à®µà¯‡à®®à¯à®ªà¯",
    "sanskrit_name": "à¤•à¤¾à¤²à¤®à¥‡à¤˜/à¤­à¥‚à¤¨à¤¿à¤®à¥à¤¬ (à¤¯à¤•à¥„à¤¤à¥à¤¯)",
    "botanical_name": "Andrographis paniculata",
    "family_name": "Acanthaceae",
    "chemical_composition": "Andrographolide, Diterpenes, Flavonoids",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Immune support, Antipyretic, Liver support",
    "dose": "As directed by an Ayurvedic practitioner (Curna=1-3g,Swarasa=5-10ml,Kwatha=20-40ml)",
    "uses": [
        "Immune support",
        "Antipyretic effects",
        "Liver support",
        "Traditionally used for respiratory and immune health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Andrographis+paniculata'
   },
   "Kampilaka": {
    "english_name": "Orange Kamala",
    "tamil_name": "à®•à®®à®²à®¾",
    "sanskrit_name": "à¤•à¤®à¥à¤ªà¤¿à¤²à¤•  (à¤•à¥„à¤®à¤¿à¤˜à¥à¤¨)",
    "botanical_name": "Mallotus philippinensis",
    "family_name": "Euphorbiaceae",
    "chemical_composition": "Tannins, Flavonoids, Resins",
    "rasa": "Tikta, Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Anthelmintic, Astringent, Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (varies with the form of preparation)",
    "uses": [
        "Anthelmintic properties",
        "Astringent effects",
        "Wound healing",
        "Traditionally used for various health conditions"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Mallotus+philippinensis'
   },
   "kanchanara": {
    "english_name": "Bauhinia",
    "tamil_name": "à®šà¯†à®®à¯à®®à®¨à¯à®¤à®¾à®°à¯ˆ",
    "sanskrit_name": "à¤•à¤¾à¤žà¥à¤šà¤¨à¤¾à¤°  (à¤—à¤£à¥à¤¡à¤®à¤¾à¤²à¤¾à¤¨à¤¾à¤¶à¤¨)",
    "botanical_name": "Bauhinia variegata",
    "family_name": "Fabaceae",
    "chemical_composition": "Flavonoids, Tannins, Sterols",
    "rasa": "Kasaya, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Lymphatic support, Anti-inflammatory, Antioxidant",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=40-80ml,Curna=3-6g,Puspa rasa=10-20ml)",
    "uses": [
        "Lymphatic support",
        "Anti-inflammatory effects",
        "Antioxidant properties",
        "Traditionally used for supporting the lymphatic system"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Bauhinia'
   },
   "kantakari": {
    "english_name": "Yellow Berried Nightshade",
    "tamil_name": "à®•à®£à¯à®Ÿà®™à¯à®•à®¤à¯à®¤à®¿à®°à®¿",
    "sanskrit_name": "à¤•à¤£à¥à¤Ÿà¤•à¤¾à¤°à¥€  (à¤•à¤¾à¤¸à¤¹à¤°)",
    "botanical_name": "Solanum xanthocarpum",
    "family_name": "Solanaceae",
    "chemical_composition": "Alkaloids, Steroidal glycosides, Flavonoids",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Expectorant, Anti-asthmatic, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner (Kwatha=50-100ml,Curna=1-2g)",
    "uses": [
        "Expectorant properties",
        "Anti-asthmatic effects",
        "Anti-inflammatory benefits",
        "Traditionally used for respiratory health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Solanum+surattense'
   },
   "kapikachu": {
    "english_name": "Velvet Bean",
    "tamil_name": "à®ªà¯‚à®©à¯ˆà®•à¯à®•à®¾à®²à®¿",
    "sanskrit_name": "à¤•à¤ªà¤¿à¤•à¤šà¥à¤›à¥  (à¤µà¥„à¤·à¥à¤¯)",
    "botanical_name": "Mucuna pruriens",
    "family_name": "Fabaceae",
    "chemical_composition": "L-DOPA, Alkaloids, Flavonoids",
    "rasa": "Madhura, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Aphrodisiac, Nervine tonic, Antioxidant",
    "dose": "As directed by an Ayurvedic practitioner (Curna=3-6g)",
    "uses": [
        "Aphrodisiac properties",
        "Nervine tonic effects",
        "Antioxidant benefits",
        "Traditionally used for reproductive health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Mucuna+prurita'
   },
   "Karkatashringi": {
    "english_name": "Karkatashringi",
    "tamil_name": "à®•à®¾à®°à¯à®•à®¾à®Ÿà®šà¯à®°à®¿à®™à¯à®•à®¿",
    "sanskrit_name": "à¤•à¤°à¥à¤•à¤Ÿà¥à¤¶à¥à¤°à¤‚à¤—à¥€  (à¤•à¤¾à¤¸à¤¹à¤°)",
    "botanical_name": "Pistacia integerrima",
    "family_name": "Anacardiaceae",
    "chemical_composition": "Tannins, Flavonoids, Resins",
    "rasa": "Kasaya, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Anti-inflammatory, Antioxidant",
    "dose": "As directed by an Ayurvedic practitioner (Curna=1-3g)",
    "uses": [
        "Digestive aid",
        "Anti-inflammatory effects",
        "Antioxidant properties",
        "Traditionally used for gastrointestinal health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Pistacia+integerrima'
   },
   "karpura": {
    "english_name": "Camphor",
    "tamil_name": "à®•à®±à¯à®ªà¯‚à®°à®®à¯",
    "sanskrit_name": "Karpura",
    "botanical_name": "Cinnamomum camphora",
    "family_name": "Lauraceae",
    "chemical_composition": "Camphor",
    "rasa": "Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Nervine tonic, Respiratory support, Antispasmodic",
    "dose": "As directed by an Ayurvedic practitioner (for external use only-0.25-0.5g)",
    "uses": [
        "Nervine tonic",
        "Respiratory support",
        "Antispasmodic effects",
        "Traditionally used for various external applications"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Cinnamomum+camphora'
   },
   "katuki": {
    "english_name": "Katuki",
    "tamil_name": "à®•à®Ÿà¯ à®°à¯‹à®•à®¿à®£à®¿",
    "sanskrit_name": "à¤•à¤Ÿà¥à¤•à¤¾  (à¤ªà¤¿à¤¤à¥à¤¤à¤µà¤¿à¤°à¥‡à¤šà¤¨)",
    "botanical_name": "Picrorhiza kurroa",
    "family_name": "Scrophulariaceae",
    "chemical_composition": "Kutkoside, Picrorhizin, Apocynin",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Liver tonic, Digestive stimulant, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner(for Virecana=3-6g)",
    "uses": [
        "Liver tonic",
        "Digestive stimulant",
        "Anti-inflammatory effects",
        "Traditionally used for liver health and digestion"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Picrorhiza+kurroa'
   },
   "khadira": {
    "english_name": "Cutch Tree",
    "tamil_name": "à®šà¯†à®™à¯à®•à®°à¯à®™à¯à®•à®¾à®²à®¿",
    "sanskrit_name": "à¤–à¤¦à¤¿à¤°  (à¤•à¥à¤·à¥à¤ à¤˜à¥à¤¨)",
    "botanical_name": "Acacia catechu",
    "family_name": "Fabaceae",
    "chemical_composition": "Catechins, Quercetin, Tannins",
    "rasa": "Kasaya, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Astringent, Antimicrobial, Dental health",
    "dose": "As directed by an Ayurvedic practitioner(Kwatha=40-60ml)",
    "uses": [
        "Astringent properties",
        "Antimicrobial effects",
        "Dental health",
        "Traditionally used for oral care and skin health"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Acacia+catechu'
   },
   "kiratatikta": {
    "english_name": "Chirata",
    "tamil_name": "à®¨à®¿à®²à®µà¯‡à®®à¯à®ªà¯",
    "sanskrit_name": "à¤•à¤¿à¤°à¤¾à¤¤à¤¤à¤¿à¤•à¥à¤¤  (à¤œà¥à¤µà¤°à¤˜à¥à¤¨ ) ",
    "botanical_name": "Swertia chirata",
    "family_name": "Gentianaceae",
    "chemical_composition": "Bitter principles, Xanthones",
    "rasa": "Tikta",
    "guna": "laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Liver support, Digestive stimulant, Antipyretic",
    "dose": "As directed by an Ayurvedic practitioner(Curna=2-6g,Kwatha=50-100ml)",
    "uses": [
        "Liver support",
        "Digestive stimulant",
        "Antipyretic effects",
        "Traditionally used for liver disorders and fevers"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Swertia+chirayata'
   },
   "kumari": {
    "english_name": "Aloe Vera",
    "tamil_name": "à®•à®±à¯à®±à®¾à®²à¯ˆ",
    "sanskrit_name": "à¤•à¥à¤®à¤¾à¤°à¥€  (à¤ªà¤¿à¤¤à¥à¤¤à¤µà¤¿à¤°à¥‡à¤šà¤¨)",
    "botanical_name": "Aloe Vera)",
    "family_name": "Asphodelaceae",
    "chemical_composition": "Polysaccharides, Anthraquinones, Amino acids",
    "rasa": "Tikta, Madhura",
    "guna": "Laghu, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta dosha, may increase Vata and decrease Kapha in excess",
    "prayoga": "Skin care, Digestive aid, Wound healing",
    "dose": "As directed by an Ayurvedic practitioner (Curna=2-6g,Kwatha=50-100ml)",
    "uses": [
        "Skin care",
        "Digestive aid",
        "Wound healing",
        "Traditionally used for various skin and digestive issues"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Aloe+vera'
   },
   "kupilu": {
    "english_name": "Nux Vomica",
    "tamil_name": "à®Žà®Ÿà¯à®Ÿà®¿ à®®à®°à®®à¯",
    "sanskrit_name": "à¤•à¥à¤ªà¥€à¤²à¥‚  (à¤†à¤•à¥à¤·à¥‡à¤ªà¤œà¤¨à¤¨)",
    "botanical_name": "Strychnos nux-vomica",
    "family_name": "Loganiaceae",
    "chemical_composition": "Strychnine, Brucine, Alkaloids",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Nervine tonic, Digestive stimulant (in small doses), Traditional medicine",
    "dose": "As directed by an Ayurvedic practitioner (toxic in high doses)",
    "uses": [
        "Nervine tonic",
        "Digestive stimulant (in small doses)",
        "Traditionally used in specific Ayurvedic formulations",
        "Caution: Toxic in high doses"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Strychnos+nux-vomica'
   },
   "kunkuma": {
    "english_name": "Saffron",
    "tamil_name": "à®•à¯à®™à¯à®•à¯à®®à®ªà¯à®ªà¯‚",
    "sanskrit_name": "à¤•à¤‚à¤•à¥à¤®  (à¤µà¤°à¥à¤£à¥à¤¯)",
    "botanical_name": "Crocus sativus",
    "family_name": "Iridaceae",
    "chemical_composition": "Crocin, Crocetin, Picrocrocin",
    "rasa": "Tikta, Katu, Madhura",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
    "prayoga": "Antioxidant, Mood enhancer, Menstrual regulator",
    "dose": "As directed by an Ayurvedic practitioner(curna=125-500mg)",
    "uses": [
        "Antioxidant properties",
        "Mood enhancer",
        "Menstrual regulator",
        "Traditionally used for various health and culinary purposes"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Crocus+sativus'
   },
   "saussurea_lappa": {
    "english_name": "Costus",
    "tamil_name": "à®•à¯à®¤à¯",
    "sanskrit_name": "Kustha",
    "botanical_name": "Saussurea lappa",
    "family_name": "Asteraceae",
    "chemical_composition": "Sesquiterpene lactones, Essential oil",
    "rasa": "Tikta, Katu",
    "guna": "Guru, Snigdha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Digestive stimulant, Skin conditions",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Anti-inflammatory effects",
        "Digestive stimulant",
        "Used in Ayurvedic formulations for skin conditions",
        "Traditionally used for various health purposes"
    ],
    "image_url":'https://www.flickr.com/search/?text=Saussurea%20lappa'
   },
   "kutaja": {
    "english_name": "Kutaja",
    "tamil_name": "à®•à®¿à®°à®¿à®®à®²à¯à®²à®¿à®•à¯ˆ",
    "sanskrit_name": ". à¤•à¥à¤Ÿà¤œ  (à¤‰à¤ªà¤¶à¥‹à¤·à¤•)",
    "botanical_name": "Holarrhena antidysenterica",
    "family_name": "Apocynaceae",
    "chemical_composition": "Alkaloids, Conessine, Holarrhimine",
    "rasa": "Tikta, Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Antidiarrheal, Antimicrobial, Digestive stimulant",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Antidiarrheal properties",
        "Antimicrobial effects",
        "Digestive stimulant",
        "Traditionally used for gastrointestinal issues"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Holarrhena+antidysenterica'
   },
   "lavanaga": {
    "english_name": "Lavanaga",
    "tamil_name": "à®²à®µà®™à¯à®•à®®à¯",
    "sanskrit_name": "à¤²à¤µà¤‚à¤—  (à¤›à¥‡à¤¦à¤¨)",
    "botanical_name": "Syzygium aromaticum",
    "family_name": "Myrtaceae",
    "chemical_composition": "Eugenol, Caryophyllene, Acetyleugenol",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Anti-inflammatory, Antioxidant",
    "dose": "As directed by an Ayurvedic practitioner(Curna=250mg-1g,Taila=4-6drops)",
    "uses": [
        "Digestive aid",
        "Anti-inflammatory effects",
        "Antioxidant properties",
        "Traditionally used for various health and culinary purposes"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Syzygium+aromaticum'
   },
   "lodhra": {
    "english_name": "Lodhra",
    "tamil_name": "à®µà¯†à®³à¯à®³à®¿à®²à®¾à®¤à®¿ à®®à®°à®®à¯",
    "sanskrit_name": "à¤²à¥‹à¤§à¥à¤°  (à¤†à¤°à¥à¤¤à¤µà¤¸à¤‚à¤—à¥à¤°à¤¹à¤£à¥€à¤¯)",
    "botanical_name": "Symplocos racemosa",
    "family_name": "Symplocaceae",
    "chemical_composition": "Flavonoids, Tannins, Alkaloids",
    "rasa": "Kasaya, Tikta",
    "guna": "Guru, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Astringent, Anti-inflammatory, Female reproductive tonic",
    "dose": "As directed by an Ayurvedic practitioner(Kwatha=50-100ml,Curna=1-2g)",
    "uses": [
        "Astringent properties",
        "Anti-inflammatory effects",
        "Female reproductive tonic",
        "Traditionally used for gynecological health"
    ],
    "image_url":'https://www.flickr.com/search/?w=all&q=Symplocos+sp.&m=text'
   },
   "madanaphala": {
    "english_name": "Madanaphala",
    "tamil_name": "à®®à®¤à¯à®•à¯à®•à®°à¯ˆ",
    "sanskrit_name": "à¤®à¤¦à¤¨à¤«à¤²  (à¤µà¤®à¤¨)",
    "botanical_name": "Randia dumetorum",
    "family_name": "Rubiaceae",
    "chemical_composition": "Alkaloids, Triterpenes, Flavonoids",
    "rasa": "Tikta, Kasaya",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Antipyretic, Anti-inflammatory, Analgesic",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Antipyretic properties",
        "Anti-inflammatory effects",
        "Analgesic benefits",
        "Traditionally used for various health purposes"
    ],
    "image_url":'https://www.flickr.com/search/show/?q=Randia+Spinosa'
   },
   "manjistha": {
    "english_name": "Manjistha",
    "tamil_name": "à®®à®žà¯à®šà®¿à®Ÿà¯à®Ÿà®¿",
    "sanskrit_name": "à¤®à¤‚à¤œà¤¿à¤·à¥à¤ à¤¾ (à¤°à¤•à¥à¤¤à¤ªà¥à¤°à¤¸à¤¾à¤§à¤¨)",
    "botanical_name": "Rubia cordifolia",
    "family_name": "Rubiaceae",
    "chemical_composition": "Alizarin, Purpurin, Munjistin",
    "rasa": "Kasaya, Tikta, Madhura",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Blood purifier, Anti-inflammatory, Skin health",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Blood purifier",
        "Anti-inflammatory effects",
        "Skin health",
        "Traditionally used for various skin conditions"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Rubia+cordifolia'
   },
   "maricha": {
    "english_name": "Maricha",
    "tamil_name": "à®®à®¿à®³à®•à¯",
    "sanskrit_name": "à¤®à¤°à¤¿à¤š  (à¤¦à¥€à¤ªà¤¨)",
    "botanical_name": "Piper nigrum",
    "family_name": "Piperaceae",
    "chemical_composition": "Piperine, Essential oil",
    "rasa": "Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Respiratory support, Analgesic",
    "dose": "As directed by an Ayurvedic practitioner(Curna=500mg-1g)",
    "uses": [
        "Digestive aid",
        "Respiratory support",
        "Analgesic effects",
        "Traditionally used for various health and culinary purposes"
    ],
    "image_url": 'http://www.flickr.com/search/show/?q=Piper+nigrum'
   },
   "musta": {
    "english_name": "Musta",
    "tamil_name": "à®•à¯‹à®°à¯ˆ à®•à®¿à®´à®™à¯à®•à¯",
    "sanskrit_name": "à¤®à¥à¤¸à¥à¤¤à¤•  (à¤¦à¥€à¤ªà¤¨)",
    "botanical_name": "Cyperus rotundus",
    "family_name": "Cyperaceae",
    "chemical_composition": "Mustakol, Cyperene, Cyperol",
    "rasa": "Tikta, Kasaya",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Digestive aid, Anti-inflammatory, Diuretic",
    "dose": "As directed by an Ayurvedic practitioner(Curna=1-3g,Kwatha=50-100ml)",
    "uses": [
        "Digestive aid",
        "Anti-inflammatory effects",
        "Diuretic properties",
        "Traditionally used for digestive and urinary health"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Cyperus+rotundus'
   },
   "nagakesara": {
    "english_name": "Nagakesara",
    "tamil_name": "à®šà®¿à®±à¯à®¨à®¾à®•à®ªà¯à®ªà¯‚",
    "sanskrit_name": "à¤¨à¤¾à¤—à¤•à¥‡à¤¶à¤°  (à¤°à¤•à¥à¤¤à¤¸à¥à¤¤à¤®à¥à¤­à¤¨)",
    "botanical_name": "Mesua ferrea",
    "family_name": "Clusiaceae",
    "chemical_composition": "Flavonoids, Essential oil, Tannins",
    "rasa": "Kasaya, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Astringent, Cardioprotective, Menstrual support",
    "dose": "As directed by an Ayurvedic practitioner(Curna=0.5-2g)",
    "uses": [
        "Astringent properties",
        "Cardioprotective effects",
        "Menstrual support",
        "Traditionally used for various health purposes"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Mesua+ferrea'
   },
   "nimba": {
    "english_name": "Nimba",
    "tamil_name": "à®µà¯‡à®®à¯à®ªà¯",
    "sanskrit_name": "à¤¨à¤¿à¤®à¥à¤¬  (à¤•à¤£à¥à¤¡à¥‚à¤˜à¥à¤¨)",
    "botanical_name": "Azadirachta indica",
    "family_name": "Meliaceae",
    "chemical_composition": "Azadirachtin, Nimbin, Quercetin",
    "rasa": "Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Antimicrobial, Antioxidant, Blood purifier",
    "dose": "As directed by an Ayurvedic practitioner(Swarasa=10-20ml,Kalka=10-20g,Curna=2-4g,Taila=5-10drops)",
    "uses": [
        "Antimicrobial effects",
        "Antioxidant properties",
        "Blood purifier",
        "Traditionally used for skin and blood disorders"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Azadiracta+indica'
   },
   "nirgundi": {
    "english_name": "Nirgundi",
    "tamil_name": "à®¨à¯Šà®šà¯à®šà®¿",
    "sanskrit_name": "à¤¨à¤¿à¤°à¥à¤—à¥à¤£à¥à¤¡à¥€  (à¤µà¥‡à¤¦à¤¨à¤¾à¤¸à¥à¤¥à¤¾à¤ªà¤¨)",
    "botanical_name": "Vitex negundo",
    "family_name": "Lamiaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Essential oil",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Analgesic, Antispasmodic",
    "dose": "As directed by an Ayurvedic practitioner(Mula Curna=1-3g,Sswarasa=10-20ml,Kwatha=40-50ml)",
    "uses": [
        "Anti-inflammatory effects",
        "Analgesic properties",
        "Antispasmodic effects",
        "Traditionally used for joint and muscle disorders"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=nirgundi'
   },
   "palasa": {
    "english_name": "Palasa",
    "tamil_name": "à®ªà¯à®°à®šà¯",
    "sanskrit_name": "Palasa",
    "botanical_name": "Butea monosperma",
    "family_name": "Fabaceae",
    "chemical_composition": "Flavonoids, Tannins, Alkaloids",
    "rasa": "Astringent, Bitter",
    "guna": "Heavy, Dry",
    "virya": "Heating",
    "vipaka": "Pungent",
    "amayoga": "Balances Kapha and Pitta doshas, may increase Vata in excess",
    "prayoga": "Astringent, Anti-inflammatory, Antimicrobial",
    "dose": "As directed by an Ayurvedic practitioner(Bija Curna=1-8g,Kwatha=50-100ml",
    "uses": [
        "Astringent properties",
        "Anti-inflammatory effects",
        "Antimicrobial benefits",
        "Traditionally used for various health purposes"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Butea+monosperma&z=m'
   },
   "patola": {
    "english_name": "Patola",
    "tamil_name": "à®•à®®à¯à®ªà¯à®ªà¯à®Ÿà®²à¯ˆ",
    "sanskrit_name": "à¤ªà¤¾à¤Ÿà¤²à¤¾	(à¤¶à¥‹à¤¥à¤¹à¤°)",
    "botanical_name": "Trichosanthes dioica",
    "family_name": "Cucurbitaceae",
    "chemical_composition": "Lectins, Triterpenoids, Sterols",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Antipyretic, Antidiabetic, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Antipyretic effects",
        "Antidiabetic properties",
        "Anti-inflammatory benefits",
        "Traditionally used for various health purposes"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Butea+monosperma&z=m'
   },
   "pipali": {
    "english_name": "Pipali",
    "tamil_name": "à®®à®¿à®³à®•à¯",
    "sanskrit_name": "à¤ªà¤¿à¤ªà¥à¤ªà¤²à¥€  (à¤•à¤¾à¤¸à¤¹à¤°)",
    "botanical_name": "Piper longum",
    "family_name": "Piperaceae",
    "chemical_composition": "Piperine, Essential oil",
    "rasa": "Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Respiratory support, Analgesic",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Digestive aid",
        "Respiratory support",
        "Analgesic effects",
        "Traditionally used for various health and culinary purposes"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Piper+longum'
   },
   "punarnava": {
    "english_name": "Punarnava",
    "tamil_name": "à®®à¯‚à®•à¯à®•à®°à®Ÿà¯à®Ÿà®¿ à®šà®¾à®°à¯ˆ à®…à®²à¯à®²à®¤à¯ à®®à¯‚à®•à¯à®•à®¿à®°à®Ÿà¯à®Ÿà¯ˆ",
    "sanskrit_name": "Punarnava",
    "botanical_name": "Boerhavia diffusa",
    "family_name": "Nyctaginaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Sterols",
    "rasa": "Tikta, Madhura",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Diuretic, Anti-inflammatory, Liver support",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Diuretic properties",
        "Anti-inflammatory effects",
        "Liver support",
        "Traditionally used for urinary and liver disorders"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Boerhavia+diffusa'
   },
   "pashana_bheda": {
    "english_name": "Pashana Bheda",
    "tamil_name": "à®ªà®¾à®·à®¾à®£ à®ªà¯‡à®Ÿà®¾",
    "sanskrit_name": "Pashana Bheda",
    "botanical_name": "Bergenia ciliata",
    "family_name": "Saxifragaceae",
    "chemical_composition": "Tannins, Flavonoids, Resins",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Diuretic, Lithotriptic, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Diuretic properties",
        "Lithotriptic effects",
        "Anti-inflammatory benefits",
        "Traditionally used for urinary disorders"
    ],
    "image_url": 'https://www.flickr.com/search/?text=Bergenia%20ciliata'
   },
   "rasna": {
    "english_name": "Rasna",
    "tamil_name": "à®ªà¯‡à®°à®°à®¤à¯à®¤à¯ˆ",
    "sanskrit_name": "Rasna",
    "botanical_name": "Alpinia galanga",
    "family_name": "Zingiberaceae",
    "chemical_composition": "Essential oil, Galangin, Alpinin",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Analgesic, Muscle relaxant",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Anti-inflammatory effects",
        "Analgesic properties",
        "Muscle relaxant",
        "Traditionally used for joint and muscle disorders"
    ],
    "image_url": 'http://www.flowersofindia.in/catalog/slides/Rasna.html'
   },
   "rasona": {
    "english_name": "Rasona",
    "tamil_name": "à®‰à®³à®¿à®°à¯à®•à®¿à®´à®™à¯à®•à¯",
    "sanskrit_name": "Rasona",
    "botanical_name": "Allium sativum",
    "family_name": "Amaryllidaceae",
    "chemical_composition": "Allicin, Alliin, Saponins",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Snigdha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Antimicrobial, Cardiovascular support, Immune enhancer",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Antimicrobial effects",
        "Cardiovascular support",
        "Immune enhancer",
        "Traditionally used for various health and culinary purposes"
    ],
    "image_url": 'https://www.flickr.com/search/show/?q=Allium+sativum'
   },
   "saireyaka": {
    "english_name": "Saireyaka",
    "tamil_name": "Not available",
    "sanskrit_name": "à¤¸à¥ˆà¤°à¥‡à¤¯à¤•  (à¤•à¥à¤·à¥à¤ à¤˜à¥à¤¨)",
    "botanical_name": "Barleria prionitis",
    "family_name": "Acanthaceae",
    "chemical_composition": "Not well-documented",
    "rasa": "Katu, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Not well-documented",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Not well-documented"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Barleria+prionitis"
    },
    "salaki": {
    "english_name": "Salaki",
    "tamil_name": "Not available",
    "sanskrit_name": "à¤¶à¤²à¥à¤²à¤•à¥€  (à¤ªà¥à¤°à¥€à¤·à¤µà¤¿à¤°à¤œà¤¨à¥€à¤¯)",
    "botanical_name": "Boswellia serrata",
    "family_name": "Burseraceae",
    "chemical_composition": "Boswellic acids, Terpenoids",
    "rasa": "Tikta, Kashaya",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Analgesic, Joint support",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Anti-inflammatory effects",
      "Analgesic properties",
      "Joint support",
      "Traditionally used for various health purposes"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Boswellia+serrata&z=m"
  },
  "sariva": {
    "english_name": "Sariva",
    "tamil_name": "à®¨à®©à¯à®©à®¾à®°à®¿",
    "sanskrit_name": "à¤¸à¤¾à¤°à¤¿à¤µà¤¾  (à¤°à¤•à¥à¤¤à¤ªà¥à¤°à¤¸à¤¾à¤§à¤¨) s",
    "botanical_name": "Hemidesmus indicus",
    "family_name": "Apocynaceae",
    "chemical_composition": "Hemidesmin, Coumarins, Flavonoids",
    "rasa": "Tikta, Madhura",
    "guna": "Laghu, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Blood purifier, Anti-inflammatory, Cooling",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Blood purifier",
      "Anti-inflammatory effects",
      "Cooling properties",
      "Traditionally used for skin and blood disorders"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Hemidesmus+indicus"
  },
  "sarpagandha": {
    "english_name": "Sarpagandha",
    "tamil_name": "à®šà®°à¯à®ªà®•à®¾à®¨à¯à®¤à®¾ or à®ªà®¾à®®à¯à®ªà¯ à®•à®²à®¾, à®šà®¿à®µà®©à¯ à®…à®®à®²à¯ à®ªà¯Šà®Ÿà®¿ ",
    "sanskrit_name": "à¤¸à¤°à¥à¤ªà¤—à¤‚à¤§à¤¾  (à¤¨à¤¿à¤¦à¥à¤°à¤¾à¤œà¤¨à¤¨)",
    "botanical_name": "Rauwolfia serpentina",
    "family_name": "Apocynaceae",
    "chemical_composition": "Reserpine, Alkaloids, Tannins",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Hypotensive, Sedative, Calming",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Hypotensive effects",
      "Sedative properties",
      "Calming effects",
      "Traditionally used for hypertension and anxiety"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Rauwolfia+serpentina"
  },
  "salaparani": {
    "english_name": "Salaparani",
    "tamil_name": "à®šà®¾à®²à®¾à®ªà®°à®£à®¿",
    "sanskrit_name": "à¤¶à¤¾à¤²à¤ªà¤°à¥à¤£à¥€  (à¤…à¤‚à¤—à¤®à¤°à¥à¤¦ à¤ªà¥à¤°à¤¶à¤®à¤¨) ",
    "botanical_name": "Desmodium gangeticum",
    "family_name": "Fabaceae",
    "chemical_composition": "Alkaloids, Flavonoids, Triterpenoids",
    "rasa": "Kashaya, Tikta",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Antispasmodic, Respiratory support",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Anti-inflammatory effects",
      "Antispasmodic properties",
      "Respiratory support",
      "Traditionally used for respiratory disorders"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Desmodium+gangeticum"
  },
  "salmali": {
    "english_name": "Salmali",
    "tamil_name": "à®®à¯à®³à¯à®³à®¿à®²à®µà¯",
    "sanskrit_name": "à¤¶à¤¾à¤²à¥à¤®à¤²à¥€  (à¤ªà¥à¤°à¥€à¤·à¤µà¤¿à¤°à¤œà¤¨à¥€à¤¯)",
    "botanical_name": "Salmalia malabarica",
    "family_name": "Malvaceae",
    "chemical_composition": "Not well-documented",
    "rasa": "Madhura, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Vata doshas, may increase Kapha in excess",
    "prayoga": "Not well-documented",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Not well-documented"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Salmalia+malabarica"
  },
  "sankapuspi": {
    "english_name": "Sankapuspi",
    "tamil_name": "Not available",
    "sanskrit_name": "à¤¶à¤‚à¤–à¤ªà¥à¤·à¥à¤ªà¥€  (à¤®à¥‡à¤§à¥à¤¯)",
    "botanical_name": "Not available",
    "family_name": "Not available",
    "chemical_composition": "Not well-documented",
    "rasa": "Tikta, Madhura",
    "guna": "Laghu, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Vata doshas, may increase Kapha in excess",
    "prayoga": "Not well-documented",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Not well-documented"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=shankhapushpi"
  },
  "shatavari": {
    "english_name": "Shatavari",
    "tamil_name": "à®šà®¤à®¾à®µà®°à®¿",
    "sanskrit_name": "à¤¶à¤¤à¤¾à¤µà¤°à¥€  (à¤µà¥„à¤·à¥à¤¯) ",
    "botanical_name": "Asparagus racemosus",
    "family_name": "Asparagaceae",
    "chemical_composition": "Saponins, Alkaloids, Tannins",
    "rasa": "Madhura",
    "guna": "Snigdha, Guru",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Pitta and Vata doshas, may increase Kapha in excess",
    "prayoga": "Rejuvenative, Female reproductive tonic, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Rejuvenative effects",
      "Female reproductive tonic",
      "Anti-inflammatory benefits",
      "Traditionally used for women's health"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Asparagus+racemosus"
  },
  "sigaru": {
    "english_name": "Sigaru",
    "tamil_name": "Not available",
    "sanskrit_name": "Sigaru",
    "botanical_name": "Not available",
    "family_name": "Not available",
    "chemical_composition": "Not well-documented",
    "rasa": "Not well-documented",
    "guna": "Not well-documented",
    "virya": "Not well-documented",
    "vipaka": "Not well-documented",
    "amayoga": "Not well-documented",
    "prayoga": "Not well-documented",
    "dose": "Not well-documented",
    "uses": [
      "Not well-documented"
    ],
    "image_url": "Not available"
  },
  "sirisa": {
    "english_name": "Sirisa",
    "tamil_name": "à®µà®¾à®•à¯ˆ",
    "sanskrit_name": "à¤¶à¤¿à¤°à¥€à¤·  (à¤µà¤¿à¤·à¤˜à¥à¤¨)",
    "botanical_name": "Albizzia lebbeck",
    "family_name": "Fabaceae",
    "chemical_composition": "Flavonoids, Alkaloids, Tannins",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Anti-inflammatory effects",
      "Antipyretic properties",
      "Respiratory support",
      "Traditionally used for respiratory disorders"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Albizzia+lebbeck"
  },
  "syonaka": {
    "english_name": "Syonaka",
    "tamil_name": "à®šà¯Šà®°à®¿à®•à¯Šà®©à¯à®±à¯ˆ",
    "sanskrit_name": "à¤¶à¥à¤¯à¥‹à¤¨à¤¾à¤•  (à¤‰à¤ªà¤¶à¥‹à¤·à¤•) ",
    "botanical_name": "Oroxylum indicum",
    "family_name": "Bignoniaceae",
    "chemical_composition": "Flavonoids, Alkaloids, Triterpenoids",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
      "Anti-inflammatory effects",
      "Antipyretic properties",
      "Respiratory support",
      "Traditionally used for respiratory disorders"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Oroxylum+indicum"
  },
  "tila": {
    "english_name": "Tila",
    "tamil_name": "à®Žà®³à¯",
    "sanskrit_name": "à¤¤à¤¿à¤²",
    "botanical_name": "Sesamum indicum",
    "family_name": "Pedaliaceae",
    "chemical_composition": "Sesamin, Sesamolin, Tocopherols",
    "rasa": "Madhura, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
    "prayoga": "Nutrient-rich, Cardiovascular support, Immune enhancer",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Nutrient-rich oil",
        "Cardiovascular support",
        "Immune enhancer",
        "Traditionally used in various culinary and medicinal applications"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Sesamum+indicum"
   },
   "trivrut": {
    "english_name": "Trivrut",
    "tamil_name": "à®¤à®¿à®°à®¿à®µà®¿à®°à¯à®¤à¯",
    "sanskrit_name": "à¤¤à¥à¤°à¤¿à¤µà¥ƒà¤¤à¥",
    "botanical_name": "Operculina turpethum",
    "family_name": "Convolvulaceae",
    "chemical_composition": "Resins, Turpethin",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Ushna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Laxative, Detoxifying, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Laxative effects",
        "Detoxifying properties",
        "Anti-inflammatory benefits",
        "Traditionally used for constipation and detoxification"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=indian+jalap"
   },
   "tulasi": {
    "english_name": "Tulasi",
    "tamil_name": "à®¤à¯à®³à®šà®¿",
    "sanskrit_name": "à¤¤à¥à¤²à¤¸à¥€",
    "botanical_name": "Ocimum sanctum",
    "family_name": "Lamiaceae",
    "chemical_composition": "Eugenol, Ursolic acid, Linalool",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Ushna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Adaptogen, Immunomodulator, Respiratory support",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Adaptogenic effects",
        "Immunomodulatory properties",
        "Respiratory support",
        "Traditionally used for various health and spiritual purposes"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Ocimum+sanctum"
   },
   "tvak": {
    "english_name": "Tvak",
    "tamil_name": "à®‡à®²à®µà®™à¯à®•à®ªà®¤à¯à®¤à®¿à®°à®¿",
    "sanskrit_name": "à¤¤à¥à¤µà¤•à¥",
    "botanical_name": "Cinnamomum zeylanicum",
    "family_name": "Lauraceae",
    "chemical_composition": "Cinnamaldehyde, Eugenol, Linalool",
    "rasa": "Madhura, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Antimicrobial, Aromatic",
    "dose": "1-3 grams per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Digestive aid",
        "Antimicrobial effects",
        "Aromatic properties",
        "Traditionally used for digestive and respiratory health"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Cinnamomum+zeylanicum"
   },
   "usira": {
    "english_name": "Usira",
    "tamil_name": "à®µà¯†à®Ÿà¯à®Ÿà®¿à®µà¯‡à®°à¯",
    "sanskrit_name": "à¤‰à¤¶à¥€à¤°",
    "botanical_name": "Vetiveria zizanioides",
    "family_name": "Poaceae",
    "chemical_composition": "Vetiverol, Khusimol, Alpha-vetivone",
    "rasa": "Tikta, Kashaya",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Cooling, Diuretic, Anti-inflammatory",
    "dose": "As directed by an Ayurvedic practitioner",
    "uses": [
        "Cooling effects",
        "Diuretic properties",
        "Anti-inflammatory benefits",
        "Traditionally used for cooling and soothing purposes"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Vetiveria+zizanioides"
   },
   "vaca": {
    "english_name": "Vaca",
    "tamil_name": "à®µà®šà®®à¯à®ªà¯",
    "sanskrit_name": "à¤µà¤šà¤¾",
    "botanical_name": "Acorus calamus",
    "family_name": "Acoraceae",
    "chemical_composition": "Asarone, Beta-asarone, Calamene",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Nervine tonic, Cognitive support, Respiratory aid",
    "dose": "250 mg to 500 mg per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Nervine tonic",
        "Cognitive support",
        "Respiratory aid",
        "Traditionally used for neurological and respiratory conditions"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Acorus+calamus"
   },
   "varuna": {
    "english_name": "Varuna",
    "tamil_name": "à®ªà®šà®£à®•à®©à¯à®©à®¿",
    "sanskrit_name": "à¤µà¤°à¥à¤£",
    "botanical_name": "Crataeva nurvala",
    "family_name": "Capparidaceae",
    "chemical_composition": "Lupeol, Quercetin, Kaempferol",
    "rasa": "Tikta, Kashaya",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Pitta and Kapha doshas, may increase Vata in excess",
    "prayoga": "Diuretic, Lithotriptic, Anti-inflammatory",
    "dose": "1-2 grams per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Diuretic effects",
        "Lithotriptic properties",
        "Anti-inflammatory benefits",
        "Traditionally used for urinary and kidney health"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Crataeva+nurvala"
   },
   "vaasa": {
    "english_name": "Vaasa",
    "tamil_name": "à®†à®Ÿà®¾à®¤à¯‹à®Ÿà¯ˆ",
    "sanskrit_name": "à¤†à¤¡à¥à¤•à¥‹à¤Ÿà¤¿",
    "botanical_name": "Adhatoda vasica",
    "family_name": "Acanthaceae",
    "chemical_composition": "Vasicine, Vasicinone, Alkaloids",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Sita",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Respiratory support, Expectorant, Anti-inflammatory",
    "dose": "3-6 grams per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Respiratory support",
        "Expectorant properties",
        "Anti-inflammatory benefits",
        "Traditionally used for respiratory health"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Adhatoda+vasica"
   },
   "vatsanabha": {
    "english_name": "Vatsanabha",
    "tamil_name": "à®µà®šà®¨à®¾à®ªà®¿",
    "sanskrit_name": "à¤µà¤¤à¥à¤¸à¤¨à¤¾à¤­",
    "botanical_name": "Aconitum ferox",
    "family_name": "Ranunculaceae",
    "chemical_composition": "Aconitine, Indicine, Alkaloids",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Nervine tonic, Anti-inflammatory, Analgesic",
    "dose": "30-100 mg in therapeutic formulations or as directed by an Ayurvedic practitioner",
    "uses": [
        "Nervine tonic",
        "Anti-inflammatory effects",
        "Analgesic properties",
        "Traditionally used for neurological and pain-related conditions"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Aconitum+ferox"
   },
   "vidari": {
    "english_name": "Vidari",
    "tamil_name": "à®µà®¿à®¤à®°à®¿à®•à®£à¯à®Ÿà¯",
    "sanskrit_name": "à¤µà¤¿à¤¦à¤¾à¤°à¥€",
    "botanical_name": "Pueraria tuberosa",
    "family_name": "Fabaceae",
    "chemical_composition": "Puerarin, Tuberosin, Isoflavonoids",
    "rasa": "Madhura, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Usna",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata dosha, may increase Pitta and Kapha in excess",
    "prayoga": "Rejuvenative, Aphrodisiac, Immune enhancer",
    "dose": "3-6 grams per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Rejuvenative effects",
        "Aphrodisiac properties",
        "Immune enhancer",
        "Traditionally used for vitality and reproductive health"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Pueraria+tuberosa"
   },
   "vidanga": {
    "english_name": "Vidanga",
    "tamil_name": "à®µà®¾à®¯à¯à®µà®¿à®²à®™à¯à®•à®®à¯",
    "sanskrit_name": "à¤µà¤¿à¤¡à¤‚à¤—",
    "botanical_name": "Embelia ribes",
    "family_name": "Myrsinaceae",
    "chemical_composition": "Quinones, Embelin, Volatile oil",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Anthelmintic, Anti-parasitic",
    "dose": "1-3 grams per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Digestive aid",
        "Anthelmintic properties",
        "Anti-parasitic effects",
        "Traditionally used for digestive and parasitic conditions"
    ],
    "image_url": "http://www.flickr.com/search/show/?q=Embelia+ribes"
   },
   "yastimadhu": {
    "english_name": "Yastimadhu",
    "tamil_name": "à®…à®¤à®¿à®®à®¤à¯à®°à®®à¯",
    "sanskrit_name": "à¤¯à¤·à¥à¤Ÿà¤¿à¤®à¤§à¥",
    "botanical_name": "Glycyrrhiza glabra",
    "family_name": "Fabaceae",
    "chemical_composition": "Glycyrrhizin, Flavonoids, Coumarins",
    "rasa": "Madhura, Tikta",
    "guna": "Guru, Snigdha",
    "virya": "Sita",
    "vipaka": "Madhura",
    "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
    "prayoga": "Anti-inflammatory, Demulcent, Respiratory support",
    "dose": "3-10 grams per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Anti-inflammatory effects",
        "Demulcent properties",
        "Respiratory support",
        "Traditionally used for various health purposes"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Glycyrrhiza+glabra"
   },
   "yavani": {
    "english_name": "Yavani",
    "tamil_name": "à®…à®œà¯à®µà¯ˆà®©à®¿",
    "sanskrit_name": "à¤¯à¤µà¤¾à¤¨à¥€",
    "botanical_name": "Trachyspermum ammi",
    "family_name": "Apiaceae",
    "chemical_composition": "Thymol, Carvacrol, Limonene",
    "rasa": "Tikta, Katu",
    "guna": "Laghu, Ruksha",
    "virya": "Usna",
    "vipaka": "Katu",
    "amayoga": "Balances Kapha and Vata doshas, may increase Pitta in excess",
    "prayoga": "Digestive aid, Carminative, Respiratory support",
    "dose": "1-3 grams per day or as directed by an Ayurvedic practitioner",
    "uses": [
        "Digestive aid",
        "Carminative properties",
        "Respiratory support",
        "Traditionally used for digestive and respiratory health"
    ],
    "image_url": "https://www.flickr.com/search/show/?q=Ajowan"
   },
}

# Ayurvedic patent and shastric medicine list
ayurvedic_medicines = {


    # Add more Ayurvedic patent and shastric medicines with details here
}

# Ayurvedic information about diseases
diseases_info = {
    "covid-19": {
        "explanation": "COVID-19 is a respiratory illness caused by the novel coronavirus SARS-CoV-2."
    },
    "diabetes": {
        "explanation": "Diabetes is a chronic condition that affects how your body processes glucose."
    },
    # Add more diseases with explanations here
}

#Ayurvedic Non Detailed Drugs List

non_detailed_drugs = {
    "agatsya": {
        "english_name": "Agatsya",
        "tamil_name": "à®…à®•à®¤à¯à®¤à®¿ à®šà¯†à®Ÿà®¿",
        "sanskrit_name": "à¤…à¤—à¤¤à¥à¤¸à¥à¤¯à¤¾",
        "botanical_name": "Agatsya plantensis",
        "family_name": "Herbaceae",
        "chemical_composition": "Agatsyacin, Agatsyol",
        "rasa": "Katu",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Digestive aid, Anti-inflammatory, Stress relief",
        "dose": "As prescribed by a qualified healthcare professional. Typically 250-500 mg per day."
    },
    "akarakarabha": {
        "english_name": "Akarakarabha",
        "tamil_name": "à®…à®•à¯à®•à®°à®¾à®•à®¾à®°à®®à¯",
        "sanskrit_name": "à¤…à¤•à¤°à¤•à¤°à¤­à¤¾",
        "botanical_name": "Anacyclus pyrethrum",
        "family_name": "Asteraceae",
        "chemical_composition": "Alkylamides, Pyrethrins",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Stimulant, Aphrodisiac, Anti-inflammatory",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "ajamoda": {
        "english_name": "Wild Celery",
        "tamil_name": "à®…à®šà®®à¯à®¤à®µà¯‹à®®à®®à¯",
        "sanskrit_name": "à¤…à¤œà¤®à¥‹à¤¦à¤¾",
        "botanical_name": "Trachyspermum roxburghianum",
        "family_name": "Apiaceae",
        "chemical_composition": "Thymol, P-Cymene",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Carminative, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 1-2 grams per day."
    },
    "amlavetasa": {
        "english_name": "Amlavetasa",
        "tamil_name": "à®†à®®à¯à®²à®µà¯‡à®¤à®¾à®šà®¾",
        "sanskrit_name": "à¤†à¤®à¥à¤²à¤µà¥‡à¤¤à¤¾à¤¸à¤¾",
        "botanical_name": "Garcinia pedunculata",
        "family_name": "Clusiaceae",
        "chemical_composition": "Hydroxycitric Acid (HCA), Xanthones",
        "rasa": "Amla, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Weight management, Digestive aid, Antioxidant",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "amra": {
        "english_name": "Mango",
        "tamil_name": "à®®à®¾à®®à®°à®®à¯",
        "sanskrit_name": "à¤†à¤®à¥à¤°à¤¾",
        "botanical_name": "Mangifera indica",
        "family_name": "Anacardiaceae",
        "chemical_composition": "Mangiferin, Polyphenols",
        "rasa": "Madhura, Amla",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Digestive aid, Antioxidant, Immunomodulator",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "ankola": {
        "english_name": "sage-leaved alangium",
        "tamil_name": "à®…à®´à®¿à®žà¯à®šà®¿à®²à¯",
        "sanskrit_name": "à¤…à¤™à¥à¤•à¥‹à¤²à¤¾",
        "botanical_name": "Alangium salvifolium",
        "family_name": "Alangiaceae",
        "chemical_composition": "Alkaloids, Triterpenoids",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Antipyretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "amragandhi_haridra": {
        "english_name": "Mango ginger",
        "tamil_name": "à®®à®¾à®™à¯à®•à®¾ à®‡à®žà¯à®šà®¿",
        "sanskrit_name": "à¤…à¤®à¥à¤°à¤—à¤¨à¥à¤§à¤¿ à¤¹à¤°à¤¿à¤¦à¥à¤°à¤¾",
        "botanical_name": "Curcuma amada",
        "family_name": "Zingiberaceae",
        "chemical_composition": "Curcumin, Essential oils",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Digestive aid, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "aparajita": {
        "english_name": "Butterfly pea",
        "tamil_name": "à®•à®¾à®•à¯à®•à®£à®¤à¯à®¤à®¿",
        "sanskrit_name": "à¤…à¤ªà¤°à¤¾à¤œà¤¿à¤¤à¤¾",
        "botanical_name": "Clitoria ternatea",
        "family_name": "Fabaceae",
        "chemical_composition": "Flavonoids, Alkaloids",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Adaptogen, Antioxidant, Memory enhancer",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "aswagola": {
        "english_name": "Aswagola",
        "tamil_name": "à®…à®šà¯à®µà®•à¯‹à®²à®¾",
        "sanskrit_name": "à¤…à¤¶à¥à¤µà¤—à¥‹à¤²à¤¾",
        "botanical_name": "Withania somnifera",
        "family_name": "Solanaceae",
        "chemical_composition": "Withanolides, Alkaloids",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Adaptogen, Immune modulator, Stress relief",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "aswattha": {
        "english_name": "Sacred Fig",
        "tamil_name": "à®…à®°à®š à®®à®°à®®à¯",
        "sanskrit_name": "à¤…à¤¶à¥à¤µà¤¤à¥à¤¥à¤¾",
        "botanical_name": "Ficus religiosa",
        "family_name": "Moraceae",
        "chemical_composition": "Flavonoids, Tannins",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Anti-inflammatory, Antioxidant, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "astisrunkhala": {
        "english_name": "Bone setter",
        "tamil_name": "à®ªà®¿à®°à®£à¯à®Ÿà¯ˆ",
        "sanskrit_name": "à¤…à¤¸à¥à¤¤à¤¿à¤¸à¥ƒà¤™à¥à¤–à¤²à¤¾",
        "botanical_name": "Cissus quadrangularis",
        "family_name": "Vitaceae",
        "chemical_composition": "Calcium, Phosphorus, Vitamins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Bone health, Anti-inflammatory, Analgesic",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "Atasi": {
        "english_name": "Flax",
        "tamil_name": "à®†à®³à®¿",
        "sanskrit_name": "à¤…à¤¤à¤¸à¥€",
        "botanical_name": "Linum usitatissimum",
        "family_name": "Linaceae",
        "chemical_composition": "Omega-3 fatty acids, Linoleic acid",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Cardiovascular health, Digestive aid, Skin health",
        "dose": "As prescribed by a qualified healthcare professional. Typically 1-2 teaspoons per day."
    },
    "Avartaki": {
        "english_name": "poison nut, seaman strychonus, and quaker buttons",
        "tamil_name": "à®Žà®Ÿà¯à®Ÿà®¿ à®®à®°à®®à¯",
        "sanskrit_name": "à¤…à¤µà¤°à¥à¤¤à¤•à¥€",
        "botanical_name": "Strychnos nux-vomica",
        "family_name": "Loganiaceae",
        "chemical_composition": "Strychnine, Brucine",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive stimulant, Nervine tonic, Antipyretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically 50-100 mg per day."
    },
    "Avartani": {
        "english_name": "Avaram Senna",
        "tamil_name": "à®†à®µà®¾à®°à¯ˆ",
        "sanskrit_name": "à¤…à¤µà¤°à¥à¤¤à¤¨à¥€",
        "botanical_name": "Cassia auriculata",
        "family_name": "Fabaceae",
        "chemical_composition": "Flavonoids, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Blood sugar regulation, Diuretic, Antioxidant",
        "dose": "As prescribed by a qualified healthcare professional. Typically 3-6 grams per day."
    },
    "babbula": {
        "english_name": "Babbula",
        "tamil_name": "à®•à®°à¯à®µà¯‡à®²à®®à¯",
        "sanskrit_name": "à¤¬à¤¬à¥à¤¬à¥‚à¤²à¤¾",
        "botanical_name": "Acacia arabica willd",
        "family_name": "Fabaceae",
        "chemical_composition": "Tannins, Alkaloids",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Oral health, Anti-inflammatory, Antidiarrheal",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "badara": {
        "english_name": "Chinese Date, Common Jujuba",
        "tamil_name": "à®‡à®²à®¨à¯à®¤à¯ˆ",
        "sanskrit_name": "à¤¬à¤¦à¤°à¤¾",
        "botanical_name": "Ziziphus jujuba",
        "family_name": "Rhamnaceae",
        "chemical_composition": "Flavonoids, Triterpenoids",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Digestive aid, Antioxidant, Stress relief",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "bakula": {
        "english_name": "Spanish cherry, medlar, and bullet wood",
        "tamil_name": "à®®à®•à®¿à®´à®®à¯à®ªà¯‚",
        "sanskrit_name": "à¤¬à¤•à¥à¤²à¤¾",
        "botanical_name": "Mimusops elengi",
        "family_name": "Sapotaceae",
        "chemical_composition": "Tannins, Alkaloids",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Dental care, Anti-inflammatory, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "bhumyamalaki": {
        "english_name": "gale of the wind",
        "tamil_name": "à®•à¯€à®´à®¾à®¨à¯†à®²à¯à®²à®¿",
        "sanskrit_name": "à¤­à¥‚à¤®à¥à¤¯à¤¾à¤®à¤²à¤¾à¤•à¥€",
        "botanical_name": "Phyllanthus niruri or Urinaria",
        "family_name": "Phyllanthaceae",
        "chemical_composition": "Phyllanthin, Hypophyllanthin",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Liver support, Antioxidant, Diuretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "bijapuraka": {
        "english_name": "Indian beech",
        "tamil_name": "à®ªà¯à®™à¯à®•à¯ˆ",
        "sanskrit_name": "à¤¬à¥€à¤œà¤¾à¤ªà¥‚à¤°à¤•à¤¾",
        "botanical_name": "Pongamia pinnata",
        "family_name": "Fabaceae",
        "chemical_composition": "Karanjin, Pongamol",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antimicrobial, Wound healing",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "bola": {
        "english_name": "Guggul",
        "tamil_name": "à®•à¯à®•à¯à®²à¯",
        "sanskrit_name": "à¤¬à¥‹à¤²à¤¾",
        "botanical_name": "Commiphora wightii",
        "family_name": "Burseraceae",
        "chemical_composition": "Guggulsterones, Resins",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Joint health, Cholesterol regulation, Anti-inflammatory",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "chakramarda": {
        "english_name": "Sickle Senna",
        "tamil_name": "à®¤à®•à®°à¯ˆ",
        "sanskrit_name": "à¤šà¤•à¥à¤°à¤®à¤°à¥à¤¦à¤¾",
        "botanical_name": "Cassia tora",
        "family_name": "Fabaceae",
        "chemical_composition": "Emodin, Anthraquinones",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Laxative, Antipyretic, Anti-inflammatory",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "champaka": {
        "english_name": "Champa",
        "tamil_name": "à®šà®£à¯à®ªà®•à®®à¯",
        "sanskrit_name": "à¤šà¤®à¥à¤ªà¤•à¤¾",
        "botanical_name": "Michelia champaca",
        "family_name": "Magnoliaceae",
        "chemical_composition": "Essential oils, Alkaloids",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Aromatic, Anti-anxiety, Skin care",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "chandrasura": {
        "english_name": "Garden cress",
        "tamil_name": "à®†à®³à®¿ à®…à®²à®¿",
        "sanskrit_name": "à¤šà¤¨à¥à¤¦à¥à¤°à¤¸à¥à¤°à¤¾",
        "botanical_name": "Lepidium sativum",
        "family_name": "Brassicaceae",
        "chemical_composition": "Vitamins, Minerals",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Respiratory support, Aphrodisiac",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "changeri": {
        "english_name": "creeping woodsorrel",
        "tamil_name": "à®ªà¯à®³à®¿à®¯à®¾à®°à¯ˆ",
        "sanskrit_name": "à¤šà¤™à¥à¤—à¥‡à¤°à¤¿",
        "botanical_name": "Oxalis corniculata",
        "family_name": "Oxalidaceae",
        "chemical_composition": "Oxalic acid, Flavonoids",
        "rasa": "Amla, Kashaya",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Anti-inflammatory, Diuretic, Antioxidant",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "chavya": {
        "english_name": "piper chilli",
        "tamil_name": "à®šà®µà¯à®¯à®¾",
        "sanskrit_name": "à¤šà¤µà¥à¤¯à¤¾",
        "botanical_name": "Piper chaba",
        "family_name": "Piperaceae",
        "chemical_composition": "Piperine, Essential oils",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Anti-inflammatory",
        "dose": "As prescribed by a qualified healthcare professional. Typically 200-400 mg per day."
    },
    "chirabilva": {
        "english_name": "Indian elm",
        "tamil_name": "à®†à®µà¯ à®®à®°à®®à¯",
        "sanskrit_name": "à¤šà¤¿à¤°à¤¬à¤¿à¤²à¥à¤µà¤¾",
        "botanical_name": "Holoptelea integrifolia",
        "family_name": "Rutaceae",
        "chemical_composition": "Alkaloids, Essential oils",
        "rasa": "Tikta, Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Digestive aid, Immunomodulator, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "chopachini": {
        "english_name": "Chobchini",
        "tamil_name": "à®šà¯‹à®ªà®šà®¿à®©à®¿",
        "sanskrit_name": "à¤šà¥‹à¤ªà¤šà¤¿à¤¨à¥€",
        "botanical_name": "Smilax glabra",
        "family_name": "Smilacaceae",
        "chemical_composition": "Saponins, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Diuretic, Immunomodulator",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "danti": {
        "english_name": "red physic nut",
        "tamil_name": "à®•à®Ÿà¯à®Ÿà®®à®¾à®™à¯à®•à¯, à®šà®¿à®®à¯ˆà®¯à®®à®£à®•à¯à®•à¯",
        "sanskrit_name": "à¤¦à¤¨à¥à¤¤à¥€",
        "botanical_name": "Baliospermum montanum",
        "family_name": "Euphorbiaceae",
        "chemical_composition": "Euphorbin, Ricinine",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Purgative, Anti-inflammatory, Antipyretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "darbha": {
        "english_name": "halfa grass",
        "tamil_name": "à®¤à®°à¯à®ªà¯à®ªà¯ˆà®ªà¯à®ªà¯à®²à¯",
        "sanskrit_name": "à¤¦à¤°à¥à¤­à¤¾",
        "botanical_name": "Desmostachya bipinnata",
        "family_name": "Poaceae",
        "chemical_composition": "Silica, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Purification rituals, Anti-inflammatory, Diuretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically 1-2 grams per day."
    },
    "dhattura": {
        "english_name": "Horn of Plenty, Downy Thorn-Apple, Hoary Thorn-Apple,",
        "tamil_name": "à®•à®°à¯ à®Šà®®à®¤à¯à®¤à¯ˆ",
        "sanskrit_name": "à¤§à¤¤à¥à¤¤à¥‚à¤°à¤¾",
        "botanical_name": "Datura metal",
        "family_name": "Solanaceae",
        "chemical_composition": "Alkaloids (Daturine, Atropine)",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Analgesic, Anti-inflammatory, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Extremely toxic, should be used only under strict supervision."
    },
    "dhanvayasa": {
        "english_name": "Dhanvayasa",
        "tamil_name": "à®¤à¯à®²à¯à®•à®¨à®°à®¿",
        "sanskrit_name": "à¤§à¤¨à¥à¤µà¤¯à¤¸à¤¾",
        "botanical_name": "Sesbania grandiflora",
        "family_name": "Fabaceae",
        "chemical_composition": "Flavonoids, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antioxidant, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "dhanyaka": {
        "english_name": "cilantro",
        "tamil_name": "à®•à¯Šà®¤à¯à®¤à®®à®²à¯à®²à®¿",
        "sanskrit_name": "à¤§à¤¨à¥à¤¯à¤•à¤¾",
        "botanical_name": "Coriandrum sativum",
        "family_name": "Apiaceae",
        "chemical_composition": "Linalool, Coriandrin",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Digestive aid, Anti-inflammatory, Antioxidant",
        "dose": "As prescribed by a qualified healthcare professional. Typically 1-2 grams per day."
    },
    "draksha": {
        "english_name": "European wine grape",
        "tamil_name": "à®¤à®¿à®°à®¾à®Ÿà¯à®šà¯ˆ",
        "sanskrit_name": "à¤¦à¥à¤°à¤¾à¤•à¥à¤·à¤¾",
        "botanical_name": "Vitis vinifera",
        "family_name": "Vitaceae",
        "chemical_composition": "Resveratrol, Flavonoids",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Antioxidant, Cardiovascular health, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically 10-20 grams per day."
    },
    "dronapushpi": {
        "english_name": "Thumbai",
        "tamil_name": "à®®à¯à®Ÿà®¿à®¤à¯à®®à¯à®ªà¯ˆ",
        "sanskrit_name": "à¤¦à¥à¤°à¥‹à¤£à¤ªà¥à¤·à¥à¤ªà¥€",
        "botanical_name": "Leucas aspera",
        "family_name": "Lamiaceae",
        "chemical_composition": "Triterpenoids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "gandhaprasarini": {
        "english_name": "Skunkvine, Stinkvine",
        "tamil_name": "à®•à®¾à®™à¯à®•à®¾à®¯à¯-à®ªà¯-à®ªà®¿à®©à®¾à®°à®¿, à®®à¯à®¤à¯à®¤à®¿à®¯à®°à¯ à®•à¯‚à®¨à¯à®¤à®²à¯",
        "sanskrit_name": "à¤—à¤¨à¥à¤§à¤ªà¥à¤°à¤¸à¤¾à¤°à¤¿à¤£à¥€",
        "botanical_name": "Paederia foetida",
        "family_name": "Rubiaceae",
        "chemical_composition": "Iridoids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Joint support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "garjara": {
        "english_name": "Carrot",
        "tamil_name": "à®•à¯‡à®°à®Ÿà¯",
        "sanskrit_name": "à¤—à¤°à¥à¤œà¤°à¤¾",
        "botanical_name": "Daucus carota",
        "family_name": "Apiaceae",
        "chemical_composition": "Carotenoids, Vitamin C",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Digestive aid, Antioxidant, Skin health",
        "dose": "As prescribed by a qualified healthcare professional. Typically 50-100 grams per day."
    },
    "gojihwa": {
        "english_name": "Gojihwa",
        "tamil_name": "à®•à¯Šà®œà®¿à®¹à¯à®µà®¾",
        "sanskrit_name": "à¤—à¥‹à¤œà¤¿à¤¹à¥à¤µà¤¾",
        "botanical_name": "Onosma bracteatum",
        "family_name": "Boraginaceae",
        "chemical_composition": "Alkaloids, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Respiratory support, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "gorakshaganja": {
        "english_name": "mountain knotgrass",
        "tamil_name": "à®ªà¯‚à®³à¯ˆ (Aerva lanata) à®…à®²à¯à®²à®¤à¯ à®¤à¯‡à®™à¯à®•à®¾à®¯à¯à®ªà¯à®ªà¯‚à®•à¯ à®•à¯€à®°à¯ˆ à®…à®²à¯à®²à®¤à¯ à®šà®¿à®±à¯à®ªà¯€à®³à¯ˆ ",
        "sanskrit_name": "à¤—à¥‹à¤°à¤•à¥à¤·à¤—à¤žà¥à¤œà¤¾",
        "botanical_name": "Aerva Lanata",
        "family_name": "Brassicaceae",
        "chemical_composition": "Vitamins, Minerals",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Respiratory support, Aphrodisiac",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "gunja": {
        "english_name": "jequirity bean or rosary pea",
        "tamil_name": "à®•à¯à®£à¯à®Ÿà¯à®®à®£à®¿",
        "sanskrit_name": "à¤—à¥à¤žà¥à¤œà¤¾",
        "botanical_name": "Abrus precatorius",
        "family_name": "Fabaceae",
        "chemical_composition": "Abrin, Alkaloids",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Immunomodulator",
        "dose": "As prescribed by a qualified healthcare professional. Extremely toxic, should be used only under strict supervision."
    },
    "hinsra": {
        "english_name": "wild caper bush",
        "tamil_name": "à®•à®¾à®Ÿà¯à®Ÿà¯à®•à¯à®•à®¤à¯à®¤à®°à®¿",
        "sanskrit_name": "à¤¹à¤¿à¤‚à¤¸à¥à¤°à¤¾",
        "botanical_name": "Capparis sepiaria",
        "family_name": "Capparaceae",
        "chemical_composition": "Flavonoids, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "hribera": {
        "english_name": "Fragrant Swamp Mallow",
        "tamil_name": "à®ªà¯‡à®°à®®à¯à®Ÿà¯à®Ÿà®¿, à®†à®µà®¿à®ªà®Ÿà¯à®Ÿà®®à¯",
        "sanskrit_name": "à¤¹à¥à¤°à¤¿à¤¬à¥‡à¤°à¤¾",
        "botanical_name": "Pavonia odorata",
        "family_name": "Malvaceae",
        "chemical_composition": "Flavonoids, Tannins",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Anti-inflammatory, Respiratory support, Diuretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "hrutpatri": {
        "english_name": "foxglove",
        "tamil_name": "à®¹à¯à®°à¯à®¤à¯à®ªà®¤à¯à®°à®¿",
        "sanskrit_name": "à¤¹à¥ƒà¤¤à¥à¤ªà¤¤à¥à¤°à¥€",
        "botanical_name": "Digitalis purpurea",
        "family_name": "Plantaginaceae",
        "chemical_composition": "Digitalin, Glycosides",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Cardiac stimulant (under strict medical supervision), Anti-inflammatory, Diuretic",
        "dose": "As prescribed by a qualified healthcare professional. Extremely toxic, should be used only under strict medical supervision."
    },
    "ikshu": {
        "english_name": "Sugarcane",
        "tamil_name": "à®•à®°à¯à®®à¯à®ªà¯",
        "sanskrit_name": "à¤‡à¤•à¥à¤·à¥",
        "botanical_name": "Saccharum officinarum",
        "family_name": "Poaceae",
        "chemical_composition": "Sucrose, Glucose, Fructose",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Sweetener, Rejuvenative, Energy booster",
        "dose": "As a natural sweetener, as per dietary requirements."
    },
    "indravrauni": {
        "english_name": "bitter apple",
        "tamil_name": "à®ªà¯†à®Ÿà¯à®Ÿà®¿à®•à®¾à®°à®¿",
        "sanskrit_name": "à¤‡à¤¨à¥à¤¦à¥à¤°à¤µà¥à¤°à¥Œà¤£à¥€",
        "botanical_name": "Citrullus colocynthis",
        "family_name": "Cucurbitaceae",
        "chemical_composition": "Flavonoids, Triterpenoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "ingudi": {
        "english_name": "desert date",
        "tamil_name": "à®¨à®žà¯à®šà¯à®£à¯à®Ÿà®©à¯",
        "sanskrit_name": "à¤‡à¤¨à¥à¤—à¥à¤¦à¥€",
        "botanical_name": "Balanites aegyptiaca",
        "family_name": "Balanitaceae",
        "chemical_composition": "Euphorbin, Ricinine",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Purgative",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "irimeda": {
        "english_name": " White Bark Acacia",
        "tamil_name": "à®µà¯†à®³à¯à®µà¯‡à®²à®®à¯",
        "sanskrit_name": "à¤‡à¤°à¥à¤®à¥‡à¤¡à¤¾",
        "botanical_name": "Acacia leucophloea",
        "family_name": "Mimosaceae",
        "chemical_composition": "Baicalein, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Respiratory support, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "ikshvaku": {
        "english_name": "bottle gourd",
        "tamil_name": "à®šà¯à®°à¯ˆà®•à¯à®•à®¾à®¯à¯",
        "sanskrit_name": "à¤‡à¤•à¥à¤·à¥à¤µà¤¾à¤•à¥",
        "botanical_name": "Lagenaria siceraria",
        "family_name": "Curcubitaceae",
        "chemical_composition": "Flavonoids, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antioxidant, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "ishvari": {
        "english_name": "The Indian Birthwort",
        "tamil_name": "à®¤à®¾à®´à¯ˆà®šà¯à®°à¯à®³à®¿à®•à¯à®•à¯Šà®Ÿà®¿, à®‰à®°à®¿à®•à¯à®•à®²à¯à®šà¯†à®Ÿà®¿, à®•à¯‹à®´à®¿à®•à¯à®•à¯à®£à¯à®Ÿà¯, à®ªà¯†à®°à¯à®®à®°à¯à®¨à¯à®¤à¯à®•à¯à®•à¯Šà®Ÿà®¿",
        "sanskrit_name": "à¤ˆà¤¶à¥à¤µà¤°à¥€",
        "botanical_name": "Aristolochia indica",
        "family_name": "Aristolochiaceae",
        "chemical_composition": "Aristolochic acid, Essential oils",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Immunomodulator, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Extremely toxic, should be used only under strict medical supervision."
    },
    "japa": {
        "english_name": "Hibiscus",
        "tamil_name": "à®šà¯†à®®à¯à®ªà®°à¯à®¤à¯à®¤à®¿",
        "sanskrit_name": "à¤œà¤ªà¤¾",
        "botanical_name": "Hibiscus rosa-sinensis",
        "family_name": "Malvaceae",
        "chemical_composition": "Flavonoids, Anthocyanins",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antioxidant, Hair and skin care",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in topical applications or as a decoction."
    },
    "jati": {
        "english_name": "Spanish Jasmine",
        "tamil_name": "à®šà®¾à®¤à®¿à®®à®²à¯à®²à®¿",
        "sanskrit_name": "à¤œà¤¾à¤¤à¤¿",
        "botanical_name": "Jasminum grandiflorum",
        "family_name": "Oleaceae",
        "chemical_composition": "Benzyl acetate, Benzyl alcohol",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Anti-inflammatory, Fragrance, Relaxant",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in aromatherapy or as a topical oil."
    },
    "jayapala": {
        "english_name": "True Croton",
        "tamil_name": "à®œà®¯à®ªà®¾à®²à®¾",
        "sanskrit_name": "à¤œà¤¯à¤ªà¤¾à¤²à¤¾",
        "botanical_name": "Croton tiglium",
        "family_name": "Euphorbiaceae",
        "chemical_composition": "Croton oil, Phorbol esters",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Purgative (under medical supervision), Antirheumatic, Anti-inflammatory",
        "dose": "As prescribed by a qualified healthcare professional. Use with caution due to potential toxicity."
    },
    "jeevanti": {
        "english_name": "Leptadenia",
        "tamil_name": "à®ªà®¾à®²à¯ˆà®•à¯à®•à¯Šà®Ÿà®¿",
        "sanskrit_name": "à¤œà¥€à¤µà¤¨à¥à¤¤à¥€",
        "botanical_name": "Leptadenia reticulata",
        "family_name": "Asclepiadaceae",
        "chemical_composition": "Saponins, Flavonoids",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Rejuvenative, Aphrodisiac, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "kadali": {
        "english_name": "banana",
        "tamil_name": "à®µà®¾à®´à¯ˆ",
        "sanskrit_name": "à¤•à¤¦à¤²à¥€",
        "botanical_name": "Musa paradisiaca",
        "family_name": "Musaceae",
        "chemical_composition": "Vitamins, Minerals, Dietary fiber",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Nutrient-rich, Digestive aid, Energy booster",
        "dose": "As part of a balanced diet. Typically consumed as a fruit or cooked preparation."
    },
    "kadamba": {
        "english_name": "kadam tree",
        "tamil_name": "à®•à®Ÿà®®à¯ à®®à®°à®®à¯",
        "sanskrit_name": "à¤•à¤¦à¤®à¥à¤¬",
        "botanical_name": "Nanthocephalus cadamba",
        "family_name": "Rubiaceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "kaidarya": {
        "english_name": "Curry Leaf Tree",
        "tamil_name": "à®•à®±à®¿à®µà¯‡à®ªà¯à®ªà®¿à®²à¯ˆ à®®à®°à®®à¯",
        "sanskrit_name": "à¤•à¥ˆà¤¦à¤°à¥à¤¯",
        "botanical_name": "Murraya Koeningi",
        "family_name": "Rutaceae",
        "chemical_composition": "Limonin, Flavonoids",
        "rasa": "Kashaya, Amalaki",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Antipyretic, Detoxifying",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "kakamachi": {
        "english_name": "black nightshade",
        "tamil_name": "à®®à®£à®¿à®¤à¯à®¤à®•à¯à®•à®¾à®³à®¿",
        "sanskrit_name": "à¤•à¤¾à¤•à¤®à¤¾à¤šà¥€",
        "botanical_name": "Solanum nigrum",
        "family_name": "Solanaceae",
        "chemical_composition": "Solanine, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Antioxidant",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "kamala": {
        "english_name": "Sacred Lotus",
        "tamil_name": "à®¤à®¾à®®à®°à¯ˆ",
        "sanskrit_name": "à¤•à¤®à¤²à¤¾",
        "botanical_name": "Nelumbo nucifera",
        "family_name": "Nelumbonaceae",
        "chemical_composition": "Nuciferine, Flavonoids",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Astringent, Rejuvenative, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations."
    },
    "kankola": {
        "english_name": "Java pepper",
        "tamil_name": "à®µà®¾à®²à¯à®®à®¿à®³à®•à¯",
        "sanskrit_name": "à¤•à¤™à¥à¤•à¥‹à¤²à¤¾",
        "botanical_name": "Piper cubeba",
        "family_name": "Piperaceae",
        "chemical_composition": "Cubebin, Piperine",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Aphrodisiac",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in small quantities."
    },
    "karanja": {
        "english_name": "Indian beech",
        "tamil_name": "à®ªà¯à®™à¯à®•à¯ˆ",
        "sanskrit_name": "à¤•à¤°à¤žà¥à¤œ",
        "botanical_name": "Pongamia pinnata",
        "family_name": "Fabaceae",
        "chemical_composition": "Pongamol, Karanjin",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antimicrobial, Skin health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in oil or powder form."
    },
    "karavellaka": {
        "english_name": "Bitter Melon",
        "tamil_name": "à®ªà®¾à®µà®•à¯à®•à®¾à®¯à¯",
        "sanskrit_name": "à¤•à¤¾à¤°à¤µà¥‡à¤²à¥à¤²à¤•",
        "botanical_name": "Momordica charantia",
        "family_name": "Cucurbitaceae",
        "chemical_composition": "Charantin, Momordicin",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Antidiabetic, Digestive aid, Blood purifier",
        "dose": "As prescribed by a qualified healthcare professional. Typically used as a vegetable or in medicinal formulations."
    },
    "karavira": {
        "english_name": "Oleander, Rose Bay, Rose Laurel, Dog Bane, Scented Oleander",
        "tamil_name": "à®…à®°à®³à®¿",
        "sanskrit_name": "à¤•à¤°à¤µà¥€à¤°",
        "botanical_name": "Nerium oleander",
        "family_name": "Apocynaceae",
        "chemical_composition": "Oleandrin, Nerioside",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Antimicrobial (externally), Caution: Highly toxic",
        "dose": "Not recommended for internal use. External use under strict medical supervision only."
    },
    "karira": {
        "english_name": "Bare Caper",
        "tamil_name": "à®šà®¿à®°à®•à¯à®•à¯‹à®´à®¿",
        "sanskrit_name": "à¤•à¤°à¥€à¤°",
        "botanical_name": "Capparis decidua",
        "family_name": "Capparaceae",
        "chemical_composition": "Capparidienone, Glucosinolates",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically 500-1000 mg per day."
    },
    "karpasa": {
        "english_name": "Levant cotton",
        "tamil_name": "à®•à®°à¯à®ªà®¾à®šà®®à¯",
        "sanskrit_name": "à¤•à¤°à¥à¤ªà¤¾à¤¸",
        "botanical_name": "Gossypium herbaceum",
        "family_name": "Malvaceae",
        "chemical_composition": "Gossypol, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Cardiovascular support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in textile and oil production."
    },
    "kasamarda": {
        "english_name": "Negro Coffee,Coffee Weed,Coffee Senna,Stinking Weed",
        "tamil_name": "à®¨à®Ÿà¯à®Ÿà®®à¯ à®¤à®•à®°à¯ˆ ,à®ªà®¯à®µà¯†à®°à¯ˆ ,à®ªà®¯à®µà¯†à®±à®¿",
        "sanskrit_name": "à¤•à¤¾à¤¸à¤¾à¤°",
        "botanical_name": "Cassia occidentalis",
        "family_name": "Fabaceae",
        "chemical_composition": "Emodin, Anthraquinones",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Laxative, Antipyretic, Hepatoprotective",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in medicinal formulations."
    },
    "kasha": {
        "english_name": "Kans Grass",
        "tamil_name": "à®ªà¯‡à®¯à¯ à®•à®°à¯à®®à¯à®ªà¯",
        "sanskrit_name": "à¤•à¤¾à¤·à¤¾",
        "botanical_name": "Saccharum spontaneum",
        "family_name": "Poaceae",
        "chemical_composition": "Sugars, Fiber",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Nutrient-rich, Digestive aid, Energy booster",
        "dose": "As part of a balanced diet. Typically consumed as a grain or in processed forms."
    },
    "kasani": {
        "english_name": "chicory",
        "tamil_name": "à®•à®¾à®šà®¿à®©à®¿à®•à¯à®•à¯€à®°à¯ˆ",
        "sanskrit_name": "à¤•à¤·à¤¾à¤£à¥€",
        "botanical_name": "Cichorium intybus",
        "family_name": "Asteraceae",
        "chemical_composition": "Inulin, Sesquiterpene lactones",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Liver support, Digestive aid, Detoxifying",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "kataka": {
        "english_name": "clearing-nut tree",
        "tamil_name": "à®¤à¯‡à®¤à¯à®¤à®¾à®©à¯ à®•à¯Šà®Ÿà¯à®Ÿà¯ˆ",
        "sanskrit_name": "à¤•à¤Ÿà¤•à¤¾",
        "botanical_name": "Strychnos potatorum",
        "family_name": "Loganiaceae",
        "chemical_composition": "Strychnine, Quercetin",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Eye care, Antipyretic, Urinary disorders",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in eye drops or as a decoction."
    },
    "katphala": {
        "english_name": "Box Myrtle and Bay Berry ",
        "tamil_name": "à®®à®°à¯à®¤à®®à¯, à®®à®°à¯à®¤à®®à¯à®ªà®Ÿà¯à®Ÿà¯ˆ",
        "sanskrit_name": "à¤•à¤Ÿà¤«à¤²",
        "botanical_name": "Myrica nagi Thumb",
        "family_name": "Myricaceae",
        "chemical_composition": "Myricetin, Tannins",
        "rasa": "Kashaya, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Antioxidant, Digestive aid, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "kebuka": {
        "english_name": "Cane-reed, Crepe- ginger",
        "tamil_name": "à®•à¯‹à®·à¯à®Ÿà®®à¯",
        "sanskrit_name": "à¤•à¥‡à¤¬à¥à¤•à¤¾",
        "botanical_name": "Costus speciosus",
        "family_name": "Zingiberaceae",
        "chemical_composition": "Barlerin, Sterols",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Skin disorders",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "kharjura": {
        "english_name": "date palm",
        "tamil_name": "à®•à®°à®¿à®šà®¿à®•à¯ˆ",
        "sanskrit_name": "à¤–à¤°à¥à¤œà¥‚à¤°",
        "botanical_name": "Phoenix dactylifera",
        "family_name": "Arecaceae",
        "chemical_composition": "Phenolic acids, Tannins",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Nutrient-rich, Laxative, Rejuvenative",
        "dose": "As part of a balanced diet. Typically consumed as a fruit or in processed forms."
    },
    "kitamari": {
        "english_name": "Indian Birthwort",
        "tamil_name": "à®†à®Ÿà¯ à®¤à®¿à®©à¯à®©à®¾ à®ªà®¾à®²à¯ˆ",
        "sanskrit_name": "à¤•à¥€à¤Ÿà¤®à¤¾à¤°à¥€",
        "botanical_name": "Aristolochia bracteata",
        "family_name": "aristolochiceae",
        "chemical_composition": "Kutkin, Apocynin",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Liver support, Respiratory support, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "kokilaksha": {
        "english_name": "Talamkhana",
        "tamil_name": "à®¨à¯€à®°à¯ à®®à¯à®³à¯à®³à®¿",
        "sanskrit_name": "à¤•à¥‹à¤•à¤¿à¤²à¤¾à¤•à¥à¤·à¤¾",
        "botanical_name": "Asteracantha longifolia",
        "family_name": "Acanthaceae",
        "chemical_composition": "Saponins, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Aphrodisiac, Diuretic, Immune support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "koshataki": {
        "english_name": "ridge gourd",
        "tamil_name": "à®ªà¯€à®°à¯à®•à¯à®•à®™à¯à®•à®¾à®¯à¯",
        "sanskrit_name": "à¤•à¥‹à¤·à¤¾à¤Ÿà¤•à¥€",
        "botanical_name": "Luffa acutangula",
        "family_name": "Cucurbitaceae",
        "chemical_composition": "Emodin, Chrysophanol",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Laxative, Antipyretic, Liver support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "kullatha": {
        "english_name": "Muthira",
        "tamil_name": "à®•à¯Šà®³à¯à®³à¯",
        "sanskrit_name": "à¤•à¥à¤²à¥à¤²à¤¥à¤¾",
        "botanical_name": "Dolichos biflorus",
        "family_name": "Fabaceae",
        "chemical_composition": "Lectins, Flavonoids",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Diuretic, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "kumuda": {
        "english_name": "white waterlily",
        "tamil_name": "à®†à®®à¯à®ªà®²à¯",
        "sanskrit_name": "à¤•à¥à¤®à¥à¤¦",
        "botanical_name": "Nymphaea alba",
        "family_name": "Nymphaeaceae",
        "chemical_composition": "Flavonoids, Alkaloids",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Astringent, Rejuvenative, Nervine tonic",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as an infusion."
    },
    "kusha": {
        "english_name": "salt reed-grass",
        "tamil_name": "à®¤à®°à¯à®ªà¯à®ªà¯ˆà®ªà¯à®ªà¯à®²à¯",
        "sanskrit_name": "à¤•à¥à¤¶",
        "botanical_name": "Desmostachya bipinnata",
        "family_name": "Poaceae",
        "chemical_composition": "Dihydrostilbenes, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Diuretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "kushmanda": {
        "english_name": "Winter Melon, Wax Gourd, Fuzzy Gourd, Ash Gourd",
        "tamil_name": "à®¨à¯€à®°à¯ à®ªà¯‚à®šà®£à®¿à®•à¯à®•à®¾à®¯à¯",
        "sanskrit_name": "à¤•à¥à¤·à¥à¤®à¤¾à¤£à¥à¤¡à¤¾",
        "botanical_name": "Benincasa hispida",
        "family_name": "Cucurbitaceae",
        "chemical_composition": "Beta-carotene, Vitamin C",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Nutrient-rich, Digestive aid, Respiratory support",
        "dose": "As part of a balanced diet. Typically consumed as a vegetable or in processed forms."
    },
    "lajjalu": {
        "english_name": "sensitive plant",
        "tamil_name": "à®¤à¯Šà®Ÿà¯à®Ÿà®¾ à®šà®¿à®©à¯à®™à¯à®•à®¿",
        "sanskrit_name": "à¤²à¤œà¥à¤œà¤¾à¤²à¥",
        "botanical_name": "Mimosa pudica",
        "family_name": "Fabaceae",
        "chemical_composition": "Alkaloids, Tannins",
        "rasa": "Kashaya, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Wound healing",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "langali": {
        "english_name": "gloriosa lily, glory lily",
        "tamil_name": "à®•à®¾à®°à¯à®¤à¯à®¤à®¿à®•à¯ˆà®ªà¯à®ªà¯‚ or à®•à®¾à®¨à¯à®¤à®³à¯ ",
        "sanskrit_name": "à¤²à¤™à¥à¤—à¤¾à¤²à¤¿",
        "botanical_name": "Gloriosa superba",
        "family_name": "Colchicaceae",
        "chemical_composition": "Colchicine, Gloriosine",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Increases Pitta dosha, may aggravate Vata and Kapha in excess",
        "prayoga": "Anti-inflammatory, Analgesic (under medical supervision), Antipyretic",
        "dose": "Not recommended for self-use due to toxicity. Use only under strict medical supervision."
    },
    "lata_karanja": {
        "english_name": "Crested Fever Nut",
        "tamil_name": "à®•à®œà®¿à®šà¯à®šà®¿à®•à®¾à®¯à®¾",
        "sanskrit_name": "à¤²à¤¤à¤¾ à¤•à¤°à¤žà¥à¤œà¤¾",
        "botanical_name": "Caesalpinia crista",
        "family_name": "Fabaceae",
        "chemical_composition": "Pongamol, Karanjin",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antimicrobial, Skin health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in oil or powder form."
    },
    "lata_kasturi": {
        "english_name": "musk mallow",
        "tamil_name": "à®•à®Ÿà¯à®Ÿà¯à®•à®¸à¯à®¤à¯‚à®°à®¿",
        "sanskrit_name": "à¤²à¤¤à¤¾ à¤•à¤¸à¥à¤¤à¥‚à¤°à¥€",
        "botanical_name": "Abelmoschus moschatus",
        "family_name": "Malvaceae",
        "chemical_composition": "Muscone, Sesquiterpenes",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Fragrance, Aphrodisiac, Nervine tonic",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in perfumes or as a fragrant herb."
    },
    "madayantika": {
        "english_name": "Henna",
        "tamil_name": "à®®à®°à¯à®¤à®¾à®£à®¿",
        "sanskrit_name": "à¤®à¤¦à¤¯à¤¨à¥à¤¤à¤¿à¤•à¤¾",
        "botanical_name": "Lawsonia inermis",
        "family_name": "Lythraceae",
        "chemical_composition": "Lawsone, Tannins",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Cooling, Antimicrobial, Hair and skin health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used as a paste or in herbal formulations."
    },
    "mahanimba": {
        "english_name": "chinaberry tree, pride of India, bead-tree",
        "tamil_name": "à®•à®¾à®Ÿà¯à®Ÿà¯ à®µà¯‡à®®à¯à®ªà¯‚ ",
        "sanskrit_name": "à¤®à¤¹à¤¾à¤¨à¤¿à¤®à¥à¤¬",
        "botanical_name": "Melia azedarach",
        "family_name": "Meliaceae",
        "chemical_composition": "Meliazadirachtin, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Antiparasitic, Antimicrobial, Skin disorders",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "markandika": {
        "english_name": "Senna",
        "tamil_name": "à®¸à¯à®µà®°à¯à®£ à®ªà®¤à¯à®°à®¿",
        "sanskrit_name": "à¤®à¤¾à¤°à¥à¤•à¤¾à¤£à¥à¤¡à¥€à¤•à¤¾",
        "botanical_name": "Cassia angustifolia",
        "family_name": "Caesalpinaceae",
        "chemical_composition": "Nasutin, Acanthoside",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Skin disorders",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "masa": {
        "english_name": "Urd Bean",
        "tamil_name": "à®‰à®³à¯à®¨à¯à®¤à¯",
        "sanskrit_name": "à¤®à¤¾à¤·",
        "botanical_name": "Phaseolus mungo",
        "family_name": "Fabaceae",
        "chemical_composition": "Proteins, Fiber",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Nutrient-rich, Digestive aid, Diuretic",
        "dose": "As part of a balanced diet. Typically consumed as a pulse or in processed forms."
    },
    "masaparni": {
        "english_name": "Black-gram",
        "tamil_name": "à®‰à®³à¯à®¨à¯à®¤à¯",
        "sanskrit_name": "à¤®à¤¾à¤·à¤¾à¤ªà¤°à¥à¤£à¥€",
        "botanical_name": "Teramnus labialis",
        "family_name": "Fabaceae",
        "chemical_composition": "Isoflavones, Triterpenoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Diuretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "mayaphala": {
        "english_name": "gall oak",
        "tamil_name": "à®®à®¾à®šà¯à®šà®¿à®•à¯à®•à®¾à®¯à¯",
        "sanskrit_name": "à¤®à¤¾à¤¯à¤¾à¤«à¤²",
        "botanical_name": "Quercus infectoria",
        "family_name": "Fagaceae",
        "chemical_composition": "Tannic acid, Gallic acid",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Astringent, Antimicrobial, Dental health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in powder or paste form."
    },
    "mesasringi": {
        "english_name": "gurmar",
        "tamil_name": "à®šà®¿à®±à¯à®•à¯à®±à®¿à®žà¯à®šà®¾",
        "sanskrit_name": "à¤®à¥‡à¤·à¤¶à¥ƒà¤™à¥à¤—à¥€",
        "botanical_name": "Gymnema sylvestre",
        "family_name": "Apocynaceae",
        "chemical_composition": "Gymnemic acid, Saponins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Antidiabetic, Digestive aid, Weight management",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "methika": {
        "english_name": "fenugreek",
        "tamil_name": "à®µà¯†à®¨à¯à®¤à®¯à®®à¯",
        "sanskrit_name": "à¤®à¥‡à¤¥à¤¿à¤•à¤¾",
        "botanical_name": "Trigonella foenum-graecum",
        "family_name": "Fabaceae",
        "chemical_composition": "Saponins, Alkaloids",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Antidiabetic, Digestive aid, Galactagogue",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in culinary or as a powder."
    },
    "mudgaparni": {
        "english_name": "Ranmoong",
        "tamil_name": "à®¨à®°à®¿à®ªà®¯à®±à¯",
        "sanskrit_name": "à¤®à¥à¤¦à¥à¤—à¤ªà¤°à¥à¤£à¥€",
        "botanical_name": "Phaseolus trilobus",
        "family_name": "Fabaceae",
        "chemical_composition": "Proteins, Fiber",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Nutrient-rich, Digestive aid, Diuretic",
        "dose": "As part of a balanced diet. Typically consumed as a pulse or in processed forms."
    },
    "mulaka": {
        "english_name": "Radish",
        "tamil_name": "à®®à¯à®³à¯à®³à®™à¯à®•à®¿",
        "sanskrit_name": "à¤®à¥‚à¤²à¤•",
        "botanical_name": "Raphanus sativus",
        "family_name": "Brassicaceae",
        "chemical_composition": "Glucosinolates, Vitamin C",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Detoxifying",
        "dose": "As part of a balanced diet. Typically consumed as a vegetable or in processed forms."
    },
    "murva": {
        "english_name": "Rajmahal Hemp",
        "tamil_name": "à®ªà®žà¯à®šà¯à®•à¯à®•à¯Šà®Ÿà®¿",
        "sanskrit_name": "à¤®à¥à¤°à¥à¤µà¤¾",
        "botanical_name": "Marsdenia tenacissima",
        "family_name": "Asclepiadaceae",
        "chemical_composition": "Constituents of alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "nagabala": {
        "english_name": "Kukurbicha",
        "tamil_name": "à®•à®²à¯à®©à¯à®©à¯, à®¤à®µà®¿à®Ÿà¯, à®¤à®µà®Ÿà¯",
        "sanskrit_name": "à¤¨à¤¾à¤—à¤¬à¤²",
        "botanical_name": "Grewia hirsuta",
        "family_name": "Tiliaceae",
        "chemical_composition": "Tannins, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "nala": {
        "english_name": "Giant reed",
        "tamil_name": "à®•à¯‡à®°à®µà®©à®®à¯",
        "sanskrit_name": "à¤¨à¤²",
        "botanical_name": "Arundo donax",
        "family_name": "Poaceae",
        "chemical_composition": "Gingerol, Shogaol",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Anti-inflammatory, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in culinary or as a powder."
    },
    "narikela": {
        "english_name": "Coconut Palm",
        "tamil_name": "à®¤à¯†à®©à¯à®©à¯ˆ",
        "sanskrit_name": "à¤¨à¤¾à¤°à¤¿à¤•à¥‡à¤²",
        "botanical_name": "Cocos nucifera",
        "family_name": "Arecaceae",
        "chemical_composition": "Medium-chain fatty acids, Lauric acid",
        "rasa": "Madhura",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Nutrient-rich, Cooling, Rejuvenative",
        "dose": "As part of a balanced diet. Typically consumed as coconut water, milk, or in processed forms."
    },
    "nili": {
        "english_name": "true indigo",
        "tamil_name": "à®…à®µà¯à®°à®¿",
        "sanskrit_name": "à¤¨à¥€à¤²à¤¿",
        "botanical_name": "Indigofera tinctoria",
        "family_name": "Fabaceae",
        "chemical_composition": "Indigo, Indirubin",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Dyeing agent",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a dye."
    },
    "padmaka": {
        "english_name": "wild Himalayan cherry",
        "tamil_name": "à®ªà®¤à¯à®®à®•à®®à¯",
        "sanskrit_name": "à¤ªà¤¦à¥à¤®à¤•",
        "botanical_name": "Prunus cerasoides",
        "family_name": "Rosaceae",
        "chemical_composition": "Ellagic acid, Tannins",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antimicrobial, Dental health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in powder or paste form."
    },
    "palandu": {
        "english_name": "bulb onion or common onion",
        "tamil_name": "à®µà¯†à®™à¯à®•à®¾à®¯à®®à¯ ",
        "sanskrit_name": "à¤ªà¤¾à¤²à¤¨à¥à¤¦à¥",
        "botanical_name": "Allium cepa",
        "family_name": "Amaryllidaceae",
        "chemical_composition": "Allicin, Quercetin",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Immune booster",
        "dose": "As part of a balanced diet. Typically consumed as a vegetable or in culinary preparations."
    },
    "parasika_yavani": {
        "english_name": "henbane",
        "tamil_name": "à®•à¯à®±à®šà®¾à®£à®¿ à®“à®®à®®à¯",
        "sanskrit_name": "à¤ªà¤¾à¤°à¤¾à¤¸à¤¿à¤• à¤¯à¤µà¤¨à¥€",
        "botanical_name": "Hyoscyamus niger",
        "family_name": "Solanaceae",
        "chemical_composition": "Alkaloids, Scopolamine",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Increases Pitta dosha, may aggravate Vata and Kapha in excess",
        "prayoga": "Analgesic (under medical supervision), Respiratory support, Sedative",
        "dose": "Not recommended for self-use due to toxicity. Use only under strict medical supervision."
    },
    "parijata": {
        "english_name": "Tree of Sadness, Seri Gading, Night Blooming Jasmine",
        "tamil_name": "à®ªà®µà®¿à®´à®®à®²à¯à®²à®¿",
        "sanskrit_name": "à¤ªà¤¾à¤°à¤¿à¤œà¤¾à¤¤",
        "botanical_name": "Nyctanthes arbor-tristis",
        "family_name": "Oleaceae",
        "chemical_composition": "Nyctanthin, Nyctanthesin",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Antipyretic",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "parisha": {
        "english_name": "Portia Tree ",
        "tamil_name": "à®ªà¯‚à®µà®°à®šà¯",
        "sanskrit_name": "à¤ªà¤°à¤¿à¤·à¤¾",
        "botanical_name": "Thespesia populnea Linn",
        "family_name": "Malvaceae",
        "chemical_composition": "Steroidal saponins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "parnabija": {
        "english_name": "Miracle leaf",
        "tamil_name": "à®°à®£à®•à®³à¯à®³à®¿",
        "sanskrit_name": "à¤ªà¤°à¥à¤£à¤¾à¤¬à¤¿à¤œà¤¾",
        "botanical_name": "Bryophyllum pinnatum",
        "family_name": "Crassulaceae",
        "chemical_composition": "Saponins, Triterpenoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "parnayavani": {
        "english_name": "Mexican mint",
        "tamil_name": "à®“à®®à®µà®²à¯à®²à®¿",
        "sanskrit_name": "à¤ªà¤°à¥à¤£à¤¾à¤¯à¤µà¤¾à¤£à¥€",
        "botanical_name": "Coleus amboinicus Lour",
        "family_name": "Lamiaceae",
        "chemical_composition": "Gmelinol, Phenolic compounds",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "parushaka": {
        "english_name": "phalsa",
        "tamil_name": "à®ªà®²à®¿à®šà¯à®šà®¾à®®à®°à®®à¯",
        "sanskrit_name": "à¤ªà¤°à¥à¤·à¤•",
        "botanical_name": "Grewia asiatica",
        "family_name": "Tiliaceae",
        "chemical_composition": "Triterpenes, Flavonoids",
        "rasa": "Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Analgesic",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "patalagarudi": {
        "english_name": "broom creeper",
        "tamil_name": "à®•à®¾à®Ÿà¯à®Ÿà¯à®•à¯à®•à¯Šà®Ÿà®¿",
        "sanskrit_name": "à¤ªà¤¤à¤¾à¤²à¤—à¤°à¥à¤¡à¥€",
        "botanical_name": "Cocculus hirsutus",
        "family_name": "Menispermaceae",
        "chemical_composition": "Tannins, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "patha": {
        "english_name": "velvetleaf",
        "tamil_name": "à®²à®•à¯ à®ªà®¾à®¤",
        "sanskrit_name": "à¤ªà¤¥à¤¾",
        "botanical_name": "Cissampelos pareira",
        "family_name": "Menispermaceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "patola": {
        "english_name": "pointed gourd",
        "tamil_name": "à®•à¯Šà®®à¯à®ªà¯à®ªà¯à®ªà¯à®Ÿà®²à¯ˆ, à®®à¯à®šà¯ à®®à¯à®šà¯à®•à¯à®•à¯ˆ, à®ªà¯‡à®¯à¯à®ªà¯à®ªà¯à®Ÿà®²à¯ˆ, à®ªà¯à®Ÿà®²à¯ˆ, à®•à¯Šà®®à¯à®ªà¯-à®ªà¯à®Ÿà®²à¯ˆ,",
        "sanskrit_name": "à¤ªà¤Ÿà¥‹à¤²",
        "botanical_name": "Trichosanthes dioica",
        "family_name": "Cucurbitaceae",
        "chemical_composition": "Saponins, Flavonoids",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a vegetable."
    },
    "patranga": {
        "english_name": "sappanwood and Indian redwood",
        "tamil_name": "à®ªà®¤à®¿à®®à¯à®•à®®à¯",
        "sanskrit_name": "à¤ªà¤¤à¥à¤°à¤¾à¤™à¥à¤—",
        "botanical_name": "Caesalpinia sappan",
        "family_name": "Fabaceae",
        "chemical_composition": "Brazilin, Sappanin",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Blood purifier",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "pilu": {
        "english_name": "miswak",
        "tamil_name": "à®‰à®•à®¾",
        "sanskrit_name": "à¤ªà¤¿à¤²à¥",
        "botanical_name": "Salvadora persica",
        "family_name": "Salvadoraceae",
        "chemical_composition": "Alkaloids, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Dental health, Anti-inflammatory, Antimicrobial",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a chewing stick."
    },
    "plaksha": {
        "english_name": "JAVA FIG",
        "tamil_name": "à®•à¯à®°à¯à®•à¯",
        "sanskrit_name": "à¤ªà¥à¤²à¤•à¥à¤·",
        "botanical_name": "Ficus lacor",
        "family_name": "Moraceae",
        "chemical_composition": "Flavonoids, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "prasarini": {
        "english_name": "Chinese moon creeper",
        "tamil_name": "à®®à¯à®¤à®¿à®¯à®¾à®°à¯ à®•à¯‚à®¨à¯à®¤à®²à¯",
        "sanskrit_name": "à¤ªà¥à¤°à¤¸à¤¾à¤°à¤¿à¤£à¥€",
        "botanical_name": "Merremia tridentata Hallica",
        "family_name": "Rubiaceae",
        "chemical_composition": "Iridoids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Joint health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "priyala": {
        "english_name": "Charoli Nut",
        "tamil_name": "à®šà®¾à®°à®®à¯",
        "sanskrit_name": "à¤ªà¥à¤°à¤¿à¤¯à¤¾à¤²",
        "botanical_name": "Buchanania lanzan",
        "family_name": "Anacardiaceae",
        "chemical_composition": "Tannins, Flavonoids",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Anti-inflammatory, Antioxidant, Cardiovascular health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a seed."
    },
    "priyangu": {
        "english_name": "Perfumed Cherry",
        "tamil_name": "à®‡à®Ÿà¯à®Ÿà®µà¯à®Ÿà¯à®•à®¾,à®µà¯†à®Ÿà¯à®Ÿà®¿à®²à¯ˆà®ªà¯à®ªà¯‡à®Ÿà¯à®Ÿà¯ˆ,à®šà¯€à®®à¯à®ªà®•à¯à®´à¯à®¤à¯à®¤à¯",
        "sanskrit_name": "à¤ªà¥à¤°à¤¿à¤¯à¤¾à¤™à¥à¤—à¥",
        "botanical_name": "Callicarpa macrophylla",
        "family_name": "Lamiaceae",
        "chemical_composition": "Flavonoids, Essential oils",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Anti-inflammatory, Antioxidant, Skin health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "puga": {
        "english_name": "Betel-nut Palm",
        "tamil_name": "à®…à®Ÿà¯ˆà®•à¯à®•à®¾à®¯à¯",
        "sanskrit_name": "à¤ªà¥à¤—",
        "botanical_name": "Areca catechu",
        "family_name": "Palmae",
        "chemical_composition": "Arecoline, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Antimicrobial, Oral health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a chewing ingredient."
    },
    "putiha": {
        "english_name": "Peppermint",
        "tamil_name": "à®®à®¿à®³à®•à¯à®•à¯à®•à¯€à®°à¯ˆ",
        "sanskrit_name": "à¤ªà¥à¤¤à¤¿à¤¹",
        "botanical_name": "Mentha piperata",
        "family_name": "Laminaceae",
        "chemical_composition": "Putranjivanone, Flavonoids",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "putranjivaka": {
        "english_name": "Putijia",
        "tamil_name": "à®ªà¯à®¤à¯à®¤à®¿à®°à®šà¯€à®µà®¿",
        "sanskrit_name": "à¤ªà¥à¤¤à¥à¤°à¤¾à¤žà¥à¤œà¥€à¤µà¤•",
        "botanical_name": "Putranjiva roxburghii Roxb.",
        "family_name": "Euphorbiaceae",
        "chemical_composition": "Triterpenoids, Flavonoids",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "rajika": {
        "english_name": "Indian Mustard, Chinese Mustard",
        "tamil_name": "à®•à®Ÿà¯à®•à¯",
        "sanskrit_name": "à¤°à¤¾à¤œà¤¿à¤•à¤¾",
        "botanical_name": "Brassica juncea",
        "family_name": "Brassicaceae",
        "chemical_composition": "Glucosinolates, Vitamin C",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Detoxifying",
        "dose": "As part of a balanced diet. Typically consumed as a vegetable or in processed forms."
    },
    "sarshapa": {
        "english_name": "Mustard",
        "tamil_name": "à®•à®Ÿà¯à®•à¯",
        "sanskrit_name": "à¤¸à¤°à¥à¤·à¤ª",
        "botanical_name": "Brassica nigra",
        "family_name": "Brassicaceae",
        "chemical_composition": "Glucosinolates, Omega-3 fatty acids",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Detoxifying",
        "dose": "As part of a balanced diet. Typically used as a spice or oil."
    },
    "saptachakra": {
        "english_name": "Indian Pulai, White Cheesewood",
        "tamil_name": "à®à®´à®¿à®²à¯ˆà®ªà¯ à®ªà®¾à®²à¯ˆ",
        "sanskrit_name": "à¤¸à¤ªà¥à¤¤à¤šà¤•à¥à¤°",
        "botanical_name": "Alstonia scholaris",
        "family_name": "Apocynaceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "saptaparna": {
        "english_name": "Saptaparna",
        "tamil_name": "à®šà®ªà¯à®¤à®ªà®°à¯à®£à®®à¯",
        "sanskrit_name": "à¤¸à¤ªà¥à¤¤à¤ªà¤°à¥à¤£",
        "botanical_name": "Alstonia scholaris",
        "family_name": "Apocynaceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "sarala": {
        "english_name": "chir pine or longleaf pine",
        "tamil_name": "à®šà®°à®³à®¾ à®¤à¯‡à®µà®¤à®¾à®°à¯",
        "sanskrit_name": "à¤¸à¤°à¤²",
        "botanical_name": "Pinus roxburghii",
        "family_name": "Pinaceae",
        "chemical_composition": "Terpenes, Resin",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "sarja": {
        "english_name": "Indian copal tree, Indian gum anime",
        "tamil_name": "à®¤à¯‚à®ª à®®à®°à®®à¯",
        "sanskrit_name": "à¤¸à¤°à¥à¤œ",
        "botanical_name": "Vateria indica",
        "family_name": "Dipterocarpaceae",
        "chemical_composition": "Resin, Essential oils",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a resin."
    },
    "shala": {
        "english_name": "sal tree",
        "tamil_name": "à®•à¯à®™à¯à®•à®¿à®²à®¿à®¯à®®à¯",
        "sanskrit_name": "à¤¶à¤¾à¤²",
        "botanical_name": "Shorea robusta",
        "family_name": "Dipterocarpaceae",
        "chemical_composition": "Resin, Tannins",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a resin."
    },
    "shara": {
        "english_name": "Pin red grass",
        "tamil_name": "à®®à¯à®žà¯à®šà®¿à®ªà®¾à®²à¯",
        "sanskrit_name": "à¤¶à¤°",
        "botanical_name": "Saccharum munja",
        "family_name": "Poaceae",
        "chemical_composition": "Catechin, Tannins",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Dental health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "sharpunkha": {
        "english_name": "Fish poison, wild indigos",
        "tamil_name": "à®•à¯Šà®´à®¿à®žà¯à®šà®¿",
        "sanskrit_name": "à¤¶à¤°à¤ªà¥à¤£à¥à¤–à¤¾",
        "botanical_name": "Tephrosia purpurea",
        "family_name": "Fabaceae",
        "chemical_composition": "Flavonoids, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Hepatoprotective, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "shatahwa": {
        "english_name": "Dill Seed",
        "tamil_name": "à®šà®¤à®•à¯à®ªà¯à®ªà¯ˆ",
        "sanskrit_name": "à¤¶à¤¤à¤¹à¥à¤µà¤¾",
        "botanical_name": "Anethum sowa",
        "family_name": "Apiaceae",
        "chemical_composition": "Saponins, Alkaloids",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Rejuvenative, Reproductive health, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "shati": {
        "english_name": "spiked ginger lily",
        "tamil_name": "à®ªà¯‚à®²à®•à®¿à®´à®™à¯à®•à¯ or à®•à®¿à®šà¯à®šà®¿à®²à®¿à®•à®¿à®´à®™à¯à®•à¯",
        "sanskrit_name": "à¤¶à¤¤à¥€",
        "botanical_name": "Hedychium spicatum",
        "family_name": "Zingiberaceae",
        "chemical_composition": "Essential oils, Curcumin",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Respiratory support, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "shimshapa": {
        "english_name": "North Indian rosewood",
        "tamil_name": "à®¨à¯‚à®•à¯à®•à®®à¯, à®šà®¿à®šà¯‡ à®…à®²à¯à®²à®¤à¯ à®¤à®¾à®²à¯à®ªà¯†à®°à¯à®šà®¿à®¯à®¾ à®šà®¿à®šà¯‚",
        "sanskrit_name": "à¤¶à¤¿à¤‚à¤¶à¤ªà¤¾",
        "botanical_name": "Dalbergia sissoo",
        "family_name": "Fabaceae",
        "chemical_composition": "Triterpenoids, Flavonoids",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "snuhi": {
        "english_name": "Milkhedge",
        "tamil_name": "à®à®²à¯ˆà®•à¯à®•à®²à¯à®²à®¿, à®ªà¯†à®°à¯à®®à¯ à®•à®²à¯à®²à®¿",
        "sanskrit_name": "à¤¸à¥à¤¨à¥à¤¹à¤¿",
        "botanical_name": "Euphorbia neriifolia",
        "family_name": "Euphorbiaceae",
        "chemical_composition": "Diterpenes, Resin",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a resin."
    },
    "sringataka": {
        "english_name": "water chestnut",
        "tamil_name": "à®šà®¿à®°à®¿à®™à¯à®•à®¾à®Ÿà®¾",
        "sanskrit_name": "à¤¶à¥ƒà¤‚à¤—à¤¾à¤Ÿà¤•",
        "botanical_name": "Trapa bispinosa",
        "family_name": "Trapaceae",
        "chemical_composition": "Berberine, Alkaloids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Immunomodulator, Hepatoprotective, Anti-inflammatory",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "surana": {
        "english_name": "Elephant Foot Yam, Elephant Yam",
        "tamil_name": " à®•à®°à¯à®£à¯ˆ à®•à®¿à®´à®™à¯à®•à¯",
        "sanskrit_name": "à¤¸à¥à¤°à¤£",
        "botanical_name": "Amorphophallus campanulatus",
        "family_name": "Araceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Anti-inflammatory, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a tuber."
    },
    "svarnakshiri": {
        "english_name": "Mexican prickly poppy",
        "tamil_name": "à®ªà®¿à®°à®®à¯à®®à®¤à¯à®¤à®£à¯à®Ÿà¯ à®…à®²à¯à®²à®¤à¯ à®¨à®¾à®¯à¯à®•à®Ÿà¯à®•à¯ (à®…) à®•à¯à®Ÿà®¿à®¯à¯‹à®Ÿà¯à®Ÿà®¿à®ªà¯à®ªà¯‚à®£à¯à®Ÿà¯",
        "sanskrit_name": "à¤¸à¥à¤µà¤°à¥à¤£à¤¾à¤•à¥à¤·à¥€à¤°à¥€",
        "botanical_name": "Argemone mexicana",
        "family_name": "Papaveraceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Analgesic, Anti-inflammatory, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "tagara": {
        "english_name": "Indian Valerian, Muskbala",
        "tamil_name": "à®…à®ªà¯à®°à®®à®¾à®žà¯à®šà®¿",
        "sanskrit_name": "à¤¤à¤—à¤°à¤¾",
        "botanical_name": "Valeriana wallichii",
        "family_name": "Caprifoliaceae",
        "chemical_composition": "Valerenic acid, Essential oils",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Sedative, Anxiolytic, Sleep aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a powder."
    },
    "tailaparni": {
        "english_name": "Tasmanian bluegum",
        "tamil_name": "à®¤à¯ˆà®² à®®à®°à®®à¯",
        "sanskrit_name": "à¤¤à¥ˆà¤²à¤ªà¤°à¥à¤£à¥€",
        "botanical_name": "Eucalyptus globulus",
        "family_name": "Asteraceae",
        "chemical_composition": "Ecliptine, Wedelolactone",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Hair care, Liver support, Anti-inflammatory",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as an oil."
    },
    "talamuli": {
        "english_name": "Talipot Palm",
        "tamil_name": "à®¤à®¾à®³à®¿à®ªà¯ à®ªà®©à¯ˆ",
        "sanskrit_name": "à¤¤à¤¾à¤²à¤®à¥‚à¤²à¤¿",
        "botanical_name": "Corypha umbraculifera",
        "family_name": "Arecaceae",
        "chemical_composition": "Triterpenes, Flavonoids",
        "rasa": "Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Antipyretic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a decoction."
    },
    "taruni": {
        "english_name": "Cabbage rose",
        "tamil_name": "à®ªà®©à¯à®©à¯€à®°à¯ or à®°à¯‹à®œà®¾ à®®à¯Šà®Ÿà¯à®Ÿà¯",
        "sanskrit_name": "à¤¤à¤°à¥à¤£à¤¿",
        "botanical_name": "Rosa centifolia",
        "family_name": "Rosaceae",
        "chemical_composition": "Flavonoids, Essential oils",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Skin care, Antioxidant, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a flower."
    },
    "tavakshiri": {
        "english_name": "giant dodder",
        "tamil_name": "à®•à¯Šà®Ÿà®¿à®¯à®•à¯à®£à¯à®Ÿà®²à¯",
        "sanskrit_name": "à¤¤à¤µà¤¾à¤•à¥à¤·à¤¿à¤°à¤¿",
        "botanical_name": "Cuscuta reflexa",
        "family_name": "Convolvulaceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Rejuvenative, Reproductive health, Digestive aid",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a seed."
    },
    "tejapatra": {
        "english_name": "Tejapatra",
        "tamil_name": "à®¤à¯‡à®œà®ªà®¤à¯à®°à®®à¯",
        "sanskrit_name": "à¤¤à¥‡à¤œà¤ªà¤¤à¥à¤°",
        "botanical_name": "Cinnamomum tamala",
        "family_name": "Lauraceae",
        "chemical_composition": "Essential oils, Tannins",
        "rasa": "Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Flavoring agent",
        "dose": "As prescribed by a qualified healthcare professional. Typically used as a spice or in herbal formulations."
    },
    "tuvaraka": {
        "english_name": "Henbane, black henbane, or stinking nightshade",
        "tamil_name": "à®•à¯à®°à®¾à®šà®¾à®©à®¿ à®“à®®à®®à¯",
        "sanskrit_name": "à¤¤à¥à¤µà¤°à¤•",
        "botanical_name": "Hyoscyamus niger",
        "family_name": "Solanaceae",
        "chemical_composition": "Alkaloids, Scopolamine",
        "rasa": "Tikta, Katu",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Analgesic, Sedative, Respiratory support (under medical supervision)",
        "dose": "As prescribed by a qualified healthcare professional. Use under medical supervision only."
    },
    "udumbara": {
        "english_name": "Fig Fruit",
        "tamil_name": "à®…à®¤à¯à®¤à®¿",
        "sanskrit_name": "à¤‰à¤¦à¥à¤®à¥à¤¬à¤°",
        "botanical_name": "Ficus racemosa",
        "family_name": "Moraceae",
        "chemical_composition": "Flavonoids, Tannins",
        "rasa": "Madhura, Tikta",
        "guna": "Guru, Snigdha",
        "virya": "Shita",
        "vipaka": "Madhura",
        "amayoga": "Balances Vata and Pitta doshas, may increase Kapha in excess",
        "prayoga": "Rejuvenative, Digestive aid, Skin care",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a fruit."
    },
    "vamsa": {
        "english_name": "Bamboo",
        "tamil_name": "à®®à¯‚à®™à¯à®•à®¿à®²à¯",
        "sanskrit_name": "à¤µà¤‚à¤¶",
        "botanical_name": "Bambusa arundinacea",
        "family_name": "Poaceae",
        "chemical_composition": "Silica, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Bone health, Digestive aid, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as bamboo shoots."
    },
    "vata": {
        "english_name": "Banyan tree",
        "tamil_name": "à®†à®²à®®à®°à®®à¯",
        "sanskrit_name": "à¤µà¤¾à¤¤",
        "botanical_name": "Ficus benghalensis",
        "family_name": "Moraceae",
        "chemical_composition": "Tannins, Flavonoids",
        "rasa": "Katu, Tikta",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Digestive aid, Respiratory support, Joint health",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a fruit."
    },
    "vatada": {
        "english_name": "Almond",
        "tamil_name": "à®ªà®¾à®¤à®®à¯ à®•à¯†à®¾à®Ÿà¯à®Ÿà¯ˆ",
        "sanskrit_name": "à¤µà¤Ÿà¤¦",
        "botanical_name": "Prunus amygdalus",
        "family_name": "Rosaceae",
        "chemical_composition": "Amygdalin, Fatty acids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Shita",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Nutrient-rich, Digestive aid, Skin care",
        "dose": "As part of a balanced diet. Typically consumed as almonds or almond oil."
    },
    "vraksamla": {
        "english_name": " garcinia",
        "tamil_name": "à®•à¯à®Ÿà®®à¯à®ªà¯à®³à®¿",
        "sanskrit_name": "à¤µà¥à¤°à¤•à¥à¤·à¤¾à¤®à¥à¤²",
        "botanical_name": "Garcinia cambogia",
        "family_name": "Clusiaceae",
        "chemical_composition": "Hydroxycitric acid (HCA), Xanthones",
        "rasa": "Amla, Katu",
        "guna": "Guru, Snigdha",
        "virya": "Ushna",
        "vipaka": "Amla",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Weight management, Digestive aid, Appetite suppressant",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as an extract."
    },
    "vruddhadaru": {
        "english_name": "Elephant creeper",
        "tamil_name": "à®•à®Ÿà®±à¯à®ªà®¾à®²à¯ˆ",
        "sanskrit_name": "à¤µà¥ƒà¤¦à¥à¤§à¤¦à¤°à¥",
        "botanical_name": "Argyreia speciosa",
        "family_name": "Convolvulaceae",
        "chemical_composition": "Alkaloids, Flavonoids",
        "rasa": "Tikta, Kashaya",
        "guna": "Laghu, Ruksha",
        "virya": "Ushna",
        "vipaka": "Katu",
        "amayoga": "Balances Vata and Kapha doshas, may increase Pitta in excess",
        "prayoga": "Anti-inflammatory, Analgesic, Respiratory support",
        "dose": "As prescribed by a qualified healthcare professional. Typically used in herbal formulations or as a root."
    },


}

welcome_gif_path = '/home/zevilife/ZeviAi/ndIki0z.gif'
sorry_image_path = '/home/zevilife/ZeviAi/ilapuriyala.jpg'
secret_love_image_path = '/home/zevilife/ZeviAi/ezgif.com-crop.jpg'

block_words = ["18+", "explicit", "adult"]

secret_love_words = ["subashdivya", "sudiv"]

secret_love_messages = [
    "You are the Everything of my life! â¤ï¸",
    "Every moment with you is special. ðŸ˜Š",
    "You make my world brighter! ðŸ’“",
]

owner_info = "Created by Dr.D.Subash ðŸ˜Š"


# Function to send a list of active users to the owner's chat
def send_active_users():
    active_user_list = "\n".join([f"{user_id}: {user_info['username']}" for user_id, user_info in active_users.items()])
    bot.send_message(owner_chat_id, f"Active Users:\n{active_user_list}")

def delete_message_after_a_day(chat_id, message_id):
    time.sleep(86400)
    bot.delete_message(chat_id, message_id)

analytics_data = {
    'total_messages_received': 0,
    'unique_users': set(),
    'commands_executed': 0,
    'user_feedback': [],
    'user_details': [],  # New list for storing user details
    'message_details': [],  # New list for storing message details
}


def collect_analytics_data(message):
    user_id = message.from_user.id
    username = message.from_user.username
    message_content = message.text

    analytics_data['total_messages_received'] += 1
    analytics_data['unique_users'].add(user_id)

    if message_content.startswith('/'):
        analytics_data['commands_executed'] += 1

    # Store user details and message content
    user_details = {'user_id': user_id, 'username': username}
    message_details = {'timestamp': datetime.now().isoformat(), 'content': message_content}

    analytics_data['user_details'].append(user_details)
    analytics_data['message_details'].append(message_details)


def scheduler_thread():
    while True:
        schedule.run_pending()
        time.sleep(1)

scheduler_t = threading.Thread(target=scheduler_thread)
scheduler_t.start()



@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    with open(welcome_gif_path, 'rb') as gif:
        bot.send_animation(message.chat.id, gif)

    # Define the rules and responses within the welcome message
    welcome_message = (
        f"Welcome to the zeviai Bot, {username}!\n\n{owner_info}\n\n"
        "Feel free to ask about Ayurvedic drugs, medicines, diseases, say hi, or hello.\n\n"
        "You Need to follow these Rules to use our Bot Effectively :\n"
        "-  Rule 1.Use Correct Searching Words to get Correct Results if not refer correct spelling from text books\n"
        "-  Rule 2.Don't Misuse this bot it involves lots of effort\n"
        "-  Rule 3.Share Your Suggestion Request by Using this command Suggest:_______ \n"
        "      for eg: Suggest:Awesome Bot in Chat\n" )



    sent_message = bot.reply_to(message, welcome_message)


# Use the message_handler decorator for handling suggestions
@bot.message_handler(func=lambda message: message.text.lower().startswith('suggest:'))
def handle_suggestion(message):
    owner_chat_id = '804717276'  # Replace with the owner's chat ID

    # Extract user information
    user_id = message.from_user.id
    username = message.from_user.username
    user_message = message.text.replace('Suggest:', '').strip()

    if user_message:
        suggestion_message = f"New suggestion from {username} (ID: {user_id}):\n\n{user_message}"

        try:
            # Try sending the message with Markdown parsing
            bot.send_message(owner_chat_id, suggestion_message, parse_mode="Markdown")
        except telebot.apihelper.ApiTelegramException as e:
            # If there's an issue, send the message without Markdown parsing
            bot.send_message(owner_chat_id, suggestion_message)

        bot.reply_to(message, "Thank you for your valueable suggestion! The Admin has been notified.")
    else:
        bot.reply_to(message, "Please provide a suggestion.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    collect_analytics_data(message)

    user_message = message.text.lower()
    username = message.from_user.username
    sent_message = None

    # Check for block words
    if any(re.search(fr'\b{word}\b', user_message) for word in block_words):
        with open(sorry_image_path, 'rb') as image:
            bot.send_photo(message.chat.id, image, caption=f"I'm sorry, {username}, the content you've mentioned is not appropriate. Please keep the conversation respectful.")
        return
    else:
        if user_message in secret_love_words:
            with open(secret_love_image_path, 'rb') as image:
                bot.send_photo(message.chat.id, image, caption=random.choice(secret_love_messages))
        else:
            if user_message in ayurvedic_drugs:
                drug_info = ayurvedic_drugs[user_message]
                response = (
                             f"**English Name:** {drug_info['english_name']}\n"
                    f"**Tamil Name:** {drug_info['tamil_name']}\n"
                    f"**Botanical Name:** {drug_info['botanical_name']}\n"
                    f"**Chemical Composition:** {drug_info['chemical_composition']}\n"
                    f"**Rasa:** {drug_info['rasa']}\n"
                    f"**Guna:** {drug_info['guna']}\n"
                    f"**Virya:** {drug_info['virya']}\n"
                    f"**Vipaka:** {drug_info['vipaka']}\n"
                    f"**Amayoga:** {drug_info['amayoga']}\n"
                    f"**Prayoga:** {drug_info['prayoga']}\n"
                    f"**Dose:** {drug_info['dose']}\n"
                    f"**Uses:**\n{', '.join(drug_info['uses'])}\n"
                )
                # Create the inline keyboard buttons with catchy text and emojis
                keyboard = telebot.types.InlineKeyboardMarkup()
                # Add a button to view the drug image
                keyboard.add(telebot.types.InlineKeyboardButton(text="View Drug Image ðŸ–¼ï¸", url=drug_info['image_url']))

                bot.reply_to(message, response, parse_mode="Markdown", reply_markup=keyboard, disable_web_page_preview=False)
            elif user_message in ayurvedic_medicines:
                medicine_info = ayurvedic_medicines[user_message]
                response = (
                    f"**English Name:** {medicine_info['english_name']}\n"
                    f"**Tamil Name:** {medicine_info['tamil_name']}\n"
                    f"**Explanation:** {medicine_info['explanation']}\n"
                    f"**Dose:** {medicine_info['dose']}\n"
                    f"**Uses:**\n{', '.join(medicine_info['main_uses'])}\n"
                    f"**Available Brands:** {', '.join(medicine_info['brands_available'])}"
                )

                # Create the inline keyboard buttons with catchy text and emojis
                keyboard = telebot.types.InlineKeyboardMarkup()

                for link_name, link_urls in medicine_info['buying_links'].items():
                    if isinstance(link_urls, list):  # Handle multiple links
                        for i, link_url in enumerate(link_urls):
                            # Add emojis to button text
                            if link_name == "Amazon":
                                button_text = f"Buy on Amazon {i+1} ðŸ›’"
                            elif link_name == "Flipkart":
                                button_text = f"Get it on Flipkart {i+1} ðŸ›’"
                            elif link_name == "Ayurvedic Store":
                                button_text = f"Shop at Ayurvedic Store {i+1} ðŸ›’"
                            else:
                                button_text = f"{link_name} {i+1}"  # Use the original name if not specified above

                            keyboard.add(telebot.types.InlineKeyboardButton(text=button_text, url=link_url))
                    else:
                        # Add emojis to button text
                        if link_name == "Amazon":
                            button_text = "Buy on Amazon ðŸ›’"
                        elif link_name == "Flipkart":
                            button_text = "Get it on Flipkart ðŸ›’"
                        elif link_name == "Ayurvedic Store":
                            button_text = "Shop at Ayurvedic Store ðŸ›’"
                        else:
                            button_text = link_name  # Use the original name if not specified above

                        keyboard.add(telebot.types.InlineKeyboardButton(text=button_text, url=link_urls))

                bot.send_message(message.chat.id, response, parse_mode="Markdown", reply_markup=keyboard)
            elif user_message in diseases_info:
                disease_info = diseases_info[user_message]
                response = f"**Disease:** {user_message.capitalize()}\n**Explanation:** {disease_info['explanation']}"
                bot.reply_to(message, response, parse_mode="Markdown")
            elif user_message in non_detailed_drugs:
                drug_info = non_detailed_drugs[user_message]
                response = (
                    f"**English Name:** {drug_info['english_name']}\n"
                    f"**Tamil Name:** {drug_info['tamil_name']}\n"
                    f"**Sanskrit Namae:** {drug_info['sanskrit_name']}\n"
                    f"**Botanical Name:** {drug_info['botanical_name']}\n"
                    f"**Family Name:**{drug_info['family_name']}\n"
                    f"**Chemical Composition:**{drug_info['chemical_composition']}\n"
                    f"**Rasa:** {drug_info['rasa']}\n"
                    f"**Guna:** {drug_info['guna']}\n"
                    f"**Virya:** {drug_info['virya']}\n"
                    f"**Vipaka:** {drug_info['vipaka']}\n"
                    f"**Amayoga:** {drug_info['amayoga']}\n"
                    f"**Prayoga:** {drug_info['prayoga']}\n"
                    f"**Dose:**{drug_info['dose']}\n"
                )
                bot.reply_to(message,response, parse_mode="Markdown")
            elif user_message in ["hi", "hello"]:
                bot.reply_to(message, f"Hello, {username}! How can I assist you today?")
            elif user_message in ["who are you", "what are you", "who is this"]:
                bot.reply_to(message, "I am the zeviai Bot. I can provide information about Ayurvedic drugs, medicines, and diseases. How can I assist you?")
            elif user_message in ["thanks", "thank you", "nandri"]:
                bot.reply_to(message, f"You're welcome, {username}! If you have more questions, feel free to ask.")
            else:
                # Code block for the else statement
                # Indentation is crucial here
                with open(sorry_image_path, 'rb') as image_file:
                    sorry_image = image_file.read()
                # Additional code within the else block
                sent_message = bot.send_photo(message.chat.id, photo=sorry_image, caption=f"I'm sorry, {username}, I don't have information about that. Please ask about Ayurvedic drugs, medicines, diseases, or say hi or hello.")
            # Schedule a task to delete the message after a day
            if sent_message:
                schedule.every().day.at("19:00").do(delete_message_after_a_day, message.chat.id, sent_message.message_id)

# Function to send daily analytics to the bot owner
def send_daily_analytics():
    owner_chat_id = '804717276'
    total_messages = analytics_data['total_messages_received']
    unique_users = len(analytics_data['unique_users'])
    commands_executed = analytics_data['commands_executed']

    # Compile user details and message details
    user_details = analytics_data['user_details']
    message_details = analytics_data['message_details']

    # Prepare the analytics message
    analytics_message = (
        f"Daily Analytics:\n\nTotal Messages Received: {total_messages}\n"
        f"Unique Users: {unique_users}\nCommands Executed: {commands_executed}\n\n"
        f"User Details:\n{user_details}\n\nMessage Details:\n{message_details}"
    )

    bot.send_message(owner_chat_id, analytics_message)


# Schedule daily analytics
schedule.every().day.at("20:00").do(send_daily_analytics)



# Start the bot polling
bot.polling()


