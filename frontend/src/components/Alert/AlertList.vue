<template>
  <van-cell-group>
    <template #title>提醒列表</template>

    <van-swipe-cell v-for="alert in info.results" v-bind:key="alert.id">
      <div @click="showDialog(alert)">
        <van-cell is-link>
          <template #title class="alertName">
            <div class="van-ellipsis">{{ alert.title }}</div>
          </template>
          <template #label class="alertKeyword">
            {{ alert.keyword }}
            <template v-if="alert.area !== '' && alert.keyword !== ''"
              >|
            </template>
            {{ alert.area }}
          </template>
        </van-cell>
      </div>
      <template #right>
        <van-button
          style="height: 100%"
          @click="removeAlert(alert.id)"
          square
          type="danger"
          text="删除"
        />
      </template>
    </van-swipe-cell>
  </van-cell-group>

  <van-dialog v-model:show="dialogShow" title="">
    <a-card>
      <!-- <template #title>
        提醒
      </template>
    <p style="font-size: 14px; color: rgba(0, 0, 0, 0.85); margin-bottom: 16px; font-weight: 500">
      提醒名字
    </p>
    <a-card title="條件">
       </a-card>
      Inner Card content -->

      <a-descriptions
        bordered
        size="middle"
        :column="{ xxl: 4, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }"
      >
        <template #title> {{ dialogInfo.title }} </template>

        <a-descriptions-item v-if="dialogInfo.keyword != ''" span="4">
          <template #label>
            <span class="drscriptionLabel">關鍵字</span>
          </template>
          {{ dialogInfo.keyword }}
        </a-descriptions-item>

        <a-descriptions-item v-if="dialogInfo.area != ''" span="4">
          <template #label>
            <span class="drscriptionLabel">地區</span>
          </template>
          {{ dialogInfo.area }}
        </a-descriptions-item>

        <a-descriptions-item v-if="dialogInfo.cat != ''" span="4">
          <template #label>
            <span class="drscriptionLabel">職務類別</span>
          </template>
          {{ dialogInfo.cat }}
        </a-descriptions-item>
      </a-descriptions>
    </a-card>
  </van-dialog>
</template>

<style>
/* .van-cell__title {
  width: 10rem;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
} */
</style>

<script>
import { ref } from "vue";
import { Dialog } from "vant";
import { useRoute } from "vue-router";
import getAlertData from "@/composables/getAlertData.js";
import deleteAlert from "@/composables/deleteAlert.js";

export default {
  methods: {},
  //API
  setup() {
    //響應式數據
    const info = ref("");
    //新增路由
    const route = useRoute();
    getAlertData(info, route);
    const removeAlert = (key) => {
      const beforeClose = (action) =>
        new Promise((resolve) => {
          setTimeout(() => {
            if (action === "confirm") {
              deleteAlert(key);
              resolve(true);
            } else {
              resolve(true);
            }
          }, 1000);
        });
      Dialog.confirm({
        title: "確定刪除嗎？",
        // message: key,
        beforeClose,
      });
    };
    const dialogShow = ref(false);
    const dialogInfo = ref("");
    const showDialog = (alert) => {
      dialogInfo.value = alert;
      dialogShow.value = true;
    };
    return {
      info,
      removeAlert,
      dialogShow,
      dialogInfo,
      showDialog,
    };
  },

  //other
};
</script>

<style scoped></style>
