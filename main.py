import os
import shutil
import os.path
import time
sss = input("Enter you source path please : ")
rrr = input("Enter you replica path please : ")


def run(path1, path2):

    global source
    global replica
    global source_list
    global replica_list
    source = path1
    replica = path2

    source_list = []
    replica_list = []

    os.chdir(replica)
    replica_list += os.listdir()
    os.chdir(source)
    source_list += os.listdir()


run(sss, rrr)
copy = 0
delete_file = 0
modify = 0
r_size = 0
s_size = 0
update = 0


def report():   # TO PRINT REPORT WHAT HAS BEEN DONE
    global copy
    global modify
    global delete_file
    global update
    print(f"The number of files and directions have been copied  = {copy}")
    print(f"The number of files and directions have been modified  = {modify}")
    print(f"The number of files and directions have been deleted  = {delete_file}")
    print(f"The number of files and directions have been updated  = {update}")
    copy = 0
    delete_file = 0
    modify = 0
    update = 0


def delete_files(file):  # TO DELETE FILE IF NECESSARY

    global delete_file
    if file not in source_list:
        os.chdir(replica)
        os.remove(file)
        print(f"The file : {file} has been deleted !")
        delete_file += 1


def delete_dir(dire):  # TO DELETE DIRECTOR IF NECESSARY

    global delete_file
    if dire not in source_list:
        os.chdir(replica)
        shutil.rmtree(dire)
        print(f"The director : {dire} has been deleted !")
        delete_file += 1


def delete_file_and_dir():  # TO RECOGNIZE IF DIRECTOR OR FILE

    for dirs in replica_list:
        name, ext = os.path.splitext(dirs)
        isdir = os.path.isdir(dirs)
        # isfile = os.path.isfile(dirs)
        if isdir or ext == '':
            delete_dir(dirs)
        else:
            delete_files(dirs)


def copy_files(s_file):  # TO COPY OR MODIFY FILE

    global copy
    global modify
    os.chdir(source)
    if s_file not in replica_list:      # TO COPY
        os.chdir(source)
        shutil.copy2(s_file, replica)
        copy += 1
        print(f"The file : {s_file} has been copied ! ")
    else:
        for r_file in replica_list:
            os.chdir(source)
            file_time = os.path.getmtime(s_file)
            os.chdir(replica)
            rfile_time = os.path.getmtime(r_file)
            if r_file == s_file and file_time != rfile_time:   # TO MODIFY
                os.chdir(replica)
                os.remove(r_file)
                os.chdir(source)
                shutil.copy2(s_file, replica)
                modify += 1
                print(f"The file : {s_file} has been modified ! ")
            else:
                continue


def copy_folder(s_file):  # TO COPY OR UPDATE DIRECTORY
    global copy
    global update
    os.chdir(source)
    if s_file not in replica_list:  # TO COPY DIRECTORY
        os.chdir(source)
        source1 = fr'C:\Users\Dado\Desktop\python codes\source\{s_file}'
        replica1 = fr"C:\Users\Dado\Desktop\python codes\replica\{s_file}"
        shutil.copytree(source1, replica1)
        copy += 1
        print(f"The director : {s_file} has been copied ! ")
    else:
        for r_file in replica_list:
            isdir = os.path.isdir(r_file)
            if isdir:
                os.chdir(replica)
            if s_file == r_file:    # TO UPDATE DIRECTORY
                os.chdir(replica)
                shutil.rmtree(r_file)
                source1 = fr'C:\Users\Dado\Desktop\python codes\source\{s_file}'
                replica1 = fr"C:\Users\Dado\Desktop\python codes\replica\{s_file}"
                shutil.copytree(source1, replica1)
                update += 1
                print(f"The director : {s_file} has been updated ! ")
            else:
                continue


def checking():  # TO RECOGNIZE IF DIRECTOR OR FILE
    for item in source_list:
        os.chdir(source)
        isdir = os.path.isdir(item)
        if isdir:
            copy_folder(item)
        else:
            copy_files(item)


while 1:

    run(sss, rrr)
    checking()
    delete_file_and_dir()
    report()
    print("--------------------------------------------------------------")
    time.sleep(20)
