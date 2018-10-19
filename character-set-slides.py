# Drawbot Character Set Slides

fonts = [{
        'title': 'ISO Regular',
        'fontPath': 'fonts/ISO-v0.4-Regular.otf'
    }, 
    {
        'title': 'ISO Bold',
        'fontPath': 'fonts/ISO-v0.4-Bold.otf'
    }
]
txtFontSize = 60
txtLineHeight = 66
numCols = 15
numRows = 14

bgColorR, bgColorG, bgColorB, bgColorA = 1,1,1,1
textColorR, textColorG, textColorB, textColorA = 0,0,0,1

docWidth, docHeight = 1200, 1200
topMargin, rightMargin, bottomMargin, leftMargin = 70, 50, 50, 50 

textBoxWidth = docWidth - leftMargin - rightMargin
textBoxHeight = docHeight - topMargin - bottomMargin

showTitle = False # enable if you'd like to display the title
titleFont = 'fonts/ISO-v0.4-Regular.otf'
titleFontSize = 18
titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA = 0,0,0,1
titleX, titleY = docWidth/2, docHeight - 50



def setup():
    newPage(docWidth, docHeight)
    fill(bgColorR, bgColorG, bgColorB, bgColorA)
    rect(0, 0, docWidth, docHeight)
    
def main():
    for f in fonts:        
        drawGlyphs(f)
    
def drawGlyphs(f):
    pNum = 1
    for glyphs in glyphGroups(f['fontPath']):
        drawPage(f, glyphs, pNum)
        pNum += 1
    
def glyphGroups(fontPath):
    font(fontPath)

    glyphs = listFontGlyphNames()
    glyphsPerPage = numCols * numRows
    glyphGroups = []
    for i in range(0, len(glyphs), glyphsPerPage):
        glyphGroups.append(glyphs[i : i+glyphsPerPage])
    
    return(glyphGroups)
    
def setupNewPage():
    newPage(docWidth, docHeight)
    fill(bgColorR, bgColorG, bgColorB, bgColorA)
    rect(0, 0, docWidth, docHeight)
    
    
def drawTitle(f):
    if showTitle:
        font(titleFont)
        fontSize(titleFontSize)
        fill(titleTextColorR, titleTextColorG, titleTextColorB, titleTextColorA)
        text(f['title'], (titleX, titleY), align='center')
    
def drawPage(f, glyphList, pNum):
    setupNewPage()
    drawTitle(f)

    txt = FormattedString()
    txt.font(f['fontPath'])
    txt.fontSize(txtFontSize)
    txt.lineHeight(txtLineHeight)
    txt.fill(textColorR,textColorG,textColorB,textColorA)
    
    tabList = []
    colWidth = textBoxWidth / (numCols)
    for col in range(numCols):
        xPos = (col * colWidth) + (colWidth * .5)
        tabList.append((xPos, "center"))
        
    txt.tabs(*tabList)
    
    txt.append('\t')
    col = 1
    for glyph in glyphList:
        txt.appendGlyph(glyph)
        if col == numCols:
            txt.append('\n\t')
            col = 1
        else:
            txt.append('\t')
            col += 1

    textBox(txt, (leftMargin, bottomMargin, textBoxWidth, textBoxHeight))
    fileName = "exports/{0}-{1}.png".format((f['title']), pNum).replace(' ', '-')
    saveImage(fileName)

main()



