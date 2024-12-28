import os
import zipfile
import tempfile
from PIL import Image
from reportlab.lib.pagesizes import LETTER, A4, landscape, portrait
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def extract_images_from_zip(zip_path, extract_to):
    """
    Extracts all files from the ZIP archive to the specified directory.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted ZIP contents to {extract_to}")

def get_image_files(directory):
    """
    Recursively retrieves all image file paths from the specified directory.
    """
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(supported_extensions):
                image_files.append(os.path.join(root, file))
    print(f"Found {len(image_files)} image(s).")
    return image_files

def create_pdf(image_paths, output_pdf, page_size=LETTER, orientation='portrait',
              margins=(0.5*inch, 0.5*inch), hspace=0.0, vspace=0.0):
    """
    Arranges images on a PDF, maintaining their physical size and specified spacing.

    :param image_paths: List of image file paths.
    :param output_pdf: Output PDF file path.
    :param page_size: Page size from reportlab.lib.pagesizes (e.g., LETTER, A4).
    :param orientation: 'portrait' or 'landscape'.
    :param margins: Tuple indicating (left/right, top/bottom) margins in points.
    :param hspace: Horizontal spacing between images in points.
    :param vspace: Vertical spacing between images in points.
    """
    # Adjust page size based on orientation
    if orientation.lower() == 'landscape':
        page_size = landscape(page_size)
    else:
        page_size = portrait(page_size)

    c = canvas.Canvas(output_pdf, pagesize=page_size)
    page_width, page_height = page_size
    margin_x, margin_y = margins

    # Card dimensions in inches
    card_width_in = 2.5
    card_height_in = 3.5

    # Convert inches to points (1 inch = 72 points)
    card_width = card_width_in * inch
    card_height = card_height_in * inch

    # Calculate available area
    available_width = page_width - 2 * margin_x
    available_height = page_height - 2 * margin_y

    # Calculate how many cards fit per row and column considering spacing
    if hspace < 0 or vspace < 0:
        raise ValueError("Spacing values must be non-negative.")

    # Prevent division by zero if spacing is very large
    try:
        cards_per_row = int((available_width + hspace) // (card_width + hspace))
        cards_per_col = int((available_height + vspace) // (card_height + vspace))
    except ZeroDivisionError:
        raise ValueError("Spacing cannot be set to zero when card dimensions are zero.")

    if cards_per_row == 0 or cards_per_col == 0:
        raise ValueError("Card size and spacing are too large for the page with the given margins.")

    print(f"Cards per row: {cards_per_row}, Cards per column: {cards_per_col}")
    print(f"Horizontal spacing: {hspace / inch} inches, Vertical spacing: {vspace / inch} inches")
    cards_per_page = cards_per_row * cards_per_col
    print(f"Cards per page: {cards_per_page}")

    current_page = 1
    for idx, img_path in enumerate(image_paths):
        if idx % cards_per_page == 0 and idx != 0:
            c.showPage()  # Start a new page
            current_page += 1
            print(f"Added page {current_page}")

        # Calculate position
        position = idx % cards_per_page
        row = position // cards_per_row
        col = position % cards_per_row

        x = margin_x + col * (card_width + hspace)
        y = page_height - margin_y - (row + 1) * card_height - row * vspace  # ReportLab's origin is at bottom-left

        # Open the image and ensure it has the correct size
        with Image.open(img_path) as img:
            img_width, img_height = img.size
            aspect = img_width / img_height
            desired_aspect = card_width_in / card_height_in

            # Optionally, handle aspect ratio differences here
            # For now, we'll preserve aspect ratio and center the image

            c.drawImage(
                img_path, 
                x, 
                y, 
                width=card_width, 
                height=card_height, 
                preserveAspectRatio=True, 
                anchor='c'
            )

    c.save()
    print(f"PDF saved as {output_pdf}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract images from a ZIP and arrange them on a PDF.")
    parser.add_argument('zip_path', help="Path to the ZIP file containing images.")
    parser.add_argument('output_pdf', help="Path for the output PDF file.")
    parser.add_argument('--page-size', choices=['LETTER', 'A4'], default='LETTER', help="Page size for the PDF.")
    parser.add_argument('--orientation', choices=['portrait', 'landscape'], default='portrait', help="Page orientation for the PDF.")
    parser.add_argument('--margin', type=float, default=0.1, help="Margin size in inches.")
    parser.add_argument('--duplicate', type=int, default=1, help="Number of times to duplicate the image set.")
    parser.add_argument('--hspace', type=float, default=0.0, help="Horizontal spacing between images in inches.")
    parser.add_argument('--vspace', type=float, default=0.0, help="Vertical spacing between images in inches.")
    args = parser.parse_args()

    # Validate duplication count
    if args.duplicate < 1:
        print("Duplication count must be at least 1.")
        return

    # Set page size
    if args.page_size == 'LETTER':
        page_size = LETTER
    elif args.page_size == 'A4':
        page_size = A4

    # Convert spacing from inches to points
    hspace_points = args.hspace * inch
    vspace_points = args.vspace * inch

    # Create a temporary directory to extract ZIP contents
    with tempfile.TemporaryDirectory() as tmpdirname:
        extract_images_from_zip(args.zip_path, tmpdirname)
        image_files = get_image_files(tmpdirname)
        if not image_files:
            print("No images found in the ZIP archive.")
            return
        
        # Duplicate the image list based on user input
        if args.duplicate > 1:
            original_count = len(image_files)
            image_files = image_files * args.duplicate
            print(f"Duplicated image set {args.duplicate} times. Total images: {len(image_files)} (Original: {original_count})")
        else:
            print("No duplication applied to image set.")

        create_pdf(
            image_paths=image_files,
            output_pdf=args.output_pdf,
            page_size=page_size,
            orientation=args.orientation,
            margins=(args.margin * inch, args.margin * inch),
            hspace=hspace_points,
            vspace=vspace_points
        )

if __name__ == "__main__":
    main()
