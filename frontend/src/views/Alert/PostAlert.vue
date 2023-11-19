<template>
  <TopBarClickLeft />
  <div class="van-hairline--surround">
    <van-cell-group inset>
      <template #title>新增提醒 </template>
      <van-field
        v-model="name"
        label="提醒名稱"
        required
        placeholder="輸入名稱"
      />
      <keywordField v-model:keyword="keyword"></keywordField>
      <areaPicker v-model:area="area"></areaPicker>
      <catPicker v-model:cat="cat"></catPicker>
      <workPeriodPicker v-model:period="period"></workPeriodPicker>
      <workExpPicker v-model:exp="exp"></workExpPicker>
      <salaryPicker v-model:salaryL="salaryL"></salaryPicker>

      <van-row>
        <van-col span="12"
          ><van-button type="primary" block @click="submit">新增</van-button>
        </van-col>
        <van-col span="12"
          ><van-button type="default" block @click="cleanRefs"
            >清除條件</van-button
          >
        </van-col>
      </van-row>
    </van-cell-group>
  </div>
  <navBar />
</template>

<script>
import { ref } from "vue";
import navBar from "@/components/Navigation/NavBar.vue";
import TopBarClickLeft from "@/components/Navigation/TopBarClickLeft.vue";
import salaryPicker from "@/components/Alert/Detail/salaryPicker.vue";
import workExpPicker from "@/components/Alert/Detail/workExpPicker.vue";
import workPeriodPicker from "@/components/Alert/Detail/workPeriodPicker.vue";
import catPicker from "@/components/Alert/Detail/catPicker.vue";
import areaPicker from "@/components/Alert/Detail/areaPicker.vue";
import keywordField from "@/components/Alert/Detail/keywordField.vue";
import axios from "axios";
export default {
  name: "PostAlert",
  components: {
    navBar,
    TopBarClickLeft,
    keywordField,
    areaPicker,
    catPicker,
    workPeriodPicker,
    workExpPicker,
    salaryPicker,
  },
  methods: {
    cleanRefs() {
      this.keyword = "";
      this.area = "";
      this.cat = "";
      this.period = "";
      this.exp = "";
      this.salaryL = "";
    },

    submit() {
      const that = this;
      let data = {
        title: that.name,
        keyword: that.keyword,
        area: that.area,
        cat: that.cat,
        period: that.period,
        exp: that.exp,
        salary: that.salary,
      };

      axios
        .post("/api/alert/", data, {
          headers: {
            Authorization:
              "Bearer " + localStorage.getItem("jobproject:access"),
          },
        })
        .then(() => {
          that.$router.push("Alert");
        });
      // .then(function (response) {
      //   that.$router.push({
      //     name: "Alert",
      //     params: { id: response.data.id },
      //   });
      // });
    },
  },
  setup() {
    const keyword = ref("");
    const area = ref("");
    const cat = ref("");
    const period = ref("");
    const exp = ref("");
    const salaryL = ref("");
    const name = ref("");
    return {
      name,
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

<style></style>
