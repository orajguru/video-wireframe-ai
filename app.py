import streamlit as st
import os
import json
from scene_detector import detect_scenes
from wireframe_ai import analyze_ui
from figma_export import generate_figma_json

st.set_page_config(page_title="Video → Wireframe AI", layout="wide")

st.title("🎬 Video → Wireframe → Figma")
st.write("Upload a short product demo video and generate basic wireframes + Figma JSON.")

video = st.file_uploader("Upload product demo video", type=["mp4","mov","avi"])

if video:

    if video.size > 20000000:
        st.error("Please upload video smaller than 20MB")
        st.stop()

    with open("input_video.mp4","wb") as f:
        f.write(video.read())

    st.success("Video uploaded")

    if st.button("Generate Wireframes"):

        os.makedirs("outputs/frames", exist_ok=True)

        scenes = detect_scenes("input_video.mp4")

        st.write("Detected screens:", len(scenes))

        frame_dir = "outputs/frames"
        components = []

        for img in os.listdir(frame_dir):

            path = f"{frame_dir}/{img}"

            st.image(path, caption=img)

            with st.spinner("Analyzing UI..."):
                result = analyze_ui(path)

            st.markdown(result)
            components.append(result)

        figma_json = generate_figma_json(components)

        os.makedirs("outputs", exist_ok=True)
        with open("outputs/figma_wireframe.json","w") as f:
            json.dump(figma_json,f, indent=2)

        st.download_button(
            "Download Figma JSON",
            json.dumps(figma_json, indent=2),
            "wireframe_figma.json"
        )