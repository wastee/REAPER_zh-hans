import os
import json
import glob

all_files = glob.glob('./pot/*.pot')

def comp2json():
    result = []

    for f in all_files:
        fn = os.path.splitext(os.path.basename(f))[0]
        fn_thin = fn.lower()
        if fn_thin != 'about':
            result.append({
                "name": fn,
                "slug": fn_thin,
                # "repo": "https://github.com/wastee/REAPER_zh-hans.git",
                "repo": "weblate://reaper/about",
                # "push": "git@github.com:wastee/REAPER_zh-hans.git",
                "branch": "master",
                "filemask": "po/{}-*.po".format(fn),
                "new_base": "pot/{}.pot".format(fn),
                "committer_name": "REAPER Weblate",
                "committer_email": "i@lado.me",
                "allow_translation_propagation": False
            })

    with open('./import_components.json', 'w+', encoding='utf-8') as f:
        json.dump(result, f)

if __name__ == '__main__':
    comp2json()
