
# -*- coding: utf-8 -*-
"""Character Forge 2.0 — Streamlit web application."""

import streamlit as st

from data import (
    CLASSES,
    RACES,
    BACKGROUNDS,
    ALIGNMENTS,
    ABILITIES,
)
from character_engine import generate_character, signed


st.set_page_config(
    page_title="Character Forge 2.0",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded",
)


def character_to_markdown(character):
    """Create a portable Markdown character sheet."""
    lines = [
        f"# {character['name']}",
        "",
        f"- **سطح:** {character['level']}",
        f"- **نژاد:** {character['race_fa']} — {character['subrace']}",
        f"- **کلاس:** {character['class_fa']}",
        f"- **پیشینه:** {character['background_fa']}",
        f"- **گرایش اخلاقی:** {character['alignment']}",
        f"- **HP:** {character['hp']}",
        f"- **پاداش مهارت:** +{character['proficiency_bonus']}",
        "",
        "## ویژگی‌ها",
        "",
        "| ویژگی | امتیاز | اصلاح‌کننده | پاداش نژادی |",
        "|---|---:|---:|---:|",
    ]

    for ability in ABILITIES:
        stat = character["stats"][ability]
        lines.append(
            f"| {stat['name']} ({ability}) | {stat['score']} | "
            f"{signed(stat['modifier'])} | +{stat['racial_bonus']} |"
        )

    lines.extend([
        "",
        "## مهارت‌ها",
        "",
    ])

    for skill in character["skills"]:
        lines.append(
            f"- {skill['name']} ({skill['ability']}): "
            f"{signed(skill['modifier'])}"
        )

    lines.extend([
        "",
        "## ویژگی نژادی",
        "",
        character["race_traits"],
        "",
        "## ویژگی کلاس",
        "",
        character["class_feature"],
        "",
        "## تجهیزات",
        "",
        character["equipment"],
        "",
        "## داستان",
        "",
        character["story"]["text"],
        "",
        "## مسیرهای پیشنهادی ماجراجویی",
        "",
    ])

    for thread in character["story"]["threads"]:
        lines.append(f"### {thread['title']}")
        lines.append("")
        lines.append(thread["description"])
        lines.append("")

    return "\n".join(lines)


st.title("⚔️ Character Forge 2.0")
st.markdown(
    "یک شخصیت فانتزی بساز، ویژگی‌هایش را بررسی کن و ماجراجویی اختصاصی او را آغاز کن."
)

with st.sidebar:
    st.header("تنظیمات شخصیت")

    level = st.slider(
        "سطح شخصیت",
        min_value=1,
        max_value=20,
        value=1,
        help="سطح ۱ برای شروع ماجراجویی و سطح ۲۰ برای شخصیت‌های بسیار قدرتمند است.",
    )

    race_name = st.selectbox(
        "نژاد",
        options=list(RACES.keys()),
        format_func=lambda key: f"{RACES[key]['fa']} ({key})",
    )

    subrace = st.selectbox(
        "زیرنژاد یا تبار",
        options=RACES[race_name]["subraces"],
    )

    class_name = st.selectbox(
        "کلاس",
        options=list(CLASSES.keys()),
        format_func=lambda key: f"{CLASSES[key]['fa']} ({key})",
    )

    background = st.selectbox(
        "پیشینه",
        options=list(BACKGROUNDS.keys()),
        format_func=lambda key: f"{BACKGROUNDS[key]['fa']} ({key})",
    )

    alignment = st.selectbox(
        "گرایش اخلاقی",
        options=ALIGNMENTS,
        index=1,
    )

    apply_racial_bonuses = st.checkbox(
        "اعمال پاداش ویژگی‌های نژاد",
        value=True,
        help="اگر غیرفعال باشد، امتیازهای پایه بدون پاداش نژادی نمایش داده می‌شوند.",
    )

    st.divider()
    create_button = st.button(
        "✨ ساخت شخصیت جدید",
        type="primary",
        use_container_width=True,
    )

    st.caption(
        "این نسخه از قوانین ساده‌شده و الهام‌گرفته از D&D 5e استفاده می‌کند. "
        "همهٔ قوانین رسمی، زیرکلاس‌ها، طلسم‌ها و قابلیت‌های هر سطح پیاده‌سازی نشده‌اند."
    )


if create_button or "character_forge_character" not in st.session_state:
    st.session_state["character_forge_character"] = generate_character(
        level=level,
        race_name=race_name,
        subrace=subrace,
        class_name=class_name,
        background=background,
        alignment=alignment,
        apply_racial_bonuses=apply_racial_bonuses,
    )

character = st.session_state["character_forge_character"]

# Character heading
st.header(character["name"])
st.write(
    f"**{character['race_fa']} — {character['subrace']}**"
    f" · **{character['class_fa']}**"
    f" · **{character['background_fa']}**"
)

metric1, metric2, metric3, metric4 = st.columns(4)
metric1.metric("سطح", character["level"])
metric2.metric("نقاط سلامتی (HP)", character["hp"])
metric3.metric("پاداش مهارت", f"+{character['proficiency_bonus']}")
metric4.metric("تاس سلامتی", f"d{character['hit_die']}")

st.divider()

# Ability scores
st.subheader("📊 ویژگی‌های اصلی")

stat_columns = st.columns(3)

for index, ability in enumerate(ABILITIES):
    stat = character["stats"][ability]
    with stat_columns[index % 3]:
        st.metric(
            f"{stat['name']} ({ability})",
            stat["score"],
            delta=f"اصلاح‌کننده {signed(stat['modifier'])}",
            help=(
                f"امتیاز پایه: {stat['base']} | "
                f"پاداش نژادی: +{stat['racial_bonus']}"
            ),
        )

with st.expander("🎲 مشاهدهٔ پرتاب‌های تاس"):
    st.write(
        "برای هر ویژگی چهار تاس شش‌وجهی پرتاب شده و کمترین نتیجه حذف شده است. "
        "سپس امتیازهای به‌دست‌آمده بر اساس اولویت کلاس تخصیص داده شده‌اند."
    )

    for index, roll in enumerate(character["roll_log"], start=1):
        dice_text = "، ".join(str(value) for value in roll["dice"])
        kept_text = "، ".join(str(value) for value in roll["kept"])
        st.write(
            f"**پرتاب {index}:** [{dice_text}] "
            f"→ سه تاس نگه‌داشته‌شده: [{kept_text}] "
            f"→ مجموع: **{roll['score']}**"
        )

st.divider()

left_column, right_column = st.columns(2)

with left_column:
    st.subheader("🧬 نژاد و کلاس")
    st.write(f"**ویژگی نژادی:** {character['race_traits']}")
    st.write(f"**ویژگی کلاس:** {character['class_feature']}")
    st.write(f"**تجهیزات پیشنهادی:** {character['equipment']}")

    st.subheader("🛡️ تیرهای نجات")
    for ability in ABILITIES:
        save = character["saving_throws"][ability]
        proficiency_text = " (دارای مهارت)" if save["proficient"] else ""
        st.write(
            f"- {ability}: {signed(save['modifier'])}{proficiency_text}"
        )

with right_column:
    st.subheader("🎯 مهارت‌ها")
    for skill in character["skills"]:
        st.write(
            f"- **{skill['name']}** — {skill['ability']}: "
            f"{signed(skill['modifier'])}"
        )

st.caption(
    "مهارت‌های پیشینه و دو مهارت تصادفی از فهرست کلاس انتخاب می‌شوند. "
    "این سازنده، انتخاب‌های مهارت را برای همهٔ کلاس‌ها به‌طور کامل محدودسازی نمی‌کند."
)

st.divider()

# Story section
st.subheader("📜 داستان پیشینه")
for paragraph in character["story"]["text"].split("\n\n"):
    st.write(paragraph)

st.subheader("🧭 مسیرهای پیشنهادی ماجراجویی")

for thread in character["story"]["threads"]:
    with st.expander(thread["title"], expanded=True):
        st.write(thread["description"])

st.divider()

# Dice-roll summary
st.subheader("🧾 خلاصهٔ شخصیت")
summary = {
    "نام": character["name"],
    "سطح": character["level"],
    "نژاد": character["race_fa"],
    "زیرنژاد": character["subrace"],
    "کلاس": character["class_fa"],
    "پیشینه": character["background_fa"],
    "گرایش اخلاقی": character["alignment"],
    "HP": character["hp"],
}
st.json(summary, expanded=True)

# Downloadable character sheet
markdown_sheet = character_to_markdown(character)
safe_name = character["name"].replace(" ", "_")

st.download_button(
    label="⬇️ دریافت برگهٔ شخصیت (Markdown)",
    data=markdown_sheet,
    file_name=f"character_{safe_name}.md",
    mime="text/markdown",
    use_container_width=True,
)

st.caption(
    "Character Forge 2.0 — موتور تولید محلی؛ برای ساخت شخصیت و داستان به API نیاز ندارد."
)
