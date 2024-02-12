import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

accepted_file_types = [
    'jpg', 'jpeg', 'png', 'gif', 
    'pdf', 'txt', 'doc', 'docx', 
    'xls', 'xlsx', 'ppt', 'pptx',
    'dmg']

image_file_types = ['jpg', 'jpeg', 'png', 'gif']
document_file_types = ['pdf', 'txt', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx']
installer_file_types = ['dmg', 'pkg', 'app', 'exe', 'msi', 'deb', 'rpm']
xml_file_types = ['xml']

def get_destination_folder(file_type):
    if file_type in image_file_types:
        return os.path.join(path, 'Images')
    elif file_type in document_file_types:
        return os.path.join(path, 'Documents')
    elif file_type in installer_file_types:
        return os.path.join(path, 'Installers')
    elif file_type in xml_file_types:
        return os.path.join(path, 'XMLs')

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            src_path = event.src_path
            file_name = os.path.basename(src_path)
            file_type = os.path.splitext(file_name)[1][1:]
        
            # Ignore the file while it's downloading
            if file_type not in accepted_file_types:
                return 
            dest_folder = get_destination_folder(file_type)
            os.makedirs(dest_folder, exist_ok=True)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_path, exist_ok=True)
            dest_path = os.path.join(dest_folder, file_name)
            shutil.move(src_path, dest_path)
            print(f"Moved file: {file_name} to {dest_folder}")

path = os.path.expanduser("~/Downloads")  # Path to the Downloads folder

# Create the main Downloads folder if it doesn't exist
os.makedirs(path, exist_ok=True)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()