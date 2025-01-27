# 📂 File Organizer

This tool helps you to automatically organize files and folders in your directory based on their type. It can move files into categorized subfolders, such as Documents, Images, Videos, Archives, and more. It also has the functionality to move existing folders to the correct category folders, detect duplicate files, and remove them if necessary.

## ✨ Features

✅ Automatically moves files to specific category folders (e.g., .pdf, .jpg, .mp4, etc.)
✅ Move existing folders to the correct category folders
✅ Detect duplicate files and remove them if necessary
✅ Optional: Move folders up
✅ Command-line interface: Use various commands to control the behavior of the tool.

## 📚 Requirements

- 🐍 Python 3.7 or higher
- 💻 Windows 10 or later
- 📦 Required Python libraries: os, shutil, hashlib, argparse, dotenv

## 📦 Installation

1. Clone the repository
2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up a `.env` file with the `DIRECTORY_PATH` environment variable to the path of the directory you want to organize.

    ```.env
    DIRECTORY_PATH=path/to/your/directory
    ```

## 🚀 Usage

The script can be executed from the command line using the following arguments:

### `--directory`

Path to the directory you want to organize. This argument is optional, and if not provided, the tool will use the DIRECTORY_PATH value from a .env file.

### `--move-folders`

This optional flag will move any existing folders like pdf, jpg, etc., into the respective category folder.

### `--file-types`

You can specify a custom list of file types to be organized. This list should be comma-separated (e.g., `.pdf`,`.jpg`,`.mp4`). If not specified, the default list will be used: `.pdf`, `.png`, `.jpg`, `.svg`, `.zip`, `.mp4`.

### `--find-duplicates`

This optional flag will find and remove duplicate files after the user specified the duplicates to be removed.

## 📂 Folder Structure

The script will create a folder structure like this:

The tool will organize your files into the following categories based on file types:

- 🖼️ Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`
- 📄 Documents: `.pdf`, `.docx`, `.txt`, `.csv`
- 🎥 Videos: `.mp4`, `.avi`, `.mkv`, `.mov`
- 📦 Archives: `.zip`, `.tar`, `.rar`
- 🗃️ Other: Any other file types not specified in the list

The tool also checks for existing folders like `pdf/`, `jpg/`, `video/`, and moves them into the appropriate category folder.

## 🔍 Duplicate File Detection

The tool uses the `SHA256` hashing algorithm to detect duplicate files in the user's directory. If duplicates are found, the user will be prompted with the option to delete them.

## 📝 Contributing

I welcome contributions to the `File Organizer` project. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch: `git checkout -b feature/my-new-feature`.
4. Make your changes and commit them: `git commit -am 'Add new feature'`.
5. Push your branch to your fork: `git push origin feature/my-new-feature`.
6. Open a pull request to merge your changes into the main repository.

Please ensure that your changes are properly tested and documented before creating a pull request.

## 📝 License

This project is open-sourced under the MIT License - see the LICENSE file for details.

## 🧑‍🤝‍🧑 Author

- [Lennard Geißler](https://github.com/lennardgeissler)
