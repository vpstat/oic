"""Helper functions for the OIC Training Guide Streamlit app."""

import streamlit as st

def render_header(title, subtitle=None):
    """Render a styled header with optional subtitle."""
    st.markdown(f"# {title}")
    if subtitle:
        st.markdown(f"*{subtitle}*")
    st.markdown("---")

def render_key_points(points):
    """Render a list of key points with checkmark icons."""
    for point in points:
        st.markdown(f"✅ {point}")

def render_warning(message):
    """Render a warning box."""
    st.warning(f"⚠️ {message}")

def render_tip(message):
    """Render a tip box."""
    st.info(f"💡 **Tip:** {message}")

def render_best_practice(message):
    """Render a best practice box."""
    st.success(f"⭐ **Best Practice:** {message}")

def render_code_example(code, language="python", title=None):
    """Render a code example with optional title."""
    if title:
        st.markdown(f"**{title}**")
    st.code(code, language=language)

def render_exercise(title, description, steps):
    """Render a hands-on exercise."""
    with st.expander(f"🎯 Exercise: {title}"):
        st.markdown(description)
        st.markdown("**Steps:**")
        for i, step in enumerate(steps, 1):
            st.markdown(f"{i}. {step}")

def create_progress_tracker(completed_modules, total_modules=8):
    """Create a visual progress tracker."""
    progress = completed_modules / total_modules
    st.progress(progress)
    st.markdown(f"**Progress:** {completed_modules}/{total_modules} modules completed ({int(progress*100)}%)")

def render_video_reference(day, title, url):
    """Render a reference to the original training video."""
    st.markdown(f"📺 **Day {day}:** [{title}]({url})")

def render_module_info(module_num, title, duration, topics):
    """Render module information card."""
    st.markdown(f"## Module {module_num}: {title}")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.metric("Duration", duration)
    with col2:
        st.markdown("**Topics Covered:**")
        for topic in topics:
            st.markdown(f"• {topic}")
    st.markdown("---")
