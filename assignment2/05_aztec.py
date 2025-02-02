import cv2
import numpy as np
import os
import subprocess

# Required JAR files for ZXing
javase_jar = "javase-3.5.0.jar"
core_jar = "core-3.5.0.jar"
jcommander_jar = "jcommander-1.82.jar"
aztec_image = "aztec.png"  # Replace with your actual image path

# Validate required files
for file in [javase_jar, core_jar, jcommander_jar, aztec_image]:
    if not os.path.exists(file):
        print(f"Error: {file} not found!")
        exit(1)

# Java command to decode the Aztec barcode
java_command = [
    "java", "-cp",
    f"{javase_jar};{core_jar};{jcommander_jar}",  # Use `:` instead of `;` on Linux/macOS
    "com.google.zxing.client.j2se.CommandLineRunner",
    aztec_image
]

# Run Java ZXing barcode decoding
try:
    result = subprocess.run(java_command, capture_output=True, text=True, check=True)
    output = result.stdout.strip()
    print("\n=== ZXing Decoding Output ===")
    print(output)
except subprocess.CalledProcessError as e:
    print("Error running ZXing:", e)
    exit(1)

# Load the image with OpenCV
image = cv2.imread(aztec_image)

# Extract result points (coordinates of detected barcode)
points = []
for line in output.split("\n"):
    if "Point" in line:
        parts = line.split(": ")[1].strip("()").split(",")
        x, y = float(parts[0]), float(parts[1])
        points.append((int(x), int(y)))

# Draw the detected barcode bounding box
if len(points) == 4:
    points_array = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
    cv2.polylines(image, [points_array], isClosed=True, color=(0, 255, 0), thickness=2)
    # Annotate the image with the decoded text
    x, y = points[0]  # Take the first point as reference
    decoded_text = output.split("Parsed result:")[1].split("\n")[0].strip() if "Parsed result:" in output else "Unknown"
    cv2.putText(image, decoded_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Display the annotated image
cv2.imshow("Aztec Code with Annotation", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the annotated image
output_file = "decoded_aztec.png"
cv2.imwrite(output_file, image)
print(f"\nAnnotated image saved as {output_file}")
