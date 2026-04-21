from PIL import Image

numberOfSegments = 8

def sliceImage(imagePath, segments = numberOfSegments):
    image = Image.open(imagePath)
    width, height = image.size
    segmentWidth = width // segments
    slices = []
    for i in range(segments):
        left = i * segmentWidth
        if i < segments - 1:
            right = (i + 1) * segmentWidth
        else:
            right = width
        imageSlice = image.crop((left, 0, right, height))
        import io
        byteArray = io.BytesIO()
        imageSlice.save(byteArray, format = "JPEG")
        slices.append(byteArray.getvalue())
    return slices
