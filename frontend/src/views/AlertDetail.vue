<template>
  <topBar />
  <div
    class="van-hairline--top-bottom van-safe-area-bottom"
    v-if="alert !== null"
  >
    <van-cell-group title="提醒內容" inset>
      <!-- <van-cell>
        <template #value>{{ alert.title }} </template>
      </van-cell> -->
      <van-cell>
        <template #value>關鍵字：{{ alert.keyword }} </template>
      </van-cell>
      <van-cell>
        <template #value>地區：{{ alert.area }} </template>
      </van-cell>
      <van-cell>
        <template #value>職務類別：{{ alert.cat }} </template>
      </van-cell>
      <van-cell>
        <template #value>工作時間：{{ alert.period }} </template>
      </van-cell>
      <van-cell>
        <template #value>薪資：{{ alert.salary }} </template>
      </van-cell>
    </van-cell-group>
  </div>
  <navBar />
</template>
<script>
import navBar from "@/components/Navigation/NavBar";
import topBar from "@/components/Navigation/TopBarClickLeft";
import axios from "axios";

export default {
  name: "AlertDetail",
  components: { navBar, topBar },
  data: function () {
    return {
      isShow: true,
      alert: null,
    };
  },
  mounted() {
    axios
      .get("/api/alert/" + this.$route.params.id)
      .then((response) => (this.alert = response.data));
  },
};
</script>
