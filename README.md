# Shadow Hunters -- Making a Physical Copy

This project includes ``zip_to_pdf.py``, which was was developed with OpenAI's 01 mini model in the following chats:
```
https://chatgpt.com/share/6770452c-b3c4-800c-9048-301343ac6672
```

```
https://chatgpt.com/share/677044fb-50f4-800c-a7e6-47434ffca45c
```
The ``README.md`` was, in part, developed in the second chat listed above to explain ``zip_to_pdf.py``.

This project is a summary of my work in producing a physical copy of Shadow Hunters. The project relies heavily on [PlayDohBear's](https://steamcommunity.com/id/PlayDohBear) work to make the delisted Shadow Hunters game available in Steam and the Steam Community's effort to make a physical copy. 



## Method
The following method produces 5 copies of the game:
1. Buy the following:
- 1 copy of 6 different colors 100-pack of cards. I used [this item](https://www.amazon.com/dp/B0CBSB6KH4?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)
- 800+ blank cards like [these](https://www.amazon.com/dp/B0BT4ZY2YB?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1) (just because they are the cheapest; if you have other cards near *standard card size*, you will be fine)
- (Optional but reccomended) Buy 10 Deck Boxes, 2 for each set. I like [Ultra Pro](https://www.amazon.com/Ultra-Pro-Orange-Purple-Yellow/dp/B00EABSFRA/ref=sr_1_6?crid=16ENGB5Q1GXDQ&dib=eyJ2IjoiMSJ9.VEOorMLrbrd2-BlLRcIOnbSOQDxpxODpcl1EYbSNdI7AwBHPM5_mayuf1hupMw4Hh-xCg7cSq-n6ET280aoWC4YBTWGt-DpQ8nhkq3iCXybqrDxBAj1ZJKeu7KS2VsWY4pKQOpX05tj089lngVSGRRfRD_DG0RflOXwRcbSIbRzCM8mwFj6QDlyVwzI29E9rNwh3aDm8oq2VBSYY4Neieid_I95rsKyPSLXHnJsimrpvs-ebpjFKt2q46dth75yhbJsHMi1rhoOWC7h2YeojutPE8nQzhp8xylWvKbTRGyRBsTyMQ1IM4e5Hh9m-TgxhRQwSHaaC5_HshEqszRLXvr3pPt2oH-7KGlgpNxWRmt5R7v6IIg3b4X6MByCK-HoT6JE6lY_dqrXUIBcTzakheMKOp2gsXDzqsPVBYTiYdZO9OqqcQ1ssoexLEgIytQC0.ezwZFJlQM5S2w7QvXDqoHSnsJUSuFF7zY8FC6Ir4i4o&dib_tag=se&keywords=yugioh+deck+box&qid=1735423807&sprefix=yugioh+deck+bo%2Caps%2C243&sr=8-6) for the price. *The first box will hold Base+Expansion Official Cards, sleeved. The second will hold other cards (paper version) created by the Steam Community.*
2. Print the board (found on [the Steam Discussion link](https://steamcommunity.com/workshop/filedetails/discussion/2207510807/4625714282762283403/) on thick, 12x18 paper at your local printer shop. The board itself is 11x16, but will shrink somewhat when printed on 11x17). 
3. Create a pdf of all the cards using ``zip_to_pdf.py``, using ``Shadow Hunters_all_cards.zip`` as the source for the pictures. Make sure to set the ``--duplicate`` flag to ``5``. Modify as desired.
4. Have the pdf printed and cut. *I reccomend something slightly thicker than regular copy paper, due to image quality. Your local printer shop should have a good reccomendation. They may even have a machine that can cut hundreds of pages at once with efficiency*. If there is a little bit of whitespace on the borders, that is fine; they will be in front of a blank card anyway. 
5. Sleeve all the blank cards as follows (per set):
- 20 gold sleeves
- 16 black sleeves
- 16 green sleeves
- 16 white sleeves
- 6 sleeves -- choose unused color. *The official game has a red backing for area cards*.
6. Sleeve the black, green, and white cards appropriately. 
7. Sleeve the 6 Area cards (per set) in the appropriate sleeves.
8. Sleeve the character cards that will be used for your current game. For the base game, use the 20 official characters given in the original games. *Their names can be found in the official rulebook*.
6. (Optional) Add chipboard as explained [here](https://www.dickblick.com/products/all-purpose-chipboard/) (Which I got from [this other site](https://boardgamegeek.com/thread/775946/what-kind-of-chip-board-do-you-use))

For me, costs were more or less as follows:

|Item| Method of Aquiring | Cost |
|---|----|----|
|Sleeves| Amazon | $15|
|800 blank Cards| Amazon| $28 |
| Player Pieces (12 colors) | personal 3D printer| $10|
| Printed Game Board | Print Store | $1.30|
| Print and cut cards | Print Store | $65 |

Total: $119.30


# Zip to PDF Converter (`zip_to_pdf.py`)

A Python script that extracts images from a ZIP archive and arranges them into a neatly formatted PDF. Customize the layout by specifying page size, orientation, margins, image duplication, and spacing between images.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Advanced Options](#advanced-options)
  - [Examples](#examples)
- [Command-Line Arguments](#command-line-arguments)
- [Notes](#notes)
- [Troubleshooting](#troubleshooting)
- [Shadow Hunters](#Shadowhunters)
- [License](#license)

## Features

- **Extract Images from ZIP**: Automatically extracts all supported image formats from a ZIP file.
- **Customizable PDF Layout**:
  - **Page Size**: Choose between LETTER and A4.
  - **Orientation**: Select portrait or landscape.
  - **Margins**: Define custom margins in inches.
  - **Spacing**: Set horizontal and vertical spacing between images.
- **Image Duplication**: Duplicate the entire set of images a specified number of times.
- **Supported Image Formats**: PNG, JPG, JPEG, BMP, GIF, TIFF.
- **Automatic Page Management**: Efficiently handles pagination based on the number of images and layout settings.

## Installation

### Prerequisites

- **Python 3.6 or higher**

### Clone the Repository

```bash
git clone https://github.com/FredJones4/Shadow-Hunters-Physical-Copy.git
cd zip_to_pdf
```

### Install Dependencies

Ensure you have `pip` installed. Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

*If you don't have a `requirements.txt`, you can install the dependencies directly:*

```bash
pip install Pillow reportlab
```

## Usage

The script is executed via the command line. Below are the instructions for using `zip_to_pdf.py`.

### Basic Usage

Convert a ZIP file containing images to a PDF with default settings.

```bash
python zip_to_pdf.py path_to_images.zip output.pdf
```

Note that any pdf name can be used in place of ``output.pdf``. If such a pdf does not exist, the program will create one for you.

### Advanced Options

Customize the PDF layout by specifying additional arguments. For example:

```bash
python zip_to_pdf.py path_to_images.zip output.pdf --page-size A4 --orientation landscape --margin 1 --duplicate 2 --hspace 0.2 --vspace 0.3
```

### Examples

1. **Basic Conversion Without Duplication or Spacing**

    ```bash
    python zip_to_pdf.py images.zip output.pdf
    ```

    - **Description**: Converts `images.zip` to `output.pdf` using default settings (LETTER size, portrait orientation, 0.1-inch margins, no duplication, no spacing).

2. **Specify Page Size and Orientation**

    ```bash
    python zip_to_pdf.py images.zip output.pdf --page-size A4 --orientation landscape
    ```

    - **Description**: Uses A4 page size with landscape orientation.

3. **Set Custom Margins**

    ```bash
    python zip_to_pdf.py images.zip output.pdf --margin 1
    ```

    - **Description**: Sets 1-inch margins on all sides.

4. **Duplicate Images Multiple Times**

    ```bash
    python zip_to_pdf.py images.zip output.pdf --duplicate 3
    ```

    - **Description**: Duplicates the image set three times, resulting in three copies of each image in the PDF.

5. **Add Spacing Between Images**

    ```bash
    python zip_to_pdf.py images.zip output.pdf --hspace 0.2 --vspace 0.3
    ```

    - **Description**: Adds 0.2 inches of horizontal spacing and 0.3 inches of vertical spacing between images.

6. **Combined Example**

    ```bash
    python zip_to_pdf.py images.zip output.pdf --page-size A4 --orientation landscape --margin 1 --duplicate 2 --hspace 0.2 --vspace 0.3
    ```

    - **Description**: Extracts images from `images.zip`, duplicates the set twice (resulting in 2x the original number of images), and arranges them on an A4 landscape-oriented PDF with 1-inch margins, 0.2 inches horizontal spacing, and 0.3 inches vertical spacing.

## Command-Line Arguments

| Argument        | Type   | Default | Description                                                            |
|-----------------|--------|---------|------------------------------------------------------------------------|
| `zip_path`      | `str`  | N/A     | **(Positional)** Path to the ZIP file containing images.              |
| `output_pdf`    | `str`  | N/A     | **(Positional)** Path for the output PDF file.                        |
| `--page-size`   | `str`  | `LETTER`| Page size for the PDF. Choices: `LETTER`, `A4`.                        |
| `--orientation` | `str`  | `portrait`| Page orientation for the PDF. Choices: `portrait`, `landscape`.    |
| `--margin`      | `float`| `0.1`   | Margin size in inches. Applies to all sides.                           |
| `--duplicate`   | `int`  | `1`     | Number of times to duplicate the entire set of images. Must be ≥1.     |
| `--hspace`      | `float`| `0.0`   | Horizontal spacing between images in inches. Must be ≥0.              |
| `--vspace`      | `float`| `0.0`   | Vertical spacing between images in inches. Must be ≥0.                |

### Argument Details

- **Positional Arguments**:
  - `zip_path`: The path to the ZIP archive containing the images you want to convert.
  - `output_pdf`: The desired path and filename for the resulting PDF.

- **Optional Arguments**:
  - `--page-size`: Define the size of the PDF pages. Defaults to `LETTER`. Choose `A4` for A4 size.
  - `--orientation`: Set the orientation of the PDF pages. Defaults to `portrait`. Choose `landscape` for horizontal layout.
  - `--margin`: Set the margin size in inches around the edges of each PDF page. Defaults to `0.1` inches.
  - `--duplicate`: Specify how many times the entire set of images should be duplicated in the PDF. Defaults to `1` (no duplication).
  - `--hspace`: Define horizontal spacing between images in inches. Defaults to `0.0` inches (no spacing).
  - `--vspace`: Define vertical spacing between images in inches. Defaults to `0.0` inches (no spacing).

## Notes

- **Supported Image Formats**: Ensure that your images are in one of the supported formats (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.tiff`).

- **Image Dimensions**: Each image is placed within a card of size 2.5 x 3.5 inches. The script maintains the aspect ratio of images and centers them within their designated space.

- **Spacing and Margins**: Increasing margins or spacing reduces the number of images that fit on a single page. Adjust these parameters based on your layout requirements.

- **Duplication**: Duplicating images can significantly increase the size of the resulting PDF, especially with high duplication counts and large image sets.

- **Performance**: For large ZIP files or high duplication counts, the script may take longer to execute and consume more memory.

## Troubleshooting

- **No Images Found in ZIP**:
  - **Issue**: The script outputs "No images found in the ZIP archive."
  - **Solution**: Ensure that the ZIP file contains images in supported formats and that there are no nested directories without images.

- **Invalid Spacing or Margin Values**:
  - **Issue**: Errors related to spacing or margins being too large.
  - **Solution**: Reduce the values for `--margin`, `--hspace`, or `--vspace` to ensure that images fit within the page.

- **Permission Errors**:
  - **Issue**: Unable to write the output PDF to the specified location.
  - **Solution**: Check write permissions for the target directory or choose a different output path.

- **Missing Dependencies**:
  - **Issue**: Errors indicating missing Python packages.
  - **Solution**: Ensure all dependencies are installed using `pip install Pillow reportlab`.

- **Corrupted Images**:
  - **Issue**: Some images may not render correctly in the PDF.
  - **Solution**: Verify that all images in the ZIP are not corrupted and are in supported formats.

## Shadowhunters

This project was developed to print out Cards for a homemade version of the retired Shadow Hunters game.

### Files

See my [Makerworld project](https://makerworld.com/en/models/901456?from=search#profileId-860558) or my [Thingiverse design](https://www.thingiverse.com/thing:6734564/files) to 3D print player pieces.

See [this G Drive link](https://drive.google.com/drive/u/4/folders/1a0_KpipPKnEo6Q8o4ssfza_WFMk2TycM) for other related files (credit given below). The files that are others' contributions can also be found at the [SH Steam Discussion](https://steamcommunity.com/sharedfiles/filedetails/comments/2207510807).

Files' purposes and sources are as follows:
|Name   |Source | Purpose   |
|-------|-------|-----------|
|Shadow Hunters_all_cards.zip|---|Compilation of all the files in the other zip folders for ease of use|
|Shadow Hunters Area (Front).zip|[PlayDohBear](https://steamcommunity.com/id/PlayDohBear) in [SH Steam Discussion 1](https://steamcommunity.com/workshop/filedetails/discussion/2207510807/4625714282762283403/)|Store location cards for areas visited|
|Shadow Hunters modesty_cards.zip|Self|  Clothed versions of certain shirtless female characters, using Smemple's card template|
|ShadowHunters_CustomCard_Template.psd|[Smemple](https://steamcommunity.com/id/RyGuySuprFly) on [SH Steam Discussion](https://steamcommunity.com/sharedfiles/filedetails/comments/2207510807) |Create custom cards, using project's subdirectories as described in the project's README|
|rules_reminder.pdf|[SH Steam Discussion 1](https://steamcommunity.com/workshop/filedetails/discussion/2207510807/4625714282762283403/)|*Not a complete list of rules.* This is a reminder of turn order and a list of the basic characters' abilities. See full rules [here](https://images.zmangames.com/filer_public/64/5b/645bebeb-6bef-4d62-8d92-b9ca65450e85/shadow-hunter-rules.pdf)|
|altering_cards_workspace.zip|Self|*Do not use as path for ``zip_to_pdf.py``.* This is a Powerpoint file with relevant images for altering Base and Expansion cards. |

[PlaydohBear's]() board scan is found [here](https://drive.google.com/file/d/1Qee6-ESGvd9Tyj6BGke9neGaUTaX-d_4/view), which can also be found at his [Steam Community link](https://drive.google.com/file/d/1Qee6-ESGvd9Tyj6BGke9neGaUTaX-d_4/view): 

NOTE: for whichever characters being played, it is a good idea to keep a list of what the characters do for all players to see. It may be helpful to compile a pdf with ``zip_to_pdf.py`` with the current folders of characters that could have been included, for that specific round.



## License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

*Feel free to contribute, report issues, or suggest improvements by opening an issue or a pull request on the [GitHub repository](https://github.com/FredJones4/Shadow-Hunters-Physical-Copy.git).*