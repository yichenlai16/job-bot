<template>
  <van-skeleton title avatar :row="4" v-if="info == ''" />
  <a-card style="width: 100%" v-if="info !== ''">
    <van-row id="users">
      <van-col span="4" style="">
        <van-image
          class="center"
          round
          width="6em"
          height="6em"
          :src="info.pictureUrl"
        >
        </van-image>
      </van-col>
      <van-col span="4"></van-col>
      <van-col span="10" style="display: flex; align-items: center">
        <ul>
          <li style="height: 50%; font-weight: bold; font-size: 20px">
            {{ info.displayName }}
          </li>
          <li style="height: 50%; font-size: 16px">Welcome</li>
        </ul>
      </van-col>
      <van-col span="2"></van-col>
    </van-row>
  </a-card>
</template>

<script>
import { ref } from "vue";
import { useRoute } from "vue-router";
import getUserData from "@/composables/getUserData.js";

export default {
  setup() {
    const info = ref("");
    const route = useRoute();

    getUserData(info, route);

    console.log(info);

    return { info };
  },
};
</script>

<style></style>
