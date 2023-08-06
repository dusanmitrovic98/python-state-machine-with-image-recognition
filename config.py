import os

MY_USERNAME = "bk2019"

FREQUENCY = 1
THRESHOLD = 0.85
TIMEOUT = FREQUENCY * 80
TIMEOUT_REGENERATION_STATE = 1100
timeout_counter = FREQUENCY

NUM_BACKSPACES_PRESSES = 13

PROCESS_ON_ENTER = True
PROCESS_ON_EXIT = True

START_STATE = 1
END_STATE_ACCOUNT_CREATION = 10
END_STATE_WATCH_ADS = 100
END_STATE_TRANSFER_GOLD = 200

current_directory = os.path.dirname(os.path.abspath(__file__))

img_acc_01 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_01.jpg"))
img_acc_02 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_02.jpg"))
img_acc_03 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_03.jpg"))
img_acc_04 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_04.jpg"))
img_acc_05 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_05.jpg"))
img_acc_06 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_06.jpg"))
img_acc_07 = os.path.join(os.path.join(current_directory, "images\\create_account\\img_acc_07.jpg"))

img_wa_10 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_10.jpg"))
img_wa_11 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_11.jpg"))
img_wa_12 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_12.jpg"))
img_wa_13 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_13.jpg"))
img_wa_14 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_14.jpg"))
img_wa_15 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_15.jpg"))
img_wa_16 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_16.jpg"))
img_wa_17 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_17.jpg"))
img_wa_18 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_18.jpg"))
img_wa_19 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_19.jpg"))
img_wa_20 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_20.jpg"))
img_wa_21 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_21.jpg"))
img_wa_22 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_22.jpg"))
img_wa_23 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_23.jpg"))
img_wa_24 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_24.jpg"))
img_wa_25 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_25.jpg"))
img_wa_26 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_26.jpg"))
img_wa_27 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_27.jpg"))
img_wa_28 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_28.jpg"))
img_wa_99 = os.path.join(os.path.join(current_directory, "images\\watch_ads\\img_wa_99.jpg"))

img_tg_100 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_100.jpg"))
img_tg_101 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_101.jpg"))
img_tg_102 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_102.jpg"))
img_tg_103 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_103.jpg"))
img_tg_104 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_104.jpg"))
img_tg_105 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_105.jpg"))
img_tg_106 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_106.jpg"))
img_tg_107 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_107.jpg"))
img_tg_108 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_108.jpg"))
img_tg_109 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_109.jpg"))
img_tg_110 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_110.jpg"))
img_tg_111 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_111.jpg"))
img_tg_112 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_112.jpg"))
img_tg_113 = os.path.join(os.path.join(current_directory, "images\\transfer_gold\\img_tg_113.jpg"))

img_cd_201 = os.path.join(os.path.join(current_directory, "images\\clear_data\\img_cd_201.jpg"))
img_cd_202 = os.path.join(os.path.join(current_directory, "images\\clear_data\\img_cd_202.jpg"))
img_cd_203 = os.path.join(os.path.join(current_directory, "images\\clear_data\\img_cd_203.jpg"))
img_cd_204 = os.path.join(os.path.join(current_directory, "images\\clear_data\\img_cd_204.jpg"))
img_cd_205 = os.path.join(os.path.join(current_directory, "images\\clear_data\\img_cd_205.jpg"))
img_cd_206 = os.path.join(os.path.join(current_directory, "images\\clear_data\\img_cd_206.jpg"))
img_cd_207 = os.path.join(os.path.join(current_directory, "images\\clear_data\\img_cd_207.jpg"))

img_1100 = os.path.join(os.path.join(current_directory, "images\\img_1100.jpg"))
img_1101 = os.path.join(os.path.join(current_directory, "images\\img_1101.jpg"))