import os
import moviepy.editor as mp

input_folder = 'Python batch video converter bot\\input'
output_folder = 'Python batch video converter bot\\converted'

target_codec = 'libx264'
target_format = 'mp4'

resolution = 480 # here you can change quality of the converted videos

try:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    
    for file in os.listdir(input_folder):
        if file.endswith('.mp4'):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, file)
            
            clip = mp.VideoFileClip(input_file)
            clip = clip.fx(mp.vfx.resize, height=resolution)
            clip.write_videofile(output_file, codec=target_codec, audio_codec='aac', preset='slow')
            
            print('Converted:', file)
except Exception as ex:
    print(f'Error {ex}')