dark_color_unset = []
dark_colors = []
light_color_unset = []
light_colors = []

# ダークテーマ用CSSを読み込み、色が設定されていないクラスを探し出す
with open("./assets/css/chroma/chroma_dark.css", "r") as file_dark:
    for line_dark in file_dark.readlines():
        name = line_dark.split("*/")[0][3:].strip()
        tmp = line_dark.split(".dark .chroma ")
        if 2 <= len(tmp):
            class_name = tmp[1].split(" {")[0]
        else:
            continue
        is_color_unset = line_dark.find("color: ") == -1
        if is_color_unset:
            # dark_colors.append([class_name[1:], "unset"])
            dark_color_unset.append([name, class_name])
        else:
            # 色が設定されている場合、chroma_vars.css用にクラス名と色を抽出する
            if class_name[0] == ".":
                values = tmp[1].split(" {")[1]
                color_start = values.find("color:")
                color = values[color_start + 7:color_start + 14]
                dark_colors.append([class_name[1:], color])

# ライトテーマ用CSSを読み込み、色が設定されていないクラスを探し出す
with open("./assets/css/chroma/chroma_light.css", "r") as file_light:
    for line_light in file_light.readlines():
        name = line_light.split("*/")[0][3:].strip()
        tmp = line_light.split(".chroma ")
        if 2 <= len(tmp):
            class_name = tmp[1].split(" {")[0]
        else:
            continue
        is_color_unset = line_light.find("color: ") == -1
        if is_color_unset:
            # light_colors.append([class_name[1:], "unset"])
            if not any([name == i[0] for i in dark_color_unset]):
                light_color_unset.append([name, class_name])
            else:
                index = [name == i[0] for i in dark_color_unset].index(True)
                dark_color_unset.pop(index)
        # 色が設定されている場合、chroma_vars.css用にクラス名と色を抽出する
        else:
            if class_name[0] == ".":
                values = tmp[1].split(" {")[1]
                color_start = values.find("color:")
                color = values[color_start + 7:color_start + 14]
                light_colors.append([class_name[1:], color])

# chroma_reset.css 用の説明
chroma_reset_output = """/* Reset Chroma styles for light/dark theme*/
/* Unset colors between light/dark */

/* for dark */
"""

# ダークテーマでcolorが未設定のクラスのcolorをunsetする
for i in sorted(dark_color_unset):
    chroma_reset_output += f"/* {i[0]} */ .dark .chroma {i[1]} " + "{ color: unset; }\n"
    dark_colors.append([i[1][1:], "unset"])

chroma_reset_output += "\n/* for light */\n"

# ライトテーマでcolorが未設定のクラスのcolorをunsetする
for i in sorted(light_color_unset):
    chroma_reset_output += f"/* {i[0]} */ .chroma {i[1]} " + "{ color: unset; }\n"
    light_colors.append([i[1][1:], "unset"])

# chroma_reset.css の書き込み
with open("./assets/css/chroma/chroma_reset.css", "w+") as fw:
    fw.write(chroma_reset_output)

# chroma_noscript.css 用の説明
chroma_noscript_output = """/* Color definitions for dark/light themes with JavaScript disabled */

/* for dark */
@media (prefers-color-scheme: dark) {
"""

for dark_color in dark_colors:
    var_name = ".chroma ." + dark_color[0]
    color = dark_color[1]
    chroma_noscript_output += "    " + var_name + " { color: " + color + "; }\n"

chroma_noscript_output += """}

/* for light */
@media (prefers-color-scheme: light) {
"""

for light_color in light_colors:
    var_name = ".chroma ." + light_color[0]
    color = light_color[1]
    chroma_noscript_output += "    " + var_name + " { color: " + color + "; }\n"

chroma_noscript_output += """}
"""

# chroma_noscript.css の書き込み
with open("./assets/css/chroma/chroma_noscript.css", "w+") as fw:
    fw.write(chroma_noscript_output)
