import random

import numpy as np
import requests
from tg.secrets import API_KEY


def random_name(gender, ethnicity="English"):
    usage = ethnicity_to_code[ethnicity]
    if gender == "mf":
        req_string = f"http://www.behindthename.com/api/random.json?usage={usage}&number=1&randomsurname=yes&key={API_KEY}"
    else:
        req_string = f"http://www.behindthename.com/api/random.json?gender={gender}&usage={usage}&number=1&randomsurname=yes&key={API_KEY}"
    try:
        n = " ".join(requests.get(req_string, timeout=10).json()["names"])
        if "href" in n:
            n = " ".join(
                [n.split(" ")[0], n.split(" ")[-1].split(">")[-2].split("<")[0]]
            )
        return n
    except KeyError:
        return f"Random Name {random.randint(0, 100000000000)}"
    except requests.ReadTimeout:
        return f"Random Name {random.randint(0, 100000000000)}"


def random_ethnicity():
    return random.choice(list(ethnicity_to_code.keys()))


ethnicity_to_code = {
    "Akan": "aka",
    "Albanian": "alb",
    "Algonquin": "alg",
    "Indigenous American": "ame",
    "Amharic": "amh",
    "Ancient": "anci",
    "Apache": "apa",
    "Arabic": "ara",
    "Armenian": "arm",
    "Assamese": "asm",
    "Asturian": "ast",
    "Indigenous Australian": "aus",
    "Avar": "ava",
    "Aymara": "aym",
    "Azerbaijani": "aze",
    "Balinese": "bal",
    "Basque": "bas",
    "Belarusian": "bel",
    "Bengali": "ben",
    "Berber": "ber",
    "Bhutanese": "bhu",
    "Bosnian": "bos",
    "Breton": "bre",
    "Bashkir": "bsh",
    "Bulgarian": "bul",
    "Burmese": "bur",
    "Catalan": "cat",
    "Ancient Celtic": "cela",
    "Chewa": "cew",
    "Chamorro": "cha",
    "Chechen": "che",
    "Chinese": "chi",
    "Cherokee": "chk",
    "Choctaw": "cht",
    "Cheyenne": "chy",
    "Circassian": "cir",
    "Comorian": "cmr",
    "Comanche": "com",
    "Coptic": "cop",
    "Cornish": "cor",
    "Cree": "cre",
    "Croatian": "cro",
    "Corsican": "crs",
    "Czech": "cze",
    "Danish": "dan",
    "Dhivehi": "dhi",
    "Dutch": "dut",
    "Ancient Egyptian": "egya",
    "English": "eng",
    "Anglo-Saxon": "enga",
    "Esperanto": "esp",
    "Estonian": "est",
    "Ethiopian": "eth",
    "Ewe": "ewe",
    "Faroese": "fae",
    "Fijian": "fij",
    "Filipino": "fil",
    "Finnish": "fin",
    "Flemish": "fle",
    "French": "fre",
    "Frisian": "fri",
    "Fula": "ful",
    "Ga": "gaa",
    "Galician": "gal",
    "Ganda": "gan",
    "Georgian": "geo",
    "German": "ger",
    "Ancient Germanic": "gmca",
    "Greek": "gre",
    "Ancient Greek": "grea",
    "Greenlandic": "grn",
    "Guarani": "gua",
    "Gujarati": "guj",
    "Hausa": "hau",
    "Hawaiian": "haw",
    "Hebrew": "heb",
    "Hindi": "hin",
    "History": "hist",
    "Hmong": "hmo",
    "Hungarian": "hun",
    "Ibibio": "ibi",
    "Icelandic": "ice",
    "Igbo": "igb",
    "Indian": "ind",
    "Ingush": "ing",
    "Indonesian": "ins",
    "Inuit": "inu",
    "Irish": "iri",
    "Iroquois": "iro",
    "Italian": "ita",
    "Japanese": "jap",
    "Javanese": "jav",
    "Jèrriais": "jer",
    "Jewish": "jew",
    "Kannada": "kan",
    "Kazakh": "kaz",
    "Khmer": "khm",
    "Kiga": "kig",
    "Kikuyu": "kik",
    "Kongo": "kon",
    "Korean": "kor",
    "Kurdish": "kur",
    "Kyrgyz": "kyr",
    "Lao": "lao",
    "Latvian": "lat",
    "Limburgish": "lim",
    "Lithuanian": "lth",
    "Luhya": "luh",
    "Luo": "luo",
    "Macedonian": "mac",
    "Maguindanao": "mag",
    "Maltese": "mal",
    "Manx": "man",
    "Maori": "mao",
    "Mapuche": "map",
    "Mari": "mar",
    "Mayan": "may",
    "Mbundu": "mbu",
    "Medieval": "medi",
    "Malayalam": "mlm",
    "Malay": "mly",
    "Mohawk": "moh",
    "Mongolian": "mon",
    "Mormon": "morm",
    "Marathi": "mrt",
    "Mwera": "mwe",
    "Nahuatl": "nah",
    "Navajo": "nav",
    "Ndebele": "nde",
    "Ancient Near Eastern": "neaa",
    "Nepali": "nep",
    "Norwegian": "nor",
    "Norman": "nrm",
    "Nuu-chah-nulth": "nuu",
    "Occitan": "occ",
    "Odia": "odi",
    "Ojibwe": "oji",
    "Oneida": "one",
    "Oromo": "oro",
    "Ossetian": "oss",
    "Pashto": "pas",
    "Picard": "pcd",
    "Persian": "per",
    "Pintupi": "pin",
    "Polish": "pol",
    "Portuguese": "por",
    "Powhatan": "pow",
    "Punjabi": "pun",
    "Quechua": "que",
    "Romanian": "rmn",
    "Ancient Roman": "roma",
    "Russian": "rus",
    "Sami": "sam",
    "Sardinian": "sar",
    "Low German": "sax",
    "Ancient Scandinavian": "scaa",
    "Scottish": "sco",
    "Scots": "sct",
    "Seneca": "sen",
    "Serbian": "ser",
    "Shawnee": "sha",
    "Shona": "sho",
    "Sicilian": "sic",
    "Siksika": "sik",
    "Sinhalese": "sin",
    "Sioux": "sio",
    "Slavic": "sla",
    "Slovak": "slk",
    "Slovene": "sln",
    "Samoan": "smn",
    "Somali": "som",
    "Sorbian": "sor",
    "Sotho": "sot",
    "Spanish": "spa",
    "Swahili": "swa",
    "Swedish": "swe",
    "Swazi": "swz",
    "Tagalog": "tag",
    "Tahitian": "tah",
    "Tajik": "taj",
    "Tamil": "tam",
    "Tatar": "tat",
    "Tausug": "tau",
    "Telugu": "tel",
    "Thai": "tha",
    "Tibetan": "tib",
    "Turkmen": "tkm",
    "Tongan": "ton",
    "Tooro": "too",
    "Tswana": "tsw",
    "Tumbuka": "tum",
    "Tupi": "tup",
    "Turkish": "tur",
    "Ukrainian": "ukr",
    "Urdu": "urd",
    "Urhobo": "urh",
    "American": "usa",
    "Uyghur": "uyg",
    "Uzbek": "uzb",
    "Various": "vari",
    "Vietnamese": "vie",
    "Welsh": "wel",
    "Xhosa": "xho",
    "Yao": "yao",
    "Yolngu": "yol",
    "Yoruba": "yor",
    "Zapotec": "zap",
    "Zulu": "zul",
}


def random_height(sex):
    if sex == "Male":
        mu = 171
    elif sex == "Female":
        mu = 159
    else:
        mu = 165
    sigma = 6
    height_in_cm = np.random.normal(loc=mu, scale=sigma)
    height_in_in = int(height_in_cm / 2.54)
    feet = height_in_in // 12
    inch = height_in_in % 12
    return f"{feet}'{inch}\""


def random_weight(sex):
    if sex == "Male":
        mu = 73.1
        sigma = 10.46
    elif sex == "Female":
        mu = 57
        sigma = 8.84
    else:
        mu = 65
        sigma = 9.65
    weight_in_kg = np.random.normal(loc=mu, scale=sigma)
    weight_in_lb = int(weight_in_kg * 2.205)
    return f"{weight_in_lb} lbs"
