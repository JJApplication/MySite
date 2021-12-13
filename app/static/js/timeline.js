const timelineData = [
{
        text: '第一个博客网站诞生，托管于wordpress',
        date: '6/28 2017',
        category: {
            tag: 'born',
            color: '#FFDB14'
        }
    },

{
  text: '博客的Telegram通知频道开通',
  date: '5/03 2018',
  category: {
    tag: 'telegram',
    color: '#1DA1F2'
  },
 },

{
  text: '更换域名为Landers1037.top',
  date: '2/21 2019',
  category: {
    tag: 'domain',
    color: '#AE72FF'
  },
},


{
  text: '开始使用Hexo，托管到Github',
  date: '5/10 2019',
  category: {
    tag: 'blog',
    color: '#e17b77'
  },

  link: {
    url: 'https://github.com/Landers1037/Landers1037.github.io',
    text: 'Check it out on Github'
  }
},

{
    text: '域名更换为lrenj.top',
    date: '6/25 2019',
    category: {
        tag: 'domain',
        color: '#AE72FF'
    },

},
{
  text: 'Flask项目开启，使用Flask建设主页',
  date: '6/25 2019',
  category: {
    tag: 'home',
    color: '#378de5'
  },

  link: {
    url: '/',
    text: 'Go to Page'
  }
},

{
    text: '全站Flask目标达成',
    date: '8/10 2019',
    category: {
        tag: 'flask',
        color: '#378952'
    },

},
{
    text: '轻量化精简页面',
    date: '9/1 2019',
    category: {
        tag: 'flask',
        color: '#378952'
    },

},
{
    text: '博客独立 Blog.renj.io',
    date: '1/1 2020',
    category: {
        tag: 'Go',
        color: '#378de0'
    },

},
{
    text: '网站重构,接口优化,模板优化',
    date: '7/20 2020',
    category: {
        tag: 'flask',
        color: '#378952'
    },

},
{
    text: '域名更换renj.io',
    date: '8/1 2020',
    category: {
        tag: 'domain',
        color: '#AE72FF'
    },

}
    ];




const TimelineItem = ({ data }) =>
React.createElement("div", { className: "timeline-item" },
React.createElement("div", { className: "timeline-item-content" },
React.createElement("span", { className: "tag", style: { background: data.category.color } },
data.category.tag),

React.createElement("time", null, data.date),
React.createElement("p", null, data.text),
data.link &&
React.createElement("a", {
  href: data.link.url,
  target: "_blank",
  rel: "noopener noreferrer" },

data.link.text),


React.createElement("span", { className: "circle" })));




const Timeline = () =>
timelineData.length > 0 &&
React.createElement("div", { className: "timeline-container" },
timelineData.map((data, idx) =>
React.createElement(TimelineItem, { data: data, key: idx })));




const App = () => React.createElement(React.Fragment, null,
React.createElement("h1", null, "时间线Timeline"),
React.createElement(Timeline, null));


ReactDOM.render(React.createElement(App, null), document.getElementById('app'));