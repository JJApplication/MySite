// 禁止复制图片
    var img = document.getElementsByTagName("img");
    for(i=0; i<img.length;i++) {
        img[i].oncontextmenu = function () {
            return false
        }
    }
