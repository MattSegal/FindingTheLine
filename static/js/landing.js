
var header = document.getElementsByTagName('header')[0]
var body = document.getElementsByTagName('body')[0]
var contactLink = document.getElementsByClassName('more-info')[0] 
var styles, height, width, aspectRatio, vertCrop, bottomCrop, trueHeight, boxHeight, boxTop, topCollision
var trueAspectRatio = 1.5
var boxTopPercent = 0.15
var bottomCropFactor = 0.4
var contactLinkHeight = 40 // px

responsiveLayout()
window.onresize = responsiveLayout

setTimeout(function() {
	header.style.opacity = 1
},400)		


function responsiveLayout() {
	styles = window.getComputedStyle(body)
	width = window.innerWidth
	height = window.innerHeight
	aspectRatio = width/height
	vertCrop = aspectRatio > trueAspectRatio
	horzCrop = aspectRatio < trueAspectRatio
	
	trueHeight = vertCrop ? width / trueAspectRatio : height
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
}