
# -*- coding: utf-8 -*-
"""Character Forge 2.0 — character generation engine."""

import random

from data import (
    ABILITIES,
    ABILITY_NAMES_FA,
    CLASSES,
    RACES,
    BACKGROUNDS,
    FIRST_NAMES,
    SURNAMES,
    NPC_ROLES,
    PLACES,
    THREATS,
    TREASURES,
    SECRETS,
)


def roll_4d6_drop_lowest():
    """Roll four six-sided dice and discard the lowest die."""
    dice = [random.randint(1, 6) for _ in range(4)]
    kept = sorted(dice)[1:]
    return {
        "dice": dice,
        "kept": kept,
        "score": sum(kept),
        "dropped": min(dice),
    }


def ability_modifier(score):
    """D&D-style ability modifier."""
    return (score - 10) // 2


def signed(number):
    return f"+{number}" if number >= 0 else str(number)


def proficiency_bonus(level):
    """Simplified 5e proficiency progression."""
    return 2 + (level - 1) // 4


def calculate_hit_points(level, hit_die, constitution_modifier):
    """Maximum HP using max hit die at level 1 and average thereafter."""
    first_level_hp = hit_die + constitution_modifier
    average_after_first = (hit_die // 2) + 1 + constitution_modifier
    return max(1, first_level_hp + max(0, level - 1) * average_after_first)


def roll_and_assign_abilities(class_name, race_name, apply_racial_bonuses=True):
    """
    Roll six ability scores, assign the highest scores to the selected
    class's primary abilities, then apply racial bonuses.
    """
    rolls = [roll_4d6_drop_lowest() for _ in ABILITIES]
    sorted_scores = sorted(
        [roll["score"] for roll in rolls],
        reverse=True,
    )

    priority = CLASSES[class_name]["priority"]
    assigned = {}

    # Assign the highest scores to the class's key abilities.
    for ability, score in zip(priority, sorted_scores):
        assigned[ability] = score

    # Assign the remaining scores to abilities not yet assigned.
    remaining_abilities = [
        ability for ability in ABILITIES if ability not in assigned
    ]
    remaining_scores = sorted_scores[len(priority):]

    for ability, score in zip(remaining_abilities, remaining_scores):
        assigned[ability] = score

    racial_bonuses = (
        RACES[race_name]["bonuses"] if apply_racial_bonuses else {}
    )

    stats = {}
    for ability in ABILITIES:
        base_score = assigned[ability]
        racial_bonus = racial_bonuses.get(ability, 0)
        final_score = min(20, base_score + racial_bonus)

        stats[ability] = {
            "name": ABILITY_NAMES_FA[ability],
            "base": base_score,
            "racial_bonus": racial_bonus,
            "score": final_score,
            "modifier": ability_modifier(final_score),
        }

    return stats, rolls


def generate_story(name, race_name, subrace, class_name, background):
    """Compose a fantasy backstory from reusable story elements."""
    race = RACES[race_name]
    char_class = CLASSES[class_name]
    bg = BACKGROUNDS[background]

    npc = random.choice(NPC_ROLES)
    place = random.choice(PLACES)
    threat = random.choice(THREATS)
    treasure = random.choice(TREASURES)
    secret = random.choice(SECRETS)

    opening = (
        f"{name}، {race['fa']} از تبار «{subrace}» و "
        f"{bg['fa']}، مدت‌ها کوشیده گذشته‌اش را پشت سر بگذارد. "
        f"{bg['hook']}"
    )

    turning_point = (
        f"اما با رسیدن نامه‌ای بی‌نام، زندگی او تغییر می‌کند. "
        f"نامه او را به {place} می‌کشاند؛ جایی که {threat}. "
        f"رد این ماجرا به {treasure} می‌رسد، شیئی که بسیاری حاضرند "
        f"برای تصاحبش دست به هر کاری بزنند."
    )

    encounter = (
        f"در مسیر، {name} با {npc} روبه‌رو می‌شود. این غریبه ادعا می‌کند "
        f"راه‌حل را می‌داند، اما حقیقتی پنهان است: {secret}. "
        f"{name} باید با مهارت‌های خود به‌عنوان {char_class['fa']} "
        f"از میان خطرها عبور کند و تصمیم بگیرد به چه کسی اعتماد کند."
    )

    ending = (
        "سرنوشت این ماجرا از پیش تعیین نشده است. انتخاب‌های قهرمان می‌توانند "
        "او را به نجات‌دهندهٔ یک سرزمین، متحد دشمنان قدیمی یا کسی تبدیل کنند "
        "که حقیقتی خطرناک را برای همیشه دفن می‌کند."
    )

    threads = [
        {
            "title": "مسیر اول: راز باستانی",
            "description": (
                f"سرنخ اصلی در {place} پنهان است. اسناد ناقص، شاهدان ترسان "
                "و نشانه‌هایی جادویی می‌توانند حقیقت را آشکار کنند."
            ),
        },
        {
            "title": "مسیر دوم: اتحاد ناپایدار",
            "description": (
                f"{npc} پیشنهادی می‌دهد که ممکن است متحدی قدرتمند بسازد؛ "
                "اما پذیرفتن آن می‌تواند بهای سنگینی داشته باشد."
            ),
        },
        {
            "title": "مسیر سوم: انتخاب دشوار",
            "description": (
                f"برای متوقف کردن تهدید، قهرمان باید بین حفظ {treasure}، "
                "نجات گروهی بی‌گناه و آشکار کردن {secret} یکی را در اولویت بگذارد."
            ),
        },
    ]

    return {
        "text": "\n\n".join([opening, turning_point, encounter, ending]),
        "npc": npc,
        "location": place,
        "threat": threat,
        "treasure": treasure,
        "secret": secret,
        "threads": threads,
    }


def generate_character(
    level=1,
    race_name="Human",
    subrace=None,
    class_name="Fighter",
    background="Folk Hero",
    alignment="خنثی نیک",
    apply_racial_bonuses=True,
):
    """Generate a complete character record."""
    level = max(1, min(20, int(level)))

    if race_name not in RACES:
        race_name = "Human"
    if class_name not in CLASSES:
        class_name = "Fighter"
    if background not in BACKGROUNDS:
        background = "Folk Hero"

    if subrace not in RACES[race_name]["subraces"]:
        subrace = RACES[race_name]["subraces"][0]

    stats, roll_log = roll_and_assign_abilities(
        class_name,
        race_name,
        apply_racial_bonuses,
    )

    class_data = CLASSES[class_name]
    background_data = BACKGROUNDS[background]

    # Two class skills are selected randomly in this simplified version.
    number_of_class_skills = min(2, len(class_data["skills"]))
    class_skills = random.sample(
        class_data["skills"],
        number_of_class_skills,
    )

    # Background skills are included automatically.
    all_skills = sorted(set(class_skills + background_data["skills"]))

    prof_bonus = proficiency_bonus(level)
    hit_die = class_data["hit_die"]
    con_mod = stats["CON"]["modifier"]
    hp = calculate_hit_points(level, hit_die, con_mod)

    name = f"{random.choice(FIRST_NAMES)} {random.choice(SURNAMES)}"

    story = generate_story(
        name,
        race_name,
        subrace,
        class_name,
        background,
    )

    # Saving throw bonuses include proficiency in the class's saving throws.
    saving_throws = {}
    for ability in ABILITIES:
        total = stats[ability]["modifier"]
        proficient = ability in class_data["saves"]
        if proficient:
            total += prof_bonus

        saving_throws[ability] = {
            "modifier": total,
            "proficient": proficient,
        }

    # Each listed skill receives the proficiency bonus.
    # Skill ability mappings follow common 5e conventions.
    skill_abilities = {
        "Acrobatics": "DEX",
        "Animal Handling": "WIS",
        "Arcana": "INT",
        "Athletics": "STR",
        "Deception": "CHA",
        "History": "INT",
        "Insight": "WIS",
        "Intimidation": "CHA",
        "Investigation": "INT",
        "Medicine": "WIS",
        "Nature": "INT",
        "Perception": "WIS",
        "Performance": "CHA",
        "Persuasion": "CHA",
        "Religion": "INT",
        "Sleight of Hand": "DEX",
        "Stealth": "DEX",
        "Survival": "WIS",
    }

    skill_details = []
    for skill in all_skills:
        ability = skill_abilities.get(skill, "WIS")
        skill_details.append({
            "name": skill,
            "ability": ability,
            "modifier": stats[ability]["modifier"] + prof_bonus,
        })

    return {
        "name": name,
        "level": level,
        "race": race_name,
        "race_fa": RACES[race_name]["fa"],
        "subrace": subrace,
        "race_traits": RACES[race_name]["traits"],
        "class": class_name,
        "class_fa": class_data["fa"],
        "background": background,
        "background_fa": background_data["fa"],
        "alignment": alignment,
        "stats": stats,
        "roll_log": roll_log,
        "hp": hp,
        "hit_die": hit_die,
        "proficiency_bonus": prof_bonus,
        "class_skills": class_skills,
        "skills": skill_details,
        "saving_throws": saving_throws,
        "equipment": class_data["equipment"],
        "class_feature": class_data["feature"],
        "story": story,
    }
