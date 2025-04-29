"""
WSGI config for Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# import os
# import time

# import multiprocessing


# def run_background_task():
#     while True:
#         print("Running background task...")
#         time.sleep(300)  # 5 minutes
# bg_process = multiprocessing.Process(target=run_background_task)
# bg_process.daemon = True
# bg_process.start()

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

# application = get_wsgi_application()


"""
WSGI config for Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""


import os
import shutil
import time
from datetime import datetime
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
application = get_wsgi_application()

# Background task - only for development
if os.environ.get('RUN_MAIN') == 'true':  # Django's autoreload check
    import threading
    import time
    
    # def background_task():
    #     while True:
    #         print("Background task running...", flush=True)
    #         time.sleep(5)  # Reduced for testing
            

    def background_task():
        backup_dir = os.path.join(settings.BASE_DIR, 'db_backups')
        os.makedirs(backup_dir, exist_ok=True)
        
        while True:
            try:
                # Close any open DB connections
                from django.db import connections
                connections.close_all()
                
                # Generate timestamp and backup path
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                original_db = os.path.join(settings.BASE_DIR, 'db.sqlite3')
                replica_path = os.path.join(backup_dir, f'db_replica_{timestamp}.sqlite3')
                
                # Verify source exists
                if not os.path.exists(original_db):
                    print(f"Source database not found: {original_db}", flush=True)
                    time.sleep(300)
                    continue
                    
                # Perform the backup
                shutil.copy2(original_db, replica_path)
                
                # Verify backup was successful
                if os.path.exists(replica_path):
                    print(f"Successfully created backup: {replica_path}", flush=True)
                else:
                    print(f"Backup failed for unknown reason", flush=True)
                    
                backups = sorted([f for f in os.listdir(backup_dir) if f.startswith('db_replica_')],key=lambda x: os.path.getmtime(os.path.join(backup_dir, x)))
                for old_backup in backups[:-1]:
                    os.remove(os.path.join(backup_dir, old_backup))        
            except Exception as e:
                print(f"Backup error: {str(e)}", flush=True)
                
            finally:
                time.sleep(20) 
    thread = threading.Thread(target=background_task, daemon=True)
    thread.start()