from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Input video files
input_video_paths = [
    r"C:\Users\Mohammad\Desktop\My_Folder\vid_one.mp4",
    r"C:\Users\Mohammad\Desktop\My_Folder\vid_two.mp4",
    r"C:\Users\Mohammad\Desktop\My_Folder\vid_three.mp4",
    r"C:\Users\Mohammad\Desktop\My_Folder\vid_four.mp4",
    r"C:\Users\Mohammad\Desktop\My_Folder\vid_five.mp4"
]

# Output directory for the concatenated video
output_directory = r"C:\Users\Mohammad\OutputFolder"
os.makedirs(output_directory, exist_ok=True)

# List of video clips
video_clips = [VideoFileClip(path) for path in input_video_paths]

# Concatenate the video clips
final_clip = concatenate_videoclips(video_clips, method="compose")

# Export the final concatenated video
output_file_path = os.path.join(output_directory, "output.mp4")
final_clip.write_videofile(output_file_path, codec="libx264", fps=24)
