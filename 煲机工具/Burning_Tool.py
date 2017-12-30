# -*- coding: utf-8 -*-
import pygame
import os
import random
import time
import datetime

TEST = 0
if TEST == 1:
      playing_time = 5
      pause_time = 2
      white_noise_time = 5
      pink_noise_time = 5
else:
      playing_time = 19 * 60
      pause_time = 60
      white_noise_time = 20 * 3600
      pink_noise_time = 10 * 3600

time_bak_ini = 0
if os.access("time.bak", os.R_OK):
      time_bak_fd = open("time.bak", "r")
      time_bak = time_bak_fd.read()
      time_bak_ini = int(time_bak)
      white_noise_time -= time_bak_ini
#print('time_bak: ',time_bak_ini)

init_time = time.time()

material_folder = 'material'
white_noise_folder = material_folder + '\\White_Noise\\'
pink_noise_folder = material_folder + '\\Pink_Noise\\'
music_folder = material_folder + '\\music\\'
#print(material_folder, white_noise_folder, pink_noise_folder, music_folder)

white_noise_list = os.listdir(white_noise_folder)
pink_noise_list = os.listdir(pink_noise_folder)
music_list = os.listdir(music_folder)
#print(white_noise_list, pink_noise_list, music_list)

white_noise_i = 0
pink_noise_i = 0
music_i = 0

start_time = time.time()
pygame.mixer.init()
while True:
      if not pygame.mixer.music.get_busy():
            all_time = time.time() - init_time
            if all_time < white_noise_time :
                  if len(white_noise_list) < 1:
                        break
                  if white_noise_i < (len(white_noise_list) - 1):
                        white_noise_i += 1
                  else:
                        white_noise_i = 0
                  playMusic = white_noise_folder + white_noise_list[white_noise_i]
            else:
                  if all_time < (white_noise_time + pink_noise_time):
                        if len(pink_noise_list) < 1:
                              break
                        if pink_noise_i < (len(pink_noise_list) - 1):
                              pink_noise_i += 1
                        else:
                              pink_noise_i = 0
                        playMusic = pink_noise_folder + pink_noise_list[pink_noise_i]
                  else:
                        if len(music_list) < 1:
                              break
                        if music_i < (len(music_list) - 1):
                              music_i += 1
                        else:
                              music_i = 0
                        playMusic = music_folder + music_list[music_i]
            pygame.mixer.music.load(playMusic)
            pygame.mixer.music.play()
            print('playing...',playMusic)
      else:
            time.sleep(5)
            tmp_time = time.time() - start_time

            all_time = time.time() - init_time
            bak_fd = open("time.bak", "w+")
            bak_fd.write(str(int(all_time)+time_bak_ini))
            bak_fd.close()

            if tmp_time >= playing_time:
                  print('pause  ... ',playMusic)
                  pygame.mixer.music.stop()
                  time.sleep(pause_time)
                  start_time = time.time()

all_time = time.time() - init_time
all_hour = all_time / 3600
all_min  = all_time % 3600 / 60
all_sec  = all_time % 60
print('All_time: ', int(all_hour), 'h', int(all_min), 'm', int(all_sec), 's')