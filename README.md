# YouTube-Video-Data-Extraction-Text-Analysis-and-Automation
YouTube Video Data Extraction, Text Analysis, and Automation
YouTube Video Data Extraction, Text Analysis, and Automation
This Python script provides a comprehensive toolkit for in-depth analysis of YouTube video content and associated comments. The script seamlessly integrates multiple functionalities, combining YouTube Data API for video details retrieval, YouTube Transcript API for transcript extraction, advanced text analysis using NLTK and TextBlob, and automation capabilities through subprocess execution.

Key Features:
1. YouTube Video Data Extraction:
Utilizes the YouTube Data API to extract crucial information about the video, including likes count, comments count, and the full list of comments.
Employs a robust approach to handle pagination and retrieve all comments efficiently.
2. Text Analysis:
Tokenizes and preprocesses the video transcript and comments for detailed analysis.
Extracts a variety of metrics, including word frequency distribution, average sentence length, percentage of complex words, Fog index, sentiment analysis, and more.
Identifies the most common words in the text and performs sentiment analysis to gauge the overall sentiment.
3. Data Export and Visualization:
Exports the comprehensive analysis results for both transcript and comments to Excel files, facilitating further exploration and sharing of insights.
Visualizes key metrics through bar charts, providing a quick overview of the data distribution.
Presents sentiment analysis results using both bar and pie charts for a clear representation of sentiment distribution.
4. Automation:
Automates the execution of two separate scripts (combined.py and text-analysis.py) using the subprocess module, streamlining the analysis workflow.
Enables the user to perform YouTube video data extraction, text analysis, and automation with a single script execution.
How to Use:
API Key Setup:

Obtain a valid YouTube Data API key from the Google Cloud Console.
Replace 'YOUR_API_KEY' in the script with the acquired API key.
Script Execution:

Run the script and provide the YouTube video link when prompted.
Observe detailed video information, comments, and comprehensive text analysis results in the console.
Exploration and Sharing:

Explore visualizations and detailed results in the console.
Utilize the exported Excel files (transcript_analysis_results.xlsx and comments_analysis_results.xlsx) for in-depth analysis and sharing of insights.
Customization:

Customize and extend the script to accommodate specific analysis requirements or integrate additional functionalities.
Requirements:
Libraries: Install the required libraries using pip install pandas nltk matplotlib numpy textblob youtube_transcript_api.
Usage:
bash
Copy code
python script_name.py
Note:
This script assumes the existence of two separate scripts (combined.py and text-analysis.py) for automation. Ensure the correct filenames are used.
Further customization and extension of the script are encouraged based on individual analysis needs.
