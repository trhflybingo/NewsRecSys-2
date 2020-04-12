<template>
    <div class="newFooter">
      <div class="footContent">
        <div class="footItem1">
          <h3>个人介绍：</h3>
          <ul>
            <li>因为热爱推荐系统与深度学习，然后我就开始了我漫长的自学道路.
            你在这个网页看到的所有内容, 都是我在网上探索, 自学而来的.
             我很欣赏网上那些默默奉献的人们, 分享自己所学的东西给了我.
             我也要回报那些奉献的人们, 将我的所学奉献给大家~
      爱分享的性格, 让我能有机会分享这些有趣的内容给大家, 帮助大家, 我也很开心~</li>

          </ul>
        </div>
        <div class="footItem2">
          <h3>微信号：</h3>
          <img class="bookcode" src="../assets/img/bookcode.jpg"/>
        </div>
        <div class="footItem3">
          <h3>关于我的动向：</h3>
          <ul>
            <li><a href="https://www.jianshu.com/u/753959d5ec9b" target="_blank">简书</a></li>
            <li><a href="https://github.com/xilepeng" target="_blank">Github</a></li>
            <li>手机：188-0013-8580</li>
            <li>Email:xilepeng@126.com</li>
          </ul>
        </div>
      </div>
      <div class="footCopy">
        <a href="https://github.com/xilepeng/NewsRecSys" target="_blank">©CopyRight X</a>
        <span></span>
      </div>
    </div>
</template>

<script>
export default {
  name: 'newFooter'
}
</script>

<style lang="less" scoped>
  /*common style*/
  a{
    color:#777
  }
  a:hover{
    color:#333
  }
  .newFooter{
    display: flex;
    flex-flow: column;
    width: 100%;
    background: #f5f6f5;
    font-size: 12px;
    color: #777;
    .footContent{
      width: 100%;
      display: flex;
      justify-content: space-around;
      padding: 0 4%;
      box-sizing: border-box;
      .footItem1,.footItem2,.footItem3{
        width: 30%;
        padding:20px 5%;
        text-align: center;
        box-sizing: border-box;
        &>h3{
          margin-bottom:10px;
          display: inline-block;
          width: 100%;
        }
      }
      .footItem2>img{
        width: 50%;
      }
      .footItem1>ul li,.footItem3>ul li{
        margin-top:10px;
        margin-left: -10px;
      }
    }
    .footCopy{
      width: 100%;
      text-align: center;
      margin-top: 20px;
      margin-bottom: 15px;
    }
  }
</style>
