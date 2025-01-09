import cv2  # Import OpenCV library

# Read the image
image = cv2.imread('assignment-001-given.jpg')

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (260, 190), bottom-right (985, 925)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 8 pixels
cv2.rectangle(image, (260, 190), (985, 925), (0, 255, 0), 8)

# Add a transparent black shadow behind the text
cv2.addWeighted(cv2.rectangle(image.copy(), (800, 85), (1230, 175), (0, 0, 0), -1), 0.5, image, 1 - 0.5, 0, dst=image)

# Adding text
cv2.putText(image, 'RAH972U', (800, 160), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)

# Display the image in a new window named 'Image'
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the resulting image to a new file
cv2.imwrite('assignment-001-my-result.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()
