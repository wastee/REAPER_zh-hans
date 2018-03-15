import os
import re
import glob

def po2lp():
    pofiles = glob.glob('./po/*.po')

    result = [
        '#NAME:简体中文 (REAPER汉化小组汉化)',
        '; 此翻译基于GPL3.0协议发布（GNU General Public License v3.0）',
        '; 本项目地址：http://translate.reaget.com',
        '; 简体中文语言包发布地址：https://bitbucket.org/Kommit/reaper_cn',
        '; 特别感谢：Kommit, zs、盖盖、青猫、JacH 以及众多给翻译提供建议的朋友。',
        '; QQ交流群：243473647',
    ]
    component_result = []

    for pofile in pofiles: # each component files

        component_name = os.path.splitext(os.path.basename(pofile))[0]
        component_name = ['\n' + component_name]

        with open(pofile, 'r', encoding='utf-8') as f:
            empty = True
            line_result = []

            content = f.read()
            firstpart_content = re.match('([\s\S]*?)(?=#:)', content).group()

            content = content[len(firstpart_content):].strip()
            line_list = content.split('\n\n')
            for line in line_list: # each line in component
                if line.endswith('\"\"') is False:
                    empty = False
                    before_convert_list = line.split('\n')
                    left_string = before_convert_list[0]
                    left_string = left_string.lstrip('#: ;^')
                    left_string = left_string.lstrip('#: ;')
                    right_string = before_convert_list[2]
                    right_string = right_string.rstrip('"')
                    right_string = right_string.lstrip('msgstr "')

                    output_line = left_string + '=' + right_string
                    line_result.append(output_line)
            if empty == False:
                component_result += (component_name + line_result)

    with open('./zh_CN.ReaperLangPack', 'w+', encoding='utf-8') as f:
        f.write('\n'.join(result+component_result))

if __name__ == '__main__':
    po2lp()