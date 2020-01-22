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


if __name__ == '__main__':

    fileName = input("Enter the PDF file name: ")
    if (os.path.exists("ticket_pdf/" + fileName + ".pdf")):
        extractImage(fileName)
    else:
        print("this file does not exist")

    # for page in file:
    #     for image in page.getImageList():
    #         # print(image)
    #         pic = fitz.Pixmap(file, image[0])
    #         finalpic = fitz.Pixmap(fitz.csRGB, pic)
    #         finalpic.writePNG("page-" + str(page.number) + ".png")
