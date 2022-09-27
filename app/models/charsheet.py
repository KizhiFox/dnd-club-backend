from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

from app.db.base_class import Base


class CharSheet(Base):
    __tablename__ = 'char_sheets'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # Page 1
    # Top section
    char_name = Column(String)

    class_level = Column(String)
    background = Column(String)
    player_name = Column(String)
    race = Column(String)
    alignment = Column(String)
    experience = Column(String)

    # Primary stats
    strength = Column(String)
    strength_mod = Column(String)

    dexterity = Column(String)
    dexterity_mod = Column(String)

    constitution = Column(String)
    constitution_mod = Column(String)

    intelligence = Column(String)
    intelligence_mod = Column(String)

    wisdom = Column(String)
    wisdom_mod = Column(String)

    charisma = Column(String)
    charisma_mod = Column(String)

    # Saving throws
    strength_save = Column(String)
    strength_save_prof = Column(Boolean)

    dexterity_save = Column(String)
    dexterity_save_prof = Column(Boolean)

    constitution_save = Column(String)
    constitution_save_prof = Column(Boolean)

    intelligence_save = Column(String)
    intelligence_save_prof = Column(Boolean)

    wisdom_save = Column(String)
    wisdom_save_prof = Column(Boolean)

    charisma_save = Column(String)
    charisma_save_prof = Column(Boolean)

    # Skills
    acrobatics = Column(String)
    acrobatics_prof = Column(Boolean)
    acrobatics_exp = Column(Boolean)

    animal_handling = Column(String)
    animal_handling_prof = Column(Boolean)
    animal_handling_exp = Column(Boolean)

    arcana = Column(String)
    arcana_prof = Column(Boolean)
    arcana_exp = Column(Boolean)

    athletics = Column(String)
    athletics_prof = Column(Boolean)
    athletics_exp = Column(Boolean)

    deception = Column(String)
    deception_prof = Column(Boolean)
    deception_exp = Column(Boolean)

    history = Column(String)
    history_prof = Column(Boolean)
    history_exp = Column(Boolean)

    insight = Column(String)
    insight_prof = Column(Boolean)
    insight_exp = Column(Boolean)

    intimidation = Column(String)
    intimidation_prof = Column(Boolean)
    intimidation_exp = Column(Boolean)

    investigation = Column(String)
    investigation_prof = Column(Boolean)
    investigation_exp = Column(Boolean)

    medicine = Column(String)
    medicine_prof = Column(Boolean)
    medicine_exp = Column(Boolean)

    nature = Column(String)
    nature_prof = Column(Boolean)
    nature_exp = Column(Boolean)

    perception = Column(String)
    perception_prof = Column(Boolean)
    perception_exp = Column(Boolean)

    performance = Column(String)
    performance_prof = Column(Boolean)
    performance_exp = Column(Boolean)

    persuasion = Column(String)
    persuasion_prof = Column(Boolean)
    persuasion_exp = Column(Boolean)

    religion = Column(String)
    religion_prof = Column(Boolean)
    religion_exp = Column(Boolean)

    sleight_of_hand = Column(String)
    sleight_of_hand_prof = Column(Boolean)
    sleight_of_hand_exp = Column(Boolean)

    stealth = Column(String)
    stealth_prof = Column(Boolean)
    stealth_exp = Column(Boolean)

    survival = Column(String)
    survival_prof = Column(Boolean)
    survival_exp = Column(Boolean)

    # Different singe stats
    inspiration = Column(Boolean)
    prof_bonus = Column(String)
    armor_class = Column(String)
    initiative = Column(String)
    speed = Column(String)
    passive_perception = Column(String)

    # Hit points and death saves
    hp = Column(String)
    hp_max = Column(String)
    hp_temp = Column(String)

    hit_dice = Column(String)
    hit_dice_total = Column(String)

    death_save_success_1 = Column(Boolean)
    death_save_success_2 = Column(Boolean)
    death_save_success_3 = Column(Boolean)
    death_save_failure_1 = Column(Boolean)
    death_save_failure_2 = Column(Boolean)
    death_save_failure_3 = Column(Boolean)

    # Large text fields
    personality_traits = Column(String)
    ideals = Column(String)
    bounds = Column(String)
    flaws = Column(String)

    features_traits = Column(String)
    other_profs_languages = Column(String)

    equipment = Column(String)

    # Attacks and spellcasting
    weapons = Column(String)  # Serialized JSON: List[{name: str, bonus: str, damage: str}]
    attacks_spellcasting = Column(String)

    # Money
    copper = Column(String)
    silver = Column(String)
    electrum = Column(String)
    gold = Column(String)
    platinum = Column(String)

    # Page 1
    # Top section
    age = Column(String)
    height = Column(String)
    weight = Column(String)
    Eyes = Column(String)
    skin = Column(String)
    hair = Column(String)

    # Text fields
    char_appearance = Column(String)  # Maybe base64-encoded image?
    char_backstory = Column(String)
    allies_organizations = Column(String)
    org_name = Column(String)
    org_symbol = Column(String)  # Maybe base64-encoded image?
    add_feats_traits = Column(String)
    treasure = Column(String)

    # Page 1
    # Top section
    sc_class = Column(String)

    sc_ability = Column(String)
    spell_save_dc = Column(String)
    spell_attack_bonus = Column(String)

    # Spells list
    cantrips = Column(String)  # Serialized JSON: List[{spell: str}]

    lvl_1_slots = Column(String)
    lvl_1_slots_total = Column(String)
    lvl_1_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_2_slots = Column(String)
    lvl_2_slots_total = Column(String)
    lvl_2_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_3_slots = Column(String)
    lvl_3_slots_total = Column(String)
    lvl_3_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_4_slots = Column(String)
    lvl_4_slots_total = Column(String)
    lvl_4_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_5_slots = Column(String)
    lvl_5_slots_total = Column(String)
    lvl_5_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_6_slots = Column(String)
    lvl_6_slots_total = Column(String)
    lvl_6_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_7_slots = Column(String)
    lvl_7_slots_total = Column(String)
    lvl_7_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_8_slots = Column(String)
    lvl_8_slots_total = Column(String)
    lvl_8_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]

    lvl_9_slots = Column(String)
    lvl_9_slots_total = Column(String)
    lvl_9_spells = Column(String)  # Serialized JSON: List[{spell: str, prepared: bool}]
