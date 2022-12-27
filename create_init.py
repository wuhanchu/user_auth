## 构建不同服务的初始化脚本

import functools
import os
from flask_frame.extension.database import file_compare_version, compare_version
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
print(os.path.dirname(SCRIPT_DIR))
sys.path.append(os.path.dirname(SCRIPT_DIR))

begin_version = "0.12.1"
end_version = "0.13"


def create_init_sql():
    from config import config

    current_config = config.get("production")
    file_name = "sql/create_all.sql"

    with open(file_name, "w") as file_obj:
        file_obj.write("SET search_path TO user_auth; \n")

        # 构建脚本
        for file in current_config.DB_INIT_FILE:
            with open(file, "r") as f:
                file_obj.write(f.read())
                file_obj.write("\n")

        # 更新脚本
        sql_path = "sql/migrate"
        version_file_list = [
            os.path.join(sql_path, item) for item in os.listdir(sql_path)
        ]
        for version_file in sorted(
            version_file_list, key=functools.cmp_to_key(file_compare_version)
        ):

            (file_path, temp_file_name) = os.path.split(version_file)
            (current_version, extension) = os.path.splitext(temp_file_name)

            # 小于当前版本 不执行
            if compare_version(current_version, begin_version) < 1:
                continue
            elif current_version == end_version:
                ...
            elif compare_version(end_version, current_version) < 1:
                break

            with open(version_file, "r") as f:
                file_obj.write(f.read())
                file_obj.write("\n")

        # 实时对象
        for file in current_config.DB_UPDATE_FILE:
            with open(file, "r") as f:
                file_obj.write(f.read())
                file_obj.write("\n")


if __name__ == "__main__":
    create_init_sql()
