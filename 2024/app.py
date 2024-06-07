

import cv2

def main():
    # Load the image, we will work with the image in BGR format this time
    image_bgr = cv2.imread("dog.jpg", cv2.IMREAD_COLOR)

    image_with_rectangle = image_bgr.copy()

    # Defined color red using the RGB format
    color_red = (255, 0, 0)

    # Draw a rectangle on the image
    cv2.rectangle(image_with_rectangle, (218, 90), (404, 412), color_red, 2)

    # Add the lable "Dog" to the bounding box
    font_size = 0.7
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image_with_rectangle, "Dog", (218, 80), font, font_size, color_red, 2, cv2.LINE_AA)

    # Display the image in the window until any key is pressed
    cv2.imshow('Dog', image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
