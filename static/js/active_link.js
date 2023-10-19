function activeLink(e) {
    var a = document.getElementsByClassName('link_activate')
    for (i = 0; i < a.length; i++) {
       a[i].classList.remove('choosen');
    }
    e.classList.add('choosen');
 }