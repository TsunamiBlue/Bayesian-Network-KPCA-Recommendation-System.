import zipfile
import os

def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

extra_file_dir = './submission_extras'
file_paths = get_all_file_paths(extra_file_dir)

with zipfile.ZipFile(f'assignment_2_submission.zip', 'w') as f:
    f.write('question_1.ipynb')
    f.write('question_2.ipynb')
    f.write('question_3.ipynb')
    for file in file_paths:
        f.write(file)

