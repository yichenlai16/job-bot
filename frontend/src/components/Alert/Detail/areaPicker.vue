<template>
  <van-field
    v-model="areaFieldValue"
    is-link
    readonly
    label="地點"
    placeholder=""
    @click="getArea()"
  />
  <van-popup
    v-model:show="areaShow"
    round
    position="bottom"
    lock-scroll="false"
    teleport="body"
  >
    <van-cascader
      v-model="areaCascaderValue"
      title=""
      :options="areaOptions"
      :field-names="fieldNames"
      @close="areaShow = false"
      @finish="areaOnFinish"
    />
  </van-popup>
</template>

<style></style>

<script>
import { ref, computed } from "vue";
import axios from "axios";
export default {
  name: "",
  components: {},
  methods: {},
  props: {
    area: {
      type: String,
      default: "",
    },
  },
  emits: ["update:area"],
  setup(props, { emit }) {
    const url = "api/data/area.json";
    const areaOptions = ref([""]);

    const getArea = () => {
      axios
        .get(url)
        .then((response) => {
          console.log(response.data);
          areaOptions.value = response.data;
        })
        .catch((e) => {
          console.error(e);
        });
      areaShow.value = true;
    };
    const fieldNames = {
      text: "des",
      value: "no",
      children: "n",
    };
    const areaShow = ref(false);
    const areaCascaderValue = ref("");

    // const areaOptions = ref([
    //   {
    //     text: "台北市",
    //     value: "100",
    //     children: [],
    //   },
    // ]);

    const areaFieldValue = computed({
      get: () => props.area,
      set: (val) => emit("update:area", val),
    });

    // const areaOnChange = ({ value }) => {
    //   if (value === areaOptions.value[0].value) {
    //     setTimeout(() => {
    //       areaOptions.value[0].children = [
    //         { text: "中正區", value: "1001" },
    //         { text: "大安區", value: "1002" },
    //       ];
    //     }, 500);
    //   }
    // };

    const areaOnFinish = ({ selectedOptions }) => {
      areaShow.value = false;
      console.log(selectedOptions[selectedOptions.length - 1]);
      areaFieldValue.value = selectedOptions[selectedOptions.length - 1].des;

      // areaFieldValue.value = selectedOptions
      //   .map((option) => option.text)
      //   .join("/");
    };

    return {
      areaShow,
      areaFieldValue,
      areaCascaderValue,
      areaOptions,
      areaOnFinish,
      fieldNames,
      getArea,
    };
  },
};
</script>
