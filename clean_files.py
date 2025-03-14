import os

CURRENT_FILE_PARENT_DIR = os.path.dirname(os.path.abspath(__file__))


def clean_files(file_count=10):
        
        file_prefixes = ['final_result_', 'req_2A', 'req_2B', 'req_4A', 'req_4B', 'req_5A', 'req_5B', 'req_6A', 'req_6B']

        for file_prefix in file_prefixes:
             # 如果result文件夹下文件名包含file_prefix的文件超过10个, 则删除最早创建的文件
            files = [file for file in os.listdir(os.path.join(CURRENT_FILE_PARENT_DIR, 'result')) if file_prefix in file]
            if len(files) > file_count:
                # 获取最早创建的文件
                files.sort(key=lambda x: os.path.getctime(os.path.join(CURRENT_FILE_PARENT_DIR, 'result', x)))
                for file in files[:-file_count]:
                    os.remove(os.path.join(CURRENT_FILE_PARENT_DIR, 'result', file))