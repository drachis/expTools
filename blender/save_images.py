import bpy
def findImages():
    images = []
    for obj in bpy.data.images: 
        images.append(obj.name)
        print ("found an image", obj.name)
    return images
def saveImage():
    return None
if __name__ == "__main__":
    assert(saveImage() == None)
    findImages()