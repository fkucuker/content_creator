# YouTube Playlist to Article Generator and WordPress Publisher

This project automates the process of downloading transcripts from YouTube videos in a playlist, generating articles from those transcripts using OpenAI's GPT-4, creating featured images using DALL·E 3, and publishing the articles to a WordPress site.

## Features

- Fetches video data from YouTube playlists using the YouTube Data API.
- Downloads video transcripts and saves them as text files.
- Generates articles from the transcripts using OpenAI's GPT-4.
- Creates featured images for the articles using OpenAI's DALL·E 3.
- Publishes the articles to a WordPress site automatically.

## Installation

1. **Requirements**: Python 3.8 or higher is required to run this project.

2. **Install Dependencies**:
   - Install the required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up API Keys**:
   - Create a `.env` file in the root directory of the project and add the following environment variables:
     ```plaintext
     YOUTUBE_API_KEY=your_youtube_api_key
     OPENAI_API_KEY=your_openai_api_key
     WORDPRESS_BASE_URL=https://your_wordpress_site_url
     WORDPRESS_USERNAME=your_wordpress_username
     WORDPRESS_PASSWORD=your_application_password
     ```
   - Replace the placeholders with your actual API keys and WordPress credentials.

4. **Prepare Playlist File**:
   - Add the URLs of the YouTube playlists you want to process in the `youtube_list.txt` file, with one URL per line.

## Usage

1. **Run the Project**:
   - Execute the project by running:
     ```bash
     python main.py
     ```

2. **Steps**:
   - The project will fetch video data from the playlists listed in `youtube_list.txt`.
   - It will download the transcripts of the videos and save them as text files.
   - Articles will be generated from the transcripts using OpenAI's GPT-4.
   - Featured images for the articles will be created using OpenAI's DALL·E 3.
   - The articles and images will be published to the specified WordPress site.

## Important Notice

This project uses transcripts from YouTube videos to generate content automatically. However, please be aware that videos on YouTube may be subject to copyright and intellectual property protections. Using this project to create and distribute content for commercial purposes may lead to copyright violations.

**User Responsibility**:
- It is your responsibility to ensure that the content generated using this project does not violate any copyright laws.
- Before using transcripts from YouTube videos, make sure to obtain the necessary permissions from the content owners.
- This project is intended for educational and personal use only. For commercial use, ensure that you have the appropriate legal permissions.

By using this project, you agree to the above terms and accept full responsibility for any legal issues that may arise.

## Contributing

This project is open-source, and contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or suggestions about the project, please open an issue or contact me at fakucuker.
