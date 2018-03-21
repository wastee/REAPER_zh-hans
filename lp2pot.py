import re
import chardet  


def lp2po(filename):
    with open('./source/{}'.format(filename), encoding='iso-8859-1') as f:
        all_pre_pot = f.read().strip().split('\n\n')[1:]

    for pre_pot in all_pre_pot:
        pre_component_name = pre_pot.split('\n')[0]
        pcn = pre_component_name
        component_name = re.findall('\[.*?\]', pcn)[0][1:-1]
        pos = pre_pot.split('\n')[1:]  
        potext = 'msgid ""\n'\
        'msgstr ""\n'\
        '"Project-Id-Version: REAPER_zh-hans\\n"\n'\
        '"Last-Translator: All Chinese REAPER Users\\n"\n'\
        '"Language-Team: Chinese REAPER users\\n"\n'\
        '"MIME-Version: 1.0\\n"\n'\
        '"Content-Type: text/plain; charset=UTF-8\\n"\n'\
        '"Content-Transfer-Encoding: 8bit\\n"\n'\
        '"X-Generator: Python Script\\n"\n'\
        '"X-Poedit-Basepath: .\\n"\n'\
        '"Plural-Forms: nplurals=2; plural=(n != 1);\\n"\n'\
        '"Language: en_US\\n"\n'\
        '"X-Poedit-KeywordsList: =\\n"\n\n'
        for po in pos:
            p = (
                '#: ' + re.findall('^(.*)(?==)', po)[0],
                'msgid "' + re.findall('\=(.*)', po)[0] + '"',
                'msgstr ""',
                '',
                '',
            )
            if re.findall('\=(.*)', po)[0] != '' and re.findall('\=(.*)', po)[0] != ' ':
                potext += '\n'.join(p)

        with open('./pot/{}.pot'.format(component_name), 'w+', encoding='utf-8') as f:
            f.write(potext)

if __name__ == '__main__':
    lp2po('template_reaper570.ReaperLangPack')