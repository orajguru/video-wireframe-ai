from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from scenedetect.scene_manager import save_images
import os

def detect_scenes(video_path):

    os.makedirs("outputs/frames", exist_ok=True)

    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()

    scene_manager.add_detector(ContentDetector(threshold=30))

    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)

    scenes = scene_manager.get_scene_list()

    save_images(
        scenes,
        video_manager,
        num_images=1,
        output_dir="outputs/frames"
    )

    return scenes