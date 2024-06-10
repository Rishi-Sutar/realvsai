import streamlit as st
from PIL import Image
from fastai.vision.all import *
import pathlib 

model_path = os.path.join('real_ai.pkl')

learn = load_learner(model_path)

# Function to check if image is AI-generated or real
def check_image(image):

    img = image.resize((460, 460))
    ans = learn.predict(img)
    return ans[0]

# Streamlit UI
def main():
    st.title("AI-Generated Image Detector")
    st.write("Upload an image to check if it's AI-generated or real")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = PILImage.create(uploaded_file)
        width, height = image.size
        
        # Check if the dimensions are smaller than the threshold
        if width < 100 or height < 100:
            st.write(f"Image Size is too small")
        else:
            st.image(image, caption='Uploaded Image.', use_column_width=True)
            st.write("")
            st.write("Classifying...")
            result = check_image(image)
            st.success(f"The uploaded image is: {result}")

if __name__ == '__main__':
    main()
