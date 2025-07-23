import os
import re

SOURCE_DIR = "source-repo"
TARGET_DIR = "."

def modify_files():
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.endswith('.list'):
                continue

            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, SOURCE_DIR)
            dst_path = os.path.join(TARGET_DIR, rel_path)

            # 确保目标目录存在
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)

            # 关键修改：'+.' -> '.' 并写入目标仓库
            with open(src_path, 'r', encoding='utf-8') as f_src, \
                 open(dst_path, 'w', encoding='utf-8') as f_dst:

                content = f_src.read()
                modified_content = content.replace('+.', '.')  # 核心替换逻辑
                f_dst.write(modified_content)

            print(f"Processed: {rel_path}")

if __name__ == '__main__':
    modify_files()
