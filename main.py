import sys

from core import (
    get_list,
    create_file,
    create_folder,
    delete_file,
    copy_file,
    save_info
)


save_info('Start')

command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('File name is missing')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('File name is missing')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('File name is missing')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('File name is missing')
    else:
        copy_file(name, new_name)
elif command == 'help':
    print('list - list of files and folders')
    print('create_file - create file')
    print('create folder - create folder')
    print('delete - delete file or folder')
    print('copy - copy file or folder')

save_info('End')
