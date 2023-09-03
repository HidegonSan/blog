dark_color_unset = []
light_color_unset = []


with open("./assets/css/extended/chroma_dark.css", "r") as file_dark:
    for line_dark in file_dark.readlines():
        name = line_dark.split("*/")[0][3:].strip()
        tmp = line_dark.split(".dark .chroma ")
        if 2 <= len(tmp):
            class_name = tmp[1].split(" {")[0]
        else:
            continue
        is_color_unset = line_dark.find("color: ") == -1
        if is_color_unset:
            dark_color_unset.append([name, class_name])


with open("./assets/css/extended/chroma_light.css", "r") as file_light:
    for line_dark in file_light.readlines():
        name = line_dark.split("*/")[0][3:].strip()
        tmp = line_dark.split(".chroma ")
        if 2 <= len(tmp):
            class_name = tmp[1].split(" {")[0]
        else:
            continue
        is_color_unset = line_dark.find("color: ") == -1
        if is_color_unset:
            if not any([name == i[0] for i in dark_color_unset]):
                light_color_unset.append([name, class_name])
            else:
                index = [name == i[0] for i in dark_color_unset].index(True)
                dark_color_unset.pop(index)


output = """/* Reset Chroma styles for light/dark theme*/
/* Unset colors between light/dark */

/* for dark */
"""

for i in sorted(dark_color_unset):
    output += f"/* {i[0]} */ .dark .chroma {i[1]} " + "{ color: unset; }\n"

output += "\n/* for light */\n"

for i in sorted(light_color_unset):
    output += f"/* {i[0]} */ .chroma {i[1]} " + "{ color: unset; }\n"


with open("./assets/css/extended/chroma_reset.css", "w+") as fw:
    fw.write(output)
