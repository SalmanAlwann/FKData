import os
import sys
import tty
import termios

options = [
    "ar_AA",
    "ar_AE",
    "ar_BH",
    "ar_EG",
    "ar_JO",
    "ar_PS",
    "ar_SA",
    "az_AZ",
    "bg_BG",
    "bn_BD",
    "bs_BA",
    "cs_CZ",
    "da_DK",
    "de",
    "de_AT",
    "de_CH",
    "de_DE",
    "dk_DK",
    "el_CY",
    "el_GR",
    "en",
    "en_AU",
    "en_CA",
    "en_GB",
    "en_IE",
    "en_IN",
    "en_NZ",
    "en_PH",
    "en_TH",
    "en_US",
    "es",
    "es_AR",
    "es_CA",
    "es_CL",
    "es_CO",
    "es_ES",
    "es_MX",
    "et_EE",
    "fa_IR",
    "fi_FI",
    "fil_PH",
    "fr_BE",
    "fr_CA",
    "fr_CH",
    "fr_FR",
    "fr_QC",
    "ga_IE",
    "he_IL",
    "hi_IN",
    "hr_HR",
    "hu_HU",
    "hy_AM",
    "id_ID",
    "it_CH",
    "it_IT",
    "ja_JP",
    "ka_GE",
    "ko_KR",
    "la",
    "lb_LU",
    "lt_LT",
    "lv_LV",
    "mt_MT",
    "ne_NP",
    "nl_BE",
    "nl_NL",
    "no_NO",
    "or_IN",
    "pl_PL",
    "pt_BR",
    "pt_PT",
    "ro_RO",
    "ru_RU",
    "sk_SK",
    "sl_SI",
    "sq_AL",
    "sv_SE",
    "ta_IN",
    "th",
    "th_TH",
    "tl_PH",
    "tr_TR",
    "tw_GH",
    "uk_UA",
    "vi_VN",
    "zh_CN",
    "zh_TW"
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
    
def print_banner():
    print('\n')
    padding = '  '

    banner = [
        "\t███████╗██╗  ██╗██████╗  █████╗ ████████╗ █████╗ ",
        "\t██╔════╝██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗",
        "\t█████╗  █████╔╝ ██║  ██║███████║   ██║   ███████║",
        "\t██╔══╝  ██╔═██╗ ██║  ██║██╔══██║   ██║   ██╔══██║",
        "\t██║     ██║  ██╗██████╔╝██║  ██║   ██║   ██║  ██║",
        "\t╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝",
        "\n\t\t% Salman Alwan % 1.0.0\n"
    ]

    final = []
    init_color = 33  # Starting color index for dark blue
    txt_color = init_color
    cl = 0

    max_length = max(len(s) for s in banner)  # Get the maximum length of any string in the banner list

    for pos in range(len(banner)):
        line = ''
        for charset in range(max_length):
            if charset < len(banner[pos]):  # Check if the current string has a character at the given index
                clr = f'\033[38;5;{txt_color}m'
                char = f'{clr}{banner[pos][charset]}'
                line += char
                cl += 1

                # Modify the color change for the wavy effect
                if cl == 2:
                    if txt_color == 33:
                        txt_color = 201  # Switch to bright pink
                    else:
                        txt_color = 33  # Switch to dark blue

                if cl >= 3:
                    cl = 0

        final.append(line)

    print('\n'.join(final))


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def print_menu(selected, op):
    for i, option in enumerate(op):
        if i == selected:
            print(f"\033[34m➤ {option}\033[0m")
        else:
            print(f"  {option}")