import os
import shutil
import sys

arg_path = sys.argv[1]

if not os.path.exists(arg_path):
    print("Folder not found")
    sys.exit()

def get_contextual_folder(file_type):
    image_file_types = ['jpg', 'jpeg', 'png', 'gif']
    document_file_types = ['pdf', 'txt', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']
    installer_file_types = ['dmg', 'pkg', 'app', 'exe', 'msi', 'deb', 'rpm']
    xml_file_types = ['xml']

    if file_type in image_file_types:
        return "Images"
    elif file_type in document_file_types:
        return "Documents"
    elif file_type in installer_file_types:
        return "Installers"
    elif file_type in xml_file_types:
        return "XMLs"
    else:
        return ""

def organize_current_folder():
    if len(arg_path) > 0:
        current_dir = arg_path
    else:
        current_dir = os.getcwd()
    
    # Get all files in the current directory
    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

    # Iterate through the files and print the file type
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension[1:]
        contextual_folder = get_contextual_folder(file_extension)
        src_path = os.path.join(current_dir, file)
        dest_path = os.path.join(current_dir, contextual_folder)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path, exist_ok=True)
        shutil.move(src_path, os.path.join(dest_path, file))
        print("Moved file")
 
if __name__ == "__main__":
    organize_current_folder()
