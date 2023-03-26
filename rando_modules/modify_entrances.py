"""
This module is used to modify entrances / loading zones statically.
Pre-determined changes are done to the world graph and loading zones in
accordance to chosen settings.
"""
from copy import deepcopy

from worldgraph import adjust

from rando_enums.enum_options import \
    GearShuffleMode,\
    BowserCastleMode

# Imports: Modify Bowser's Castle
from maps.graph_edges.bc_shorten.edges_kpa import \
    edges_kpa_add, edges_kpa_remove
from maps.graph_edges.bc_bossrush.edges_hos import \
    edges_hos_add, edges_hos_remove
from maps.graph_edges.bc_bossrush.edges_kpa import \
    edges_kpa_add    as edges_kpa_bossrush_add, \
    edges_kpa_remove as edges_kpa_bossrus_remove
from maps.graph_edges.gear_location_shuffle.edges_isk import \
    edges_isk_add    as edges_isk_gls_add, \
    edges_isk_remove as edges_isk_gls_remove
from maps.graph_edges.gear_location_shuffle.edges_kzn import \
    edges_kzn_add    as edges_kzn_gls_add, \
    edges_kzn_remove as edges_kzn_gls_remove
from maps.graph_edges.gear_location_shuffle.edges_tik import \
    edges_tik_add    as edges_tik_gls_add, \
    edges_tik_remove as edges_tik_gls_remove

# Imports: Glitched logic
from optionset import GlitchOptionSet

# Glitched Logic - Prologue
from maps.graph_edges.glitched_logic.kmr_prologue_gel_early import \
    edges_kmr_add_prologue_gel_early
from maps.graph_edges.glitched_logic.kmr_reverse_goomba_king_bridge import \
    edges_kmr_add_reverse_goomba_king_bridge
from maps.graph_edges.glitched_logic.kmr_goomba_village_entry_fence_clip import \
    edges_kmr_add_goomba_village_entry_fence_clip
from maps.graph_edges.glitched_logic.kmr_goomba_village_hammerless_exit import \
    edges_kmr_add_goomba_village_hammerless_exit_npc_lure, edges_kmr_add_goomba_village_hammerless_exit_laki
from maps.graph_edges.glitched_logic.kmr_hammerless_jr_playground_laki import \
    edges_kmr_add_hammerless_jr_playground_laki
from maps.graph_edges.glitched_logic.kmr_prologue_sushie_glitch import \
    edges_kmr_add_prologue_sushie_glitch_ksj, edges_kmr_add_prologue_sushie_glitch_common, edges_kmr_add_prologue_sushie_glitch_ultra_boots_laki

# Glitched Logic - Toad Town
from maps.graph_edges.glitched_logic.mac_odd_key_early import \
    edges_mac_odd_key_early
from maps.graph_edges.glitched_logic.mac_blue_house_skip import \
    edges_mac_add_bhs_jump, edges_mac_add_bhs_laki, edges_mac_add_bhs_toad_lure
from maps.graph_edges.glitched_logic.mac_bowless_toy_box import \
    edges_mac_add_bowless_toybox_hammer_lure, edges_mac_add_bowless_toybox_hammerless_lure
from maps.graph_edges.glitched_logic.mac_enter_storeroom_without_key import \
    edges_mac_add_storeroom_without_key_hammer, edges_mac_add_storeroom_without_key_parakarry, edges_mac_add_storeroom_without_key_hammerless_lure
from maps.graph_edges.glitched_logic.mac_sushieless_toad_town_star_piece import \
    edges_mac_add_sushieless_starpiece
from maps.graph_edges.glitched_logic.mac_whale_early import \
    edges_mac_add_whale_early_lzs
from maps.graph_edges.glitched_logic.mac_toad_town_sushie_glitch import \
    edges_mac_add_toad_town_sushie_glitch

# Glitched Logic - Toad Town Tunnels
from maps.graph_edges.glitched_logic.tik_island_pipe_blooper_skip import \
    edges_tik_add_island_pipe_blooper_skip
from maps.graph_edges.glitched_logic.tik_parakarryless_sewer_star_piece import \
    edges_tik_add_parakarryless_sewer_star_piece
from maps.graph_edges.glitched_logic.tik_sewer_blocks_without_ultra_boots import \
    edges_tik_add_sewer_blocks_without_ultra_boots
from maps.graph_edges.glitched_logic.tik_clippy_boots import \
    edges_tik_add_clippy_boots_metal_block_skip, edges_tik_add_clippy_boots_stone_block_skip
from maps.graph_edges.glitched_logic.tik_first_block_to_shiver_city_without_super_boots import \
    edges_tik_add_first_block_to_shiver_city_witout_super_boots
from maps.graph_edges.glitched_logic.tik_blocks_to_shiver_city_kooper_shell_item_throw import \
    edges_tik_add_blocks_to_shiver_city_kooper_shell_item_throw
from maps.graph_edges.glitched_logic.tik_break_sewer_yellow_block_with_ultra_boots import \
    edges_tik_add_break_sewer_yellow_block_with_ultra_boots
from maps.graph_edges.glitched_logic.tik_jumpless_sewer_shooting_star import \
    edges_tik_add_jumpless_sewer_shooting_star_kooper

# Glitched Logic - Pleasant Path
from maps.graph_edges.glitched_logic.nok_kooperless_pleasant_path_star_piece import \
    edges_nok_add_kooperless_starpiece_clippy
from maps.graph_edges.glitched_logic.nok_hammerless_pleasant_path_bridge_skip import \
    edges_nok_add_hammerless_bridge_skip_ultra_boots_parakarry
from maps.graph_edges.glitched_logic.nok_invisible_bridge_clip import \
    edges_nok_add_invisible_bridge_clip_laki, edges_nok_add_invisible_bridge_clip_lzs
from maps.graph_edges.glitched_logic.nok_kooperless_pleasant_path_thunderbolt import \
    edges_nok_add_kooperless_thunderbolt

# Glitched Logic - Koopa Bros Fortress
from maps.graph_edges.glitched_logic.nok_bombetteless_kbf_fp_plus import \
    edges_nok_add_bombetteless_fp_plus_laki, edges_nok_add_bombetteless_fp_plus_lzs
from maps.graph_edges.glitched_logic.trd_laki_jailbreak import \
    edges_trd_add_laki_jailbreak
from maps.graph_edges.glitched_logic.trd_bombetteless_right_fortress_jail_key import \
    edges_trd_add_bombetteless_right_key
from maps.graph_edges.glitched_logic.trd_water_staircase_skip import \
    edges_trd_add_water_staircase_skip

# Glitched Logic - Mt.Rugged
from maps.graph_edges.glitched_logic.iwa_mt_rugged_quake_hammer_and_letter_laki import \
    edges_iwa_add_quake_hammer_and_letter_laki
from maps.graph_edges.glitched_logic.iwa_parakarryless_mt_rugged_seed import \
    edges_iwa_add_parakarryless_mt_rugged_seed
from maps.graph_edges.glitched_logic.iwa_parakarryless_mt_rugged_star_piece import \
    edges_iwa_add_parakarryless_star_piece_laki
from maps.graph_edges.glitched_logic.iwa_buzzar_gap_skip import \
    edges_iwa_add_buzzar_gap_skip_clippy
from maps.graph_edges.glitched_logic.iwa_mt_rugged_coins_with_kooper import \
    edges_iwa_add_mt_rugged_coins_with_kooper
from maps.graph_edges.glitched_logic.iwa_mt_rugged_station_jumpless_climb import \
    edges_iwa_add_mt_rugged_station_jumpless_climb_bombette, edges_iwa_add_mt_rugged_station_jumpless_climb_laki
from maps.graph_edges.glitched_logic.iwa_jumpless_mt_rugged_train_platform import \
    edges_iwa_add_jumpless_mt_rugged_train_platform_parakarry

# Glitched Logic - Dry Dry Desert
from maps.graph_edges.glitched_logic.sbk_desert_brick_block_item_with_parakarry import \
    edges_sbk_add_desert_brick_block_item_parakarry
from maps.graph_edges.glitched_logic.sbk_early_ruins import \
    edges_sbk_add_laki, edges_sbk_add_ultraboots

# Glitched Logic - Dry Dry Ruins
from maps.graph_edges.glitched_logic.isk_artifact_jump import \
    edges_isk_add_artifact_jump_laki, edges_isk_add_artifact_jump_ultra_boots
from maps.graph_edges.glitched_logic.isk_ruins_key_laki_jump import \
    edges_isk_add_ruins_key_laki_jump
from maps.graph_edges.glitched_logic.isk_parakarryless_second_sand_room import \
    edges_isk_add_parakarryless_second_sand_room_normal_boots, \
    edges_isk_add_parakarryless_second_sand_room_ultra_boots
from maps.graph_edges.glitched_logic.isk_parakarryless_super_hammer_room import \
    edges_isk_add_parakarryless_super_hammer_room_normal_boots, edges_isk_add_parakarryless_super_hammer_room_ultra_boots
from maps.graph_edges.glitched_logic.isk_ruins_locks_skip import \
    edges_isk_add_ruins_locks_skip_clippy

# Glitched Logic - Boo's Mansion
from maps.graph_edges.glitched_logic.obk_record_skip import \
    edges_obk_add_record_skip_bombette_push, edges_obk_add_record_skip_spin_jump
from maps.graph_edges.glitched_logic.obk_parakarryless_boos_portrait import \
    edges_obk_add_boo_portrait_kooper, edges_obk_add_boo_portrait_laki
from maps.graph_edges.glitched_logic.mim_jumpless_mansion_entry import \
    edges_mim_add_jumpless_mansion_entry_parakarry
    
# Glitched Logic - Gusty Gulch
from maps.graph_edges.glitched_logic.mim_gusty_gulch_gate_skip import \
    edges_mim_add_gusty_gulch_gate_skip_lzs, edges_mim_add_gusty_gulch_gate_skip_laki
from maps.graph_edges.glitched_logic.arn_gusty_gulch_gap_skip import \
    edges_arn_add_gusty_gulch_gap_skip_jump
from maps.graph_edges.glitched_logic.arn_kooperless_gusty_gulch_dizzy_dial import \
    edges_arn_add_gusty_gulch_dizzy_dial_jump, edges_arn_add_gusty_gulch_dizzy_dial_laki, edges_arn_add_gusty_gulch_dizzy_dial_parakarry

# Glitched Logic - Tubba's Castle
from maps.graph_edges.glitched_logic.dgb_bowless_tubbas_castle import \
    edges_dgb_add_bowless_tubbas_castle
from maps.graph_edges.glitched_logic.dgb_tubbas_table_jump_clock import \
    edges_dgb_add_tubbas_table_clock_laki_jump,\
    edges_dgb_add_tubbas_table_clock_ultra_boots
from maps.graph_edges.glitched_logic.dgb_tubbas_table_jump_study import \
    edges_dgb_add_tubbas_table_laki_jump_study
from maps.graph_edges.glitched_logic.dgb_tubba_castle_super_boots_skip import \
    edges_dgb_add_tubbas_castle_super_boots_skip_laki
from maps.graph_edges.glitched_logic.dgb_parakarryless_mega_rush import \
    edges_dgb_add_parakarryless_mega_rush

# Glitched Logic - Toy Box
from maps.graph_edges.glitched_logic.omo_gourmet_guy_skip import \
    edges_omo_add_gourmet_guy_skip_jump, edges_omo_add_gourmet_guy_skip_laki, edges_omo_add_gourmet_guy_skip_parakarry
from maps.graph_edges.glitched_logic.omo_parakarryless_blue_station_star_piece import \
    edges_omo_add_parakarryless_blue_station_star_piece
from maps.graph_edges.glitched_logic.omo_bowless_green_station import \
    edges_omo_add_bowless_green_station_laki
from maps.graph_edges.glitched_logic.omo_kooperless_red_station_shooting_star import \
    edges_omo_add_red_station_shooting_star_parakarry
from maps.graph_edges.glitched_logic.omo_gearless_red_station_shooting_star import \
    edges_omo_add_red_station_shooting_star_gearless
from maps.graph_edges.glitched_logic.omo_parakarryless_blue_block_city_gap import \
    edges_omo_add_parakarryless_blue_block_city_gap
from maps.graph_edges.glitched_logic.omo_blue_switch_skip import \
    edges_omo_add_blue_switch_skip_laki, edges_omo_add_blue_switch_skip_ultra_boots
from maps.graph_edges.glitched_logic.omo_red_barricade_skip import \
    edges_omo_add_red_barricade_skip
from maps.graph_edges.glitched_logic.omo_hammerless_blue_station import \
    edges_omo_add_hammerless_blue_station_laki
from maps.graph_edges.glitched_logic.omo_hammerless_pink_station import \
    edges_omo_add_hammerless_pink_station_laki

# Glitched Logic - Jade Jungle
from maps.graph_edges.glitched_logic.jan_raph_skip_english import \
    edges_jan_add_raph_skip_english
from maps.graph_edges.glitched_logic.jan_kzn_ch5_sushie_glitch import \
    edges_jan_kzn_add_ch5_sushie_glitch, edges_kzn_add_volcano_sushie_glitch
from maps.graph_edges.glitched_logic.jan_sushieless_jungle_starpiece_and_letter import \
    edges_jan_add_sushieless_jungle_starpiece_and_letter_lzs
from maps.graph_edges.glitched_logic.jan_jumpless_deep_jungle import \
    edges_jan_add_jumpless_deep_jungle_laki

# Glitched Logic - Mt. Lavalava
from maps.graph_edges.glitched_logic.kzn_kooperless_lavalava_pow_block import \
    edges_kzn_add_kooperless_pow_block_parakarry, edges_kzn_add_kooperless_pow_block_super_boots
from maps.graph_edges.glitched_logic.kzn_jumpless_lavalava_pow_block import \
    edges_kzn_add_jumpless_pow_block_kooper
from maps.graph_edges.glitched_logic.kzn_ultra_hammer_skip import \
    edges_kzn_add_ultra_hammer_skip, edges_kzn_add_ultra_hammer_skip_laki, edges_kzn_add_ultra_hammer_skip_sushie
from maps.graph_edges.glitched_logic.kzn_flarakarry import \
    edges_kzn_add_flarakarry_bombette, edges_kzn_add_flarakarry_laki, edges_kzn_add_flarakarry_parakarry

# Glitched Logic - Flower Fields
from maps.graph_edges.glitched_logic.flo_early_lakilester import \
    edges_flo_add_early_lakilester_bombette_push, edges_flo_add_early_lakilester_without_bombette
from maps.graph_edges.glitched_logic.flo_bombetteless_mega_smash import \
    edges_flo_add_bombetteless_mega_smash
from maps.graph_edges.glitched_logic.flo_sun_tower_skip import \
    edges_flo_add_sun_tower_skip_lzs
from maps.graph_edges.glitched_logic.flo_yellow_berry_gate_skip import \
    edges_flo_add_yellow_berry_gate_skip_bombette_push, edges_flo_add_yellow_berry_gate_skip_laki, edges_flo_add_yellow_berry_gate_skip_lzs
from maps.graph_edges.glitched_logic.flo_red_berry_gate_skip import \
    edges_flo_add_red_berry_gate_skip_bombette_push, edges_flo_add_red_berry_gate_skip_laki
from maps.graph_edges.glitched_logic.flo_blue_berry_gate_skip import \
    edges_flo_add_blue_berry_gate_skip_bombette_push, edges_flo_add_blue_berry_gate_skip_laki
from maps.graph_edges.glitched_logic.flo_bubble_berry_tree_early import \
    edges_flo_add_bubble_berry_tree_early_laki, edges_flo_add_bubble_berry_tree_early_ultra_boots

# Glitched Logic - Shiver Region
from maps.graph_edges.glitched_logic.sam_murder_solved_early import \
    edges_sam_add_murder_solved_early_laki, edges_sam_add_murder_solved_early_bombette_push
from maps.graph_edges.glitched_logic.sam_ch7_sushie_glitch import \
    edges_sam_add_ch7_sushie_glitch, edges_sam_add_star_stone_with_ch7_sushie_glitch
from maps.graph_edges.glitched_logic.sam_shiver_mtn_hidden_block_without_ultra_boots import \
    edges_sam_add_shiver_mountain_hidden_block_normal_throw, edges_sam_add_shiver_mountain_hidden_block_laki_throw
from maps.graph_edges.glitched_logic.sam_snowmen_skip import \
    edges_sam_add_snowmen_skip_laki
from maps.graph_edges.glitched_logic.sam_shiver_mountain_switch_skip import \
    edges_sam_add_shiver_mountain_switch_skip
from maps.graph_edges.glitched_logic.sam_sushieless_warehouse_key import \
    edges_sam_add_sushieless_warehouse_key_bombette_push, edges_sam_add_sushieless_warehouse_key_kooper_ksj

# Glitched Logic - Crystal Palace
from maps.graph_edges.glitched_logic.pra_mirror_clip import \
    edges_pra_add_mirror_clip_laki

# Glitched Logic - Bowser's Castle
from maps.graph_edges.glitched_logic.kpa_bowless_bowsers_castle_basement import \
    edges_kpa_add_bowless_bowsers_castle_basement_laki
from maps.graph_edges.glitched_logic.kpa_fast_flood_room import \
    edges_kpa_add_fast_flood_room_bombette_ultra_boots, edges_kpa_add_fast_flood_room_kooper
from maps.graph_edges.glitched_logic.kpa_bombetteless_bowsers_castle_basement import \
    edges_kpa_add_bombetteless_bowsers_castle_basement_laki

# Glitched Logic - Global
from maps.graph_edges.glitched_logic.global_break_stone_blocks_with_ultra_boots import \
    edges_kmr_tik_isk_add_break_stone_blocks_ultra_boots
from maps.graph_edges.glitched_logic.kmr_break_yellow_blocks_with_super_boots import \
    edges_kmr_add_break_yellow_blocks_super_boots
from maps.graph_edges.glitched_logic.global_knows_puzzle_solutions import \
    edges_global_knows_puzzle_solutions
from maps.graph_edges.glitched_logic.global_reach_high_blocks_with_super_boots import \
    edges_global_reach_high_blocks_with_super_boots

# Streamlined Chapters
from maps.graph_edges.streamlined_chapters.edges_ch1 import streamlined_edges_ch1_add, streamlined_edges_ch1_remove
from maps.graph_edges.streamlined_chapters.edges_ch2 import streamlined_edges_ch2_add, streamlined_edges_ch2_remove
from maps.graph_edges.streamlined_chapters.edges_ch3 import streamlined_edges_ch3_add, streamlined_edges_ch3_remove
from maps.graph_edges.streamlined_chapters.edges_ch4 import streamlined_edges_ch4_add, streamlined_edges_ch4_remove
from maps.graph_edges.streamlined_chapters.edges_ch5 import streamlined_edges_ch5_add, streamlined_edges_ch5_remove
from maps.graph_edges.streamlined_chapters.edges_ch6 import streamlined_edges_ch6_add, streamlined_edges_ch6_remove
from maps.graph_edges.streamlined_chapters.edges_ch7 import streamlined_edges_ch7_add, streamlined_edges_ch7_remove
from maps.graph_edges.streamlined_chapters.edges_hos import get_streamlined_edges_hos_add, streamlined_edges_hos_remove

def get_shorter_bowsercastle(world_graph: dict):
    """
    Returns a list of db data tuples representing modified entrances in Bowser's
    Castle to shorten it, as well as the corresponding adjusted world graph.
    """
    # Sets up the following connections:
    # kpa_50  (1)  <-> kpa_82  (0) (Hall to Guard Door 1 <-> Guard Door 2)
    # kpa_82  (1)  <-> kpa_32  (0) (Guard Door 2 <-> Lower Grand Hall)
    # kpa_51  (1)  <-> kpa_130 (0) (Hall to Water Puzzle <-> Bill Blaster Hall)
    # kpa_112 (1)  <-> kpa_61  (0) (Hidden Passage 1 <-> Battlement)
    # kpa_33  (2)  <-> kpa_102 (0) (Upper Grand Hall <-> Blue Fire Bridge)
    world_graph, kpa_entrance_modifications = adjust(
        world_graph,
        new_edges=edges_kpa_add,
        edges_to_remove=edges_kpa_remove
    )

    return kpa_entrance_modifications, world_graph


def get_bowsercastle_bossrush(world_graph: dict):
    """
    Returns a list of db data tuples representing modified entrances in Bowser's
    Castle and Shooting Star Summit to skip straight to the Fake Peach Hallway
    for as boss rush.
    """
    # Sets up the following connection:
    # hos_20 (2) <-> kpa_53 (0) (Riding Star Ship Scene <-> Fake Peach Hallway)
    all_entrance_modifications = []

    world_graph, hos_entrance_modifications = adjust(
        world_graph,
        new_edges=edges_hos_add,
        edges_to_remove=edges_hos_remove
    )
    world_graph, kpa_entrance_modifications = adjust(
        world_graph,
        new_edges=edges_kpa_bossrush_add,
        edges_to_remove=edges_kpa_bossrus_remove
    )

    all_entrance_modifications.extend(hos_entrance_modifications)
    all_entrance_modifications.extend(kpa_entrance_modifications)

    return all_entrance_modifications, world_graph

def get_gear_location_shuffle(world_graph: dict, gear_shuffle_mode: int):
    """
    Returns the modified world graph itself for Gear Location Shuffle and Full Shuffle,
    which removes dynamic hammer block logic.
    """
    all_new_edges = []
    all_edges_to_remove = []

    all_new_edges.extend(edges_isk_gls_add)
    all_new_edges.extend(edges_kzn_gls_add)
    all_edges_to_remove.extend(edges_isk_gls_remove)
    all_edges_to_remove.extend(edges_kzn_gls_remove)

    # The blocks are the same for isk and kzn and all non-vanilla modes, but only GLS modifies tik
    if gear_shuffle_mode == GearShuffleMode.GEAR_LOCATION_SHUFFLE:
        all_new_edges.extend(edges_tik_gls_add)
        all_edges_to_remove.extend(edges_tik_gls_remove)

    world_graph, _ = adjust(
        world_graph,
        new_edges=all_new_edges,
        edges_to_remove=all_edges_to_remove
    )

    return world_graph


def get_glitched_logic(
    world_graph: dict,
    glitch_settings: GlitchOptionSet,
    bowsers_castle_mode: int,
    shuffle_dungeon_entrances: bool
):
    """
    Returns the modified world graph itself for glitched logic, depending
    on settings chosen.
    """
    all_new_edges = []
    all_edges_to_remove = []

    # Goomba Region
    if glitch_settings.prologue_gel_early["value"]:
        all_new_edges.extend(edges_kmr_add_prologue_gel_early)
    if glitch_settings.reverse_goomba_king_bridge["value"]:
        all_new_edges.extend(edges_kmr_add_reverse_goomba_king_bridge)
    if glitch_settings.goomba_village_entry_fence_clip["value"]:
        all_new_edges.extend(edges_kmr_add_goomba_village_entry_fence_clip)
    if glitch_settings.goomba_village_npc_lure_exit["value"]:
        all_new_edges.extend(edges_kmr_add_goomba_village_hammerless_exit_npc_lure)
    if glitch_settings.goomba_village_laki_exit["value"]:
        all_new_edges.extend(edges_kmr_add_goomba_village_hammerless_exit_laki)
    if glitch_settings.hammerless_jr_playground_laki["value"]:
        all_new_edges.extend(edges_kmr_add_hammerless_jr_playground_laki)
    if glitch_settings.prologue_sushie_glitch_ksj["value"]:
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_ksj)
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_common)
    if glitch_settings.prologue_sushie_glitch_ultra_boots_laki["value"]:
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_ultra_boots_laki)
        all_new_edges.extend(edges_kmr_add_prologue_sushie_glitch_common)

    # Toad Town
    if glitch_settings.odd_key_early["value"]:
        all_new_edges.extend(edges_mac_odd_key_early)
    if glitch_settings.blue_house_skip["value"]:
        all_new_edges.extend(edges_mac_add_bhs_jump)
    if glitch_settings.blue_house_skip_laki["value"]:
        all_new_edges.extend(edges_mac_add_bhs_laki)
    if glitch_settings.blue_house_skip_toad_lure["value"]:
        all_new_edges.extend(edges_mac_add_bhs_toad_lure)
    if glitch_settings.bowless_toy_box_hammer["value"]:
        all_new_edges.extend(edges_mac_add_bowless_toybox_hammer_lure)
    if glitch_settings.bowless_toy_box_hammerless_lure["value"]:
        all_new_edges.extend(edges_mac_add_bowless_toybox_hammerless_lure)
    if glitch_settings.early_storeroom_parakarry["value"]:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_parakarry)
    if glitch_settings.early_storeroom_hammer["value"]:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_hammer)
    if glitch_settings.early_storeroom_hammerless_lure["value"]:
        all_new_edges.extend(edges_mac_add_storeroom_without_key_hammerless_lure)
    if glitch_settings.whale_early["value"]:
        all_new_edges.extend(edges_mac_add_whale_early_lzs)
    if glitch_settings.sushiesless_toad_town_star_piece["value"]:
        all_new_edges.extend(edges_mac_add_sushieless_starpiece)
    if glitch_settings.toad_town_sushie_glitch["value"]:
        all_new_edges.extend(edges_mac_add_toad_town_sushie_glitch)

    # Toad Town Tunnels
    if glitch_settings.clippy_boots_stone_block_skip["value"]:
        all_new_edges.extend(edges_tik_add_clippy_boots_stone_block_skip)
    if glitch_settings.clippy_boots_metal_block_skip["value"]:
        all_new_edges.extend(edges_tik_add_clippy_boots_metal_block_skip)
    if glitch_settings.island_pipe_blooper_skip["value"]:
        all_new_edges.extend(edges_tik_add_island_pipe_blooper_skip)
    if glitch_settings.parakarryless_sewer_star_piece["value"]:
        all_new_edges.extend(edges_tik_add_parakarryless_sewer_star_piece)
    if glitch_settings.sewer_blocks_without_ultra_boots["value"]:
        all_new_edges.extend(edges_tik_add_sewer_blocks_without_ultra_boots)
    if glitch_settings.first_block_to_shiver_city_without_super_boots["value"]:
        all_new_edges.extend(edges_tik_add_first_block_to_shiver_city_witout_super_boots)
    if glitch_settings.blocks_to_shiver_city_kooper_shell_item_throw["value"]:
        all_new_edges.extend(edges_tik_add_blocks_to_shiver_city_kooper_shell_item_throw)
    if glitch_settings.sewer_yellow_block_with_ultra_boots["value"]:
        all_new_edges.extend(edges_tik_add_break_sewer_yellow_block_with_ultra_boots)
    if glitch_settings.jumpless_sewer_shooting_star["value"]:
        all_new_edges.extend(edges_tik_add_jumpless_sewer_shooting_star_kooper)

    # Pleasant Path
    if glitch_settings.kooperless_pleasant_path_star_piece["value"]:
        all_new_edges.extend(edges_nok_add_kooperless_starpiece_clippy)
    if glitch_settings.hammerless_pleasant_path_bridge_ultra_boots_parakarry["value"]:
        all_new_edges.extend(edges_nok_add_hammerless_bridge_skip_ultra_boots_parakarry)
    if glitch_settings.invisible_bridge_clip_laki["value"]:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_laki)
    if glitch_settings.invisible_bridge_clip_lzs["value"]:
        all_new_edges.extend(edges_nok_add_invisible_bridge_clip_lzs)
    if glitch_settings.kooperless_pleasant_path_thunderbolt["value"]:
        all_new_edges.extend(edges_nok_add_kooperless_thunderbolt)

    # Koopa Bros Fortress
    if glitch_settings.bombetteless_kbf_fp_plus_laki["value"]:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_laki)
    if glitch_settings.bombetteless_kbf_fp_plus_lzs["value"] and not shuffle_dungeon_entrances:
        all_new_edges.extend(edges_nok_add_bombetteless_fp_plus_lzs)
    if glitch_settings.laki_jailbreak["value"]:
        all_new_edges.extend(edges_trd_add_laki_jailbreak)
    if glitch_settings.bombetteless_right_fortress_jail_key["value"]:
        all_new_edges.extend(edges_trd_add_bombetteless_right_key)
    if glitch_settings.water_staircase_skip["value"]:
        all_new_edges.extend(edges_trd_add_water_staircase_skip)

    # Mt. Rugged
    if glitch_settings.mt_rugged_quake_hammer_and_letter_with_laki["value"]:
        all_new_edges.extend(edges_iwa_add_quake_hammer_and_letter_laki)
    if glitch_settings.parakarryless_mt_rugged_seed["value"]:
        all_new_edges.extend(edges_iwa_add_parakarryless_mt_rugged_seed)
    if glitch_settings.parakarryless_mt_rugged_star_piece["value"]:
        all_new_edges.extend(edges_iwa_add_parakarryless_star_piece_laki)
    if glitch_settings.buzzar_gap_skip_clippy["value"]:
        all_new_edges.extend(edges_iwa_add_buzzar_gap_skip_clippy)
    if glitch_settings.mt_rugged_coins_with_kooper["value"]:
        all_new_edges.extend(edges_iwa_add_mt_rugged_coins_with_kooper)
    if glitch_settings.mt_rugged_station_jumpless_climb_bombette["value"]:
        all_new_edges.extend(edges_iwa_add_mt_rugged_station_jumpless_climb_bombette)
    if glitch_settings.mt_rugged_station_jumpless_climb_laki["value"]:
        all_new_edges.extend(edges_iwa_add_mt_rugged_station_jumpless_climb_laki)
    if glitch_settings.jumpless_mt_rugged_train_platform_parakarry["value"]:
        all_new_edges.extend(edges_iwa_add_jumpless_mt_rugged_train_platform_parakarry)

    # Dry Dry Desert
    if glitch_settings.early_ruins_laki_jump["value"]:
        all_new_edges.extend(edges_sbk_add_laki)
    if glitch_settings.early_ruins_ultra_boots["value"]:
        all_new_edges.extend(edges_sbk_add_ultraboots)
    if glitch_settings.desert_brick_block_item_with_parakarry["value"]:
        all_new_edges.extend(edges_sbk_add_desert_brick_block_item_parakarry)

    # Dry Dry Ruins
    if glitch_settings.artifact_jump_laki["value"]:
        all_new_edges.extend(edges_isk_add_artifact_jump_laki)
    if glitch_settings.artifact_jump_ultra_boots["value"]:
        all_new_edges.extend(edges_isk_add_artifact_jump_ultra_boots)
    if glitch_settings.parakarryless_second_sand_room_normal_boots["value"]:
        all_new_edges.extend(edges_isk_add_parakarryless_second_sand_room_normal_boots)
    if glitch_settings.parakarryless_second_sand_room_ultra_boots["value"]:
        all_new_edges.extend(edges_isk_add_parakarryless_second_sand_room_ultra_boots)
    if glitch_settings.parakarryless_super_hammer_room_normal_boots["value"]:
        all_new_edges.extend(edges_isk_add_parakarryless_super_hammer_room_normal_boots)
    if glitch_settings.parakarryless_super_hammer_room_ultra_boots["value"]:
        all_new_edges.extend(edges_isk_add_parakarryless_super_hammer_room_ultra_boots)
    if glitch_settings.ruins_key_laki_jump["value"]:
        all_new_edges.extend(edges_isk_add_ruins_key_laki_jump)
    if glitch_settings.ruins_locks_skip_clippy["value"]:
        all_new_edges.extend(edges_isk_add_ruins_locks_skip_clippy)

    # Boo's Mansion
    if glitch_settings.record_skip_bombette_push["value"]:
        all_new_edges.extend(edges_obk_add_record_skip_bombette_push)
    if glitch_settings.record_skip_no_bombette_push["value"]:
        all_new_edges.extend(edges_obk_add_record_skip_spin_jump)
    if glitch_settings.boos_portrait_with_kooper["value"]:
        all_new_edges.extend(edges_obk_add_boo_portrait_kooper)
    if glitch_settings.boos_portrait_with_laki["value"]:
        all_new_edges.extend(edges_obk_add_boo_portrait_laki)
    if glitch_settings.jumpless_mansion_entry["value"]:
        all_new_edges.extend(edges_mim_add_jumpless_mansion_entry_parakarry)

    # Gusty Gulch
    if glitch_settings.gusty_gulch_gate_skip_lzs["value"]:
        all_new_edges.extend(edges_mim_add_gusty_gulch_gate_skip_lzs)
    if glitch_settings.gusty_gulch_gate_skip_laki["value"]:
        all_new_edges.extend(edges_mim_add_gusty_gulch_gate_skip_laki)
    if glitch_settings.kooperless_gusty_gulch_dizzy_dial_jump["value"]:
        all_new_edges.extend(edges_arn_add_gusty_gulch_dizzy_dial_jump)
    if glitch_settings.kooperless_gusty_gulch_dizzy_dial_laki["value"]:
        all_new_edges.extend(edges_arn_add_gusty_gulch_dizzy_dial_laki)
    if glitch_settings.kooperless_gusty_gulch_dizzy_dial_parakarry["value"]:
        all_new_edges.extend(edges_arn_add_gusty_gulch_dizzy_dial_parakarry)
    if glitch_settings.gusty_gulch_gap_skip["value"]:
        all_new_edges.extend(edges_arn_add_gusty_gulch_gap_skip_jump)

    # Tubba's Castle
    if glitch_settings.bowless_tubbas_castle["value"]:
        all_new_edges.extend(edges_dgb_add_bowless_tubbas_castle)
    if glitch_settings.tubbas_table_laki_jump_clock["value"]:
        all_new_edges.extend(edges_dgb_add_tubbas_table_clock_laki_jump)
    if glitch_settings.tubbas_table_ultra_boots["value"]:
        all_new_edges.extend(edges_dgb_add_tubbas_table_clock_ultra_boots)
    if glitch_settings.tubbas_table_laki_jump_study["value"]:
        all_new_edges.extend(edges_dgb_add_tubbas_table_laki_jump_study)
    if glitch_settings.tubbas_castle_super_boots_skip["value"]:
        all_new_edges.extend(edges_dgb_add_tubbas_castle_super_boots_skip_laki)
    if glitch_settings.parakarryless_mega_rush["value"]:
        all_new_edges.extend(edges_dgb_add_parakarryless_mega_rush)

    # Toy Box
    if glitch_settings.parakarryless_blue_building_star_piece["value"]:
        all_new_edges.extend(edges_omo_add_parakarryless_blue_station_star_piece)
    if glitch_settings.gourmet_guy_skip_jump["value"]:
        all_new_edges.extend(edges_omo_add_gourmet_guy_skip_jump)
    if glitch_settings.gourmet_guy_skip_laki["value"]:
        all_new_edges.extend(edges_omo_add_gourmet_guy_skip_laki)
    if glitch_settings.gourmet_guy_skip_parakarry["value"]:
        all_new_edges.extend(edges_omo_add_gourmet_guy_skip_parakarry)
    if glitch_settings.bowless_green_station["value"]:
        all_new_edges.extend(edges_omo_add_bowless_green_station_laki)
    if glitch_settings.kooperless_red_station_shooting_star["value"]:
        all_new_edges.extend(edges_omo_add_red_station_shooting_star_parakarry)
    if glitch_settings.gearless_red_station_shooting_star["value"]:
        all_new_edges.extend(edges_omo_add_red_station_shooting_star_gearless)
    if glitch_settings.parakarryless_blue_block_city_gap["value"]:
        all_new_edges.extend(edges_omo_add_parakarryless_blue_block_city_gap)
    if glitch_settings.blue_switch_skip_laki["value"]:
        all_new_edges.extend(edges_omo_add_blue_switch_skip_laki)
    if glitch_settings.blue_switch_skip_ultra_boots["value"]:
        all_new_edges.extend(edges_omo_add_blue_switch_skip_ultra_boots)
    if glitch_settings.red_barricade_skip["value"]:
        all_new_edges.extend(edges_omo_add_red_barricade_skip)
    if glitch_settings.hammerless_blue_station_laki["value"]:
        all_new_edges.extend(edges_omo_add_hammerless_blue_station_laki)
    if glitch_settings.hammerless_pink_station_laki["value"]:
        all_new_edges.extend(edges_omo_add_hammerless_pink_station_laki)

    # Jade Jungle
    if glitch_settings.raph_skip_english["value"]:
        all_new_edges.extend(edges_jan_add_raph_skip_english)
    if glitch_settings.ch5_sushie_glitch["value"]:
        all_new_edges.extend(edges_jan_kzn_add_ch5_sushie_glitch)
    if glitch_settings.sushieless_jungle_starpiece_and_letter["value"]:
        all_new_edges.extend(edges_jan_add_sushieless_jungle_starpiece_and_letter_lzs)
    if glitch_settings.jumpless_deep_jungle_laki["value"]:
        all_new_edges.extend(edges_jan_add_jumpless_deep_jungle_laki)

    # Mt. Lavalava
    if glitch_settings.kooperless_lavalava_pow_block_parakarry["value"]:
        all_new_edges.extend(edges_kzn_add_kooperless_pow_block_parakarry)
    if glitch_settings.kooperless_lavalava_pow_block_super_boots["value"]:
        all_new_edges.extend(edges_kzn_add_kooperless_pow_block_super_boots)
    if glitch_settings.jumpless_lavalava_pow_block["value"]:
        all_new_edges.extend(edges_kzn_add_jumpless_pow_block_kooper)
    if glitch_settings.ultra_hammer_skip["value"]:
        all_new_edges.extend(edges_kzn_add_ultra_hammer_skip)
    if glitch_settings.ultra_hammer_skip_laki["value"]:
        all_new_edges.extend(edges_kzn_add_ultra_hammer_skip_laki)
    if glitch_settings.ultra_hammer_skip_sushie["value"]:
        all_new_edges.extend(edges_kzn_add_ultra_hammer_skip_sushie)
    if glitch_settings.flarakarry["value"]:
        all_new_edges.extend(edges_kzn_add_flarakarry_parakarry)
    if glitch_settings.parakarryless_flarakarry_bombette["value"]:
        all_new_edges.extend(edges_kzn_add_flarakarry_bombette)
    if glitch_settings.parakarryless_flarakarry_laki["value"]:
        all_new_edges.extend(edges_kzn_add_flarakarry_laki)
    if glitch_settings.volcano_sushie_glitch["value"]:
        all_new_edges.extend(edges_kzn_add_volcano_sushie_glitch)

    # Flower Fields
    if glitch_settings.early_laki_lzs["value"]:
        all_new_edges.extend(edges_flo_add_early_lakilester_without_bombette)
    if glitch_settings.early_laki_bombette_push["value"]:
        all_new_edges.extend(edges_flo_add_early_lakilester_bombette_push)
    if glitch_settings.bombetteless_mega_smash["value"]:
        all_new_edges.extend(edges_flo_add_bombetteless_mega_smash)
    if glitch_settings.sun_tower_skip["value"]:
        all_new_edges.extend(edges_flo_add_sun_tower_skip_lzs)
    if glitch_settings.yellow_berry_gate_skip_bombette_push["value"]:
        all_new_edges.extend(edges_flo_add_yellow_berry_gate_skip_bombette_push)
    if glitch_settings.yellow_berry_gate_skip_laki["value"]:
        all_new_edges.extend(edges_flo_add_yellow_berry_gate_skip_laki)
    if glitch_settings.yellow_berry_gate_skip_lzs["value"]:
        all_new_edges.extend(edges_flo_add_yellow_berry_gate_skip_lzs)
    if glitch_settings.red_berry_gate_skip_bombette_push["value"]:
        all_new_edges.extend(edges_flo_add_red_berry_gate_skip_bombette_push)
    if glitch_settings.red_berry_gate_skip_laki["value"]:
        all_new_edges.extend(edges_flo_add_red_berry_gate_skip_laki)
    if glitch_settings.blue_berry_gate_skip_bombette_push["value"]:
        all_new_edges.extend(edges_flo_add_blue_berry_gate_skip_bombette_push)
    if glitch_settings.blue_berry_gate_skip_laki["value"]:
        all_new_edges.extend(edges_flo_add_blue_berry_gate_skip_laki)
    if glitch_settings.bubble_berry_tree_early_laki_jump["value"]:
        all_new_edges.extend(edges_flo_add_bubble_berry_tree_early_laki)
    if glitch_settings.bubble_berry_tree_early_ultra_boots["value"]:
        all_new_edges.extend(edges_flo_add_bubble_berry_tree_early_ultra_boots)

    # Shiver Region
    if glitch_settings.murder_solved_early_bombette_push["value"]:
        all_new_edges.extend(edges_sam_add_murder_solved_early_bombette_push)
    if glitch_settings.murder_solved_early_laki["value"]:
        all_new_edges.extend(edges_sam_add_murder_solved_early_laki)
    if glitch_settings.ch7_sushie_glitch["value"]:
        all_new_edges.extend(edges_sam_add_ch7_sushie_glitch)
    if glitch_settings.star_stone_with_ch7_sushie_glitch["value"]:
        all_new_edges.extend(edges_sam_add_star_stone_with_ch7_sushie_glitch)
    if glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_laki["value"]:
        all_new_edges.extend(edges_sam_add_shiver_mountain_hidden_block_laki_throw)
    if glitch_settings.shiver_mountain_hidden_block_without_ultra_boots_no_laki["value"]:
        all_new_edges.extend(edges_sam_add_shiver_mountain_hidden_block_normal_throw)
    if glitch_settings.snowmen_skip_laki["value"]:
        all_new_edges.extend(edges_sam_add_snowmen_skip_laki)
    if glitch_settings.shiver_mountain_switch_skip["value"]:
        all_new_edges.extend(edges_sam_add_shiver_mountain_switch_skip)
    if glitch_settings.sushieless_warehouse_key_bombette["value"]:
        all_new_edges.extend(edges_sam_add_sushieless_warehouse_key_bombette_push)
    if glitch_settings.sushieless_warehouse_key_kooper["value"]:
        all_new_edges.extend(edges_sam_add_sushieless_warehouse_key_kooper_ksj)

    # Crystal Palace
    if glitch_settings.mirror_clip["value"]:
        all_new_edges.extend(edges_pra_add_mirror_clip_laki)

    # Bowser's Castle
    if bowsers_castle_mode == BowserCastleMode.VANILLA:
        if glitch_settings.bowless_bowsers_castle_basement["value"]:
            all_new_edges.extend(edges_kpa_add_bowless_bowsers_castle_basement_laki)
        if glitch_settings.fast_flood_room_kooper["value"]:
            all_new_edges.extend(edges_kpa_add_fast_flood_room_kooper)
        if glitch_settings.fast_flood_room_bombette_ultra_boots["value"]:
            all_new_edges.extend(edges_kpa_add_fast_flood_room_bombette_ultra_boots)
        if glitch_settings.bombetteless_bowsers_castle_basement["value"]:
            all_new_edges.extend(edges_kpa_add_bombetteless_bowsers_castle_basement_laki)

    # Global
    if glitch_settings.break_stone_blocks_with_ultra_boots["value"]:
        all_new_edges.extend(edges_kmr_tik_isk_add_break_stone_blocks_ultra_boots)
    if glitch_settings.break_yellow_blocks_with_super_boots["value"]:
        all_new_edges.extend(edges_kmr_add_break_yellow_blocks_super_boots)
    if glitch_settings.knows_puzzle_solutions["value"]:
        all_new_edges.extend(edges_global_knows_puzzle_solutions)
    if glitch_settings.reach_high_blocks_with_super_boots["value"]:
        all_new_edges.extend(edges_global_reach_high_blocks_with_super_boots)

    #print(all_new_edges)

    # Modify graph with all pending changes, if any
    if all_new_edges or all_edges_to_remove:
        world_graph, _ = adjust(
            world_graph,
            new_edges=all_new_edges,
            edges_to_remove=all_edges_to_remove
        )

    return world_graph


def adjust_shop_logic(
    world_graph: dict,
    rowf_in_logic:bool,
    merlow_in_logic:bool,
    ripcheato_cnt_in_logic:int
):
    if not rowf_in_logic:
        world_graph = _set_rowf_out_of_logic(world_graph)
    if not merlow_in_logic:
        world_graph = _set_merlow_out_of_logic(world_graph)

    world_graph = _adjust_rip_cheato_logic(world_graph, ripcheato_cnt_in_logic)

    return world_graph


def _set_rowf_out_of_logic(world_graph:dict):
    remove_rowf_edges = []
    adjusted_rowf_edges = []

    for edge in world_graph["MAC_01/0"]["edge_list"]:
        if (    isinstance(edge["to"]["id"], str)
            and edge["to"]["id"].startswith("ShopBadge")
        ):
            remove_rowf_edges.append(deepcopy(edge))

            out_of_logic_edge = deepcopy(edge)
            out_of_logic_edge["reqs"] = [["RF_OutOfLogic"]]
            adjusted_rowf_edges.append(out_of_logic_edge)

    world_graph, _ = adjust(
        world_graph,
        new_edges=adjusted_rowf_edges,
        edges_to_remove=remove_rowf_edges
    )

    return world_graph


def _set_merlow_out_of_logic(world_graph:dict):
    remove_merlow_edges = []
    adjusted_merlow_edges = []

    for edge in world_graph["HOS_06/0"]["edge_list"]:
        if (    isinstance(edge["to"]["id"], str)
            and edge["to"]["id"] == "ShopRewardA"
        ):
            remove_merlow_edges.append(deepcopy(edge))

            out_of_logic_edge = deepcopy(edge)
            out_of_logic_edge["reqs"] = [["RF_OutOfLogic"]]
            adjusted_merlow_edges.append(out_of_logic_edge)
            break

    world_graph, _ = adjust(
        world_graph,
        new_edges=adjusted_merlow_edges,
        edges_to_remove=remove_merlow_edges
    )

    return world_graph


def _adjust_rip_cheato_logic(world_graph: dict, checks_in_logic:int):
    """
    Returns the modified world graph itself with adjusted item check logic for
    the 11 item checks of Rip Cheato.
    """
    base_cheato_edges = []
    base_cheato_edges.extend([deepcopy(edge) for edge in world_graph["TIK_15/1"]["edge_list"] if isinstance(edge["to"]["id"], str)])
    for x in "ABCDEFGHIJ":
        base_cheato_edges.extend(deepcopy([edge for edge in world_graph[f"TIK_15/Gift{x}"]["edge_list"]]))

    # late checks first to mark out of logic from the back of Cheato's item list
    base_cheato_edges.sort(key=lambda edge: edge["to"]["id"], reverse=True)

    checks_out_of_logic = len(base_cheato_edges) - checks_in_logic

    remove_cheato_edges = []
    adjusted_cheato_edges = []

    adjusted_edges_cnt = 0
    for edge in base_cheato_edges:
        if adjusted_edges_cnt >= checks_out_of_logic:
            break
        remove_cheato_edges.append(edge)
        new_edge = deepcopy(edge)
        new_edge["reqs"] = [["RF_OutOfLogic"]]
        adjusted_cheato_edges.append(new_edge)
        adjusted_edges_cnt += 1

    if adjusted_cheato_edges:
        world_graph, _ = adjust(
            world_graph,
            new_edges=adjusted_cheato_edges,
            edges_to_remove=remove_cheato_edges
        )

    return world_graph


def get_streamlined_chapters(world_graph: dict, required_chapters: list):
    all_new_edges = []
    all_edges_to_remove = []

    if len(required_chapters) < 7:
        all_new_edges.extend(get_streamlined_edges_hos_add(len(required_chapters)))
        all_edges_to_remove.extend(streamlined_edges_hos_remove)

    if 1 not in required_chapters:
        all_new_edges.extend(streamlined_edges_ch1_add)
        all_edges_to_remove.extend(streamlined_edges_ch1_remove)

    if 2 not in required_chapters:
        all_new_edges.extend(streamlined_edges_ch2_add)
        all_edges_to_remove.extend(streamlined_edges_ch2_remove)

    if 3 not in required_chapters:
        all_new_edges.extend(streamlined_edges_ch3_add)
        all_edges_to_remove.extend(streamlined_edges_ch3_remove)

    if 4 not in required_chapters:
        all_new_edges.extend(streamlined_edges_ch4_add)
        all_edges_to_remove.extend(streamlined_edges_ch4_remove)

    if 5 not in required_chapters:
        all_new_edges.extend(streamlined_edges_ch5_add)
        all_edges_to_remove.extend(streamlined_edges_ch5_remove)

    if 6 not in required_chapters:
        all_new_edges.extend(streamlined_edges_ch6_add)
        all_edges_to_remove.extend(streamlined_edges_ch6_remove)

    if 7 not in required_chapters:
        all_new_edges.extend(streamlined_edges_ch7_add)
        all_edges_to_remove.extend(streamlined_edges_ch7_remove)

    # Modify graph with all pending changes, if any
    if all_new_edges or all_edges_to_remove:
        world_graph, _ = adjust(
            world_graph,
            new_edges=all_new_edges,
            edges_to_remove=all_edges_to_remove
        )

    return world_graph
