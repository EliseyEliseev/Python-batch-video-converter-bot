# Python Batch Video Converter Bot
This script is a simple batch video converter that uses the moviepy module to convert all .mp4 files found in a specified input folder to the .mp4 format with the libx264 video codec and aac audio codec. The script also allows you to change the quality of the converted videos by setting the desired resolution.

# Prerequisites
To use this script, you need to have Python 3 and the moviepy module installed on your computer.

You can install the moviepy module using pip:


pip install moviepy


# Usage
Download this repository to your computer.

Put the videos you want to convert into the input folder.

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script using the following command:


python main.py


The script will convert all .mp4 files found in the input folder to the .mp4 format with the libx264 video codec and aac audio codec, and save them to the converted folder. The quality of the converted videos can be changed by modifying the resolution variable in the script.