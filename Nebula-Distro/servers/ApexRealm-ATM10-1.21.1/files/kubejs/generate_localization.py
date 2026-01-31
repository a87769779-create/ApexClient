import json
import os
import re

# Paths
# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(script_dir, "assets", "atm10_localization", "lang")
# Ensure directory exists
os.makedirs(base_dir, exist_ok=True)

pt_file = os.path.join(base_dir, "pt_br.json")
ru_file = os.path.join(base_dir, "ru_ru.json")
ua_file = os.path.join(base_dir, "uk_ua.json")

# Dictionaries for translation
# Core Manual Translations (items, specific blocks)
manual_ru = {
    "item.kubejs.alchemical_sulfur": "Алхимическая сера",
    "item.kubejs.inert_nether_star": "Инертная звезда Незера",
    "item.kubejs.rudimentary_flower": "Рудиментарный цветок",
    "item.kubejs.cursed_doll": "Проклятая кукла",
    "item.kubejs.corrupted_emerald": "Коррапченный изумруд",
    "block.kubejs.corrupted_emerald_block": "Блок коррапченного изумруда",
    "item.allthemodium.allthemodium_pickaxe": "Кирка из Оллземодия",
    "item.allthemodium.vibranium_pickaxe": "Кирка из Вибраниума",
    "item.allthemodium.unobtainium_pickaxe": "Кирка из Анобтейниума",
    "item.allthemodium.allthemodium_axe": "Топор из Оллземодия",
    "item.allthemodium.vibranium_axe": "Топор из Вибраниума",
    "item.allthemodium.unobtainium_axe": "Топор из Анобтейниума",
    "item.allthemodium.allthemodium_shovel": "Лопата из Оллземодия",
    "item.allthemodium.vibranium_shovel": "Лопата из Вибраниума",
    "item.allthemodium.unobtainium_shovel": "Лопата из Анобтейниума",
    "item.allthemodium.allthemodium_hoe": "Мотыга из Оллземодия",
    "item.allthemodium.vibranium_hoe": "Мотыга из Вибраниума",
    "item.allthemodium.unobtainium_hoe": "Мотыга из Анобтейниума",
    "item.allthemodium.allthemodium_sword": "Меч из Оллземодия",
    "item.allthemodium.vibranium_sword": "Меч из Вибраниума",
    "item.allthemodium.unobtainium_sword": "Меч из Анобтейниума",
    "item.allthemodium.allthemodium_plate": "Пластина из Оллземодия",
    "item.allthemodium.vibranium_plate": "Пластина из Вибраниума",
    "item.allthemodium.unobtainium_plate": "Пластина из Анобтейниума",
    "item.allthemodium.allthemodium_rod": "Стержень из Оллземодия",
    "item.allthemodium.vibranium_rod": "Стержень из Вибраниума",
    "item.allthemodium.unobtainium_rod": "Стержень из Анобтейниума",
    "item.allthemodium.allthemodium_gear": "Шестеренка из Оллземодия",
    "item.allthemodium.vibranium_gear": "Шестеренка из Вибраниума",
    "item.allthemodium.unobtainium_gear": "Шестеренка из Анобтейниума",
    "item.allthemodium.raw_allthemodium": "Сырой Оллземодий",
    "item.allthemodium.raw_vibranium": "Сырой Вибраниум",
    "item.allthemodium.raw_unobtainium": "Сырой Анобтейниум",
    "item.allthemodium.allthemodium_apple": "Яблоко из Оллземодия",
    "item.allthemodium.allthemodium_dust": "Пыль Оллземодия",
    "item.allthemodium.allthemodium_nugget": "Кусочек Оллземодия",
    "item.allthemodium.allthemodium_ingot": "Слиток Оллземодия",
    "item.allthemodium.allthemodium_carrot": "Морковь из Оллземодия",
    "block.allthemodium.allthemodium_ore": "Руда Оллземодия",
    "block.allthemodium.allthemodium_slate_ore": "Глубинная руда Оллземодия",
    "block.allthemodium.allthemodium_block": "Блок Оллземодия",
    "item.allthemodium.allthemodium_helmet": "Шлем из Оллземодия",
    "item.allthemodium.allthemodium_chestplate": "Нагрудник из Оллземодия",
    "item.allthemodium.allthemodium_leggings": "Поножи из Оллземодия",
    "item.allthemodium.allthemodium_boots": "Ботинки из Оллземодия",
    "item.allthemodium.crushed_allthemodium": "Измельченный Оллземодий",
    "item.allthemodium.crushed_vibranium": "Измельченный Вибраниум",
    "item.allthemodium.crushed_unobtainium": "Измельченный Анобтейниум",
    "item.allthemodium.vibranium_helmet": "Шлем из Вибраниума",
    "item.allthemodium.vibranium_chestplate": "Нагрудник из Вибраниума",
    "item.allthemodium.vibranium_leggings": "Поножи из Вибраниума",
    "item.allthemodium.vibranium_boots": "Ботинки из Вибраниума",
    "item.allthemodium.unobtainium_helmet": "Шлем из Анобтейниума",
    "item.allthemodium.unobtainium_chestplate": "Нагрудник из Анобтейниума",
    "item.allthemodium.unobtainium_leggings": "Поножи из Анобтейниума",
    "item.allthemodium.unobtainium_boots": "Ботинки из Анобтейниума",
    "item.allthemodium.alloy_axe": "Сплавной Топор",
    "item.allthemodium.alloy_pick": "Сплавная Кирка",
    "item.allthemodium.alloy_sword": "Сплавной Меч",
    "item.allthemodium.alloy_shovel": "Сплавная Лопата",
    "item.allthemodium.alloy_paxel": "Сплавной Паксель",
    "item.allthemodium.vibranium_nugget": "Кусочек Вибраниума",
    "block.allthemodium.vibranium_ore": "Руда Вибраниума",
    "block.allthemodium.other_vibranium_ore": "Руда Вибраниума Другого",
    "block.allthemodium.vibranium_block": "Блок Вибраниума",
    "item.allthemodium.vibranium_ingot": "Слиток Вибраниума",
    "item.allthemodium.vibranium_dust": "Пыль Вибраниума",
    "item.allthemodium.unobtainium_nugget": "Кусочек Анобтейниума",
    "block.allthemodium.unobtainium_ore": "Руда Анобтейниума",
    "block.allthemodium.unobtainium_block": "Блок Анобтейниума",
    "item.allthemodium.unobtainium_ingot": "Слиток Анобтейниума",
    "item.allthemodium.unobtainium_dust": "Пыль Анобтейниума",
    "block.allthemodium.teleport_pad": "Телепортационная платформа",
    "block.allthemodium.piglich_heart_block": "Блок Сердца Пиглича",
    "item.allthemodium.piglich_heart": "Сердце Пиглича",
    "item.allthetweaks.atm_star_shard": "Осколок Звезды ATM",
    "item.allthetweaks.atm_star": "Звезда ATM",
    "item.allthetweaks.nexium_emitter": "Излучатель Нексиума",
    "item.allthetweaks.pulsating_black_hole": "Пульсирующая Черная Дыра",
    "item.allthetweaks.oblivion_shard": "Осколок Забвения",
    "item.allthetweaks.dragon_soul": "Душа Дракона",
    "item.allthetweaks.withers_compass": "Компас Иссушителя",
    "item.allthetweaks.dimensional_seed": "Семечко Измерений",
    "item.allthetweaks.patrick_star": "Патрик Стар",
    "item.allthetweaks.improbable_probability_device": "Устройство невероятной вероятности",
    "item.allthetweaks.mini_nether": "Мини-Незер",
    "item.allthetweaks.mini_exit": "Мини-Выход",
    "item.allthetweaks.mini_end": "Мини-Энд",
    "item.allthetweaks.philosophers_fuel": "Топливо Философа",
    "block.allthetweaks.nether_star_block": "Блок Звезды Незера",
    "block.allthetweaks.atm_star_block": "Блок Звезды ATM",
}

manual_ua = {
    "item.kubejs.alchemical_sulfur": "Алхімічна сірка",
    "item.kubejs.inert_nether_star": "Інертна зірка Незера",
    "item.kubejs.rudimentary_flower": "Рудиментарна квітка",
    "item.kubejs.cursed_doll": "Проклята лялька",
    "item.kubejs.corrupted_emerald": "Зіпсований смарагд",
    "block.kubejs.corrupted_emerald_block": "Блок зіпсованого смарагда",
    "item.allthemodium.allthemodium_pickaxe": "Кайло з Оллземодію",
    "item.allthemodium.vibranium_pickaxe": "Кайло з Вібраніуму",
    "item.allthemodium.unobtainium_pickaxe": "Кайло з Анобтейніуму",
    "item.allthemodium.allthemodium_axe": "Сокира з Оллземодію",
    "item.allthemodium.vibranium_axe": "Сокира з Вібраніуму",
    "item.allthemodium.unobtainium_axe": "Сокира з Анобтейніуму",
    "item.allthemodium.allthemodium_shovel": "Лопата з Оллземодію",
    "item.allthemodium.vibranium_shovel": "Лопата з Вібраніуму",
    "item.allthemodium.unobtainium_shovel": "Лопата з Анобтейніуму",
    "item.allthemodium.allthemodium_hoe": "Мотика з Оллземодію",
    "item.allthemodium.vibranium_hoe": "Мотика з Вібраніуму",
    "item.allthemodium.unobtainium_hoe": "Мотика з Анобтейніуму",
    "item.allthemodium.allthemodium_sword": "Меч з Оллземодію",
    "item.allthemodium.vibranium_sword": "Меч з Вібраніуму",
    "item.allthemodium.unobtainium_sword": "Меч з Анобтейніуму",
    "item.allthemodium.allthemodium_plate": "Пластина з Оллземодію",
    "item.allthemodium.vibranium_plate": "Пластина з Вібраніуму",
    "item.allthemodium.unobtainium_plate": "Пластина з Анобтейніуму",
    "item.allthemodium.allthemodium_rod": "Стрижень з Оллземодію",
    "item.allthemodium.vibranium_rod": "Стрижень з Вібраніуму",
    "item.allthemodium.unobtainium_rod": "Стрижень з Анобтейніуму",
    "item.allthemodium.allthemodium_gear": "Шестерня з Оллземодію",
    "item.allthemodium.vibranium_gear": "Шестерня з Вібраніуму",
    "item.allthemodium.unobtainium_gear": "Шестерня з Анобтейніуму",
    "item.allthemodium.raw_allthemodium": "Сирий Оллземодій",
    "item.allthemodium.raw_vibranium": "Сирий Вібраніум",
    "item.allthemodium.raw_unobtainium": "Сирий Анобтейніум",
    "item.allthemodium.allthemodium_apple": "Яблуко з Оллземодію",
    "item.allthemodium.allthemodium_dust": "Пил Оллземодію",
    "item.allthemodium.allthemodium_nugget": "Шматочок Оллземодію",
    "item.allthemodium.allthemodium_ingot": "Зливок Оллземодію",
    "item.allthemodium.allthemodium_carrot": "Морква з Оллземодію",
    "block.allthemodium.allthemodium_ore": "Руда Оллземодію",
    "block.allthemodium.allthemodium_slate_ore": "Глибинна руда Оллземодію",
    "block.allthemodium.allthemodium_block": "Блок Оллземодію",
    "item.allthemodium.allthemodium_helmet": "Шолом з Оллземодію",
    "item.allthemodium.allthemodium_chestplate": "Нагрудник з Оллземодію",
    "item.allthemodium.allthemodium_leggings": "Поножі з Оллземодію",
    "item.allthemodium.allthemodium_boots": "Черевики з Оллземодію",
    "item.allthemodium.crushed_allthemodium": "Подрібнений Оллземодій",
    "item.allthemodium.crushed_vibranium": "Подрібнений Вібраніум",
    "item.allthemodium.crushed_unobtainium": "Подрібнений Анобтейніум",
    "item.allthemodium.vibranium_helmet": "Шолом з Вібраніуму",
    "item.allthemodium.vibranium_chestplate": "Нагрудник з Вібраніуму",
    "item.allthemodium.vibranium_leggings": "Поножі з Вібраніуму",
    "item.allthemodium.vibranium_boots": "Черевики з Вібраніуму",
    "item.allthemodium.unobtainium_helmet": "Шолом з Анобтейніуму",
    "item.allthemodium.unobtainium_chestplate": "Нагрудник з Анобтейніуму",
    "item.allthemodium.unobtainium_leggings": "Поножі з Анобтейніуму",
    "item.allthemodium.unobtainium_boots": "Черевики з Анобтейніуму",
    "item.allthemodium.alloy_axe": "Сплавна Сокира",
    "item.allthemodium.alloy_pick": "Сплавне Кайло",
    "item.allthemodium.alloy_sword": "Сплавний Меч",
    "item.allthemodium.alloy_shovel": "Сплавна Лопата",
    "item.allthemodium.alloy_paxel": "Сплавний Паксель",
    "item.allthemodium.vibranium_nugget": "Шматочок Вібраніуму",
    "block.allthemodium.vibranium_ore": "Руда Вібраніуму",
    "block.allthemodium.other_vibranium_ore": "Руда Вібраніуму Іншого",
    "block.allthemodium.vibranium_block": "Блок Вібраніуму",
    "item.allthemodium.vibranium_ingot": "Зливок Вібраніуму",
    "item.allthemodium.vibranium_dust": "Пил Вібраніуму",
    "item.allthemodium.unobtainium_nugget": "Шматочок Анобтейніуму",
    "block.allthemodium.unobtainium_ore": "Руда Анобтейніуму",
    "block.allthemodium.unobtainium_block": "Блок Анобтейніуму",
    "item.allthemodium.unobtainium_ingot": "Зливок Анобтейніуму",
    "item.allthemodium.unobtainium_dust": "Пил Анобтейніуму",
    "block.allthemodium.teleport_pad": "Телепортаційна платформа",
    "block.allthemodium.piglich_heart_block": "Блок Серця Пігліча",
    "item.allthemodium.piglich_heart": "Серце Пігліча",
    "item.allthetweaks.atm_star_shard": "Уламок Зірки ATM",
    "item.allthetweaks.atm_star": "Зірка ATM",
    "item.allthetweaks.nexium_emitter": "Випромінювач Нексіуму",
    "item.allthetweaks.pulsating_black_hole": "Пульсуюча Чорна Діра",
    "item.allthetweaks.oblivion_shard": "Уламок Забуття",
    "item.allthetweaks.dragon_soul": "Душа Дракона",
    "item.allthetweaks.withers_compass": "Компас Візера",
    "item.allthetweaks.dimensional_seed": "Насіння Вимірів",
    "item.allthetweaks.patrick_star": "Патрік Стар",
    "item.allthetweaks.improbable_probability_device": "Пристрій неймовірної ймовірності",
    "item.allthetweaks.mini_nether": "Міні-Незер",
    "item.allthetweaks.mini_exit": "Міні-Вихід",
    "item.allthetweaks.mini_end": "Міні-Енд",
    "item.allthetweaks.philosophers_fuel": "Паливо Філософа",
    "block.allthetweaks.nether_star_block": "Блок Зірки Незера",
    "block.allthetweaks.atm_star_block": "Блок Зірки ATM",
}

# Materials for Compressed Blocks
# key_part : (Ru Name, Ua Name)
materials = {
    "acacia_log": ("Бревно акации", "Колода акації"),
    "acacia_planks": ("Доски акации", "Дошки акації"),
    "allthemodium_block": ("Блок Оллземодия", "Блок Оллземодію"),
    "aluminum_block": ("Алюминиевый блок", "Алюмінієвий блок"),
    "amethyst_block": ("Блок аметиста", "Блок аметисту"),
    "ancient_log_0": ("Древнее бревно", "Стародавня колода"),
    "ancient_stone": ("Древний камень", "Стародавній камінь"),
    "andesite": ("Андезит", "Андезит"),
    "antimatter_block": ("Блок антиматерии", "Блок антиматерії"),
    "atm_star_block": ("Блок Звезды ATM", "Блок Зірки ATM"),
    "basalt": ("Базальт", "Базальт"),
    "birch_log": ("Березовое бревно", "Березова колода"),
    "birch_planks": ("Березовые доски", "Березові дошки"),
    "black_concrete": ("Черный бетон", "Чорний бетон"),
    "blackstone": ("Чернит", "Чорнит"),
    "blaze_rod_block": ("Блок стержней ифрита", "Блок стрижнів іфриту"),
    "blazing_crystal_block": ("Блок пылающего кристалла", "Блок палаючого кристалу"),
    "blue_concrete": ("Синий бетон", "Синій бетон"),
    "bone_block": ("Костяной блок", "Кістковий блок"),
    "brass_block": ("Латунный блок", "Латунний блок"),
    "bricks": ("Кирпичи", "Цегла"),
    "bronze_block": ("Бронзовый блок", "Бронзовий блок"),
    "brown_concrete": ("Коричневый бетон", "Коричневий бетон"),
    "calcite": ("Кальцит", "Кальцит"),
    "certus_quartz_block": ("Блок истинного кварца", "Блок істинного кварцу"),
    "charged_redstone_block": ("Заряженный блок редстоуна", "Заряджений блок редстоуну"),
    "cinnabar_block": ("Блок киновари", "Блок кіновару"),
    "clay": ("Глина", "Глина"),
    "coal_block": ("Угольный блок", "Вугільний блок"),
    "cobbled_deepslate": ("Дробленый сланец", "Подрібнений сланець"),
    "cobblestone": ("Булыжник", "Кругляк"),
    "compressed_iron_block": ("Блок сжатого железа", "Блок стисненого заліза"),
    "conductive_alloy_block": ("Блок проводящего сплава", "Блок провідного сплаву"),
    "constantan_block": ("Блок константана", "Блок константану"),
    "copper_alloy_block": ("Блок медного сплава", "Блок мідного сплаву"),
    "copper_block": ("Медный блок", "Мідний блок"),
    "cyan_concrete": ("Бирюзовый бетон", "Бірюзовий бетон"),
    "dark_oak_log": ("Бревно темного дуба", "Колода темного дуба"),
    "dark_oak_planks": ("Доски темного дуба", "Дошки темного дуба"),
    "dark_steel_block": ("Блок темной стали", "Блок темної сталі"),
    "deepslate": ("Глубинный сланец", "Глибинний сланець"),
    "diamond_block": ("Алмазный блок", "Діамантовий блок"),
    "diorite": ("Диорит", "Діорит"),
    "dirt": ("Земля", "Земля"),
    "dried_kelp_block": ("Блок сушеной ламинарии", "Блок сушеної ламінарії"),
    "dripstone_block": ("Блок капельника", "Блок крапельника"),
    "electrum_block": ("Блок электрума", "Блок електруму"),
    "emerald_block": ("Изумрудный блок", "Смарагдовий блок"),
    "end_steel_block": ("Блок стали Энда", "Блок сталі Енду"),
    "end_stone": ("Камень Энда", "Камінь Енду"),
    "ender_pearl_block": ("Блок жемчуга Энда", "Блок перлини Енду"),
    "enderium_block": ("Блок эндериума", "Блок ендеріуму"),
    "energetic_alloy_block": ("Блок энергетического сплава", "Блок енергетичного сплаву"),
    "energized_steel_block": ("Блок заряженной стали", "Блок зарядженої сталі"),
    "entro_block": ("Блок энтро", "Блок ентро"),
    "flint_block": ("Блок кремня", "Блок креміню"),
    "fluix_block": ("Блок флюикса", "Блок флюїксу"),
    "fluorite_block": ("Блок флюорита", "Блок флюориту"),
    "glass": ("Стекло", "Скло"),
    "glowstone": ("Светокамень", "Світлокамінь"),
    "gold_block": ("Золотой блок", "Золотий блок"),
    "granite": ("Гранит", "Граніт"),
    "grass_block": ("Блок травы", "Блок трави"),
    "gravel": ("Гравий", "Гравій"),
    "gray_concrete": ("Серый бетон", "Сірий бетон"),
    "green_concrete": ("Зеленый бетон", "Зелений бетон"),
    "greg_star_block": ("Блок GregStar", "Блок GregStar"),
    "hay_block": ("Сноп сена", "Сніп сіна"),
    "honey_block": ("Блок меда", "Блок меду"),
    "honeycomb_block": ("Блок сот", "Блок стільників"),
    "invar_block": ("Блок инвара", "Блок інвару"),
    "iridium_block": ("Блок иридия", "Блок іридію"),
    "iron_block": ("Железный блок", "Залізний блок"),
    "jungle_log": ("Бревно тропического дерева", "Колода тропічного дерева"),
    "jungle_planks": ("Доски тропического дерева", "Дошки тропічного дерева"),
    "kivi": ("Киви", "Ківі"),
    "lapis_block": ("Лазуритовый блок", "Лазуритовий блок"),
    "lead_block": ("Свинцовый блок", "Свинцевий блок"),
    "light_blue_concrete": ("Голубой бетон", "Блакитний бетон"),
    "light_gray_concrete": ("Светло-серый бетон", "Світло-сірий бетон"),
    "lime_concrete": ("Лаймовый бетон", "Лаймовий бетон"),
    "lumium_block": ("Блок люмиума", "Блок люміуму"),
    "magenta_concrete": ("Пурпурный бетон", "Пурпуровий бетон"),
    "magma_block": ("Блок магмы", "Блок магми"),
    "mangrove_log": ("Мангровое бревно", "Мангрова колода"),
    "mangrove_planks": ("Мангровые доски", "Мангрові дошки"),
    "melon": ("Арбуз", "Кавун"),
    "moss_block": ("Блок мха", "Блок моху"),
    "mycelium": ("Мицелий", "Міцелій"),
    "nether_star_block": ("Блок Звезды Незера", "Блок Зірки Незера"),
    "netherite_block": ("Незеритовый блок", "Незеритовий блок"),
    "netherrack": ("Незерак", "Незерак"),
    "nickel_block": ("Никелевый блок", "Нікелевий блок"),
    "niotic_crystal_block": ("Блок ниотического кристалла", "Блок ніотичного кристалу"),
    "nitro_crystal_block": ("Блок нитро-кристалла", "Блок нітро-кристалу"),
    "oak_log": ("Дубовое бревно", "Дубова колода"),
    "oak_planks": ("Дубовые доски", "Дубові дошки"),
    "obsidian": ("Обсидиан", "Обсидіан"),
    "orange_concrete": ("Оранжевый бетон", "Помаранчевий бетон"),
    "osmium_block": ("Осмиевый блок", "Осмієвий блок"),
    "peridot_block": ("Блок перидота", "Блок перидоту"),
    "piglich_heart_block": ("Блок сердца Пиглича", "Блок серця Пігліча"),
    "pink_concrete": ("Розовый бетон", "Рожевий бетон"),
    "platinum_block": ("Платиновый блок", "Платиновий блок"),
    "podzol": ("Подзол", "Підзол"),
    "pulsating_alloy_block": ("Блок пульсирующего сплава", "Блок пульсуючого сплаву"),
    "pumpkin": ("Тыква", "Гарбуз"),
    "purple_concrete": ("Фиолетовый бетон", "Фіолетовий бетон"),
    "quartz_block": ("Кварцевый блок", "Кварцовий блок"),
    "raw_allthemodium_block": ("Блок сырого Оллземодия", "Блок сирого Оллземодію"),
    "raw_aluminum_block": ("Блок сырого алюминия", "Блок сирого алюмінію"),
    "raw_copper_block": ("Блок сырой меди", "Блок сирої міді"),
    "raw_gold_block": ("Блок сырого золота", "Блок сирого золота"),
    "raw_iridium_block": ("Блок сырого иридия", "Блок сирого іридію"),
    "raw_iron_block": ("Блок сырого железа", "Блок сирого заліза"),
    "raw_lead_block": ("Блок сырого свинца", "Блок сирого свинцю"),
    "raw_nickel_block": ("Блок сырого никеля", "Блок сирого нікелю"),
    "raw_osmium_block": ("Блок сырого осмия", "Блок сирого осмію"),
    "raw_platinum_block": ("Блок сырой платины", "Блок сирої платини"),
    "raw_silver_block": ("Блок сырого серебра", "Блок сирого срібла"),
    "raw_tin_block": ("Блок сырого олова", "Блок сирого олова"),
    "raw_unobtainium_block": ("Блок сырого Анобтейниума", "Блок сирого Анобтейніуму"),
    "raw_uranium_block": ("Блок сырого урана", "Блок сирого урану"),
    "raw_vibranium_block": ("Блок сырого Вибраниума", "Блок сирого Вібраніуму"),
    "raw_zinc_block": ("Блок сырого цинка", "Блок сирого цинку"),
    "red_concrete": ("Красный бетон", "Червоний бетон"),
    "red_sand": ("Красный песок", "Червоний пісок"),
    "redstone_alloy_block": ("Блок редстоунового сплава", "Блок редстоунового сплаву"),
    "redstone_block": ("Редстоуновый блок", "Редстоуновий блок"),
    "ruby_block": ("Рубиновый блок", "Рубіновий блок"),
    "salt_block": ("Блок соли", "Блок солі"),
    "sand": ("Песок", "Пісок"),
    "sapphire_block": ("Сапфировый блок", "Сапфіровий блок"),
    "signalum_block": ("Блок сигналлума", "Блок сігналуму"),
    "silicon_block": ("Кремниевый блок", "Кремнієвий блок"),
    "silver_block": ("Серебряный блок", "Срібний блок"),
    "sky_bronze_block": ("Блок небесной бронзы", "Блок небесної бронзи"),
    "sky_osmium_block": ("Блок небесного осмия", "Блок небесного осмію"),
    "sky_steel_block": ("Блок небесной стали", "Блок небесної сталі"),
    "sky_stone_block": ("Блок небесного камня", "Блок небесного каменю"),
    "smooth_stone": ("Гладкий камень", "Гладкий камінь"),
    "snow": ("Снег", "Сніг"),
    "soul_sand": ("Песок душ", "Пісок душ"),
    "soul_soil": ("Почва душ", "Грунт душ"),
    "soularium_block": ("Блок соулариума", "Блок соуларіуму"),
    "spirited_crystal_block": ("Блок духовного кристалла", "Блок духовного кристалу"),
    "sponge": ("Губка", "Губка"),
    "spruce_log": ("Еловое бревно", "Ялинова колода"),
    "spruce_planks": ("Еловые доски", "Ялинові дошки"),
    "steel_block": ("Стальной блок", "Сталевий блок"),
    "stone": ("Камень", "Камінь"),
    "sulfur_block": ("Серный блок", "Сірчаний блок"),
    "terracotta": ("Терракота", "Теракота"),
    "tin_block": ("Оловянный блок", "Олов'яний блок"),
    "tuff": ("Туф", "Туф"),
    "unobtainium_allthemodium_alloy_block": ("Сплав Анобтейниум-Оллземодий", "Сплав Анобтейніум-Оллземодій"),
    "unobtainium_block": ("Блок Анобтейниума", "Блок Анобтейніуму"),
    "unobtainium_vibranium_alloy_block": ("Сплав Анобтейниум-Вибраниум", "Сплав Анобтейніум-Вібраніум"),
    "uraninite_block": ("Блок уранинита", "Блок уранініту"),
    "uranium_block": ("Урановый блок", "Урановий блок"),
    "vibranium_allthemodium_alloy_block": ("Сплав Вибраниум-Оллземодий", "Сплав Вібраніум-Оллземодій"),
    "vibranium_block": ("Блок Вибраниума", "Блок Вібраніуму"),
    "vibrant_alloy_block": ("Блок вибрантного сплава", "Блок вібрантного сплаву"),
    "wax_block": ("Блок воска", "Блок воску"),
    "white_concrete": ("Белый бетон", "Білий бетон"),
    "xychorium_storage_blue": ("Блок синего ксикориума", "Блок синього ксікоріуму"),
    "xychorium_storage_dark": ("Блок темного ксикориума", "Блок темного ксікоріуму"),
    "xychorium_storage_green": ("Блок зеленого ксикориума", "Блок зеленого ксікоріуму"),
    "xychorium_storage_light": ("Блок светлого ксикориума", "Блок світлого ксікоріуму"),
    "xychorium_storage_red": ("Блок красного ксикориума", "Блок червоного ксікоріуму"),
    "yellow_concrete": ("Желтый бетон", "Жовтий бетон"),
    "zinc_block": ("Цинковый блок", "Цинковий блок"),
}


def load_dump_translations():
    dump_file = os.path.join(os.path.dirname(base_dir), "..", "missing_translations_dump.json")
    # Adjust path if needed. base_dir is .../kubejs/assets/atm10_localization/lang
    # dump file is in .../kubejs/missing_translations_dump.json
    # so we need to go up 3 levels?
    # base_dir = kubejs/assets/atm10_localization/lang
    # target = kubejs/missing_translations_dump.json
    
    # Actually, let's just use the absolute path relative to the script execution or something reliable.
    # The script is usually run from the server root or kubejs folder.
    # Let's try dynamic path assumption based on script location.
    # Script is likely in D:\бэкап сервера 29.01\kubejs\generate_localization.py
    # Dump is in D:\бэкап сервера 29.01\kubejs\missing_translations_dump.json
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dump_path = os.path.join(script_dir, "missing_translations_dump.json")
    
    if os.path.exists(dump_path):
        with open(dump_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    print(f"Warning: Dump file not found at {dump_path}")
    return {}

# Pattern Matchers for Auto-Translation
# (Regex, Ru Replacement, Ua Replacement)
patterns = [
    (r"(.*) Spawn Egg", r"Яйцо призыва \1", r"Яйце призиву \1"),
    (r"Block of (.*)", r"Блок \1", r"Блок \1"),
    (r"(.*) Ore", r"Руда \1", r"Руда \1"),
    (r"(.*) Bricks", r"Кирпичи \1", r"Цегла \1"),
    (r"(.*) Planks", r"Доски \1", r"Дошки \1"),
    (r"(.*) Log", r"Бревно \1", r"Колода \1"),
    (r"(.*) Wood", r"Древесина \1", r"Деревина \1"),
    (r"(.*) Leaves", r"Листва \1", r"Листя \1"),
    (r"(.*) Sapling", r"Саженец \1", r"Саджанець \1"),
    (r"(.*) Slab", r"Плита \1", r"Плита \1"),
    (r"(.*) Stairs", r"Ступеньки \1", r"Сходи \1"),
    (r"(.*) Fence Gate", r"Калитка \1", r"Хвіртка \1"),
    (r"(.*) Fence", r"Забор \1", r"Паркан \1"),
    (r"(.*) Wall", r"Стена \1", r"Стіна \1"),
    (r"(.*) Trapdoor", r"Люк \1", r"Люк \1"),
    (r"(.*) Door", r"Дверь \1", r"Двері \1"),
    (r"(.*) Button", r"Кнопка \1", r"Кнопка \1"),
    (r"(.*) Pressure Plate", r"Нажимная плита \1", r"Натискна плита \1"),
    (r"(.*) Ingot", r"Слиток \1", r"Зливок \1"),
    (r"(.*) Nugget", r"Кусочек \1", r"Шматочок \1"),
    (r"(.*) Dust", r"Пыль \1", r"Пил \1"),
    (r"(.*) Gem", r"Драгоценный камень \1", r"Коштовний камінь \1"),
    (r"(.*) Shard", r"Осколок \1", r"Уламок \1"),
    (r"(.*) Crystal", r"Кристалл \1", r"Кристал \1"),
    (r"(.*) Clump", r"Гроздь \1", r"Гроно \1"),
    (r"(.*) Seed", r"Семя \1", r"Насіння \1"),
    (r"(.*) Seeds", r"Семена \1", r"Насіння \1"),
    (r"(.*) Bucket", r"Ведро \1", r"Відро \1"),
    (r"(.*) Helmet", r"Шлем \1", r"Шолом \1"),
    (r"(.*) Chestplate", r"Нагрудник \1", r"Нагрудник \1"),
    (r"(.*) Leggings", r"Поножи \1", r"Поножі \1"),
    (r"(.*) Boots", r"Ботинки \1", r"Черевики \1"),
    (r"(.*) Sword", r"Меч \1", r"Меч \1"),
    (r"(.*) Pickaxe", r"Кирка \1", r"Кайло \1"),
    (r"(.*) Axe", r"Топор \1", r"Сокира \1"),
    (r"(.*) Shovel", r"Лопата \1", r"Лопата \1"),
    (r"(.*) Hoe", r"Мотыга \1", r"Мотика \1"),
    (r"(.*) Blueprint", r"Чертеж \1", r"Креслення \1"),
    (r"(.*) Template", r"Шаблон \1", r"Шаблон \1"),
    (r"(.*) Beehive", r"Улей \1", r"Вулик \1"),
    (r"(.*) Nest", r"Гнездо \1", r"Гніздо \1"),
    (r"Raw (.*)", r"Сырой \1", r"Сирий \1"),
    (r"Chiseled (.*)", r"Резной \1", r"Різьблений \1"),
    (r"Smooth (.*)", r"Гладкий \1", r"Гладкий \1"),
    (r"Polished (.*)", r"Полированный \1", r"Полірований \1"),
    (r"Deepslate (.*)", r"Глубинный \1", r"Глибинний \1"),
    (r"Crushed (.*)", r"Измельченный \1", r"Подрібнений \1"),
    (r"Reinforced (.*)", r"Укрепленный \1", r"Укріплений \1"),
    (r"Advanced (.*)", r"Продвинутый \1", r"Просунутий \1"),
]

def auto_translate(text, lang='ru'):
    # Simple regex replacement attempt
    for pattern, ru_repl, ua_repl in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            repl = ru_repl if lang == 'ru' else ua_repl
            try:
                # Use regex sub to replace the captured group in the target string
                # We need to flip the logic slightly: 
                # If regex is "(.*) Ore", text is "Silver Ore", group 1 is "Silver".
                # Rep string is "Руда \1" -> "Руда Silver".
                # Ideally we recursively translate "Silver" too, but that's hard.
                # Let's just do the structure swap first.
                return re.sub(pattern, repl, text, flags=re.IGNORECASE)
            except:
                pass
    return text

def generate():
    # Load source keys
    if os.path.exists(pt_file):
        with open(pt_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = {}

    # Load dump data
    dump_data = load_dump_translations()
    
    # Merge existing data with dump data (dump data takes priority if we want to ensure coverage, 
    # but initially we just want to ADD missing items that aren't in PT file if any)
    # Actually, we want to iterate over EVERYTHING for translation.
    
    all_keys = set(data.keys()) | set(dump_data.keys())

    ru_out = {}
    ua_out = {}

    for key in all_keys:
        # Get English text (or whatever value is available)
        val = dump_data.get(key, data.get(key, ""))

        # Handle manual overrides first
        if key in manual_ru:
            ru_out[key] = manual_ru[key]
        if key in manual_ua:
            ua_out[key] = manual_ua[key]

        # Handle Compressed Blocks
        if "allthecompressed" in key and "_1x" in key:
            match = re.search(r"allthecompressed\.(.+)_(\d)x", key)
            if match:
                mat_key = match.group(1)
                tier = match.group(2)
                
                if mat_key in materials:
                    ru_name, ua_name = materials[mat_key]
                    ru_out[key] = f"{ru_name} {tier}x"
                    ua_out[key] = f"{ua_name} {tier}x"

        # If still not translated, try to be smart or leave generic
        if key not in ru_out:
            if key in dump_data:
                ru_out[key] = auto_translate(val, 'ru')
            else:
                 ru_out[key] = val

        if key not in ua_out:
             if key in dump_data:
                 ua_out[key] = auto_translate(val, 'ua')
             else:
                 ua_out[key] = val

    # Write files
    with open(ru_file, 'w', encoding='utf-8') as f:
        json.dump(ru_out, f, indent=4, ensure_ascii=False)
    
    with open(ua_file, 'w', encoding='utf-8') as f:
        json.dump(ua_out, f, indent=4, ensure_ascii=False)

    print(f"Generation complete. Processed {len(all_keys)} keys.")

if __name__ == "__main__":
    try:
        generate()
    except Exception as e:
        with open("error_log.txt", "w") as f:
            import traceback
            traceback.print_exc(file=f)
            print(e)


