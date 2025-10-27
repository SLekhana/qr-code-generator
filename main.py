import qrcode
import argparse
import os
from datetime import datetime

def generate_qr_code(url, output_dir='qr_codes'):
    """
    Generate a QR code for the given URL and save it to the output directory.
    
    Args:
        url (str): The URL to encode in the QR code
        output_dir (str): Directory to save the QR code image
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"qr_code_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)
    
    # Save the image
    img.save(filepath)
    
    # Log the operation
    log_message = f"[{datetime.now()}] QR Code generated for URL: {url} - Saved to: {filepath}"
    print(log_message)
    
    # Also save to log file
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'qr_generator.log')
    
    with open(log_file, 'a') as f:
        f.write(log_message + '\n')
    
    return filepath

def main():
    """Main function to parse arguments and generate QR code."""
    parser = argparse.ArgumentParser(description='Generate QR codes from URLs')
    parser.add_argument('--url', type=str, default='http://github.com/kaw393939',
                        help='URL to encode in QR code')
    parser.add_argument('--output', type=str, default='qr_codes',
                        help='Output directory for QR codes')
    
    args = parser.parse_args()
    
    print(f"Starting QR Code Generator...")
    print(f"Target URL: {args.url}")
    print(f"Output Directory: {args.output}")
    
    try:
        filepath = generate_qr_code(args.url, args.output)
        print(f"✓ Success! QR code saved to: {filepath}")
    except Exception as e:
        print(f"✗ Error generating QR code: {str(e)}")
        raise

if __name__ == "__main__":
    main()
