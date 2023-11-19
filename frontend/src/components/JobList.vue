<template>
  <div class="van-hairline--surround">
    <a-skeleton v-if="info == ''" active />

    <van-cell-group title="職缺列表">
      <div
        v-for="(job, index) in info.results"
        v-bind:key="index"
        @click="showDrawer(job)"
      >
        <van-cell is-link>
          <template #title>
            <div class="van-ellipsis jobName">{{ job.name }}</div>
          </template>
          <template #label>
            <div class="companyName">
              {{ job.company_name }}
            </div>
          </template>
        </van-cell>
      </div>
    </van-cell-group>

    <van-row justify="center">
      <van-col span="6">
        <p v-if="info.next != null">
          <van-button size="large" type="default" @click="loadMore(info.next)"
            >查看更多</van-button
          >
        </p>
      </van-col>
    </van-row>

    <a-drawer
      v-model:visible="visible"
      class="custom-class"
      placement="right"
      maskStyle="background-color: rgb(0 0 0 / 10%);"
      @after-visible-change="afterVisibleChange"
      getContainer=".van-tabs__content"
    >
      <template #title> {{ drawerInfo.name }}</template>

      <a-descriptions
        bordered
        size="middle"
        :column="{ xxl: 4, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }"
      >
        <template #title> {{ drawerInfo.name }}</template>
        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">職缺名稱</span>
          </template>
          {{ drawerInfo.name }}
        </a-descriptions-item>

        <a-descriptions-item span="2">
          <template #label>
            <span class="drscriptionLabel">公司名稱</span>
          </template>
          {{ drawerInfo.company_name }}
        </a-descriptions-item>

        <a-descriptions-item span="1">
          <template #label>
            <span class="drscriptionLabel">上班地點</span>
          </template>
          {{ drawerInfo.name }}
        </a-descriptions-item>

        <a-descriptions-item label="上班地點"
          >{{ drawerInfo.area }}{{ drawerInfo.address }}
        </a-descriptions-item>

        <a-descriptions-item label="職務類別">
          <template v-for="(x, index) in drawerInfo.category"
            >{{ x }}
            <template v-if="index != drawerInfo.category.length - 1"
              >、
            </template>
          </template>
        </a-descriptions-item>
        <a-descriptions-item label="需求人數">{{
          drawerInfo.needEmployee
        }}</a-descriptions-item>
      </a-descriptions>

      <a-descriptions layout="vertical" bordered>
        <a-descriptions-item label="工作內容">
          {{ drawerInfo.jobDesc }}
        </a-descriptions-item>
      </a-descriptions>

      <a-descriptions
        bordered
        size="middle"
        :column="{ xxl: 4, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }"
      >
        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">出差外派</span>
          </template>
          {{ drawerInfo.businessTrip }}
        </a-descriptions-item>

        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">上班時段</span>
          </template>
          {{ drawerInfo.workPeriod }}
        </a-descriptions-item>

        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">管理責任</span>
          </template>
          {{ drawerInfo.manageRespon }}
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">條件要求</span>
          </template>
          <template v-for="(x, index) in drawerInfo.roleDesc"
            >{{ x }}
            <template v-if="index != drawerInfo.roleDesc.length - 1"
              >、
            </template>
          </template>
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">可上班日</span>
          </template>
          {{ drawerInfo.startWorkDay }}
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">學歷要求</span>
          </template>
          {{ drawerInfo.edu }}
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">工作技能</span>
          </template>
          <template v-for="(x, index) in drawerInfo.skill"
            >{{ x }}
            <template v-if="index != drawerInfo.skill.length - 1">、 </template>
          </template>
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">具備駕照</span>
          </template>
          <template v-for="(x, index) in drawerInfo.driverLicense"
            >{{ x }}
            <template v-if="index != drawerInfo.driverLicense.length - 1"
              >、
            </template>
          </template>
        </a-descriptions-item>
      </a-descriptions>

      <div class="van-safe-area-bottom" style="height: 60px"></div>
    </a-drawer>
  </div>
</template>

<style>
.drscriptionLabel {
  white-space: nowrap;
}
</style>

<script>
import { ref } from "vue";
import { useRoute } from "vue-router";
import getJobData from "@/composables/getJobData.js";
import axios from "axios";

export default {
  //API
  setup() {
    //響應式數據
    const info = ref("");
    //新增路由
    const route = useRoute();

    getJobData(info, route);

    const visible = ref(false);

    const drawerInfo = ref("");

    const showDrawer = (job) => {
      drawerInfo.value = job;
      visible.value = true;
    };


    const loadMore = async (url) => {
      const params = new URL(url);
      url = "api/job/?" + params.searchParams.toString();
      const response = await axios.get(url);
      info.value.next = response.data.next;
      Array.prototype.push.apply(info.value.results, response.data.results);
    };

    return {
      loadMore,
      drawerInfo,
      visible,
      showDrawer,
      info,
    };
  },

  //other
};
</script>

<style scoped></style>
