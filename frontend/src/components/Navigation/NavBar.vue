<template>
  <router-view />
  <van-tabbar fixed placeholder="true" route z-index="1">
    <van-tabbar-item replace to="/search" icon="search">搜尋</van-tabbar-item>
    <van-tabbar-item replace to="/main" icon="home-o">主頁</van-tabbar-item>
    <van-tabbar-item replace to="/alert" icon="setting-o">關於</van-tabbar-item>
  </van-tabbar>
  <div class="van-safe-area-bottom"></div>
</template>

<script></script>

<style></style>
