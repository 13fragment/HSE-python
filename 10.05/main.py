import os
import os.path
dirs=os.walk('/home/max/Документы/task_os/Actors')
file_source1='/home/max/Документы/task_os/Actors/Actor_01/'
file_source2='/home/max/Документы/task_os/Actors/Actor_02/'
file_source3='/home/max/Документы/task_os/Actors/Actor_03/'
file_source4='/home/max/Документы/task_os/Actors/Actor_04/'
file_source5='/home/max/Документы/task_os/Actors/Actor_05/'
file_source6='/home/max/Документы/task_os/Actors/Actor_06/'
file_source7='/home/max/Документы/task_os/Actors/Actor_07/'

get_files1=os.listdir(file_source1)
for path_from_top, subdirs, files in dirs:
    for f in get_files1:
      if f.startswith('03-01-01'):
        file_destination='/home/max/Документы/task_os/neutral/'
        os.replace(file_source1+f, file_destination+f)
      elif f.startswith('03-01-02'):
          file_destination='/home/max/Документы/task_os/calm/'
          os.replace(file_source1+f, file_destination+f)
      elif f.startswith('03-01-03'):
        file_destination='/home/max/Документы/task_os/happy/'
        os.replace(file_source1+f, file_destination+f)
      elif f.startswith('03-01-04'):
        file_destination='/home/max/Документы/task_os/sad/'
        os.replace(file_source1+f, file_destination+f)
      elif f.startswith('03-01-05'):
        file_destination='/home/max/Документы/task_os/angry/'
        os.replace(file_source1+f, file_destination+f)
      elif f.startswith('03-01-06'):
        file_destination='/home/max/Документы/task_os/fearful/'
        os.replace(file_source1+f, file_destination+f)
      elif f.startswith('03-01-07'):
        file_destination='/home/max/Документы/task_os/disgust/'
        os.replace(file_source1+f, file_destination+f)
      elif f.startswith('03-01-08'):
        file_destination='/home/max/Документы/task_os/surprised/'
        os.replace(file_source1+f, file_destination+f)

get_files2=os.listdir(file_source2)
for path_from_top, subdirs, files in dirs:
    for f in get_files2:
      if f.startswith('03-01-01'):
        file_destination='/home/max/Документы/task_os/neutral/'
        os.replace(file_source2+f, file_destination+f)
      elif f.startswith('03-01-02'):
          file_destination='/home/max/Документы/task_os/calm/'
          os.replace(file_source2+f, file_destination+f)
      elif f.startswith('03-01-03'):
        file_destination='/home/max/Документы/task_os/happy/'
        os.replace(file_source2+f, file_destination+f)
      elif f.startswith('03-01-04'):
        file_destination='/home/max/Документы/task_os/sad/'
        os.replace(file_source2+f, file_destination+f)
      elif f.startswith('03-01-05'):
        file_destination='/home/max/Документы/task_os/angry/'
        os.replace(file_source2+f, file_destination+f)
      elif f.startswith('03-01-06'):
        file_destination='/home/max/Документы/task_os/fearful/'
        os.replace(file_source2+f, file_destination+f)
      elif f.startswith('03-01-07'):
        file_destination='/home/max/Документы/task_os/disgust/'
        os.replace(file_source2+f, file_destination+f)
      else:
        file_destination='/home/max/Документы/task_os/surprised/'
        os.replace(file_source2+f, file_destination+f)

get_files3=os.listdir(file_source3)
for path_from_top, subdirs, files in dirs:
    for f in get_files3:
      if f.startswith('03-01-01'):
        file_destination='/home/max/Документы/task_os/neutral/'
        os.replace(file_source3+f, file_destination+f)
      elif f.startswith('03-01-02'):
          file_destination='/home/max/Документы/task_os/calm/'
          os.replace(file_source3+f, file_destination+f)
      elif f.startswith('03-01-03'):
        file_destination='/home/max/Документы/task_os/happy/'
        os.replace(file_source3+f, file_destination+f)
      elif f.startswith('03-01-04'):
        file_destination='/home/max/Документы/task_os/sad/'
        os.replace(file_source3+f, file_destination+f)
      elif f.startswith('03-01-05'):
        file_destination='/home/max/Документы/task_os/angry/'
        os.replace(file_source3+f, file_destination+f)
      elif f.startswith('03-01-06'):
        file_destination='/home/max/Документы/task_os/fearful/'
        os.replace(file_source3+f, file_destination+f)
      elif f.startswith('03-01-07'):
        file_destination='/home/max/Документы/task_os/disgust/'
        os.replace(file_source3+f, file_destination+f)
      else:
        file_destination='/home/max/Документы/task_os/surprised/'
        os.replace(file_source3+f, file_destination+f)

get_files4=os.listdir(file_source4)
for path_from_top, subdirs, files in dirs:
    for f in get_files4:
      if f.startswith('03-01-01'):
        file_destination='/home/max/Документы/task_os/neutral/'
        os.replace(file_source4+f, file_destination+f)
      elif f.startswith('03-01-02'):
          file_destination='/home/max/Документы/task_os/calm/'
          os.replace(file_source4+f, file_destination+f)
      elif f.startswith('03-01-03'):
        file_destination='/home/max/Документы/task_os/happy/'
        os.replace(file_source4+f, file_destination+f)
      elif f.startswith('03-01-04'):
        file_destination='/home/max/Документы/task_os/sad/'
        os.replace(file_source4+f, file_destination+f)
      elif f.startswith('03-01-05'):
        file_destination='/home/max/Документы/task_os/angry/'
        os.replace(file_source4+f, file_destination+f)
      elif f.startswith('03-01-06'):
        file_destination='/home/max/Документы/task_os/fearful/'
        os.replace(file_source4+f, file_destination+f)
      elif f.startswith('03-01-07'):
        file_destination='/home/max/Документы/task_os/disgust/'
        os.replace(file_source4+f, file_destination+f)
      else:
        file_destination='/home/max/Документы/task_os/surprised/'
        os.replace(file_source4+f, file_destination+f)

get_files5=os.listdir(file_source5)
for path_from_top, subdirs, files in dirs:
    for f in get_files5:
      if f.startswith('03-01-01'):
        file_destination='/home/max/Документы/task_os/neutral/'
        os.replace(file_source5+f, file_destination+f)
      elif f.startswith('03-01-02'):
          file_destination='/home/max/Документы/task_os/calm/'
          os.replace(file_source5+f, file_destination+f)
      elif f.startswith('03-01-03'):
        file_destination='/home/max/Документы/task_os/happy/'
        os.replace(file_source5+f, file_destination+f)
      elif f.startswith('03-01-04'):
        file_destination='/home/max/Документы/task_os/sad/'
        os.replace(file_source5+f, file_destination+f)
      elif f.startswith('03-01-05'):
        file_destination='/home/max/Документы/task_os/angry/'
        os.replace(file_source5+f, file_destination+f)
      elif f.startswith('03-01-06'):
        file_destination='/home/max/Документы/task_os/fearful/'
        os.replace(file_source5+f, file_destination+f)
      elif f.startswith('03-01-07'):
        file_destination='/home/max/Документы/task_os/disgust/'
        os.replace(file_source5+f, file_destination+f)
      else:
        file_destination='/home/max/Документы/task_os/surprised/'
        os.replace(file_source5+f, file_destination+f)

get_files6=os.listdir(file_source6)
for path_from_top, subdirs, files in dirs:
    for f in get_files6:
      if f.startswith('03-01-01'):
        file_destination='/home/max/Документы/task_os/neutral/'
        os.replace(file_source6+f, file_destination+f)
      elif f.startswith('03-01-02'):
          file_destination='/home/max/Документы/task_os/calm/'
          os.replace(file_source6+f, file_destination+f)
      elif f.startswith('03-01-03'):
        file_destination='/home/max/Документы/task_os/happy/'
        os.replace(file_source6+f, file_destination+f)
      elif f.startswith('03-01-04'):
        file_destination='/home/max/Документы/task_os/sad/'
        os.replace(file_source6+f, file_destination+f)
      elif f.startswith('03-01-05'):
        file_destination='/home/max/Документы/task_os/angry/'
        os.replace(file_source6+f, file_destination+f)
      elif f.startswith('03-01-06'):
        file_destination='/home/max/Документы/task_os/fearful/'
        os.replace(file_source6+f, file_destination+f)
      elif f.startswith('03-01-07'):
        file_destination='/home/max/Документы/task_os/disgust/'
        os.replace(file_source6+f, file_destination+f)
      else:
        file_destination='/home/max/Документы/task_os/surprised/'
        os.replace(file_source6+f, file_destination+f)

get_files7=os.listdir(file_source7)
for path_from_top, subdirs, files in dirs:
    for f in get_files7:
      if f.startswith('03-01-01'):
        file_destination='/home/max/Документы/task_os/neutral/'
        os.replace(file_source7+f, file_destination+f)
      elif f.startswith('03-01-02'):
          file_destination='/home/max/Документы/task_os/calm/'
          os.replace(file_source7+f, file_destination+f)
      elif f.startswith('03-01-03'):
        file_destination='/home/max/Документы/task_os/happy/'
        os.replace(file_source7+f, file_destination+f)
      elif f.startswith('03-01-04'):
        file_destination='/home/max/Документы/task_os/sad/'
        os.replace(file_source7+f, file_destination+f)
      elif f.startswith('03-01-05'):
        file_destination='/home/max/Документы/task_os/angry/'
        os.replace(file_source7+f, file_destination+f)
      elif f.startswith('03-01-06'):
        file_destination='/home/max/Документы/task_os/fearful/'
        os.replace(file_source7+f, file_destination+f)
      elif f.startswith('03-01-07'):
        file_destination='/home/max/Документы/task_os/disgust/'
        os.replace(file_source7+f, file_destination+f)
      else:
        file_destination='/home/max/Документы/task_os/surprised/'
        os.replace(file_source7+f, file_destination+f)

for dirpath, dirnames, filenames in os.walk('/home/max/Документы/task_os/'):
    for filename in [f for f in filenames if f.endswith('wav')]:
      print(os.path.join(dirpath, filename))