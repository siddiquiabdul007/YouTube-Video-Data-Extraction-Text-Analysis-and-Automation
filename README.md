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


# How to Use the Combined YouTube Video Analysis Script
This combined script integrates YouTube video data extraction, advanced text analysis, and automation for a comprehensive analysis of video content and comments. Follow these detailed steps to utilize the script effectively:

# Prerequisites:
API Key Setup:

Obtain a valid YouTube Data API key from the Google Cloud Console.
Replace 'YOUR_API_KEY' in the script with the acquired API key.
Library Installation:

Ensure you have the necessary Python libraries installed. Run the following command to install them:
bash
Copy code
pip install pandas nltk matplotlib numpy textblob youtube_transcript_api
Script Execution:
Run the Script:

Open your terminal or command prompt.
Navigate to the directory containing the script using the cd command.
Execute the script by running the following command:
bash
Copy code
python script_name.py
Replace script_name.py with the actual filename of your script.
Enter YouTube Video Link:

The script will prompt you to enter the YouTube video link.
Input the link and press Enter.
YouTube Video Data Extraction:

The script will utilize the YouTube Data API to extract information about the video, including likes count, comments count, and the complete list of comments.
Detailed information about the video will be displayed in the console.
Text Analysis:

The script will proceed to perform advanced text analysis on both the video transcript and comments.
Metrics such as word frequency distribution, average sentence length, percentage of complex words, Fog index, sentiment analysis, and more will be presented in the console.
Data Export:

Comprehensive analysis results for both the transcript and comments will be exported to Excel files.
Find the exported Excel files named transcript_analysis_results.xlsx and comments_analysis_results.xlsx in the script's directory.
Visualization:

Bar charts showcasing mean values of numeric metrics for both transcript and comments will be displayed in the console.
Sentiment analysis results will be visualized using both bar and pie charts.
Automation (Optional):
Automated Execution:

The script includes an automation section that executes two separate scripts (combined.py and text-analysis.py) using the subprocess module.
To automate the execution of these scripts, ensure that the subprocess section is uncommented in the script.
Run the Automation Section:

After uncommenting the subprocess section, execute the script again.
The script will now automatically run the two specified scripts using the Python interpreter.
Customization:
Customizing the Script:
The script is designed for customization. You can modify and extend it based on your specific analysis requirements or integrate additional functionalities.
Note:
Ensure your system has internet access to fetch data from YouTube and the necessary permissions to execute scripts.

# Libraries: Install the required libraries using pip install pandas nltk matplotlib numpy textblob youtube_transcript_api.
Usage:
bash
Copy code
python script_name.py
Note:
This script assumes the existence of two separate scripts (combined.py and text-analysis.py) for automation. Ensure the correct filenames are used.
Further customization and extension of the script are encouraged based on individual analysis needs.
