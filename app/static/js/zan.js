var zanbox = document.getElementById("zanbox");
function zanwo() {
    axios.post("/zan","1").then(res=>{
        if(zanbox){
            zanbox.innerText = res.data;
        }
}).catch((e)=>{
   console.log("点赞失败");
});
}