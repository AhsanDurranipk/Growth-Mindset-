import streamlit as st;

st.set_page_config(page_title = "My webPage" , page_icon= ":tada:", layout= "wide");

# Header
st.title("Welcome to Ahsan Durrani Quotes Collection");
st.subheader("A page packed with powerful and inspiring thoughts.");
st.write("One thought can change your entire day—let it be a powerful one!")

#section
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with  left_column:
        st.subheader("Elevate Your Mind, Unlock Your True Potential!")
        st.write("A space where real motivation turns dreams into action, pushing you to achieve more every day.")
        st.write("######")
        st.subheader("Step into a world of powerful inspiration—where action begins with belief!")
        st.write(""" Life is a tough journey filled with ups and downs, but the right mindset can turn any challenge into an opportunity. Here, every word is crafted to boost your confidence, fuel your ambition, and spark your inner strength. Whether you're aiming higher, fighting self-doubt, or chasing your goals, this page is your daily boost of positive energy.
Let these words fuel your passion, strengthen your mindset, and remind you that true greatness comes from within.
Believe in yourself, embrace your journey, and transform motivation into unstoppable success! """)
        st.write("[learn more] (https://www.instagram.com/ahsan_durani_pk/)")
        st.write("[Instagram] (https://www.instagram.com/ahsan_durani_pk/#)")
        st.write("####")
        st.text("""Thank you for visiting!
        May you leave with a stronger spirit and a mind ready to conquer everything ahead.
Keep pushing, keep shining, and always remember — greatness starts with the first step! 🚀✨""")
        
