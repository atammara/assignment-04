import qrcode
import cv2
import numpy as np
from PIL import Image
import os

def generate_qr(data, filename='qrcode.png', fill_color='black', back_color='white', size=10):
    """Generate QR code"""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"QR code saved as {filename}")
        img.show()
        return True
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return False

def read_qr(filename):
    """Read QR code using OpenCV"""
    try:
        if not os.path.exists(filename):
            print("File not found!")
            return None
            
        img = cv2.imread(filename)
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(img)
        return data if data else None
    except Exception as e:
        print(f"Error reading QR code: {e}")
        return None

def scan_qr_from_webcam():
    """Scan QR code using webcam"""
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    print("Press 'q' to quit scanning...")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break
            
        data, vertices, _ = detector.detectAndDecode(frame)
        
        if vertices is not None:
            data = data if data else "No data"
            print(f"Decoded: {data}")
            pts = vertices[0].astype(np.int32)
            cv2.polylines(frame, [pts], True, (0,255,0), 2)
        
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main_menu():
    """Main menu interface"""
    while True:
        print("\nQR Code Encoder/Decoder")
        print("1. Generate QR Code")
        print("2. Read QR Code from Image")
        print("3. Scan QR Code with Webcam")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            data = input("Enter text or URL to encode: ").strip()
            if not data:
                print("Input cannot be empty!")
                continue
                
            filename = input("Enter output filename [qrcode.png]: ").strip() or 'qrcode.png'
            generate_qr(data, filename)
            
        elif choice == '2':
            filename = input("Enter image filename: ").strip()
            result = read_qr(filename)
            if result:
                print("Decoded data:", result)
            else:
                print("No QR code found or could not decode")
                
        elif choice == '3':
            scan_qr_from_webcam()
            
        elif choice == '4':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please enter 1-4")

if __name__ == "__main__":
    main_menu()