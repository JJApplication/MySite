// 按钮失效
// var button = document.getElementById("xhj");
// function able() {
//         setTimeout(no,1000);
//         setTimeout(ok,5000);
// }
//
// function ok() {
//     button.disabled = false;
// }
// function no() {
//     button.disabled = true;
// }
var clip = new ClipboardJS('#copy');
clip.on('success',function (e) {
        alert('复制成功');
        e.clearSelection();
        clip.destroy();
    });
clip.on('error',function (e) {
        alert('复制失败');
        clip.destroy();
    });

statlist = document.getElementsByClassName("stat");
sslist = document.getElementsByClassName("ss");
for(i=0;i<statlist.length;i++){
    sstxt = sslist[i].href;
    st = statlist[i];
    if(sstxt.indexOf("null")!=-1){
        st.innerText = "BAD";
        st.style.background = "indianred";
    }
    else {
        st.innerText = "GOOD";
        st.style.background = "forestgreen";
    }
}