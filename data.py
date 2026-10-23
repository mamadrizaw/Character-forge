
# -*- coding: utf-8 -*-
"""Character Forge 2.0 — game data."""

ABILITIES = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

ABILITY_NAMES_FA = {
    "STR": "قدرت",
    "DEX": "چابکی",
    "CON": "استقامت",
    "INT": "هوش",
    "WIS": "حکمت",
    "CHA": "جاذبه",
}

CLASSES = {
    "Barbarian": {
        "fa": "بربر", "hit_die": 12,
        "priority": ["STR", "CON", "DEX"],
        "saves": ["STR", "CON"],
        "skills": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
        "equipment": "تبر جنگی، دو تبر دستی، چهار نیزه و بستهٔ کاوشگر",
        "feature": "خشم جنگجو؛ در نبرد می‌تواند وارد حالت خشم شود و ضربات نیرومندتری بزند.",
    },
    "Bard": {
        "fa": "نغمه‌سرا", "hit_die": 8,
        "priority": ["CHA", "DEX", "CON"],
        "saves": ["DEX", "CHA"],
        "skills": ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"],
        "equipment": "سلاح ظریف، ساز موسیقی، زره چرمی و بستهٔ هنرمند",
        "feature": "الهام‌بخشی؛ با سخن یا موسیقی به هم‌رزمانش انگیزه می‌دهد.",
    },
    "Cleric": {
        "fa": "روحانی", "hit_die": 8,
        "priority": ["WIS", "CON", "STR"],
        "saves": ["WIS", "CHA"],
        "skills": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        "equipment": "سپر، سلاح ساده، نماد مقدس و زره",
        "feature": "نیروی الهی؛ از نیروی مقدس برای درمان، محافظت یا مقابله با دشمنان بهره می‌برد.",
    },
    "Druid": {
        "fa": "دروید", "hit_die": 8,
        "priority": ["WIS", "CON", "DEX"],
        "saves": ["INT", "WIS"],
        "skills": ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
        "equipment": "سپر چوبی، عصای طبیعت‌گردی، نماد طبیعت و بستهٔ کاوشگر",
        "feature": "پیوند طبیعت؛ جادوی او از نیروهای طبیعی و چرخهٔ زندگی سرچشمه می‌گیرد.",
    },
    "Fighter": {
        "fa": "جنگجو", "hit_die": 10,
        "priority": ["STR", "DEX", "CON"],
        "saves": ["STR", "CON"],
        "skills": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
        "equipment": "زره، سلاح جنگی، سپر و بستهٔ کاوشگر",
        "feature": "استراحت جنگی؛ می‌تواند در لحظه‌ای حساس بخشی از نیروی خود را بازیابی کند.",
    },
    "Monk": {
        "fa": "راهب", "hit_die": 8,
        "priority": ["DEX", "WIS", "CON"],
        "saves": ["STR", "DEX"],
        "skills": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
        "equipment": "سلاح ساده، دارت و بستهٔ کاوشگر",
        "feature": "هنرهای رزمی؛ سرعت، تمرکز و ضربات دقیق را در مبارزه به کار می‌گیرد.",
    },
    "Paladin": {
        "fa": "پالادین", "hit_die": 10,
        "priority": ["STR", "CHA", "CON"],
        "saves": ["WIS", "CHA"],
        "skills": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
        "equipment": "زره سنگین، سپر، سلاح جنگی و نماد مقدس",
        "feature": "سوگند مقدس؛ باور و عهد او می‌تواند نیرویی مقدس به حملاتش ببخشد.",
    },
    "Ranger": {
        "fa": "ره‌یاب", "hit_die": 10,
        "priority": ["DEX", "WIS", "CON"],
        "saves": ["STR", "DEX"],
        "skills": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
        "equipment": "کمان، شمشیر کوتاه، زره چرمی و بستهٔ کاوشگر",
        "feature": "ردیابی؛ در طبیعت رد دشمنان و مسیرهای پنهان را پیدا می‌کند.",
    },
    "Rogue": {
        "fa": "دزدماهر", "hit_die": 8,
        "priority": ["DEX", "INT", "CON"],
        "saves": ["DEX", "INT"],
        "skills": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
        "equipment": "زره چرمی، دو خنجر، ابزار دزدی و کمان دستی",
        "feature": "حملهٔ غافلگیرانه؛ از فرصت مناسب برای وارد کردن ضربه‌ای دقیق استفاده می‌کند.",
    },
    "Sorcerer": {
        "fa": "جادوگر ذاتی", "hit_die": 6,
        "priority": ["CHA", "CON", "DEX"],
        "saves": ["CON", "CHA"],
        "skills": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
        "equipment": "دو خنجر، کیف اجزای جادو و یادگاری اسرارآمیز",
        "feature": "جادوی ذاتی؛ نیروی جادویی از درون او سرچشمه می‌گیرد.",
    },
    "Warlock": {
        "fa": "پیمان‌دار", "hit_die": 8,
        "priority": ["CHA", "CON", "DEX"],
        "saves": ["WIS", "CHA"],
        "skills": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
        "equipment": "سلاح ساده، زره سبک و نشانه‌ای از پیمان اسرارآمیز",
        "feature": "پیمان فراطبیعی؛ قدرتش را از پیوندی مرموز با موجودی قدرتمند می‌گیرد.",
    },
    "Wizard": {
        "fa": "جادوگر دانش‌آموخته", "hit_die": 6,
        "priority": ["INT", "CON", "DEX"],
        "saves": ["INT", "WIS"],
        "skills": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
        "equipment": "کتاب جادو، عصا، کیف اجزای جادو و بستهٔ دانشمند",
        "feature": "مطالعهٔ جادو؛ دانش و تمرین به او امکان می‌دهد طلسم‌های پیچیده اجرا کند.",
    },
}

RACES = {
    "Human": {
        "fa": "انسان", "bonuses": {"STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1},
        "subraces": ["انسان معمولی"], "traits": "سازگار، بلندپرواز و متنوع",
    },
    "Elf": {
        "fa": "الف", "bonuses": {"DEX": 2},
        "subraces": ["الف بلندمرتبه", "الف جنگلی", "الف تاریک"],
        "traits": "حواس تیز، دید در تاریکی و پیوندی کهن با جادو",
    },
    "Dwarf": {
        "fa": "کوتوله", "bonuses": {"CON": 2},
        "subraces": ["کوتولهٔ تپه‌ای", "کوتولهٔ کوهستانی"],
        "traits": "استوار، مقاوم و آشنا با سنگ و فلز",
    },
    "Halfling": {
        "fa": "نیم‌قد", "bonuses": {"DEX": 2},
        "subraces": ["نیم‌قد سبک‌پا", "نیم‌قد نیرومند"],
        "traits": "چابک، خوش‌اقبال و وفادار به دوستان",
    },
    "Dragonborn": {
        "fa": "اژدهازاد", "bonuses": {"STR": 2, "CHA": 1},
        "subraces": ["تبار اژدهای سرخ", "تبار اژدهای آبی", "تبار اژدهای طلایی"],
        "traits": "میراث اژدهایی و پیوند با نیروی عنصری",
    },
    "Gnome": {
        "fa": "گنوم", "bonuses": {"INT": 2},
        "subraces": ["گنوم جنگلی", "گنوم سنگی"],
        "traits": "کنجکاو، زیرک و مشتاق کشف رازهای جادویی",
    },
    "Half-Elf": {
        "fa": "نیمه‌الف", "bonuses": {"CHA": 2, "DEX": 1, "WIS": 1},
        "subraces": ["نیمه‌الف معمولی"],
        "traits": "میان دو فرهنگ رشد کرده و در تعامل اجتماعی انعطاف‌پذیر است",
    },
    "Half-Orc": {
        "fa": "نیمه‌اورک", "bonuses": {"STR": 2, "CON": 1},
        "subraces": ["نیمه‌اورک معمولی"],
        "traits": "نیرومند، سرسخت و دشوار برای شکست دادن",
    },
    "Tiefling": {
        "fa": "تیفلینگ", "bonuses": {"CHA": 2, "INT": 1},
        "subraces": ["تبار جهنمی", "تبار مغاکی"],
        "traits": "میراث فراطبیعی، ظاهری متمایز و پیوند با نیروهای اسرارآمیز",
    },
    "Aasimar": {
        "fa": "آسیمر", "bonuses": {"CHA": 2, "WIS": 1},
        "subraces": ["محافظ", "سوخته", "سقوط‌کرده"],
        "traits": "میراثی آسمانی و پیوندی با نور یا داوری",
    },
    "Goliath": {
        "fa": "گولیات", "bonuses": {"STR": 2, "CON": 1},
        "subraces": ["گولیات کوهستانی"],
        "traits": "اندامی تنومند، تحمل بالا و فرهنگ رقابت",
    },
    "Orc": {
        "fa": "اورک", "bonuses": {"STR": 2, "CON": 1},
        "subraces": ["اورک خاکستری"],
        "traits": "نیرومند، پرتحرک و دارای اراده‌ای سرسخت",
    },
    "Tabaxi": {
        "fa": "تباکسی", "bonuses": {"DEX": 2, "CHA": 1},
        "subraces": ["تباکسی معمولی"],
        "traits": "چابک، کنجکاو و مشتاق کشف سرزمین‌های دور",
    },
    "Firbolg": {
        "fa": "فایربالگ", "bonuses": {"WIS": 2, "STR": 1},
        "subraces": ["فایربالگ معمولی"],
        "traits": "آرام، طبیعت‌دوست و آشنا با جادوی پنهان جنگل",
    },
}

BACKGROUNDS = {
    "Acolyte": {
        "fa": "خدمت‌گزار معبد", "skills": ["Insight", "Religion"],
        "hook": "در معبدی دورافتاده به رازی برخورده که بزرگان از آن سخن نمی‌گویند.",
    },
    "Charlatan": {
        "fa": "حقه‌باز", "skills": ["Deception", "Sleight of Hand"],
        "hook": "هویت جعلی قدیمی‌اش ناگهان در شهری مهم دوباره ظاهر شده است.",
    },
    "Criminal": {
        "fa": "تبهکار", "skills": ["Deception", "Stealth"],
        "hook": "سازمان سابقش اکنون طلبی خطرناک از او دارد.",
    },
    "Entertainer": {
        "fa": "هنرمند", "skills": ["Acrobatics", "Performance"],
        "hook": "ترانه‌ای که اجرا می‌کند، ناخواسته پیام یک توطئه را در خود دارد.",
    },
    "Folk Hero": {
        "fa": "قهرمان مردمی", "skills": ["Animal Handling", "Survival"],
        "hook": "مردم زادگاهش او را ناجی می‌دانند، اما حقیقت آن روز پیچیده‌تر است.",
    },
    "Guild Artisan": {
        "fa": "صنعتگر صنفی", "skills": ["Insight", "Persuasion"],
        "hook": "سفارشی ویژه که ساخته، نشانی از خاندانی گمشده دارد.",
    },
    "Hermit": {
        "fa": "گوشه‌نشین", "skills": ["Medicine", "Religion"],
        "hook": "در دوران انزوا کشفی کرده که شاید تعادل جهان را تغییر دهد.",
    },
    "Noble": {
        "fa": "اشراف‌زاده", "skills": ["History", "Persuasion"],
        "hook": "خانواده‌اش درگیر رقابت جانشینی است و نام او در وصیتی محرمانه آمده.",
    },
    "Outlander": {
        "fa": "آوارهٔ سرزمین‌های وحشی", "skills": ["Athletics", "Survival"],
        "hook": "ردی را در طبیعت دنبال می‌کند که هیچ نقشه‌ای آن را ثبت نکرده است.",
    },
    "Sage": {
        "fa": "دانشمند", "skills": ["Arcana", "History"],
        "hook": "صفحه‌ای از نسخه‌ای باستانی ناپدید شده و تنها او می‌داند چه چیزی در آن بوده.",
    },
    "Sailor": {
        "fa": "ملوان", "skills": ["Athletics", "Perception"],
        "hook": "کشتی پیشینش در نقشه‌ها غرق شده، اما هر ماه در افق دیده می‌شود.",
    },
    "Soldier": {
        "fa": "سرباز", "skills": ["Athletics", "Intimidation"],
        "hook": "فرماندهٔ سابقش دستوری غیرممکن داده بود؛ اکنون شاهدی تازه پیدا شده است.",
    },
    "Urchin": {
        "fa": "کودک خیابانی", "skills": ["Sleight of Hand", "Stealth"],
        "hook": "پیامی رمزگذاری‌شده از شبکهٔ کودکان خیابانی به دستش رسیده است.",
    },
}

ALIGNMENTS = [
    "قانون‌مدار نیک", "خنثی نیک", "آشوب‌گرا نیک",
    "قانون‌مدار خنثی", "خنثی حقیقی", "آشوب‌گرا خنثی",
    "قانون‌مدار شرور", "خنثی شرور", "آشوب‌گرا شرور",
]

FIRST_NAMES = [
    "آرِن", "لیورا", "دارین", "میرال", "کِیل", "سِرین", "رُوان", "نیما",
    "اِلارا", "تورِن", "وِسرا", "آریون", "کاسیا", "رِین", "مارِک", "تالیا",
    "آدرین", "وِرنا", "سورِن", "ناریا",
]
SURNAMES = [
    "سایه‌زاد", "آذرپیکر", "ماه‌رو", "سنگ‌دل", "سپیده‌بان", "کلاغ‌نشان",
    "توفان‌زاد", "خاکسترین", "شب‌گرد", "رودآواز", "تیغ‌سپید", "رازنگار",
    "یخ‌نشان", "آهن‌دل", "مه‌پوش",
]

NPC_ROLES = [
    "جادوگری تبعیدی", "فرمانده‌ای زخمی", "دلالی مرموز", "وارثی گمشده",
    "کشیشی شکاک", "شکارچی هیولاها", "خبرچینی ناشناس", "نگهبان دروازه‌ای باستانی",
]
PLACES = [
    "قلعهٔ فروریختهٔ وِرِن", "جنگل زمزمه‌گر", "بندر مه‌گرفتهٔ آذرین",
    "آرشیو زیرزمینی شاهان", "درهٔ استخوان‌های سفید", "شهر بی‌خورشید",
    "معبد مدفون در یخ", "بازار پنهان زیر شهر", "برج ساعتِ متوقف‌شده",
]
THREATS = [
    "فرقه‌ای که نام خدای خود را فراموش کرده در حال گردآوری ارتشی پنهانی است",
    "اژدهایی خاطرات مردم را می‌بلعد و تاریخ شهرها را تغییر می‌دهد",
    "طاعونی جادویی سایه‌ها را زنده می‌کند",
    "وارثی که از تاریخ پاک شده برای بازپس‌گیری تاج بازگشته است",
    "دروازه‌ای به آینده باز شده و موجوداتی ناشناخته از آن عبور می‌کنند",
    "پادشاهی که سال‌ها پیش مرده هنوز از پشت پرده فرمان می‌دهد",
]
TREASURES = [
    "نقشه‌ای که مسیرش هر شب عوض می‌شود",
    "شمشیری که نام صاحب بعدی را زمزمه می‌کند",
    "مهری با نشان یک خاندان منقرض‌شده",
    "قطعه‌ای از ستاره‌ای سقوط‌کرده",
    "کتابی که فقط در خواب خوانده می‌شود",
    "کلیدی که هیچ قفلی را دوبار باز نمی‌کند",
]
SECRETS = [
    "یکی از متحدان آینده‌اش به دشمن خدمت می‌کند",
    "قهرمان در گذشته ناخواسته باعث نجات دشمن شده است",
    "این تهدید در واقع می‌کوشد از فاجعه‌ای بزرگ‌تر جلوگیری کند",
    "نام واقعی شخصیت در سندی ممنوعه ثبت شده است",
    "شخصی که مرده تصور می‌شد، از دور مراقب اوست",
    "گنج مورد جست‌وجو در حقیقت زندانی است که نباید آزاد شود",
]
