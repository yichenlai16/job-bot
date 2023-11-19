<template>
  <div id="app">
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
import { onMounted } from "vue";
import { useRouter } from "vue-router";

import liff from "@line/liff";
import axios from "axios";
export default {
  porps: {},
  setup() {
    const router = useRouter();
    const storage = localStorage;
    const expiredTime = Number(storage.getItem("jobproject:expiredtime"));
    const current = new Date().getTime();
    const refreshToken = storage.getItem("jobproject:refresh");

    const login = (accessToken) => {
      axios
        .post("api/oauth/line/liff", {
          access_token: accessToken,
        })
        .then(function (response) {
          console.log(response);
          const expiredTime = Date.parse(response.headers.date) + 60000;
          storage.setItem("jobproject:access", response.data.token.access);
          storage.setItem("jobproject:refresh", response.data.token.refresh);
          storage.setItem("jobproject:expiredtime", expiredTime);
          router.replace({ name: "Main" });
        });
    };

    onMounted(async () => {
      try {
        await liff.init({ liffId: "1656495409-YPJpOrV4" }); // Use own liffId
        if (!liff.isLoggedIn())
          liff.login({ redirectUri: window.location.href });

        const getProfile = Promise.resolve(liff.getProfile());
        getProfile.then(function (result) {
          console.log(result);
          storage.setItem("displayName", result.displayName);
          storage.setItem("pictureUrl", result.pictureUrl);
          storage.setItem("userId", result.userId);
          console.log(expiredTime, current);
          login(liff.getAccessToken());

          console.log("Liff initilized");
          if (expiredTime > current) {
            this.hasLogin = true;
            console.log(this.hasLogin);
          } else if (refreshToken == null) {
            login(liff.getAccessToken());
            this.hasLogin = true;
            console.log(this.hasLogin);
          }
        });
      } catch (err) {
        console.log(`liff.state init error ${err}`);
        storage.clear();
        this.hasLogin = false;
      }
    });

    return { login };
  },
};
</script>

<style>
body {
  height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  margin: 0;
  color: #323233;
  font-size: 16px;
  font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Helvetica Neue",
    Helvetica, Segoe UI, Arial, Roboto, "PingFang SC", "miui",
    "Hiragino Sans GB", "Microsoft Yahei", sans-serif;
  background-color: #f7f8fa;
  -webkit-font-smoothing: antialiased;
  padding-top: env(safe-area-inset-top);
  padding-right: env(safe-area-inset-right);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
}

p {
  margin: 0;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  margin: 0;
  font-size: inherit;
}

input,
textarea,
van-search {
  font-size: initial;
}

ul,
ol {
  margin: 0;
  padding: 0;
  list-style: none;
}

a {
  text-decoration: none;
}

.router-view {
  width: 100%;
  height: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  margin: 0 auto;
  -webkit-overflow-scrolling: touch;
}
</style>
