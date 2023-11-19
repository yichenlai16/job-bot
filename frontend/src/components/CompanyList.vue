<template>
  <van-cell-group>
    <template #title>公司列表</template>

    <div v-for="company in info.results" v-bind:key="company.url">
      <router-link :to="{ name: 'Company', params: { id: company.id } }">
        <van-cell is-link>
          <template #title class="jobName"> {{ company.name }} </template>
          <template #label class="companyName"
            >{{ company.area }} | {{ company.categoryDesc }}</template
          >
          <!-- <template #value></template> -->
        </van-cell>
      </router-link>
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
</template>

<style>
.van-cell__title {
  width: 10rem;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>

<script>
import { ref } from "vue";
import { useRoute } from "vue-router";
import getCompanydata from "@/composables/getCompanydata.js";
import axios from "axios";

export default {
  //API
  setup() {
    //響應式數據
    const info = ref("");
    //新增路由
    const route = useRoute();
    getCompanydata(info, route);

    const loadMore = async (url) => {
      const params = new URL(url);
      url = "api/company/?" + params.searchParams.toString();
      const response = await axios.get(url);
      info.value.next = response.data.next;
      Array.prototype.push.apply(info.value.results, response.data.results);
    };

    return {
      info,
      loadMore,
    };
  },

  //other
};
</script>

<style scoped></style>
