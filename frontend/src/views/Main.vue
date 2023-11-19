<template>
  <div class="home" v-if="status !== ''">
    <UserBar />
    <SearchBar />
    <van-skeleton title avatar :row="4" v-if="status == ''" />

    <div style="background-color: #ececec; padding: 20px" v-if="status !== ''">
      <a-space direction="vertical" style="width: 100%">
        <van-row justify="center">
          <van-col span="20"
            ><a-card>
              <a-statistic
                title="提醒數量"
                :value="status.notifyTotal"
                :precision="0"
                suffix=""
                class="demo-class"
                :value-style="{ color: '#2687ff' }"
              >
                <template #prefix>
                  <arrow-down-outlined />
                </template>
              </a-statistic> </a-card
          ></van-col>
        </van-row>

        <van-row gutter="20" justify="center">
          <van-col span="10">
            <a-card>
              <a-statistic
                title="職缺數量"
                :value="status.jobTotal"
                :precision="0"
                suffix=""
                class="demo-class"
                :value-style="{ color: '#2687ff' }"
              >
                <template #prefix>
                  <arrow-down-outlined />
                </template>
              </a-statistic>
            </a-card>
          </van-col>
          <van-col span="10">
            <a-card>
              <a-statistic
                title="今日更新"
                :value="status.todayTotal"
                :precision="0"
                suffix=""
                class="demo-class"
                :value-style="{ color: '#2687ff' }"
              >
                <template #prefix>
                  <arrow-down-outlined />
                </template>
              </a-statistic>
            </a-card>
          </van-col>
        </van-row>
      </a-space>
    </div>

    <van-row justify="center">
      <van-col>
        <van-button type="primary" @click="showPopup"
          >Web Scraper Demo</van-button
        >
      </van-col>
    </van-row>
  </div>

  <navBar />
</template>

<script>
// @ is an alias to /src
import navBar from "@/components/Navigation/NavBar";
import SearchBar from "@/components/Main/SearchBar";
import UserBar from "@/components/Main/UserBar";
import liff from "@line/liff";
import axios from "axios";
import { onMounted, ref } from "vue";
import getCookie from "@/composables/getCookie.js";
import { Toast } from "vant";
export default {
  name: "Home",
  components: {
    navBar,

    SearchBar,
    UserBar,
  },
  setup() {
    const show = ref(true);
    const showPopup = () => {
      Toast.loading({
        message: "Loading...",
        forbidClick: true,
        duration: 0,
      });
      axios.post("api/demo/").then(() => {
        window.location.reload();
      });
    };

    const storage = localStorage;
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
          getStatus();
        });
    };
    const status = ref("");
    const getStatus = async () => {
      const response = await axios.get("api/main/", {
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          Authorization: "Bearer " + localStorage.getItem("jobproject:access"),
        },
      });
      status.value = response.data;
    };

    onMounted(() => {
      liff
        .init({
          liffId: "1656495409-YPJpOrV4", // Use own liffId
        })
        .then(() => {
          if (!liff.isLoggedIn())
            liff.login({ redirectUri: window.location.href });
          login(liff.getAccessToken());
        })
        .catch((err) => {
          console.log(err.code, err.message);
        });
    });

    return {
      show,
      showPopup,
      status,
    };
  },
};
</script>

<style>
.home {
  padding-bottom: 0px;
}
.main-notice {
  padding: 20px;
}
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>
