import os
import stat
# # ! Membuat direktory bernama Fruit
# os.mkdir("Fruit")
# # ! Membuat direktory didalam direktory bernama car
# os.makedirs("vehicles/four_wheeler/car")
# # ! Menghapus direktory didalam direktory
# os.removedirs("vehicles/four_wheeler")
# # ! Menghapus direktory
# os.rmdir("Fruit")

# file_name = "apple.txt"
# file = os.popen(file_name, 'w')
# file.write("Apples are healthy")
# file = os.popen(file_name, 'r')

# print("Before renaming:", os.listdir())
# os.renames("apple.txt", "Mango.txt")
# ! Menghapus secara permanen dan file tidak bisa digunakan
# os.unlink('Mango.txt')
# print("After renaming:", os.listdir())
# print(os.listdir())
# print(os.getcwd()) 
# ! Melihat lokasi, list direktori, list file
# for i, j, k in os.walk(os.getcwd()):
#    print("path =", i)
#    print("List of directories =", j)
#    print("List of files =", k)
   
# print(os.path.getsize('main.py'))
# print(os.getgid())
# print(os.getpid())
# print(os.getuid())
# os.system("node --version")


# print(os.access('main.py', os.R_OK))
# ! mengeksekusi panggilan sistem stat pada jalur yang dilewati dan mengembalikan informasi berikut tentang jalur tersebut.
# print(os.stat("modules"))
# print(os.chflags("modules", stat.SF_APPEND))

# ! mengubah UID dan GID file masing-masing menjadi UID numerik dan GID.
# fd1 = os.open("modules", os.O_RDONLY)
# print(os.fchown(fd1, -1, 100))

# ! Change mode of direktory/file
# print(os.chmod("modules", stat.S_IRWXU))

fd1 = os.open("modules/file1.txt", os.O_RDWR)
print(os.fstatvfs(fd1))
