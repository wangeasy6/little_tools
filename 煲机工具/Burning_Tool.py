# -*- coding: utf-8 -*-
import pygame
import os
import random
import time
import datetime

TEST = 0
UPDATE_FOLDER = 1

#----------------------------- 初始化 播放时长设置 -------------------------
if TEST == 1:
      playing_time = 5
      pause_time = 2
      white_noise_time = 10
      pink_noise_time = 10
else:
      playing_time = 19 * 60
      pause_time = 60
      white_noise_time = 20 * 3600
      pink_noise_time = 10 * 3600

#----------------------------- 初始化 断点时间 -------------------------
time_bak_ini = 0
if os.access("time.bak", os.R_OK):
      time_bak_fd = open("time.bak", "r")
      time_bak = time_bak_fd.read()
      time_bak_ini = int(time_bak)
      white_noise_time -= time_bak_ini
print('Last Time: ', \
      int(time_bak_ini / 3600), 'h ', \
      int(time_bak_ini % 3600 / 60), 'm ', \
      int(time_bak_ini % 60), 's ')

#----------------------------- 初始化 文件夹 -------------------------
material_folder = 'material'
white_noise_folder = material_folder + '\\White_Noise\\'
pink_noise_folder = material_folder + '\\Pink_Noise\\'
music_folder = material_folder + '\\music\\'
#print(material_folder, white_noise_folder, pink_noise_folder, music_folder)

#----------------------------- 初始化 文件列表 -------------------------
white_noise_list = os.listdir(white_noise_folder)
pink_noise_list = os.listdir(pink_noise_folder)
music_list = os.listdir(music_folder)
#print(white_noise_list, pink_noise_list, music_list)

#----------------------------- 初始化 歌曲播放次序 -------------------------
white_noise_i = 0
pink_noise_i = 0
music_i = 0

def update_folder():
      global white_noise_i
      global pink_noise_i
      global music_i
      global white_noise_list
      global pink_noise_list
      global music_list

      if UPDATE_FOLDER == 1:
            white_noise_list = os.listdir(white_noise_folder)
            if white_noise_i >= len(white_noise_list):
                  white_noise_i = 0
            pink_noise_list = os.listdir(pink_noise_folder)
            if pink_noise_i >= len(pink_noise_list):
                  pink_noise_i = 0
            music_list = os.listdir(music_folder)
            if music_i >= len(music_list):
                  music_i = 0

def next_song():
      global white_noise_i
      global pink_noise_i
      global music_i

      all_time = time.time() - init_time
      if all_time < white_noise_time :
            if len(white_noise_list) < 1:
                  return None
            playMusic = white_noise_folder + white_noise_list[white_noise_i]
            white_noise_i += 1
            if white_noise_i >= len(white_noise_list):
                  white_noise_i = 0
      else:
            if all_time < (white_noise_time + pink_noise_time):
                  if len(pink_noise_list) < 1:
                        return None
                  playMusic = pink_noise_folder + pink_noise_list[pink_noise_i]
                  pink_noise_i += 1
                  if pink_noise_i >= len(pink_noise_list):
                        pink_noise_i = 0
            else:
                  if len(music_list) < 1:
                        return None
                  playMusic = music_folder + music_list[music_i]
                  music_i += 1
                  if music_i >= len(music_list):
                        music_i = 0
      return playMusic

def bak_file_write():
      all_time = time.time() - init_time
      bak_fd = open("time.bak", "w+")
      bak_fd.write(str(int(all_time)+time_bak_ini))
      bak_fd.close()

init_time = time.time()
def main():
      start_time = time.time()
      pygame.mixer.init()
      while True:
            if not pygame.mixer.music.get_busy():
                  update_folder()
                  playMusic = next_song()
                  if not playMusic:
                        break
                  pygame.mixer.music.load(playMusic)
                  pygame.mixer.music.play()
                  print('playing...',playMusic)
            else:
                  time.sleep(5)
                  bak_file_write()
                  tmp_time = time.time() - start_time
                  if tmp_time >= playing_time:
                        print('pause  ... ',playMusic)
                        pygame.mixer.music.stop()
                        time.sleep(pause_time)
                        start_time = time.time()

      all_time = time.time() - init_time
      print('All Time : ', \
            int(all_time / 3600), 'h ', \
            int(all_time % 3600 / 60), 'm ', \
            int(all_time % 60), 's ')

if __name__ == '__main__':
      main()
