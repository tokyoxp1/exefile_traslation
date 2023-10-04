import re
from googletranslatepy import Translator

# 設定要翻譯的語言
target_lang = 'zh-TW'

# 創建翻譯器
translator = Translator(target=target_lang)

# 讀取文件
filename = 'Menu7.rc'
with open(filename, 'r', encoding='utf-16') as f:
    lines = f.readlines()

# 定義正則表達式
filename_pattern = r'(?<!\w)(\w+\.\w{3})(?!\w)'
string_pattern = r'"((?:[^"&]|&[a-zA-Z]+)*?)"'

# 翻譯字符串
for i, line in enumerate(lines):
    # 如果行以 BLOCK 或 VALUE 開頭，則跳過翻譯
    if line.startswith('BLOCK') or line.startswith('VALUE'):
        continue
    matches = re.findall(string_pattern, line)
    for match in matches:
        if not re.search(filename_pattern, match):
            if match:
                translated = translator.translate(match)
                if isinstance(translated, str):
                    translated = translated.replace('＆', '')
                    lines[i] = lines[i].replace(match, translated)
                    # 移除 & 符號後面沒有英文字母的情況
                    if re.search(r'&[^a-zA-Z]', lines[i]):
                        lines[i] = lines[i].replace('&', '')
        print(lines[i])

# COPY原始文件filename，存為 .bak
import shutil
shutil.copy(filename, filename + '.bak')

# 將翻譯後的內容寫回檔案
with open(filename, 'w', encoding='utf-16') as f:
    f.writelines(lines)