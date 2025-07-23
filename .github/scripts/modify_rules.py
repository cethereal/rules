import os
import re

SOURCE_DIR = "source-repo"

def modify_files():
    processed_count = 0

    for root, dirs, files in os.walk(SOURCE_DIR):
        # 跳过 .git 目录
        if ".git" in root:
            continue

        for file in files:
            if not file.endswith('.list'):
                continue

            file_path = os.path.join(root, file)

            # 处理文件
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 核心替换：'+.' -> '.'
            modified_content = content.replace('+.', '.')

            # 写回原文件（覆盖）
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)

            processed_count += 1
            print(f"Processed: {os.path.relpath(file_path, SOURCE_DIR)}")

    print(f"\nTotal files processed: {processed_count}")

if __name__ == '__main__':
    modify_files()
