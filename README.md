# Ash's Gasket Maker
<a href="#"><img src="https://github.com/user-attachments/assets/8c8c5e89-3dd9-4fc4-83de-7829e9a5a903" /></a>


## Description
Ash's Gasket Maker is a simple, user-friendly application designed to create DXF files for custom gaskets. It allows users to specify the dimensions of a gasket, including the outer and inner diameters, as well as bolt hole patterns. This tool is perfect for engineers, makers, and DIY enthusiasts who need to quickly design custom gaskets for various projects.

## Features
- Create circular gaskets with customizable dimensions
- Specify bolt hole patterns with adjustable Pitch Circle Diameter (PCD)
- Generate DXF files compatible with CAD software
- Simple graphical user interface
- Available as both a Python script and a standalone Windows executable

## Requirements
For running the Python script:
- Python 3.x
- tkinter (usually comes pre-installed with Python)
- ezdxf library

For running the executable:
- Windows operating system

## Installation

### Option 1: Running the Executable (Windows only)
1. Download the `GasketMaker.exe` file from the [GitHub releases page](https://github.com/Booth-Ashley/Ashs-Gasket-Maker/releases).
2. Double-click the downloaded file to run the application.

### Option 2: Running the Python Script
1. Ensure you have Python 3.x installed on your system.
2. Install the required ezdxf library using pip:
   ```
   pip install ezdxf
   ```
3. Download the `gasketmaker.py` file from the GitHub repository.

## Usage
1. If using the executable, simply double-click `GasketMaker.exe`.
   If using the Python script, run it by executing:
   ```
   python gasketmaker.py
   ```
2. The Gasket Maker window will appear with input fields for:
   - Outside Diameter
   - Inside Diameter
   - PCD (Pitch Circle Diameter)
   - Number of Holes
   - Hole Diameter

3. Enter the desired measurements for your gasket. All dimensions should be in the same unit (e.g., millimeters).

4. Click the "Create Gasket" button.

5. Choose a location to save your DXF file when prompted.

6. The application will generate a DXF file with your specified gasket design.

## Notes
- Ensure that the Outside Diameter is always larger than the Inside Diameter.
- The PCD should be between the Inside and Outside Diameters.
- The Number of Holes must be a positive integer.
- The Hole Diameter should be appropriate for your application and not too large relative to the gasket size.

## Troubleshooting
- If you're using the Python script and encounter an error about the ezdxf library not being found, ensure you've installed it correctly using pip.
- For the executable version, ensure you have the necessary Visual C++ redistributables installed. These are usually already present on most Windows systems.
- If the application doesn't start, try running it as an administrator.

## Version History
- V1.01: Added support for bolt hole patterns and standalone executable
- V1.00: Initial release with basic gasket creation

## License
[MIT License](https://github.com/Booth-Ashley/Ashs-Gasket-Maker/blob/main/LICENSE)

## Author
[Ashley Booth](https://github.com/Booth-Ashley)

## Acknowledgments
- ezdxf library developers
- All contributors and users of Ash's Gasket Maker
