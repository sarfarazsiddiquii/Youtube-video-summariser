import streamlit as st
from youtube_search import fetch_video_links
from video_info import get_video_id, get_video_title, get_transcript
from summariser import GeminiSummariser

def main():
    st.title('YouTube Video Summarizer')
    keyword = st.text_input('Enter a keyword to search on YouTube:', '')

    try:
        summarizer = GeminiSummariser()
    except ValueError as e:
        st.error(f"Error initializing the summarizer: {str(e)}")
        return  # Stop further execution if there is an error with the summarizer

    if st.button('Search'):
        if keyword:
            links = fetch_video_links(keyword)
            transcripts = []
            video_details = []
            if links:
                for link in links:
                    video_id = get_video_id(link)
                    title = get_video_title(link)
                    transcript = get_transcript(video_id)
                    if transcript:
                        transcripts.append(transcript)
                        video_details.append(f"Title: {title}, ID: {video_id}, Link: {link}")
                    else:
                        video_details.append(f"Title: {title} (No Transcript Available), ID: {video_id}, Link: {link}")
                
                # Concatenate all transcripts for a collective summary
                combined_transcript = " ".join(transcripts)
                if combined_transcript:
                    summary = summarizer.summarize_transcript(combined_transcript)
                    st.subheader("Aggregated Summary Based on Top 5 Videos:")
                    st.text_area("Summary", summary, height=300)
                else:
                    st.error("No transcripts available to summarize.")

                # Optionally display video details
                for detail in video_details:
                    st.write(detail)
            else:
                st.error('No videos found.')
        else:
            st.error('Please enter a keyword to search.')

if __name__ == '__main__':
    main()
