# Aptitude Test Application

A Python-based desktop application for practicing aptitude questions across various categories.

## Features

- Multiple aptitude categories:
  - Ratio and Proportion
  - Average
  - Profit and Loss
  - Time and Work
  - Reasoning Skills
- Timed tests with a 5-minute countdown
- Random question selection from a large question pool
- Score tracking and immediate feedback
- Simple and intuitive user interface

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/Aptitude_test.git
cd Aptitude_test
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
python aptitude.py
```

## How to Use

1. Launch the application by running `aptitude.py`
2. Select a topic from the dropdown menu
3. Click "Start" to begin the test
4. Answer the questions by selecting the appropriate option
5. Submit your answers before the timer runs out
6. View your score and correct answers

## Project Structure

- `aptitude.py`: Main application file containing the UI and game logic
- `questions.json`: Database of questions organized by category
- `requirements.txt`: List of Python dependencies

## Requirements

- Python 3.6+
- Tkinter (included in standard Python installation)
- Pandas

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request