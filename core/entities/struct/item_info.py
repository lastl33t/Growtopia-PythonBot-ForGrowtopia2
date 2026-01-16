from dataclasses import dataclass, field
from core.entities.enums import ItemFlag

@dataclass
class Item:
    id: int = 0
    flags: ItemFlag = field(default_factory=lambda: ItemFlag(0))
    action_type: int = 0
    material: int = 0
    name: str = ""
    texture_file_name: str = ""
    texture_hash: int = 0
    cooking_ingredient: int = 0
    visual_effect: int = 0
    texture_x: int = 0
    texture_y: int = 0
    render_type: int = 0
    is_stripey_wallpaper: int = 0
    collision_type: int = 0
    block_health: int = 0
    drop_chance: int = 0
    clothing_type: int = 0
    rarity: int = 0
    level_required: int = 0 # level restrictions
    max_item: int = 0
    file_name: str = ""
    file_hash: int = 0
    audio_volume: int = 0
    pet_name: str = ""
    pet_prefix: str = ""
    pet_suffix: str = ""
    pet_ability: str = ""
    seed_base_sprite: int = 0
    seed_overlay_sprite: int = 0
    tree_base_sprite: int = 0
    tree_overlay_sprite: int = 0
    base_color: int = 0
    overlay_color: int = 0
    ingredient: int = 0
    grow_time: int = 0
    is_rayman: int = 0
    extra_options: str = ""
    texture_path_2: str = ""
    extra_option2: str = ""
    punch_option: str = ""
    description: str = ""