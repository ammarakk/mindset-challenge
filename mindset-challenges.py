import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import time

def load_animation(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def display_animation(image, duration=0.1):
    for frame in range(0, image.n_frames):
        image.seek(frame)
        st.image(image)
        time.sleep(duration)

animation_url = "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"
animation_image = load_animation(animation_url)
def main():
    st.set_page_config(page_title="Mastering Growth Mindset", layout="wide")
    
    # Sidebar Navigation
    st.sidebar.title("📌 Quick Access")
    page = st.sidebar.radio("Navigate", ["Home", "Core Principles", "Actionable Steps", "Success Stories", "Challenges & Goals"])
    
    # Hero Section
    
    st.title("🚀 Mastering a Growth Mindset for Success")
    st.subheader("Elevate Your Potential Through Continuous Learning & Resilience")
    
    if page == "Home":
        st.markdown("""
        ## What is a Growth Mindset?
        A **growth mindset** is the belief that intelligence and abilities are not fixed but can be developed with **dedication, perseverance, and learning**. 
        Coined by psychologist **Carol Dweck**, this approach fuels success by fostering adaptability and resilience.
        """)
    
    elif page == "Core Principles":
        st.markdown("""
        ## Core Principles of a Growth Mindset
        - 🌟 **Challenges Are Opportunities:** Face obstacles with curiosity and determination.
        - 📚 **Embrace Continuous Learning:** Every setback teaches something valuable.
        - 💪 **Persistence Leads to Mastery:** Success comes from sustained effort.
        - 🏆 **Effort Over Talent:** Hard work beats natural ability in the long run.
        - 🔄 **Adapt & Evolve:** Keep an open mind and refine strategies as needed.
        """)
    
    elif page == "Actionable Steps":
        st.markdown("""
        ## Practical Steps to Build a Growth Mindset
        - 🎯 **Set Learning-Based Goals:** Prioritize skill development over outcomes.
        - ✍ **Self-Reflection:** Regularly assess what worked and what can improve.
        - 🔍 **Seek Constructive Feedback:** Use criticism as a growth opportunity.
        - 🔥 **Maintain a Positive Mindset:** Believe in your ability to evolve and grow.
        - 🤝 **Surround Yourself with Growth-Oriented People:** Learn from those who inspire progress.
        """)
    
    elif page == "Success Stories":
        st.markdown("""
        ## Real-World Success Stories
        - **Elon Musk:** Embraced failures as stepping stones for SpaceX and Tesla.
        - **Oprah Winfrey:** Overcame adversity through relentless learning and adaptation.
        - **Michael Jordan:** Used setbacks to fuel determination and become an icon.
        - **J.K. Rowling:** Transformed rejection into one of the greatest literary successes.
        """)
    
    elif page == "Challenges & Goals":
        st.markdown("""
        ## Interactive Challenges & Goals
        - ✅ **Daily Challenge:** Write down one lesson learned from a recent mistake.
        - 🎯 **Weekly Goal:** Identify a skill you want to improve and make a plan.
        - 🔥 **Growth Challenge:** Step out of your comfort zone and document the experience.
        - 🏆 **Achievement Milestone:** Share your growth journey with someone and discuss insights.
        """)
        
        challenge = st.text_input("🔍 What growth mindset challenge will you take on today?")
        if st.button("Submit My Challenge"):
            st.success(f"Great choice! Stay committed to '{challenge}' and reflect on your progress.")
        
        st.markdown("---")
        st.markdown("## Reflect & Impact Activity")
        st.write("💡 After completing your challenge, take a moment to reflect on your experience.")
        
        reflection = st.text_area("✍ What did you learn from this challenge?")
        impact = st.text_area("🌟 How did this challenge impact your mindset and growth?")
        
        if st.button("Submit Reflection"):
            st.success("Reflection submitted! Keep practicing a growth mindset and continue evolving.")
    
    st.markdown("---")
    st.markdown("*Crafted with Excellence by Ammar Ahmed ✨*")

if __name__ == "__main__":
    main()
