// var all_apps = document.querySelectorAll('.app');
var search = document.querySelector('#search');
var listContainer = document.querySelector('.suggestion-list');

var app_list = [];

for (let i = 0; i < all_apps.length; i++) {
  let app_title = all_apps[i].title.toLowerCase();
  let app_icon = "📄";
  let app_url = "/blog/post/"+all_apps[i].url;

  let obj = {};
  obj.app_title = app_title;
  obj.app_icon = app_icon;
  obj.app_url = app_url;

  app_list.push(obj);
}

search.addEventListener('keyup', generateAppList);

function generateAppList(event) {
  var fragment = document.createDocumentFragment();

  var userInput = event.target.value;

  if (userInput.length === 0) {
    listContainer.classList.add('hidden');
    return false;
  }

  listContainer.innerHTML = '';
  setTimeout(()=>{
      listContainer.classList.remove('hidden');
  },500);
  var filteredList = app_list.filter(function (arr) {
    return arr.app_title.includes(userInput);
  });

  if (filteredList.length === 0) {
    let paragraph = document.createElement('p');
    paragraph.innerText = 'No results found';
    fragment.appendChild(paragraph);
  }

  else {
    for (let i = 0; i < filteredList.length; i++) {
      let paragraph = document.createElement('p');
      let icon = document.createElement('i');
      let span = document.createElement('span');
      let a = document.createElement('a');

      icon.innerText = filteredList[i].app_icon;
      span.innerText = filteredList[i].app_title;
      a.innerText = "阅读";
      a.href = filteredList[i].app_url;
      paragraph.appendChild(icon);
      paragraph.appendChild(span);
      paragraph.appendChild(a);
      fragment.appendChild(paragraph);
    }
  }

  listContainer.appendChild(fragment);
}

// 点击隐藏
// function hideAppList() {
//   listContainer.classList.add('hidden');
// }