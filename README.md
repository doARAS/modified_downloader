# VFHQ-downloader

VFHQ-downloader is a Python-based utility designed for the easy downloading and processing of videos from the [VFHQ dataset](https://liangbinxie.github.io/projects/vfhq/).

## Warnning

This may cause [temporary IP block](https://github.com/yt-dlp/yt-dlp/issues/7860) by YouTube.

## Setup

1. Clone the repository or download the source code.
2. Install required Python packages: `pip install -r requirements.txt`.
3. Ensure `yt-dlp` and `aria2c` are installed and accessible in your system's PATH.

~~ 4. Download and decompress the [meta_info.zip](https://1drv.ms/u/s!Ag1HH_EDGMqqh2i5sgNyHpcVldos?e=8wKFtV) file in the root directory of the project to obtain the metadata files needed for video processing. ~~

## Usage

1. Ensure the metadata files are located in the `meta_info/` directory.
2. Copy paste all the files from the speicfic batch that needs to be downloaded into the meta_info/ directory. 
2. Run `main.py` to start the downloading and processing pipeline.
3. Processed videos will be available in the `data/outputs/` directory.
4. Delete the full "youtube videos" folder, we do not need the full videos. 
5. Download the videos in the output folder into the VFHQ RAW output Drive folder. "https://drive.google.com/drive/u/1/folders/1_xOg-BuVCstk08891Im4e7N8fMVJNDgP"

6. Do not forget to update the batch checklist from the same drive folder. Write how manyt videos failed from the 50 videos. "https://docs.google.com/document/d/1NzY2jaS4QrsPGLLmiQOc2ZNXW3e2xQnQZFqQf_IswMw/edit" 

7. To repeat the process, delete all the files inside meta_info, and copy paste the new batch. 


~~4. Make sure you modify `VIDEO_NUM` in `config.py`.~~

## Note

This tool is specifically tailored for the VFHQ dataset and require modifications to work with other datasets or video sources.
