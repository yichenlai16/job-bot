<template>
  <van-search
    key="search"
    background="#1e8cfa"
    show-action
    shape="round"
    v-model="searchText"
    placeholder="輸入關鍵字"
    @search="searchSite"
  >
    <template #left>
      <van-icon
        size="20"
        color="#FFFFFF"
        v-on:click.exact="clickGoBack"
        name="arrow-left"
      />
    </template>
    <template #action>
      <div @click="detailShow = true">進階</div>
    </template>
  </van-search>

  <van-overlay :show="detailShow" z-index="2">
    <div class="wrapper">
      <div class="block">
        <div class="container">
          <p class="title">進階搜尋</p>
          <van-icon
            class="van-cell__right-ico icon"
            name="close"
            @click="detailShow = false"
          />
        </div>

        <keywordField v-model:keyword="keyword"></keywordField>
        <areaPicker v-model:area="area"></areaPicker>
        <catPicker v-model:cat="cat"></catPicker>
        <workPeriodPicker v-model:period="period"></workPeriodPicker>
        <workExpPicker v-model:exp="exp"></workExpPicker>
        <salaryPicker v-model:salaryL="salaryL"></salaryPicker>
        <div style="height:5px;"></div>
        <van-row gutter="20" type="flex" justify="center">
          <van-col span="8">
            <van-button @click="detailSearch" type="primary" plain size="large"
              >搜尋</van-button
            >
          </van-col>
          <van-col span="8">
            <van-button @click="detailShow = false" type="primary" plain size="large"
              >關閉</van-button
            >
          </van-col>
        </van-row>
      </div>
    </div>
  </van-overlay>
</template>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.title {
  justify-content: left;
  align-items: left;
}
.icon {
  justify-content: right;
  align-items: right;
}
.close-icon {
  /* padding-top:16px; */
  /* padding-right:16px; */
  /* padding: 16px; */
  text-align: center;
  width: 25%;
  align-items: center;
}
.van-search {
  padding: 10px;
}
.wrapper {
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.block {
  border-radius: 16px;
  -webkit-font-smoothing: antialiased;
  z-index: 10;
  width: 85%;
  height: 42%;
  background-color: #f7f8fa;
  padding: 1rem;
}
</style>

<script>
import { ref } from "vue";
// import { VueRouter, routes } from 'vue-router'
// import qs from 'qs';
// import clickGoBack from '@/composables/clickGoBack.js'
// import  from '@/components/Search/Detail/'
import salaryPicker from "@/components/Search/Detail/salaryPicker.vue";
import workExpPicker from "@/components/Search/Detail/workExpPicker.vue";
import workPeriodPicker from "@/components/Search/Detail/workPeriodPicker.vue";
import catPicker from "@/components/Search/Detail/catPicker.vue";
import areaPicker from "@/components/Search/Detail/areaPicker.vue";
import keywordField from "@/components/Search/Detail/keywordField.vue";
export default {
  name: "Search",
  components: {
    keywordField,
    areaPicker,
    catPicker,
    workPeriodPicker,
    workExpPicker,
    salaryPicker,
  },
  methods: {
    clickGoBack() {
      this.$router.go(-1);
    },
    searchSite() {
      const Text = this.searchText.trim();
      this.$router.replace({ name: "SearchResults", query: { search: Text } });
    },
    detailSearch() {
      // GetNullableString()?.Trim(); // returns NULL or trimmed string
      const Text = this.keyword.trim();
      const area = this.area.trim();
      const cat = this.cat.trim();
      const period = this.period.trim();
      const exp = this.exp.trim();
      const salarylow = this.salaryL.trim();
      console.log(Text);
      this.$router.replace({
        query: {
          area: area,
          cat: cat,
          period: period,
          exp: exp,
          salarylow: salarylow,
        },
      });
      this.detailShow = false;
    },
  },
  setup() {
    let params = new URLSearchParams(window.location.search);
    const searchText = ref(params.get("search"));
    const detailShow = ref(false);
    const keyword = ref(params.get("search"));
    const area = ref("");
    const cat = ref("");
    const period = ref("");
    const exp = ref("");
    const salaryL = ref("");

    return {
      searchText,
      detailShow,
      keyword,
      area,
      cat,
      period,
      exp,
      salaryL,
    };
  },
};
</script>
