<template>
  <topBar />

  <van-cell-group title="提醒功能">
    <van-cell>
      <template #title>
        <van-button to="/alertpost" type="primary" size="large"
          >新增提醒</van-button
        >
      </template>
    </van-cell>

    <van-cell>
      <van-row justify="center">
        <van-col>
          <van-button
            plain
            type="primary"
            size="normal"
            @click="getNotifyToken()"
          >
            綁訂Line Notify</van-button
          ></van-col
        >
        <van-col span="2"></van-col>
        <van-col>
          <van-button plain type="primary" size="normal" @click="testNotify()">
            測試Line Notify</van-button
          ></van-col
        >
      </van-row>
    </van-cell>
  </van-cell-group>
  <AlertList />

  <navBar />
</template>

<script>
import { ref } from "vue";
import { useRoute } from "vue-router";
import AlertList from "@/components/Alert/AlertList";
import navBar from "@/components/Navigation/NavBar";
import topBar from "@/components/Navigation/TopBar";
import getAlertData from "@/composables/getAlertData.js";
import axios from "axios";
// import pagination from "@/composables/pagination.js"
export default {
  name: "Alert",
  components: {
    navBar,
    topBar,
    AlertList,
  },
  setup() {
    const info = ref("");
    const route = useRoute();
    getAlertData(info, route);

    const getNotifyToken = () => {
      console.log("hi");
      window.location.href =
        "https://notify-bot.line.me/oauth/authorize?response_type=code&client_id=9fyAdKInMP3Si136avB3DR&redirect_uri=https://home.yichenlai.com/callback&scope=notify&state=state";
    };

    const testNotify = () => {
      axios.get("api/oauth/notify/test", {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("jobproject:access"),
        },
      });
    };
    return {
      info,
      getNotifyToken,
      testNotify,
    };
  },
};
</script>
