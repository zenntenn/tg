from characters.models.mage.focus import Instrument, Practice
from characters.models.mage.resonance import Resonance
from populate_db.abilities import (
    academics,
    acrobatics,
    alertness,
    animal_kinship,
    area_knowledge,
    art,
    athletics,
    awareness,
    belief_systems,
    biotech,
    brawl,
    carousing,
    chantry_politics,
    computer,
    cooking,
    cosmology,
    crafts,
    cryptography,
    diplomacy,
    disguise,
    empathy,
    energy_weapons,
    enigmas,
    etiquette,
    expression,
    fast_talk,
    fencing,
    finance,
    firearms,
    fortune_telling,
    gunsmith,
    hunting,
    instruction,
    intimidation,
    intrigue,
    intuition,
    investigation,
    jury_rigging,
    law,
    leadership,
    lucid_dreaming,
    media,
    medicine,
    meditation,
    melee,
    microgravity_operations,
    misdirection,
    negotiation,
    newspeak,
    occult,
    pharmacopeia,
    politics,
    power_brokering,
    propaganda,
    research,
    science,
    scrounging,
    seduction,
    stealth,
    streetwise,
    style,
    subterfuge,
    survival,
    technology,
    theology,
    torture,
    vice,
)
from populate_db.instruments_INC import (
    armor,
    artwork,
    blessings,
    blood,
    body_modification,
    bodywork,
    bones,
    books,
    brain_computer_interface,
    brews,
    cards,
    celestial_alignments,
    circles,
    computer_gear,
    contracts,
    cosmetics,
    crossroads,
    cups,
    cybernetic_implants,
    dances,
    devices,
    drugs,
    elements,
    energy,
    eye_contact,
    fashion,
    food,
    formulae,
    gadgets,
    gems,
    genetic_manipulation,
    governments,
    group_rites,
    herbs,
    household_tools,
    knots,
    labs,
    languages,
    management,
    mantras,
    markets,
    mass_media,
    medical_procedures,
    meditation_instrument,
    memories,
    money,
    music,
    nanotech,
    numbers,
    offerings,
    ordeals,
    physical_media,
    prayers,
    precious_metals,
    qi_tools,
    sacred_ground,
    sacred_iconography,
    sex,
    social_dominion,
    social_media,
    symbols,
    thought_forms,
    toys,
    tricks,
    true_names,
    vehicles,
    voice,
    wands,
    weapons,
    writings,
)

alchemy = Practice.objects.get_or_create(name="Alchemy")[0].add_source(
    "Prism of Focus", 34
)
animalism = Practice.objects.get_or_create(name="Animalism")[0].add_source(
    "Prism of Focus", 36
)
appropriation = Practice.objects.get_or_create(name="Appropriation")[0].add_source(
    "Prism of Focus", 40
)
artofdesire = Practice.objects.get_or_create(name="Art of Desire")[0].add_source(
    "Prism of Focus", 42
)
bardism = Practice.objects.get_or_create(name="Bardism")[0].add_source(
    "Prism of Focus", 46
)
chaosmagick = Practice.objects.get_or_create(name="Chaos Magick")[0].add_source(
    "Prism of Focus", 49
)
charity = Practice.objects.get_or_create(name="Charity")[0].add_source(
    "Prism of Focus", 51
)
craftwork = Practice.objects.get_or_create(name="Craftwork")[0].add_source(
    "Prism of Focus", 54
)
crazywisdom = Practice.objects.get_or_create(name="Crazy Wisdom")[0].add_source(
    "Prism of Focus", 56
)
cybernetics = Practice.objects.get_or_create(name="Cybernetics")[0].add_source(
    "Prism of Focus", 60
)
dominion = Practice.objects.get_or_create(name="Dominion")[0].add_source(
    "Prism of Focus", 63
)
elementalism = Practice.objects.get_or_create(name="Elementalism")[0].add_source(
    "Prism of Focus", 65
)
faith = Practice.objects.get_or_create(name="Faith")[0].add_source("Prism of Focus", 68)
godbonding = Practice.objects.get_or_create(name="God-Bonding")[0].add_source(
    "Prism of Focus", 72
)
guttermagick = Practice.objects.get_or_create(name="Gutter Magick")[0].add_source(
    "Prism of Focus", 74
)
highritualmagick = Practice.objects.get_or_create(name="High Ritual Magick")[
    0
].add_source("Prism of Focus", 77)
hypertech = Practice.objects.get_or_create(name="Hypertech")[0].add_source(
    "Prism of Focus", 82
)
investment = Practice.objects.get_or_create(name="Investment")[0].add_source(
    "Prism of Focus", 85
)
invigoration = Practice.objects.get_or_create(name="Invigoration")[0].add_source(
    "Prism of Focus", 87
)
maleficia = Practice.objects.get_or_create(name="Maleficia")[0].add_source(
    "Prism of Focus", 90
)
martialarts = Practice.objects.get_or_create(name="Martial Arts")[0].add_source(
    "Prism of Focus", 93
)
mediacontrol = Practice.objects.get_or_create(name="Media Control")[0].add_source(
    "Prism of Focus", 96
)
medicinework = Practice.objects.get_or_create(name="Medicine-Work")[0].add_source(
    "Prism of Focus", 99
)
mediumship = Practice.objects.get_or_create(name="Mediumship")[0].add_source(
    "Prism of Focus", 101
)
psionics = Practice.objects.get_or_create(name="Psionics")[0].add_source(
    "Prism of Focus", 103
)
realityhacking = Practice.objects.get_or_create(name="Reality Hacking")[0].add_source(
    "Prism of Focus", 106
)
shamanism = Practice.objects.get_or_create(name="Shamanism")[0].add_source(
    "Prism of Focus", 109
)
voudoun = Practice.objects.get_or_create(name="Voudoun")[0].add_source(
    "Prism of Focus", 113
)
weirdscience = Practice.objects.get_or_create(name="Weird Science")[0].add_source(
    "Prism of Focus", 115
)
witchcraft = Practice.objects.get_or_create(name="Witchcraft")[0].add_source(
    "Prism of Focus", 118
)
yoga = Practice.objects.get_or_create(name="Yoga")[0].add_source("Prism of Focus", 122)

alchemy.add_abilities(
    [
        art,
        crafts,
        cryptography,
        enigmas,
        occult,
        medicine,
        pharmacopeia,
        science,
    ]
)
alchemy.instruments.add(books, brews, circles, devices, drugs, formulae, labs)
alchemy.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Changing")[0],
    Resonance.objects.get_or_create(name="Immortal")[0],
    Resonance.objects.get_or_create(name="Mad")[0],
    Resonance.objects.get_or_create(name="Mutable")[0],
    Resonance.objects.get_or_create(name="Practical")[0],
    Resonance.objects.get_or_create(name="Reactive")[0],
    Resonance.objects.get_or_create(name="Secretive")[0],
    Resonance.objects.get_or_create(name="Transformative")[0],
)
alchemy.save()


animalism.add_abilities(
    [
        athletics,
        awareness,
        brawl,
        crafts,
        occult,
        hunting,
        stealth,
        survival,
    ]
)
animalism.instruments.add(
    armor,
    artwork,
    blood,
    bones,
    brews,
    circles,
    cups,
    dances,
    drugs,
    eye_contact,
    fashion,
    food,
    herbs,
    languages,
    voice,
    music,
    offerings,
    prayers,
    ordeals,
    social_dominion,
    symbols,
    thought_forms,
    weapons,
    devices,
    gadgets,
    body_modification,
    cybernetic_implants,
    genetic_manipulation,
    medical_procedures,
    computer_gear,
)
animalism.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Animalistic")[0],
    Resonance.objects.get_or_create(name="Cold-Blooded")[0],
    Resonance.objects.get_or_create(name="Feathered")[0],
    Resonance.objects.get_or_create(name="Furry")[0],
    Resonance.objects.get_or_create(name="Instinctive")[0],
    Resonance.objects.get_or_create(name="Predatory")[0],
    Resonance.objects.get_or_create(name="Primal")[0],
    Resonance.objects.get_or_create(name="Scaly")[0],
)
animalism.save()

appropriation.add_abilities([brawl, firearms, intimidation, law, politics])
appropriation.instruments.add(
    contracts, sacred_ground, social_dominion, precious_metals
)
appropriation.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Acquisitive")[0],
    Resonance.objects.get_or_create(name="Claiming")[0],
    Resonance.objects.get_or_create(name="Con Artist")[0],
    Resonance.objects.get_or_create(name="Greedy")[0],
    Resonance.objects.get_or_create(name="Profitable")[0],
    Resonance.objects.get_or_create(name="Swindling")[0],
    Resonance.objects.get_or_create(name="Taking")[0],
    Resonance.objects.get_or_create(name="Thieving")[0],
    Resonance.objects.get_or_create(name="Wealthy")[0],
)
appropriation.save()

artofdesire.add_abilities(
    [
        academics,
        athletics,
        awareness,
        carousing,
        diplomacy,
        disguise,
        etiquette,
        expression,
        fast_talk,
        fencing,
        finance,
        intimidation,
        intrigue,
        leadership,
        brawl,
        media,
        negotiation,
        politics,
        seduction,
        style,
        subterfuge,
    ]
)
artofdesire.instruments.add(
    cards,
    cosmetics,
    dances,
    eye_contact,
    fashion,
    gadgets,
    mass_media,
    money,
    sex,
    social_dominion,
    vehicles,
    voice,
    weapons,
)
artofdesire.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Accomodating")[0],
    Resonance.objects.get_or_create(name="Connected")[0],
    Resonance.objects.get_or_create(name="Covetious")[0],
    Resonance.objects.get_or_create(name="Desired")[0],
    Resonance.objects.get_or_create(name="Productive")[0],
    Resonance.objects.get_or_create(name="Wanted")[0],
    Resonance.objects.get_or_create(name="Wealthy")[0],
)
artofdesire.save()

bardism.add_abilities(
    [
        academics,
        art,
        awareness,
        cosmology,
        crafts,
        empathy,
        enigmas,
        expression,
        seduction,
        technology,
    ]
)
bardism.instruments.add(
    artwork,
    dances,
    drugs,
    food,
    energy,
    eye_contact,
    fashion,
    group_rites,
    mass_media,
    meditation_instrument,
    ordeals,
    prayers,
    sex,
    symbols,
    tricks,
    true_names,
    voice,
)
bardism.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Artistic")[0],
    Resonance.objects.get_or_create(name="Bardic")[0],
    Resonance.objects.get_or_create(name="Charming")[0],
    Resonance.objects.get_or_create(name="Epic")[0],
    Resonance.objects.get_or_create(name="Inspiring")[0],
    Resonance.objects.get_or_create(name="Melodic")[0],
    Resonance.objects.get_or_create(name="Musical")[0],
    Resonance.objects.get_or_create(name="Persuasive")[0],
    Resonance.objects.get_or_create(name="Spoony")[0],
    Resonance.objects.get_or_create(name="Storied")[0],
)
bardism.save()

chaosmagick.add_abilities(
    [
        art,
        awareness,
        carousing,
        computer,
        occult,
        expression,
        lucid_dreaming,
        intuition,
        meditation,
        misdirection,
        pharmacopeia,
        streetwise,
        technology,
    ]
)
chaosmagick.instruments.add(*list(Instrument.objects.all()))
chaosmagick.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Adaptive")[0],
    Resonance.objects.get_or_create(name="Chaotic")[0],
    Resonance.objects.get_or_create(name="Eccentric")[0],
    Resonance.objects.get_or_create(name="Experimental")[0],
    Resonance.objects.get_or_create(name="Flexible")[0],
    Resonance.objects.get_or_create(name="Individualistic")[0],
    Resonance.objects.get_or_create(name="Innovative")[0],
    Resonance.objects.get_or_create(name="Spontaneous")[0],
    Resonance.objects.get_or_create(name="Unconventional")[0],
)
chaosmagick.save()

charity.add_abilities(
    [art, cosmology, crafts, empathy, expression, politics, technology]
)
charity.instruments.add(blessings, governments, money, physical_media)
charity.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Altruistic")[0],
    Resonance.objects.get_or_create(name="Benevolent")[0],
    Resonance.objects.get_or_create(name="Compassionate")[0],
    Resonance.objects.get_or_create(name="Generous")[0],
    Resonance.objects.get_or_create(name="Giving")[0],
    Resonance.objects.get_or_create(name="Helpful")[0],
    Resonance.objects.get_or_create(name="Philanthropic")[0],
    Resonance.objects.get_or_create(name="Selfless")[0],
)
charity.save()

craftwork.add_abilities(
    [
        academics,
        art,
        computer,
        cooking,
        crafts,
        energy_weapons,
        occult,
        gunsmith,
        jury_rigging,
        research,
        science,
        technology,
    ]
)
craftwork.instruments.add(
    artwork,
    blood,
    books,
    computer_gear,
    devices,
    elements,
    gadgets,
    household_tools,
    labs,
    symbols,
    weapons,
)
craftwork.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Constructive")[0],
    Resonance.objects.get_or_create(name="Crafted")[0],
    Resonance.objects.get_or_create(name="Creative")[0],
    Resonance.objects.get_or_create(name="Designed")[0],
    Resonance.objects.get_or_create(name="Fine")[0],
    Resonance.objects.get_or_create(name="Forged")[0],
    Resonance.objects.get_or_create(name="Masterwork")[0],
    Resonance.objects.get_or_create(name="Sewn")[0],
    Resonance.objects.get_or_create(name="Stitched-Together")[0],
)
craftwork.save()

crazywisdom.add_abilities(
    [
        art,
        athletics,
        carousing,
        enigmas,
        occult,
        intuition,
        lucid_dreaming,
        meditation,
        pharmacopeia,
        survival,
    ]
)
crazywisdom.instruments.add(
    blood,
    bones,
    brain_computer_interface,
    dances,
    drugs,
    music,
    ordeals,
    sex,
    social_dominion,
    thought_forms,
    toys,
    tricks,
    voice,
)
crazywisdom.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Daring")[0],
    Resonance.objects.get_or_create(name="Eccentric")[0],
    Resonance.objects.get_or_create(name="Irreverent")[0],
    Resonance.objects.get_or_create(name="Offbeat")[0],
    Resonance.objects.get_or_create(name="Quirky")[0],
    Resonance.objects.get_or_create(name="Strange")[0],
    Resonance.objects.get_or_create(name="Unconventional")[0],
    Resonance.objects.get_or_create(name="Unorthodox")[0],
    Resonance.objects.get_or_create(name="Whimsical")[0],
)
crazywisdom.save()

cybernetics.add_abilities(
    [
        academics,
        biotech,
        computer,
        crafts,
        energy_weapons,
        media,
        politics,
        science,
        technology,
    ]
)
cybernetics.instruments.add(
    books,
    brain_computer_interface,
    computer_gear,
    devices,
    gadgets,
    labs,
    languages,
    mass_media,
    nanotech,
    numbers,
    weapons,
    writings,
)
cybernetics.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Artificial")[0],
    Resonance.objects.get_or_create(name="Automated")[0],
    Resonance.objects.get_or_create(name="Digital")[0],
    Resonance.objects.get_or_create(name="Futuristic")[0],
    Resonance.objects.get_or_create(name="Mechanical")[0],
    Resonance.objects.get_or_create(name="Networked")[0],
    Resonance.objects.get_or_create(name="Prosthetic")[0],
    Resonance.objects.get_or_create(name="Robotic")[0],
    Resonance.objects.get_or_create(name="Synthetic")[0],
    Resonance.objects.get_or_create(name="Virtual")[0],
)
cybernetics.save()

dominion.add_abilities(
    [
        academics,
        art,
        belief_systems,
        chantry_politics,
        diplomacy,
        empathy,
        expression,
        instruction,
        intimidation,
        leadership,
        media,
        politics,
        power_brokering,
        propaganda,
        seduction,
        technology,
    ]
)
dominion.instruments.add(
    artwork,
    brain_computer_interface,
    eye_contact,
    fashion,
    group_rites,
    languages,
    mass_media,
    music,
    social_dominion,
    symbols,
    thought_forms,
    tricks,
    voice,
)
dominion.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Assertive")[0],
    Resonance.objects.get_or_create(name="Authoritative")[0],
    Resonance.objects.get_or_create(name="Autocratic")[0],
    Resonance.objects.get_or_create(name="Commanding")[0],
    Resonance.objects.get_or_create(name="Controlling")[0],
    Resonance.objects.get_or_create(name="Dominant")[0],
    Resonance.objects.get_or_create(name="Forceful")[0],
    Resonance.objects.get_or_create(name="Influential")[0],
    Resonance.objects.get_or_create(name="Resolute")[0],
)
dominion.save()

elementalism.add_abilities(
    [
        art,
        athletics,
        awareness,
        crafts,
        empathy,
        occult,
        meditation,
        survival,
    ]
)
elementalism.instruments.add(
    armor,
    bones,
    blood,
    brews,
    dances,
    drugs,
    elements,
    energy,
    herbs,
    household_tools,
    knots,
    meditation_instrument,
    music,
    prayers,
    offerings,
    ordeals,
    symbols,
    weapons,
    writings,
)
elementalism.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Breezy")[0],
    Resonance.objects.get_or_create(name="Burning")[0],
    Resonance.objects.get_or_create(name="Electric")[0],
    Resonance.objects.get_or_create(name="Fluid")[0],
    Resonance.objects.get_or_create(name="Glowing")[0],
    Resonance.objects.get_or_create(name="Grounded")[0],
    Resonance.objects.get_or_create(name="Metallic")[0],
    Resonance.objects.get_or_create(name="Radioactive")[0],
    Resonance.objects.get_or_create(name="Wooden")[0],
)
elementalism.save()

faith.add_abilities(
    [
        academics,
        awareness,
        belief_systems,
        cosmology,
        empathy,
        enigmas,
        occult,
        expression,
        medicine,
        theology,
    ]
)
faith.instruments.add(
    blessings,
    books,
    cups,
    energy,
    food,
    group_rites,
    music,
    offerings,
    ordeals,
    prayers,
    sacred_iconography,
    symbols,
    thought_forms,
    voice,
    writings,
)
faith.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Faithful")[0],
    Resonance.objects.get_or_create(name="Holy")[0],
    Resonance.objects.get_or_create(name="Infallible")[0],
    Resonance.objects.get_or_create(name="Profane")[0],
    Resonance.objects.get_or_create(name="Sacred")[0],
    Resonance.objects.get_or_create(name="Unerring")[0],
    Resonance.objects.get_or_create(name="Worshipful")[0],
)
faith.save()

godbonding.add_abilities(
    [
        awareness,
        belief_systems,
        cosmology,
        empathy,
        enigmas,
        occult,
        expression,
        lucid_dreaming,
        medicine,
        meditation,
    ]
)
godbonding.instruments.add(
    blessings,
    blood,
    elements,
    group_rites,
    music,
    offerings,
    ordeals,
    prayers,
    sacred_iconography,
    voice,
    weapons,
)
godbonding.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Awe-Inspiring")[0],
    Resonance.objects.get_or_create(name="Divine")[0],
    Resonance.objects.get_or_create(name="Ethereal")[0],
    Resonance.objects.get_or_create(name="Heavenly")[0],
    Resonance.objects.get_or_create(name="Ridden")[0],
    Resonance.objects.get_or_create(name="Sacred")[0],
)
godbonding.save()

guttermagick.add_abilities(
    [
        animal_kinship,
        area_knowledge,
        art,
        crafts,
        expression,
        firearms,
        intimidation,
        jury_rigging,
        pharmacopeia,
        scrounging,
        streetwise,
        survival,
        technology,
    ]
)
guttermagick.instruments.add(
    artwork,
    blood,
    bones,
    cards,
    dances,
    drugs,
    eye_contact,
    fashion,
    herbs,
    household_tools,
    music,
    offerings,
    sex,
    social_dominion,
    symbols,
    thought_forms,
    toys,
    tricks,
    weapons,
    vehicles,
)
guttermagick.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Coarse")[0],
    Resonance.objects.get_or_create(name="Dangerous")[0],
    Resonance.objects.get_or_create(name="Improvised")[0],
    Resonance.objects.get_or_create(name="Lowbrow")[0],
    Resonance.objects.get_or_create(name="Ragged")[0],
    Resonance.objects.get_or_create(name="Reckless")[0],
    Resonance.objects.get_or_create(name="Resourceful")[0],
    Resonance.objects.get_or_create(name="Unrefined")[0],
)
guttermagick.save()

highritualmagick.add_abilities(
    [
        academics,
        belief_systems,
        cosmology,
        crafts,
        expression,
        enigmas,
        occult,
        investigation,
        leadership,
        meditation,
        occult,
        research,
    ]
)
highritualmagick.instruments.add(
    books,
    celestial_alignments,
    circles,
    computer_gear,
    cups,
    elements,
    eye_contact,
    fashion,
    gems,
    dances,
    languages,
    meditation_instrument,
    numbers,
    offerings,
    prayers,
    social_dominion,
    symbols,
    thought_forms,
    true_names,
    wands,
    weapons,
    writings,
)
highritualmagick.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Arrogant")[0],
    Resonance.objects.get_or_create(name="Detail-Oriented")[0],
    Resonance.objects.get_or_create(name="Elemental")[0],
    Resonance.objects.get_or_create(name="Knowledgable")[0],
    Resonance.objects.get_or_create(name="Meticulous")[0],
    Resonance.objects.get_or_create(name="Precise")[0],
)
highritualmagick.save()

hypertech.add_abilities(
    [
        academics,
        fortune_telling,
        computer,
        crafts,
        investigation,
        medicine,
        microgravity_operations,
        research,
        science,
        technology,
    ]
)
hypertech.instruments.add(
    books,
    brain_computer_interface,
    computer_gear,
    devices,
    household_tools,
    gadgets,
    labs,
    nanotech,
    writings,
)
hypertech.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Augmented")[0],
    Resonance.objects.get_or_create(name="Digital")[0],
    Resonance.objects.get_or_create(name="Futuristic")[0],
    Resonance.objects.get_or_create(name="High-Tech")[0],
    Resonance.objects.get_or_create(name="Nanotech")[0],
    Resonance.objects.get_or_create(name="Robotic")[0],
    Resonance.objects.get_or_create(name="Synthetic")[0],
)
hypertech.save()

investment.add_abilities(
    [academics, occult, investigation, law, leadership, politics, research]
)
investment.instruments.add(blessings, contracts, markets, money)
investment.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Acquisitive")[0],
    Resonance.objects.get_or_create(name="Growing")[0],
    Resonance.objects.get_or_create(name="Opportunstic")[0],
    Resonance.objects.get_or_create(name="Profitable")[0],
    Resonance.objects.get_or_create(name="Prosperous")[0],
    Resonance.objects.get_or_create(name="Prudent")[0],
    Resonance.objects.get_or_create(name="Resourceful")[0],
    Resonance.objects.get_or_create(name="Savvy")[0],
    Resonance.objects.get_or_create(name="Wealthy")[0],
)
investment.save()

invigoration.add_abilities(
    [
        athletics,
        biotech,
        brawl,
        occult,
        lucid_dreaming,
        medicine,
        meditation,
        science,
    ]
)
invigoration.instruments.add(
    blood,
    bodywork,
    brain_computer_interface,
    brews,
    dances,
    devices,
    gadgets,
    drugs,
    energy,
    eye_contact,
    fashion,
    food,
    herbs,
    labs,
    meditation_instrument,
    money,
    nanotech,
    sex,
    social_dominion,
    thought_forms,
    voice,
)
invigoration.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Dynamic")[0],
    Resonance.objects.get_or_create(name="Energizing")[0],
    Resonance.objects.get_or_create(name="Fortifying")[0],
    Resonance.objects.get_or_create(name="Rejuvenating")[0],
    Resonance.objects.get_or_create(name="Resilient")[0],
    Resonance.objects.get_or_create(name="Stimulating")[0],
    Resonance.objects.get_or_create(name="Vibrant")[0],
)
invigoration.save()

maleficia.add_abilities(
    [
        cosmology,
        disguise,
        enigmas,
        occult,
        expression,
        intimidation,
        intrigue,
        melee,
        newspeak,
        occult,
        pharmacopeia,
        propaganda,
        seduction,
        torture,
        vice,
    ]
)
maleficia.instruments.add(
    artwork,
    blood,
    bodywork,
    bones,
    circles,
    cups,
    blessings,
    elements,
    eye_contact,
    drugs,
    gems,
    group_rites,
    music,
    offerings,
    prayers,
    sex,
    voice,
    weapons,
)
maleficia.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Dead;y")[0],
    Resonance.objects.get_or_create(name="Jinxed")[0],
    Resonance.objects.get_or_create(name="Malevolent")[0],
    Resonance.objects.get_or_create(name="Noxious")[0],
    Resonance.objects.get_or_create(name="Pestilent")[0],
    Resonance.objects.get_or_create(name="Poisonous")[0],
    Resonance.objects.get_or_create(name="Vicious")[0],
    Resonance.objects.get_or_create(name="Wicked")[0],
)
maleficia.save()

martialarts.add_abilities(
    [
        acrobatics,
        alertness,
        athletics,
        awareness,
        occult,
        etiquette,
        fencing,
        intimidation,
        brawl,
        medicine,
        meditation,
        melee,
    ]
)
martialarts.instruments.add(
    bodywork,
    dances,
    energy,
    herbs,
    meditation_instrument,
    ordeals,
    symbols,
    wands,
    weapons,
    voice,
)
martialarts.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Agile")[0],
    Resonance.objects.get_or_create(name="Controlled")[0],
    Resonance.objects.get_or_create(name="Fierce")[0],
    Resonance.objects.get_or_create(name="Focused")[0],
    Resonance.objects.get_or_create(name="In Motion")[0],
    Resonance.objects.get_or_create(name="Kinetic")[0],
    Resonance.objects.get_or_create(name="Lethal")[0],
    Resonance.objects.get_or_create(name="Precise")[0],
    Resonance.objects.get_or_create(name="Skillful")[0],
)
martialarts.save()

mediacontrol.add_abilities(
    [art, empathy, expression, intimidation, politics, subterfuge, technology]
)
mediacontrol.instruments.add(
    artwork,
    books,
    eye_contact,
    fashion,
    mass_media,
    physical_media,
    social_media,
    writings,
)
mediacontrol.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Compelling")[0],
    Resonance.objects.get_or_create(name="Controlling")[0],
    Resonance.objects.get_or_create(name="Dominant")[0],
    Resonance.objects.get_or_create(name="Hypnotic")[0],
    Resonance.objects.get_or_create(name="Influential")[0],
    Resonance.objects.get_or_create(name="Manipulative")[0],
    Resonance.objects.get_or_create(name="Persuasive")[0],
    Resonance.objects.get_or_create(name="Propagandistic")[0],
    Resonance.objects.get_or_create(name="Subversive")[0],
)
mediacontrol.save()

medicinework.add_abilities(
    [
        academics,
        art,
        awareness,
        empathy,
        occult,
        medicine,
        meditation,
        pharmacopeia,
        science,
        technology,
    ]
)
medicinework.instruments.add(
    artwork,
    blessings,
    blood,
    bodywork,
    bones,
    books,
    brews,
    computer_gear,
    cups,
    dances,
    devices,
    drugs,
    group_rites,
    herbs,
    labs,
    languages,
    meditation_instrument,
    music,
    offerings,
    prayers,
    social_dominion,
    voice,
    weapons,
)
medicinework.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Healing")[0],
    Resonance.objects.get_or_create(name="Medical")[0],
    Resonance.objects.get_or_create(name="Rehabilitative")[0],
    Resonance.objects.get_or_create(name="Restorative")[0],
    Resonance.objects.get_or_create(name="Soothing")[0],
    Resonance.objects.get_or_create(name="Therapeutic")[0],
    Resonance.objects.get_or_create(name="Wholesome")[0],
)
medicinework.save()

mediumship.add_abilities(
    [
        awareness,
        belief_systems,
        cosmology,
        empathy,
        enigmas,
        occult,
        expression,
        intimidation,
        investigation,
        lucid_dreaming,
        meditation,
        occult,
        research,
    ]
)
mediumship.instruments.add(
    artwork,
    blood,
    bodywork,
    bones,
    brews,
    dances,
    drugs,
    eye_contact,
    fashion,
    gems,
    herbs,
    languages,
    meditation_instrument,
    ordeals,
    sex,
    social_dominion,
    voice,
    writings,
)
mediumship.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Channeling")[0],
    Resonance.objects.get_or_create(name="Dead")[0],
    Resonance.objects.get_or_create(name="Ectoplasmic]")[0],
    Resonance.objects.get_or_create(name="Ethereal")[0],
    Resonance.objects.get_or_create(name="Otherworldly")[0],
    Resonance.objects.get_or_create(name="Psychic")[0],
    Resonance.objects.get_or_create(name="Spectral")[0],
    Resonance.objects.get_or_create(name="Spiritual")[0],
    Resonance.objects.get_or_create(name="Transcendant")[0],
)
mediumship.save()

psionics.add_abilities(
    [
        alertness,
        awareness,
        empathy,
        enigmas,
        occult,
        intimidation,
        lucid_dreaming,
        brawl,
        meditation,
    ]
)
psionics.instruments.add(
    bodywork,
    brain_computer_interface,
    devices,
    nanotech,
    cards,
    dances,
    drugs,
    energy,
    eye_contact,
    fashion,
    formulae,
    numbers,
    group_rites,
    music,
    languages,
    management,
    meditation_instrument,
    sex,
    social_dominion,
    symbols,
    thought_forms,
    true_names,
    voice,
)
psionics.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Astral")[0],
    Resonance.objects.get_or_create(name="Intuitive")[0],
    Resonance.objects.get_or_create(name="Mental")[0],
    Resonance.objects.get_or_create(name="Psychic")[0],
    Resonance.objects.get_or_create(name="Telekinetic")[0],
    Resonance.objects.get_or_create(name="Telepathic")[0],
)
psionics.save()

realityhacking.add_abilities(
    [
        academics,
        art,
        belief_systems,
        computer,
        cryptography,
        expression,
        jury_rigging,
        media,
        politics,
        science,
        subterfuge,
        technology,
    ]
)
realityhacking.instruments.add(
    artwork,
    books,
    brain_computer_interface,
    computer_gear,
    devices,
    drugs,
    eye_contact,
    group_rites,
    languages,
    mass_media,
    money,
    music,
    nanotech,
    sex,
    social_dominion,
    symbols,
    thought_forms,
    tricks,
    voice,
    weapons,
)
realityhacking.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Ad Libbed")[0],
    Resonance.objects.get_or_create(name="Elastic")[0],
    Resonance.objects.get_or_create(name="Fluid")[0],
    Resonance.objects.get_or_create(name="Fractal")[0],
    Resonance.objects.get_or_create(name="Improvised")[0],
    Resonance.objects.get_or_create(name="Malleable")[0],
    Resonance.objects.get_or_create(name="Plastic")[0],
    Resonance.objects.get_or_create(name="Transformative")[0],
    Resonance.objects.get_or_create(name="Viral")[0],
)
realityhacking.save()

shamanism.add_abilities(
    [
        alertness,
        art,
        cosmology,
        enigmas,
        occult,
        expression,
        lucid_dreaming,
        medicine,
        pharmacopeia,
        streetwise,
        survival,
    ]
)
shamanism.instruments.add(
    blood,
    bones,
    computer_gear,
    dances,
    drugs,
    elements,
    herbs,
    household_tools,
    offerings,
    ordeals,
    sex,
    thought_forms,
    toys,
    true_names,
    voice,
    weapons,
)
shamanism.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Ancestral")[0],
    Resonance.objects.get_or_create(name="Guided")[0],
    Resonance.objects.get_or_create(name="Otherworldly")[0],
    Resonance.objects.get_or_create(name="Soulful")[0],
    Resonance.objects.get_or_create(name="Spiritual")[0],
    Resonance.objects.get_or_create(name="Transcendant")[0],
    Resonance.objects.get_or_create(name="Visionary")[0],
)
shamanism.save()

voudoun.add_abilities(
    [
        art,
        athletics,
        awareness,
        belief_systems,
        carousing,
        crafts,
        empathy,
        intimidation,
        lucid_dreaming,
        medicine,
        meditation,
        streetwise,
    ]
)
voudoun.instruments.add(
    artwork,
    blessings,
    blood,
    bones,
    cards,
    cups,
    crossroads,
    dances,
    drugs,
    elements,
    eye_contact,
    fashion,
    group_rites,
    herbs,
    household_tools,
    knots,
    languages,
    meditation_instrument,
    music,
    offerings,
    prayers,
    sex,
    symbols,
    true_names,
    voice,
    wands,
    weapons,
    writings,
)
voudoun.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Ancestral")[0],
    Resonance.objects.get_or_create(name="Intense")[0],
    Resonance.objects.get_or_create(name="Mesmerizing")[0],
    Resonance.objects.get_or_create(name="Possessed")[0],
    Resonance.objects.get_or_create(name="Revelatory")[0],
    Resonance.objects.get_or_create(name="Soulful")[0],
    Resonance.objects.get_or_create(name="Spirit-Guided")[0],
    Resonance.objects.get_or_create(name="Transcendental")[0],
)
voudoun.save()

weirdscience.add_abilities(
    [
        academics,
        crafts,
        occult,
        jury_rigging,
        energy_weapons,
        research,
        science,
        technology,
    ]
)
weirdscience.instruments.add(
    armor,
    books,
    bones,
    brain_computer_interface,
    celestial_alignments,
    computer_gear,
    devices,
    elements,
    gadgets,
    labs,
    languages,
    numbers,
    toys,
    vehicles,
    weapons,
    writings,
)
weirdscience.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Bizarre")[0],
    Resonance.objects.get_or_create(name="Clockwork")[0],
    Resonance.objects.get_or_create(name="Creative")[0],
    Resonance.objects.get_or_create(name="Electric")[0],
    Resonance.objects.get_or_create(name="Homeopathic")[0],
    Resonance.objects.get_or_create(name="Hyperspatial")[0],
    Resonance.objects.get_or_create(name="Insightful")[0],
    Resonance.objects.get_or_create(name="Radiant")[0],
    Resonance.objects.get_or_create(name="Studious")[0],
)
weirdscience.save()

witchcraft.add_abilities(
    [
        academics,
        animal_kinship,
        art,
        awareness,
        crafts,
        fortune_telling,
        medicine,
        meditation,
        occult,
        pharmacopeia,
    ]
)
witchcraft.instruments.add(
    artwork,
    blessings,
    blood,
    bodywork,
    bones,
    books,
    brews,
    cards,
    celestial_alignments,
    circles,
    crossroads,
    cups,
    dances,
    drugs,
    elements,
    eye_contact,
    group_rites,
    household_tools,
    knots,
    music,
    offerings,
    sex,
    social_dominion,
    symbols,
    true_names,
    wands,
    weapons,
    writings,
)
witchcraft.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Ancient")[0],
    Resonance.objects.get_or_create(name="Bloody")[0],
    Resonance.objects.get_or_create(name="Eerie")[0],
    Resonance.objects.get_or_create(name="Eldritch")[0],
    Resonance.objects.get_or_create(name="Fertile")[0],
    Resonance.objects.get_or_create(name="Fey")[0],
    Resonance.objects.get_or_create(name="Natural")[0],
    Resonance.objects.get_or_create(name="Seasonal")[0],
)
witchcraft.save()

yoga.add_abilities(
    [
        athletics,
        awareness,
        enigmas,
        occult,
        expression,
        medicine,
        meditation,
        survival,
    ]
)
yoga.instruments.add(
    bodywork,
    circles,
    dances,
    energy,
    languages,
    meditation_instrument,
    music,
    ordeals,
    prayers,
    sex,
    symbols,
    thought_forms,
    voice,
    writings,
)
yoga.common_resonance_traits.add(
    Resonance.objects.get_or_create(name="Astral")[0],
    Resonance.objects.get_or_create(name="Balanced")[0],
    Resonance.objects.get_or_create(name="Centered")[0],
    Resonance.objects.get_or_create(name="Energetic")[0],
    Resonance.objects.get_or_create(name="Grounded")[0],
    Resonance.objects.get_or_create(name="Meditative")[0],
    Resonance.objects.get_or_create(name="Mindful")[0],
    Resonance.objects.get_or_create(name="Relaxed")[0],
)
yoga.save()

qi_manipulation = Practice.objects.get_or_create(name="Qi Manipulation")[0].add_source("Lore of the Traditions", 33)

qi_manipulation.instruments.add(qi_tools, mantras, memories)