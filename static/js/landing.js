
// cache the DOM
var header = document.getElementsByTagName('header')[0]
var body = document.getElementsByTagName('body')[0]
var contactLink = document.getElementsByClassName('more-info')[0] 

// page geometry
var styles, height, width, aspectRatio, vertCrop, bottomCrop, topCrop, trueHeight
var trueAspectRatio = 1.5
var bottomCropFactor = 0.4
var topCropFactor = 1 - bottomCropFactor

// resize contact link
var boxHeight, boxTop, topCollision
var boxTopPercent = 0.15
var contactLinkHeight = 40 // px

// resize title
var titleHeight, fontSize
var referenceHeight = 820 // px
var titleMaxTopOffset = 560 // px
var titleMinTopOffset = 250 // px
var trueTitleHeight = 310 // px

responsiveLayout()
window.onresize = responsiveLayout

function responsiveLayout() {
	styles = window.getComputedStyle(body)
	width = window.innerWidth
	height = window.innerHeight
	aspectRatio = width/height
	vertCrop = aspectRatio > trueAspectRatio
	horzCrop = aspectRatio < trueAspectRatio
	
	trueHeight = vertCrop ? width / trueAspectRatio : height
	
	// resize contact link
	bottomCrop = vertCrop ? (trueHeight - height) * bottomCropFactor : 0
	boxTop = trueHeight * boxTopPercent - bottomCrop
	if (boxTop < contactLinkHeight) {
		contactLink.className = "more-info top-left"
		body.style.backgroundPosition = "right 60%"
		body.style.fontSize = (height < 525) ?  "2.5px" : null
	} else {
		contactLink.className = "more-info"
		body.style.backgroundPosition = null
		body.style.fontSize = null

		contactLink.style.bottom = (boxTop - contactLinkHeight ) / 2 + "px"
	}

	// resize title
	var imageScale = trueHeight/referenceHeight
	if (vertCrop) {
		topCrop = (trueHeight - height) * topCropFactor
		titleSpace = titleMaxTopOffset * imageScale - topCrop 
		titleHeight = trueTitleHeight * imageScale - topCrop 
		titleOffset = titleSpace - titleHeight
	} else {
		titleHeight = trueTitleHeight * imageScale
		titleSpace = titleMaxTopOffset * imageScale
		titleOffset = titleSpace - titleHeight
	}
	fontSize = (1/35) * titleHeight // yay for magic numbers
	titleWidth =  80.4 * fontSize
	fontSize = (titleWidth >= width) ? width / 80.4 : fontSize
	body.style.fontSize = fontSize + "px"
	header.style.top = titleOffset
}