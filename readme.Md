````markdown
# StreamLit Blog

Welcome to the StreamLit Blog project! This application allows users to create and manage blog posts with image headers using Streamlit, Firebase Storage, and Firestore.

## Features

- **Blog Creation**: Users can create new blog posts with a title, content, and an image header.
- **Image Upload**: Image headers are uploaded to Firebase Storage and linked to the blog post.
- **Authentication**: Email and Password Sign-In is integrated for user authentication.
- **Data Storage**: Blog data is stored in Firestore.

## Technologies Used

- **Streamlit**: For building the interactive web app.
- **Firebase**: For image storage and Firestore database.
- **Google Sign-In**: For user authentication.

## Getting Started

To get started with the StreamLit Blog project, follow these steps:

### Prerequisites

- Python 3.9 or higher
- Streamlit
- Firebase account with configured Storage, Firestore and Auth

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Suramyavns/StreamLit-Blog.git
   cd StreamLit-Blog
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Firebase:

   - Go to the Firebase Console and create a new project.
   - Set up Firebase Storage and Firestore.
   - Obtain your Firebase configuration details and place them in a file named `blogsite-firebase-config.json` in the `config/` directory of the project.
   - Set API key and storage bucket URL (without `gc://`) in `config/general.json`

### Running the App

To run the Streamlit app, use the following command:

```bash
python -m streamlit run main.py
```

### Usage

1. **Sign In**: Use Email and Password Sign-In to authenticate.
2. **Create a Blog Post**: Enter the blog title, content, and upload an image for the header.
3. **View Posts**: Published posts will appear in the home page with their respective header images.
4. **Create a Task**: Enter task name and date.
5. **View tasks**: Saved tasks will appear in the tasks page.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## Contact

For any inquiries, please contact Suramya Didwania at [sdidwania645@gmail.com](mailto:sdidwania645@gmail.com).

---

Feel free to customize the `README.md` further based on specific details or instructions related to your project!

```

You can adjust the email address and other specific details as needed.
```
````
