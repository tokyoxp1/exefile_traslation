import re
from googletranslatepy import Translator

# 設定要翻譯的語言
target_lang = 'zh-TW'

# 創建翻譯器
translator = Translator(target=target_lang)

# 讀取文件
filename = '1.rc'
with open(filename, 'r', encoding='utf-16') as f:
    lines = f.readlines()

# 定義正則表達式
filename_pattern = r'(?<!\w)(\w+\.\w{3})(?!\w)'
string_pattern = r'"((?:[^"&]|&[a-zA-Z]+)*?)"'

# 翻譯字符串
for i, line in enumerate(lines):
    # 如果行以 BLOCK 或 VALUE 開頭，則跳過翻譯
    if line.strip().startswith('BLOCK') or line.strip().startswith('VALUE'):
        continue
    # 找到第一個 "" 的位置
    first_quote = line.find('"')
    second_quote = line.find('"', first_quote + 1)
    # 如果找到了 ""，則進行翻譯
    if first_quote != -1 and second_quote != -1:
        # 翻譯 "" 中的內容
        to_translate = line[first_quote+1:second_quote]
        # 如果 "" 中的內容不是檔案名稱，則進行翻譯
        if not re.search(filename_pattern, to_translate):
            translated_str = translator.translate(to_translate)
            # 將翻譯後的內容替換回原始字符串中
            if isinstance(translated_str, str):
                translated_str = translated_str.replace('＆', '')
                line = line[:first_quote+1] + translated_str + line[second_quote:]
                # 移除 & 符號後面沒有英文字母的情況
                if re.search(r'&[^a-zA-Z]', line):
                    line = line.replace('&', '')
        lines[i] = line
    print(line)

# COPY原始文件filename，存為 .bak
import shutil
shutil.copy(filename, filename + '.bak')

# 將翻譯後的內容寫回檔案
with open(filename, 'w', encoding='utf-16') as f:
    f.writelines(lines)
