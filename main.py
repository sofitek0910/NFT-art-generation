from PIL import Image 
from IPython.display import display 
import random
import json
import sys

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = [
    "background 01", 
    "background 02", 
    "background 03", 
    "background 04", 
    "background 05",
    "background 06", 
    "background 07", 
    "background 08", 
    "background 09", 
    "background 10"
] 
background_weights = [
    30, 25, 15, 20, 10
]

body = [
    "Body 01",
    "Body 02",
    "Body 03",
    "Body 04",
    "Body 05",
    "Body 06",
    "Body 07",
    "Body 08",
    "Body 09",
    "Body 10",
    "Body 11",
    "Body 12"
] 

body_weights = [
    50, 50
]

clothes = [
    "Dress 01",
    "Dress 02",
    "Dress 03",
    "Dress 04",
    "Dress 05",
    "Dress 06",
    "Dress 07",
    "Dress 08",
    "Dress 09",
    "Dress 10",
    "Dress 11",
    "Dress 12",
    "Dress 13",
    "Dress 14",
    "Dress 15",
    "Dress 16",
    "Dress 17",
    "Dress 18",
    "Dress 19",
    "Dress 20",
    "Dress 21",
    "Dress 22",
    "Dress 23",
    "Dress 24",
    "Dress 25",
    "Dress 26",
    "Dress 27",
    "Dress 28",
    "Dress 29",
    "Dress 30",
    "Dress 31",
    "Dress 32",
    "Dress 33",
    "Dress 34",
    "Dress 35",
    "Dress 36",
    "Dress 37",
    "Dress 38",
    "Dress 39"
] 

clothes_weights = [
    20, 40, 25, 15
]

hat = [
    "Head 01",
    "Head 02",
    "Head 03",
    "Head 04",
    "Head 05",
    "Head 06",
    "Head 07",
    "Head 08",
    "Head 09",
    "Head 10",
    "Head 11",
    "Head 12",
    "Head 13",
    "Head 14",
    "Head 15",
    "Head 16",
    "Head 17",
    "Head 18",
    "Head 19",
    "Head 20"
] 

hat_weights = [
    40, 30 ,30
]

eye = [
    "Eye 01",
    "Eye 02",
    "Eye 03",
    "Eye 04",
    "Eye 05",
    "Eye 06",
    "Eye 07",
    "Eye 08",
    "Eye 09",
    "Eye 10"
] 

eye_weights = [
    30, 30, 40
]

mouth = [
    "Mouth 01",
    "Mouth 02",
    "Mouth 03",
    "Mouth 04",
    "Mouth 05",
    "Mouth 06",
    "Mouth 07",
    "Mouth 08",
    "Mouth 09",
    "Mouth 10"
] 

mouth_weights = [
    5, 5, 3, 3, 3, 5, 3, 3, 5, 3, 
    5, 3, 5, 3, 5, 3, 12, 13, 13
]

accessories = [
    "Accessories 01",
    "Accessories 02",
    "Accessories 03",
    "Accessories 04",
    "Accessories 05",
    "Accessories 06",
    "Accessories 07",
    "Accessories 08",
    "Accessories 09",
    "Accessories 10",
    "Accessories 11",
    "Accessories 12",
    "Accessories 13",
    "Accessories 14",
    "Accessories 15",
    "Accessories 16",
    "Accessories 17",
    "Accessories 18",
    "Accessories 19",
    "Accessories 20"
] 


# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

background_files = {
    "background-1": "1",
    "background-2": "2",
    "background-3": "3",
    "background-4": "4",
    "background-5": "5"
}

skin_color_files = {
    "skin-1": "1",
    "skin-2": "2"
}

clothes_files = {
    "clothes-1": "1",
    "clothes-2": "2",
    "clothes-3": "3",
    "clothes-4": "4"
}

hat_files = {
    "hat-1": "1",
    "hat-2": "2",
    "hat-3": "3"
}


facial_files = {
    "facial-1": "1",
    "facial-2": "2",
    "facial-3": "3"
}

hair_files = {
    "hair-1": "1",
    "hair-2": "2",
    "hair-3": "3",
    "hair-4": "4",
    "hair-5": "5",
    "hair-6": "6",
    "hair-7": "7",
    "hair-8": "8",
    "hair-9": "9",
    "hair-10": "10",
    "hair-11": "11", 
    "hair-12": "12",
    "hair-13": "13",
    "hair-14": "14",
    "hair-15": "15",
    "hair-16": "16",
    "hair-17": "17",
    "hair-18": "18",
    "hair-19": "19"
}

## Generate Traits
TOTAL_IMAGES = 50   # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():

    sys.setrecursionlimit(3000)

    new_image = {} #
    
    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Skin_color"] = random.choices(skin_color, skin_color_weights)[0]
    new_image ["Clothes"] = random.choices(clothes, clothes_weights)[0]
    # new_image ["Hat"] = random.choices(hat, hat_weights)[0]
    new_image ["Facial"] = random.choices(facial, facial_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    # new_image ["Background"] = random.choices(background, background_weights)[0]
    # new_image ["Helm_backpieces"] = 'helm_backpieces-5'
    # new_image ["Armor_back_pieces"] = random.choices(armor_back_pieces, armor_back_pieces_weights)[0]
    # new_image ["Base_body"] = random.choices(base_body, base_body_weights)[0]
    # new_image ["Tattoos"] = random.choices(tattoos, tattoos_weights)[0]
    # new_image ["Battle_armors"] = random.choices(battle_armors, battle_armors_weights)[0]
    # new_image ["Scars"] = random.choices(scars, scars_weights)[0]  
    
    # new_image ["War_paint"] = random.choices(war_paint, war_paint_weights)[0]  
    # new_image ["Eyebrows"] = random.choices(eyebrows, eyebrows_weights)[0]
    # new_image ["Hair"] = random.choices(hair, hair_weights)[0]   
    # new_image ["Mage_hoods"] = random.choices(mage_hoods, mage_hoods_weights)[0]
    # new_image ["Beards"] = random.choices(beards, beards_weights)[0]
    # new_image ["Weapon"] = random.choices(weapon, weapon_weights)[0]
    # new_image ["Arm_armor"] = random.choices(arm_armor, arm_armor_weights)[0]
    # new_image ["Extras"] = random.choices(extras, extras_weights)[0]


    # Constraint first

    # #  Color of beard must match color of hair and eyebrows
    # random_color_index = random.randint(0, 8)
    # random_type_eyebrow = random.randint(0, 4)
    # random_type_hair = random.randint(0, 7)
    # random_type_beard = random.randint(0, 4)
    
    # new_image['Eyebrows'] = eyebrows[random_type_eyebrow * 9 + random_color_index]
    # new_image['Hair'] = hair[random_type_hair * 9 + random_color_index]
    # new_image['Beards'] = beards[random_type_beard * 9 + random_color_index]

    # # Color for Base Body, Arm Position and Facial Expression must be the same color = eg: Black or Tan or White Skin colors
    # random_color_index_two = random.randint(0, 2)
    # random_type_arms = random.randint(0, 4)
    # random_type_expressions = random.randint(0, 28)

    # new_image['Arms'] = arms[random_type_arms * 3 + random_color_index_two]
    # new_image['Base_body'] = base_body[random_color_index_two]
    # new_image['Facial_expressions'] = facial_expressions[random_type_expressions * 3 + random_color_index_two]

    # # Colors of ARMOR, ARM ARMOR and HELMET must all be the same
    # # enclosed armors and helmetless armors
    # random_color_index_three = random.randint(0, 9)
    # if 'explorer' in battle_armors_files[new_image['Battle_armors']] or 'observer' in battle_armors_files[new_image['Battle_armors']] or 'Explorer' in battle_armors_files[new_image['Battle_armors']]:
        
    #     random_type_arm_armor = random.randint(0, 9)
    #     random_type_helmetless_armor = random.randint(0, 3)
    #     random_type_warpaint = random.randint(0, 1)

    #     new_image['Arm_armor'] = arm_armor[random_type_arm_armor * 10 + random_color_index_three]
    #     new_image['Battle_armors'] = battle_armors[random_type_helmetless_armor * 10 + 16 + random_color_index_three]
    #     new_image["War_paint"] = war_paint[random_type_warpaint * 10 + random_color_index_three]

    # # battle armors
    # else:
    #     random_type_warpaint_special = random.randint(0, 13)

    #     if 'commander silver' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'commander silver' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         else: 
    #             new_image["War_paint"] = war_paint[random_type_warpaint_special * 10]
    #         # if not 'silver' in head_pieces_files[new_image['Head_pieces']] and 'and silver' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()
    #     if 'aqua' in battle_armors_files[new_image['Battle_armors']] or 'trooper angel' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'aqua' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
            
    #         # if not 'aqua' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'trooper black' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'black' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         else: 
    #             new_image["War_paint"] = war_paint[random_type_warpaint_special * 10 + 1]
    #         # if not 'black' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'brawler' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'brawler' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'aqua' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'bubblegum' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'bubblegum' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'Bubblegum' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'commander bronze' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'commander bronze' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'gold' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'gold commander' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'commander gold' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         else: 
    #             new_image["War_paint"] = war_paint[random_type_warpaint_special * 10 + 4]
    #         # if not 'gold' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'gold and silver' in battle_armors_files[new_image['Battle_armors']] or 'trooper gold' in battle_armors_files[new_image['Battle_armors']]:
    #         print('trooper gold')
    #         if not 'trooper gold' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         else: 
    #             new_image["War_paint"] = war_paint[random_type_warpaint_special * 10]
    #         # if not 'gold and silver' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'trooper lava' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'lava' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'lava' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'moss' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'moss' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'moss' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'protector' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'protector' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'angel' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'rainbow' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'rainbow' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'rainbow' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'armor silver' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'trooper silver' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         else: 
    #             new_image["War_paint"] = war_paint[random_type_warpaint_special * 10]
    #         # if not 'silver' in head_pieces_files[new_image['Head_pieces']] and 'and silver' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    #     if 'trooper sun' in battle_armors_files[new_image['Battle_armors']]:
    #         if not 'sun' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         # if not 'sun' in head_pieces_files[new_image['Head_pieces']]:
    #         #     return create_new_image()

    # # enclosed armors and mage hood can only have short hair
    # if 'enclosed_armors' in new_image['Battle_armors'] or 'mage hood' in mage_hoods_files[new_image['Mage_hoods']]:
    #     if not ('short' in hair_files[new_image['Hair']] or 'lizard' in hair_files[new_image['Hair']]):
    #         return create_new_image()
    #     if not('handlebars' in beards_files[new_image['Beards']] or 'goatee mustache' in beards_files[new_image['Beards']] or 'scruffy braid' in beards_files[new_image['Beards']]  or 'short braids' in beards_files[new_image['Beards']]):
    #         return create_new_image()
        

    # #  Only BEARDS = Handlebars, Goatee mustache, Scruffy Braid beards can go with enclosed armors or Pilot Helmets
    # if 'handlebars' in beards_files[new_image['Beards']] or 'goatee mustache' in beards_files[new_image['Beards']] or 'scruffy braid' in beards_files[new_image['Beards']]:
    #     if not 'enclosed_armors' in new_image['Battle_armors']:
    #         return create_new_image()

    # #  Helmet Eyebrows are for Helmets and Enclose Suits/Armors
    # if 'helmet' in eyebrows_files[new_image['Eyebrows']]:
    #     # if new_image['Head_pieces'] == 'head_pieces-5' or not 'enclosed_armors' in new_image['Battle_armors']:
    #     if not 'enclosed_armors' in new_image['Battle_armors']:
    #         return create_new_image()
            
    # #  When a suit is picked it's corresponding suit back must be added  
    # if ('explorer' in battle_armors_files[new_image['Battle_armors']] or 'Explorer' in battle_armors_files[new_image['Battle_armors']]) and not 'helmetless' in battle_armors_files[new_image['Battle_armors']]:
    #     new_image['Armor_back_pieces'] = 'armor_back_pieces-40'
    # elif 'observer' in battle_armors_files[new_image['Battle_armors']] and not 'helmetless' in battle_armors_files[new_image['Battle_armors']]:
    #     new_image['Armor_back_pieces'] = 'armor_back_pieces-41' 
    # else: 

    #     if 'helmetless explorer' in battle_armors_files[new_image['Battle_armors']]:

    #         arr_helmetless_explorer = [
    #             "armor_back_pieces-16",
    #             "armor_back_pieces-17",
    #             "armor_back_pieces-18",
    #             "armor_back_pieces-19",
    #             "armor_back_pieces-20",
    #             "armor_back_pieces-21",
    #             "armor_back_pieces-22",
    #             "armor_back_pieces-23",
    #             "armor_back_pieces-24",
    #             "armor_back_pieces-25",
    #             "armor_back_pieces-26",
    #             "armor_back_pieces-27",
    #         ]
    #         new_image['Armor_back_pieces'] = random.choice(arr_helmetless_explorer)
    #     else:
    #         arr_helmetless_observer = [
    #             "armor_back_pieces-28",
    #             "armor_back_pieces-29",
    #             "armor_back_pieces-30",
    #             "armor_back_pieces-31",
    #             "armor_back_pieces-32",
    #             "armor_back_pieces-33",
    #             "armor_back_pieces-34",
    #             "armor_back_pieces-35",
    #             "armor_back_pieces-36",
    #             "armor_back_pieces-37",
    #             "armor_back_pieces-38",
    #             "armor_back_pieces-39",
    #         ]
    #         new_image['Armor_back_pieces'] = random.choice(arr_helmetless_observer)

    # #  position Mage Hand, Mage Hand with Mage Effect Weapons
    # if 'mage' in arms_files[new_image['Arms']]:
    #     if  not 'mage' in arm_armor_files[new_image['Arm_armor']]:           
    #         return create_new_image()
    #     # if new_image['Weapon_mage_effect'] == "weapon_mage_effect-6":   
    #     #     return create_new_image()

    # else:
    #     # Double Grip position, with Double Grip arms with Double Grip weapon
    #     if 'double' in arms_files[new_image['Arms']]:
    #         if not 'double' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()

    #         if not 'weapon_double_grip' in new_image['Weapon']:            
    #             return create_new_image()   

        
    #     # position One Hand with, One Arm, with Single Weapon
    #     if 'single' in arms_files[new_image['Arms']]:
    #         if not 'single' in arm_armor_files[new_image['Arm_armor']]:
    #             return create_new_image()
    #         if not 'weapon_one_hand' in new_image['Weapon']:          
    #             return create_new_image()
    #     else:
    #         # position Staff, with Staff Hand, with Staff Weapons
    #         if 'staff' in arms_files[new_image['Arms']]:  
    #             if not 'staff' in arm_armor_files[new_image['Arm_armor']]:
    #                 return create_new_image()
    #             if not 'weapon_staff' in new_image['Weapon']: 
    #                 return create_new_image()  
    #         else:
    #             # position Two Arms, with Two Arms, with Dual Wield Weapons
    #             if 'two' in arms_files[new_image['Arms']]:                     
    #                 if not 'two' in arm_armor_files[new_image['Arm_armor']]:
    #                     return create_new_image()
    #                 if not 'weapon_dual_wield' in new_image['Weapon']:
    #                     return create_new_image()
 
    # # HELMETS can only be put on BATTLE ARMORS (not enclosed armors or helmetless explorer/observer)
    # # if 'Helmet' in head_pieces_files[new_image['Head_pieces']]:
    # #     if 'enclosed_armors' in new_image['Battle_armors']:
    # #         return create_new_image()
    # #     if not ('short' in hair_files[new_image['Hair']] or 'lizard' in hair_files[new_image['Hair']]):
    # #         return create_new_image()

    # # Mage hood is added onto HELMETLESS Explorer or Observer suits, and must have NO HELM 
    # if not 'No hood#78' in mage_hoods_files[new_image['Mage_hoods']] and 'mage' in mage_hoods_files[new_image['Mage_hoods']]:
    #     if 'blue' in mage_hoods_files[new_image['Mage_hoods']] or 'green' in mage_hoods_files[new_image ["Mage_hoods"]]:
    #         new_image ['Helm_backpieces'] = 'helm_backpieces-2'
    #     if 'gold' in mage_hoods_files[new_image['Mage_hoods']] or 'purple' in mage_hoods_files[new_image['Mage_hoods']]:
    #         new_image['Helm_backpieces'] = 'helm_backpieces-3'
    #     if 'red' in mage_hoods_files[new_image['Mage_hoods']] or 'silver' in mage_hoods_files[new_image['Mage_hoods']]:
    #         new_image['Helm_backpieces'] = 'helm_backpieces-4'
    #     if not 'helmetless' in battle_armors_files[new_image['Battle_armors']]:
    #         return create_new_image()

    # # Mage hoods CAN ONLY have short unkept or short bun hairs
    # if new_image["Mage_hoods"] != "mage_hoods-7":       
    #     if not 'short' in hair_files[new_image['Hair']]:
    #        return create_new_image()

    # # Mage hand CAN ONLY be with mage hood 
    
    # if 'mage hand' in arms_files[new_image['Arms']]:
    #     new_image['Weapon'] = 'no_weapon'
    #     if 'enclosed_armors' in new_image['Battle_armors'] or not 'helmetless explorer' in battle_armors_files[new_image['Battle_armors']]:
    #         return create_new_image()
    #     # if  new_image ["Weapon_mage_effect"] == 'weapon_mage_effect-6':
    #     #     return create_new_image()
    #     if  new_image ["Mage_hoods"] == 'mage_hoods-7':
    #         return create_new_image()
        
    # # else:
    # #     new_image ["Weapon_mage_effect"] = 'weapon_mage_effect-6'



    # # other exception
    # if 'enclosed_armors' in new_image['Battle_armors']:
    #     if not 'short' in hair_files[new_image['Hair']] or 'fluffy' in beards_files[new_image['Beards']]:
    #         return create_new_image() 

    # # mage staff with only mage hood
    # if 'staff' in weapon_files[new_image['Weapon']]:
    #     if 'No hood#78' in mage_hoods_files[new_image['Mage_hoods']]:
    #         return create_new_image() 

    # # no armours ALWAYS has a tattoo
    # if 'no_battle_armors' in battle_armors_files[new_image['Battle_armors']]:
    #     if 'no_tattoos' in tattoos_files[new_image['Tattoos']]:
    #         return create_new_image()

    # # thunder tattoo always have thunder warpaint
    # if 'thunder' in war_paint_files[new_image['War_paint']]:
    #     if not 'thunder' in tattoos_files[new_image['Tattoos']]:
    #         return create_new_image()

    if  new_image in all_images:
        return create_new_image()
    else:
        return new_image

    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
  
    new_trait_image = create_new_image()

    all_images.append(new_trait_image)
	
# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

# print(all_images)

# # Get Trait Counts
# background_count = {}
# for item in background:
#     background_count[item] = 0
    
# weapon_back_count = {}
# for item in weapon_back:
#     weapon_back_count[item] = 0

# helm_backpieces_count = {}
# for item in helm_backpieces:
#     helm_backpieces_count[item] = 0

# armor_back_pieces_count = {}
# for item in armor_back_pieces:
#     armor_back_pieces_count[item] = 0

# base_body_count = {}
# for item in base_body:
#     base_body_count[item] = 0

# tattoos_count = {}
# for item in tattoos:
#     tattoos_count[item] = 0

# battle_armors_count = {}
# for item in battle_armors:
#     battle_armors_count[item] = 0 

# scars_count = {}
# for item in scars:
#     scars_count[item] = 0

# facial_expressions_count = {}
# for item in facial_expressions:
#     facial_expressions_count[item] = 0

# war_paint_count = {}
# for item in war_paint:
#     war_paint_count[item] = 0

# eyebrows_count = {}
# for item in eyebrows:
#     eyebrows_count[item] = 0

# hair_count = {}
# for item in hair:
#     hair_count[item] = 0

# mage_hoods_count = {}
# for item in mage_hoods:
#     mage_hoods_count[item] = 0

# beards_count = {}
# for item in beards:
#     beards_count[item] = 0

# arms_count = {}
# for item in arms:
#     arms_count[item] = 0

# weapon_count = {}
# for item in weapon:
#     weapon_count[item] = 0

# arm_armor_count = {}
# for item in arm_armor:
#     arm_armor_count[item] = 0

# weapon_mage_effect_count = {}
# for item in weapon_mage_effect:
#     weapon_mage_effect_count[item] = 0

# extras_count = {}
# for item in extras:
#     extras_count[item] = 0

# head_pieces_count = {}
# for item in head_pieces:
#     head_pieces_count[item] = 0

# for image in all_images:
#     background_count[image["Background"]] += 1
#     weapon_back_count[image["Weapon_back"]] += 1
#     helm_backpieces_count[image["Helm_backpieces"]] += 1
#     armor_back_pieces_count[image["Armor_back_pieces"]] += 1
#     base_body_count[image["Base_body"]] += 1
#     tattoos_count[image["Tattoos"]] += 1
#     battle_armors_count[image["Battle_armors"]] += 1
#     scars_count[image["Scars"]] += 1    
#     facial_expressions_count[image["Facial_expressions"]] += 1
#     war_paint_count[image["War_paint"]] += 1    
#     eyebrows_count[image["Eyebrows"]] += 1
#     hair_count[image["Hair"]] += 1
#     mage_hoods_count[image["Mage_hoods"]] += 1
#     beards_count[image["Beards"]] += 1
#     arms_count[image["Arms"]] += 1
#     weapon_count[image["Weapon"]] += 1
#     arm_armor_count[image["Arm_armor"]] += 1
#     weapon_mage_effect_count[image["Weapon_mage_effect"]] += 1
#     extras_count[image["Extras"]] += 1
#     head_pieces_count[image["Head_pieces"]] += 1


    
# print(background_count)
# print(weapon_back_count)
# print(helm_backpieces_count)
# print(armor_back_pieces_count)
# print(base_body_count)
# print(tattoos_count)
# print(battle_armors_count)
# print(scars_count)
# print(facial_expressions_count)
# print(war_paint_count)
# print(eyebrows_count)
# print(hair_count)
# print(mage_hoods_count)
# print(beards_count)
# print(arms_count)
# print(weapon_count)
# print(arm_armor_count)
# print(weapon_mage_effect_count)
# print(extras_count)
# print(head_pieces_count)

#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

#### Generate Images    
for item in all_images:
    im0 = Image.open(f'./trait-layers/Background/{background_files[item["Background"]]}.png').convert('RGBA')
    im1 = Image.open(f'./trait-layers/SkinColor/{skin_color_files[item["Skin_color"]]}.png').convert('RGBA')
    im2 = Image.open(f'./trait-layers/Clothes/{clothes_files[item["Clothes"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/FacialExpression/{facial_files[item["Facial"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/HairColor/{hair_files[item["Hair"]]}.png').convert('RGBA')
    # im5 = Image.open(f'./trait-layers/Hat/{hat_files[item["Hat"]]}.png').convert('RGBA')
    # im7 = Image.open(f'./trait-layers/9. FACIAL EXPRESSIONS/{facial_expressions_files[item["Facial_expressions"]]}.png').convert('RGBA')
    # im8 = Image.open(f'./trait-layers/10. WAR PAINT/{war_paint_files[item["War_paint"]]}.png').convert('RGBA')
    # im9 = Image.open(f'./trait-layers/12. HAIR/{hair_files[item["Hair"]]}.png').convert('RGBA')    
    # im10 = Image.open(f'./trait-layers/8. SCARS/{scars_files[item["Scars"]]}.png').convert('RGBA')
    # im11 = Image.open(f'./trait-layers/11. EYEBROWS/{eyebrows_files[item["Eyebrows"]]}.png').convert('RGBA')
    # im12 = Image.open(f'./trait-layers/14. BEARDS/{beards_files[item["Beards"]]}.png').convert('RGBA')
    # im13 = Image.open(f'./trait-layers/7. BATTLE ARMORS/{battle_armors_files[item["Battle_armors"]]}.png').convert('RGBA')  
    # im14 = Image.open(f'./trait-layers/13. MAGE HOODS/{mage_hoods_files[item["Mage_hoods"]]}.png').convert('RGBA')
    # im15 = Image.open(f'./trait-layers/15. ARMS/{arms_files[item["Arms"]]}.png').convert('RGBA')
    # im16 = Image.open(f'./trait-layers/16. EXTRAS/{extras_files[item["Extras"]]}.png').convert('RGBA')
    # im17 = Image.open(f'./trait-layers/18. WEAPON/{weapon_files[item["Weapon"]]}.png').convert('RGBA')
    # im18 = Image.open(f'./trait-layers/19. ARM ARMOR/{arm_armor_files[item["Arm_armor"]]}.png').convert('RGBA')
    # im19 = Image.open(f'./trait-layers/20. WEAPON MAGE EFFECT/{weapon_mage_effect_files[item["Weapon_mage_effect"]]}.png').convert('RGBA')
    # im20 = Image.open(f'./trait-layers/21. HEAD PIECES/{head_pieces_files[item["Head_pieces"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im0, im1)
    com2 = Image.alpha_composite(im2, im3)
    com3 = Image.alpha_composite(com1, com2)

    com4 = Image.alpha_composite(com3, im4)

    #Convert to RGB
    rgb_im = com4.convert('RGBA')
    
        

    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
	
#### Generate Metadata for each Image    
f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Skin_color", i["Skin_color"]))
    token["attributes"].append(getAttribute("Clothes", i["Clothes"]))
    token["attributes"].append(getAttribute("Hair", i["Hair"]))
    token["attributes"].append(getAttribute("Facial", i["Facial"]))
    token["attributes"].append(getAttribute("Background", i["Background"]))
    # token["attributes"].append(getAttribute("Battle_armors", i["Battle_armors"]))
    # token["attributes"].append(getAttribute("Scars", i["Scars"]))
    # token["attributes"].append(getAttribute("Facial_expressions", i["Facial_expressions"]))
    # token["attributes"].append(getAttribute("War_paint", i["War_paint"]))
    # token["attributes"].append(getAttribute("Hair", i["Hair"]))
    # token["attributes"].append(getAttribute("Mage_hoods", i["Mage_hoods"]))
    # token["attributes"].append(getAttribute("Beards", i["Beards"]))
    # token["attributes"].append(getAttribute("Arms", i["Arms"]))
    # token["attributes"].append(getAttribute("Weapon", i["Weapon"]))
    # token["attributes"].append(getAttribute("Arm_armor", i["Arm_armor"]))
    # token["attributes"].append(getAttribute("Weapon_mage_effect", i["Weapon_mage_effect"]))
    # token["attributes"].append(getAttribute("Extras", i["Extras"]))
    # token["attributes"].append(getAttribute("Head_pieces", i["Head_pieces"]))
                            
    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()