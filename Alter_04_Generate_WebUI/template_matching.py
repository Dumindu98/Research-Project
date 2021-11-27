import cv2
import numpy as np
from matplotlib import pyplot as plt

def generatecode(strPath):
    img_rgb = cv2.imread('img/'+strPath)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('img/slider.jpg', 0)
    templateTwo = cv2.imread('img/content.jpg', 0)
    templateThree = cv2.imread('img/banner.jpg', 0)
    templateFour = cv2.imread('img/image-slider.jpg', 0)
    templateFive = cv2.imread('img/content-two.jpg', 0)
    templateSix = cv2.imread('img/slider-two.jpg', 0)
    templateSeven = cv2.imread('img/image-content.jpg', 0)
    templateEight = cv2.imread('img/video.jpg', 0)
    templateNine = cv2.imread('img/form.jpg', 0)

    h, w = template.shape[::]
    h1, w1 = templateTwo.shape[::]
    h2, w2 = templateThree.shape[::]
    h3, w3 = templateFour.shape[::]
    h4, w4 = templateFive.shape[::]
    h5, w5 = templateSix.shape[::]
    h6, w6 = templateSeven.shape[::]
    h7, w7 = templateEight.shape[::]
    h8, w8 = templateNine.shape[::]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    plt.imshow(res, cmap='gray')

    resTwo = cv2.matchTemplate(img_gray, templateTwo, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    resThree = cv2.matchTemplate(img_gray, templateThree, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    resFour = cv2.matchTemplate(img_gray, templateFour, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    resFive = cv2.matchTemplate(img_gray, templateFive, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    resSix = cv2.matchTemplate(img_gray, templateSix, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    resSeven = cv2.matchTemplate(img_gray, templateSeven, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    resEight = cv2.matchTemplate(img_gray, templateEight, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    resNine = cv2.matchTemplate(img_gray, templateNine, cv2.TM_CCOEFF_NORMED)
    plt.imshow(resTwo, cmap='gray')

    threshold = 0.8
    loc = np.where(res >= threshold)
    locTwo = np.where(resTwo >= threshold)
    locThree = np.where(resThree >= threshold)
    locFour = np.where(resFour >= threshold)
    locFive = np.where(resFive >= threshold)
    locSix = np.where(resSix >= threshold)
    locSeven = np.where(resSeven >= threshold)
    locEight = np.where(resEight >= threshold)
    locNine = np.where(resNine >= threshold)

    # Open a file with access mode 'a'
    file_object = open('output/index.html', 'w', encoding='utf-8')
    file_object.write(
        '<!DOCTYPE html> <html lang="en"> <head> <meta name="viewport" content="width=device-width, initial-scale=1"> <title>Sample HTML Page</title> <meta name="keywords" content=""> <meta name="description" content=""> <meta name="author" content=""> <link rel="shortcut icon" href="https://ifsolutions.icu/projects/kalindu/sample-index/images/favicon.ico" type="image/x-icon"> <link rel="apple-touch-icon" href="https://ifsolutions.icu/projects/kalindu/sample-index/images/sample-logo.png"> <link rel="stylesheet" href="https://ifsolutions.icu/projects/kalindu/sample-index/css/bootstrap.min.css"> <link rel="stylesheet" href="https://ifsolutions.icu/projects/kalindu/sample-index/css/style.css"> <link rel="stylesheet" href="https://ifsolutions.icu/projects/kalindu/sample-index/css/responsive.css"> <link rel="stylesheet" href="https://ifsolutions.icu/projects/kalindu/sample-index/css/custom.css"> <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous"> </head> <body> <div class="main-top"> <div class="container-fluid"> <div class="row"> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <div class="text-slid-box"> <div id="offer-box" class="carouselTicker"> <ul class="offer-box"> <li> <i class="fab fa-opencart"></i> Off 10%! Shop Now Man </li> <li> <i class="fab fa-opencart"></i> 50% - 80% off on Fashion </li> <li> <i class="fab fa-opencart"></i> 20% off Entire Purchase Promo code: offT20 </li> <li> <i class="fab fa-opencart"></i> Off 50%! Shop Now </li> <li> <i class="fab fa-opencart"></i> Off 10%! Shop Now Man </li> <li> <i class="fab fa-opencart"></i> 50% - 80% off on Fashion </li> <li> <i class="fab fa-opencart"></i> 20% off Entire Purchase Promo code: offT20 </li> <li> <i class="fab fa-opencart"></i> Off 50%! Shop Now </li> </ul> </div> </div> </div> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <div class="custom-select-box"> <select id="basic" class="selectpicker show-tick form-control" data-placeholder="USD"> <option>JPY</option> <option>USD</option> <option>EUR</option> </select> </div> <div class="right-phone-box"> <p>Call US :- <a href="#"> +11 900 800 100</a></p> </div> <div class="our-link"> <ul> <li><a href="#">My Account</a></li> <li><a href="#">Our location</a></li> <li><a href="#">Contact Us</a></li> </ul> </div> </div> </div> </div> </div> <header class="main-header"> <nav class="navbar navbar-expand-lg navbar-light bg-light navbar-default bootsnav"> <div class="container"> <div class="navbar-header"> <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-menu" aria-controls="navbars-rs-food" aria-expanded="false" aria-label="Toggle navigation"> <i class="fa fa-bars"></i> </button> <a class="navbar-brand" href="https://ifsolutions.icu/projects/kalindu/sample-index/index.html"><img src="https://ifsolutions.icu/projects/kalindu/sample-index/images/logo-sample-test.png" class="logo" alt=""></a> </div> <div class="collapse navbar-collapse" id="navbar-menu"> <ul class="nav navbar-nav ml-auto" data-in="fadeInDown" data-out="fadeOutUp"> <li class="nav-item active"><a class="nav-link" href="https://ifsolutions.icu/projects/kalindu/sample-index/index.html">Home</a></li> <li class="nav-item"><a class="nav-link" href="https://ifsolutions.icu/projects/kalindu/sample-index/about.html">About Us</a></li> <li class="dropdown megamenu-fw"> <a href="#" class="nav-link dropdown-toggle arrow" data-toggle="dropdown">Product</a> <ul class="dropdown-menu megamenu-content" role="menu"> <li> <div class="row"> <div class="col-menu col-md-3"> <h6 class="title">Top</h6> <div class="content"> <ul class="menu-col"> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Jackets</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Shirts</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Sweaters & Cardigans</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">T-shirts</a></li> </ul> </div> </div> <div class="col-menu col-md-3"> <h6 class="title">Bottom</h6> <div class="content"> <ul class="menu-col"> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Swimwear</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Skirts</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Jeans</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Trousers</a></li> </ul> </div> </div> <div class="col-menu col-md-3"> <h6 class="title">Clothing</h6> <div class="content"> <ul class="menu-col"> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Top Wear</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Party wear</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Bottom Wear</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Indian Wear</a></li> </ul> </div> </div> <div class="col-menu col-md-3"> <h6 class="title">Accessories</h6> <div class="content"> <ul class="menu-col"> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Bags</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Sunglasses</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Fragrances</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop.html">Wallets</a></li> </ul> </div> </div> </div> </li> </ul> </li> <li class="dropdown"> <a href="#" class="nav-link dropdown-toggle arrow" data-toggle="dropdown">SHOP</a> <ul class="dropdown-menu"> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/cart.html">Cart</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/checkout.html">Checkout</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/my-account.html">My Account</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/wishlist.html">Wishlist</a></li> <li><a href="https://ifsolutions.icu/projects/kalindu/sample-index/shop-detail.html">Shop Detail</a></li> </ul> </li> <li class="nav-item"><a class="nav-link" href="https://ifsolutions.icu/projects/kalindu/sample-index/service.html">Our Service</a></li> <li class="nav-item"><a class="nav-link" href="https://ifsolutions.icu/projects/kalindu/sample-index/contact-us.html">Contact Us</a></li> </ul> </div> <div class="attr-nav"> <ul> <li class="search"><a href="#"><i class="fa fa-search"></i></a></li> <li class="side-menu"><a href="#"> <i class="fa fa-user-circle"></i> </a></li> </ul> </div> </div> <div class="side"> <a href="#" class="close-side"><i class="fa fa-times"></i></a> <img class="d-block m-auto" width="100" height="100" src="https://img.icons8.com/external-kiranshastry-lineal-color-kiranshastry/64/000000/external-user-interface-kiranshastry-lineal-color-kiranshastry.png" class="cart-thumb" alt="" /> <form action="/action_page.php"> <div class="form-group text-white"> <label for="email">Email address:</label> <input type="email" class="form-control" placeholder="Enter email" id="email"> </div> <div class="form-group text-white"> <label for="pwd">Password:</label> <input type="password" class="form-control" placeholder="Enter password" id="pwd"> </div> <div class="form-group form-check"> <label class="form-check-label"> <input class="form-check-input text-white" type="checkbox"> Remember me </label> </div> <button type="submit" class="d-block m-auto hvr-hover text-white border-0">Sign In</button> </form> </div> </nav> </header> <div class="top-search"> <div class="container"> <div class="input-group"> <span class="input-group-addon"><i class="fa fa-search"></i></span> <input type="text" class="form-control" placeholder="Search"> <span class="input-group-addon close-search"><i class="fa fa-times"></i></span> </div> </div> </div>')

    ptTempOne = -10
    ptTempTwo = -10

    # Carousel
    for pt in zip(*loc[::-1]):

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            file_object.write('<div id="slides-shop" class="cover-slides"> <ul class="slides-container"> <li class="text-left"> <img src="https://dummyimage.com/1920x1080/0a0791/#000" alt=""> </li> <li class="text-center"> <img src="https://dummyimage.com/1920x1080/817c85/#000" alt=""> </li> <li class="text-right"> <img src="https://dummyimage.com/1920x1080/0a6f7a/#000" alt=""> </li> </ul> <div class="slides-navigation"> <a href="#" class="next"><i class="fa fa-angle-right" aria-hidden="true"></i></a> <a href="#" class="prev"><i class="fa fa-angle-left" aria-hidden="true"></i></a> </div> </div>')
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10

    # Carousel-two
    for pt in zip(*locSix[::-1]):

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w5, pt[1] + h5), (0, 0, 255), 2)
            file_object.write('<div id="slides-shop" class="cover-slides"> <ul class="slides-container"> <li class="text-left"> <img src="https://dummyimage.com/1920x1080/21ccbb/#fff" alt=""> </li> <li class="text-center"> <img src="https://dummyimage.com/1920x1080/f44775/#fff" alt=""> </li> <li class="text-right"> <img src="https://dummyimage.com/1920x1080/228888/#fff" alt=""> </li> </ul> <div class="slides-navigation"> <a href="#" class="next"><i class="fa fa-angle-right" aria-hidden="true"></i></a> <a href="#" class="prev"><i class="fa fa-angle-left" aria-hidden="true"></i></a> </div> </div>')
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10

    content_html = '<div class="container-fluid pt-5"> <div class="row">'
    iterator = 0

    # Content
    for pt in zip(*locTwo[::-1]):
        iterator = iterator + 1

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w1, pt[1] + h1), (0, 0, 255), 2)
            content_html += '<div class="col-6"> <div class="row"> <div class="col-4"> <img class="w-100" src="https://dummyimage.com/300x300/0b6e66/#000" alt=""> </div> <div class="col-8 d-flex align-items-center"> <div class="service-block-inner"> <h3>Heading</h3> <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p> </div> </div> </div> </div>'
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
            # print(ptTempOne)
            if iterator == 3:
                content_html += '</div></div></div></div><div class="container-fluid pt-3"> <div class="row"> <div class="col-md-6"> <div class="row">'
                iterator = -1

    content_html += '</div></div>'
    file_object.write(content_html)

    # form
    for pt in zip(*locNine[::-1]):

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w8, pt[1] + h8), (0, 0, 255), 2)
            file_object.write('<div class="container py-5"> <form> <div class="form-group row"> <label class="col-sm-2 col-form-label">From</label> <div class="col-sm-10"> <input type="email" class="form-control" placeholder="someone@gmail.com" > </div> </div> <div class="form-group row"> <label class="col-sm-2 col-form-label">Subject</label> <div class="col-sm-10"> <input type="text" class="form-control" placeholder="Lorem"> </div> </div> <div class="form-group row"> <label class="col-sm-2 col-form-label">To</label> <div class="col-sm-10"> <input type="text" class="form-control" placeholder="someone@gmail.com"> </div> </div> <div class="form-group row"> <label class="col-sm-2 col-form-label">Cc</label> <div class="col-sm-10"> <input type="text" class="form-control" placeholder="someone@gmail.com"> </div> </div> <div class="form-group row"> <label class="col-sm-2 col-form-label">Bcc</label> <div class="col-sm-10"> <input type="text" class="form-control" placeholder="someone@gmail.com"> </div> </div> <div class="form-group"> <label>Text Area</label> <textarea class="form-control" rows="5" style="font-style: italic;">Lorem ipsum dolor sit amet, consectetur adipisicing elit</textarea></div></form></div>')
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10

    # Banner
    for pt in zip(*locThree[::-1]):

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0, 0, 255), 2)
            file_object.write(
                '<img class="w-100 h-75 py-5" src="https://ifsolutions.icu/projects/kalindu/banner.jpg"/>')
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        # print(ptTempOne)

    contents_html = '<div class="container-fluid pt-3"> <div class="row">'
    iterators = 0

    # Images slider
    for pt in zip(*locFour[::-1]):

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (0, 0, 255), 2)
            file_object.write('<?xml version="1.0"?><div class="instagram-box"><div class="main-instagram owl-carousel owl-theme"><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/850c28/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/800080/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/c00000/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/228b22/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/565287/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/0a85ab/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/e1e1e1/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/4c4c4c/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/738a93/#000" alt=""/></div></div><div class="item"><div class="ins-inner-box"><img src="https://dummyimage.com/238x238/d3d5da/#000" alt=""/></div></div></div></div>')
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        # print(ptTempOne)

    contentssss_html = '<div class="container-fluid pt-3"> <div class="row">'
    iteratorssss = 0

    # Content Two
    for pt in zip(*locFive[::-1]):
        iteratorssss = iteratorssss + 1

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w4, pt[1] + h4), (0, 0, 255), 2)
            contentssss_html += '<div class="col-sm-6"> <div class="row d-flex align-items-center pt-2"> <div class="col-4"> <img class="w-100" src="https://dummyimage.com/300x300/0b6e66/#000" alt=""> </div> <div class="col-5"> <div class="service-block-inner"> <h3>Heading</h3> <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p> </div> </div> <div class="col-1"> <img src="https://img.icons8.com/color/20/000000/ok--v1.png"/> </div> <div class="col-2"> <a href="#"><button type="button" name="button" class="bg-primary text-white border-0 px-3" style="border-radius:10%;">Add</button></a> </div> </div> </div>'
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
            # print(ptTempOne)
            if iteratorssss == 8:
                contentssss_html += '</div></div></div></div><div class="container-fluid pt-3"> <div class="row"> <div class="col-md-6"> <div class="row">'
                iteratorssss = 1

    contentssss_html += '</div></div>'
    file_object.write(contentssss_html)

    contentss_html = '<div class="container-fluid pt-3"> <div class="row">'
    iteratorss = 0

    # Image Content
    for pt in zip(*locSeven[::-1]):
        iteratorss = iteratorss + 1

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w6, pt[1] + h6), (0, 0, 255), 2)
            contentss_html += '<div class="col-6"> <div class="row"> <img class="lazy-loaded w-50 d-block m-auto" src="https://dummyimage.com/300x300/565287/#000"/> </div> <div class="col-12"> <h2 class="text-center py-3">Heading</h2> <p class="text-center pb-3">Lorem ipsum dolor sit amet, <br>consectetur adipisicing elit, sed do <br>eiusmod tempor ua.</p> <button class="d-block m-auto px-3 border-0 bg-primary w-25 my-5 text-white" style="border-radius:5px;" type="button" name="button" >Read More</button> </div> </div>'
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
            # print(ptTempOne)
            if iteratorss == 3:
                contentss_html += '</div></div></div></div><div class="container-fluid pt-3"> <div class="row"> <div class="col-md-6"> <div class="row">'
                iteratorss = -1

    contentss_html += '</div></div>'
    file_object.write(contentss_html)

    contentsss_html = '<div class="container-fluid"> <div class="row">'
    iteratorsss = 0

    # Video
    for pt in zip(*locEight[::-1]):
        iteratorsss = iteratorsss + 1

        if ptTempOne > pt[0] and ptTempTwo > pt[1]:
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
        else:
            cv2.rectangle(img_rgb, pt, (pt[0] + w7, pt[1] + h7), (0, 0, 255), 2)
            contentsss_html += '<div class="col-6"> <iframe class="w-100" height="315" src="https://www.youtube.com/embed/BHACKCNDMW8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> </div>'
            ptTempOne = pt[0] + 10
            ptTempTwo = pt[1] + 10
            # print(ptTempOne)
            if iteratorsss == 2:
                contentsss_html += '</div></div></div></div><div class="container-fluid pt-3"> <div class="row">'
                iteratorsss = -1

    contentsss_html += '</div></div>'
    file_object.write(contentsss_html)

    file_object.write('<footer class="pt-5"><div class="footer-main"><div class="container"><div class="row"><div class="col-lg-4 col-md-12 col-sm-12"><div class="footer-widget"><h4>About ThewayShop</h4><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p><ul><li><a href="#"><i class="fab fa-facebook" aria-hidden="true"></i></a></li><li><a href="#"><i class="fab fa-twitter" aria-hidden="true"></i></a></li><li><a href="#"><i class="fab fa-linkedin" aria-hidden="true"></i></a></li><li><a href="#"><i class="fab fa-google-plus" aria-hidden="true"></i></a></li><li><a href="#"><i class="fa fa-rss" aria-hidden="true"></i></a></li><li><a href="#"><i class="fab fa-pinterest-p" aria-hidden="true"></i></a></li><li><a href="#"><i class="fab fa-whatsapp" aria-hidden="true"></i></a></li></ul></div></div><div class="col-lg-4 col-md-12 col-sm-12"><div class="footer-link"><h4>Information</h4><ul><li><a href="#">About Us</a></li><li><a href="#">Customer Service</a></li><li><a href="#">Our Sitemap</a></li><li><a href="#">Terms & Conditions</a></li><li><a href="#">Privacy Policy</a></li><li><a href="#">Delivery Information</a></li></ul></div></div><div class="col-lg-4 col-md-12 col-sm-12"><div class="footer-link-contact"><h4>Contact Us</h4><ul><li><p><i class="fas fa-map-marker-alt"></i>Address: Michael I. Days 3756 <br>Preston Street Wichita,<br> KS 67213 </p></li><li><p><i class="fas fa-phone-square"></i>Phone: <a href="tel:+1-888705770">+1-888 705 770</a></p></li><li><p><i class="fas fa-envelope"></i>Email: <a href="mailto:contactinfo@gmail.com">contactinfo@gmail.com</a></p></li></ul></div></div></div></div></div></footer><a href="#" id="back-to-top" title="Back to top" style="display:none">↑</a><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/jquery-3.2.1.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/popper.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/bootstrap.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/jquery.superslides.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/bootstrap-select.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/inewsticker.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/bootsnav.js."></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/images-loded.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/isotope.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/owl.carousel.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/baguetteBox.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/form-validator.min.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/contact-form-script.js"></script><script src="https://ifsolutions.icu/projects/kalindu/sample-index/js/custom.js"></script></body></html>')
    # Close the file
    file_object.close()

    file_object = open('output/index.html', 'r')
    str = file_object.read();
    print("Generated HTML Code : ", str)
    file_object.close()

    return str;

   # cv2.imshow("Detected Image", str)
   # cv2.waitKey()
   # cv2.destroyAllWindows()