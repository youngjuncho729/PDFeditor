import fitz
import os
import shutil


def extractImage(fileName: str) -> None:
    file = fitz.open("ticket_pdf/" + fileName + ".pdf")
    pages = len(file)  # number of pages

    newDir = fileName + "_output"
    os.mkdir(newDir)

    for i in range(pages):
        image = file.getPageImageList(i)
        pic = fitz.Pixmap(file, image[1][0])
        name = "ticket-" + str(i + 1) + ".png"
        pic.writePNG(name)

        shutil.move(os.getcwd() + "/" + name,
                    os.getcwd() + "/" + newDir + "/" + name)


def extractText():
    pass


def insertImage() -> None:
    # the file to be inserted
    pdf_to_add = "blank.pdf"

    for i in range(1, 4):
        # the image to be insert
        image_to_add = "ticket-" + str(i) + ".png"

        # Set the size and coordinates of the image
        img = fitz.Rect(400, 400, 600, 600)

        # open the pdf file
        document = fitz.open(pdf_to_add)

        # choice the page
        page = document[0]
        page.insertImage(img, image_to_add)

        # new file with image added
        new_file = "added" + str(i) + ".pdf"
        document.save(new_file)

        document.close()


if __name__ == '__main__':

    # fileName = input("Enter the PDF file name: ")
    # if (os.path.exists("ticket_pdf/" + fileName + ".pdf")):
    #     extractImage(fileName)
    # else:
    #     print("this file does not exist")

    insertImage()
