<template>
  <van-field
    v-model="checkboxLength"
    is-link
    readonly
    label="職務類別"
    placeholder=""
    @click="getJobCat()"
  />
  <van-popup
    v-model:show="catPickerShow"
    round
    position="bottom"
    closeable
    :style="{ height: '80%' }"
    closable
    teleport="body"
  >
    <van-collapse v-model="activeCatNames">
      <!-- <van-cell> <br/></van-cell> -->

      <div class="van-cascader__header">
        <h2 class="van-cascader__title"></h2>
        <i
          class="van-badge__wrapper van-icon van-icon-cross van-cascader__close-icon"
          ><!----><!----><!----></i
        >
      </div>
      <div v-for="cat in jobcat" :key="cat">
        <van-collapse-item v-for="(item, index) in cat['child']" :key="item">
          <template #title> {{ item["name"] }}</template>
          <template #name> {{ index }} </template>
          <!-- {{ item }}{{ index }} -->

          <van-checkbox-group
            v-model="checked"
            ref="checkboxGroup"
            @change="checkboxChange"
          >
            <!-- <van-button  v-on:click="loggy(item)" > click</van-button> -->
            <van-cell-group inset>
              <van-cell
                v-for="item in item['child']"
                clickable
                :key="item['no']"
                :title="`${item['name']}`"
                @click="toggle(item['no'])"
              >
                <template #right-icon>
                  <van-checkbox
                    :name="item['name']"
                    :ref="(el) => (checkboxRefs[item['no']] = el)"
                    @click.stop
                  />
                </template>
              </van-cell>
            </van-cell-group>
          </van-checkbox-group>
        </van-collapse-item>
      </div>
    </van-collapse>
  </van-popup>
</template>

<style></style>

<script>
import { ref, computed, onBeforeUpdate } from "vue";
import axios from "axios";
export default {
  name: "",
  components: {},
  methods: {},
  props: {
    cat: {
      type: String,
      default: "",
    },
  },
  emits: ["update:keyword"],
  setup(props, { emit }) {
    const catPickerShow = ref(false);
    const catPickerValue = computed({
      get: () => props.cat,
      set: (val) => emit("update:cat", val),
    });

    const activeCatNames = ref(["0"]);

    const checked = ref([]);
    const checkboxRefs = ref([]);
    const toggle = (index) => {
      checkboxRefs.value[index].toggle();
      console.log(checkboxRefs.value[index]);
    };
    const jobcat = ref({});

    const loggy = (content) => {
      for (var i in content["child"]) {
        console.log(content["child"][i]["no"]);
        checkboxRefs.value[content["child"][i]["no"]].toggle();
      }
    };

    const getJobCat = () => {
      catPickerShow.value = true;
      axios.get("/api/data/job-category.json").then((response) => {
        console.log(response.data);
        jobcat.value = response.data;
        console.log(jobcat);
      });
    };

    const checkboxLength = ref("已選0個");

    const checkboxChange = (Event) => {
      console.log(Event);
      console.log(Event.length);
      checkboxLength.value = "已選" + Event.length + "個";
      let searchCat = "";
      Event.forEach(function (item) {
        searchCat += item + ",";
      });
      catPickerValue.value = searchCat;
      console.log(searchCat);
    };

    onBeforeUpdate(() => {
      checkboxRefs.value = [];
    });

    return {
      list: ["a", "b"],
      toggle,
      checked,
      checkboxRefs,
      getJobCat,
      catPickerShow,
      catPickerValue,
      checkboxLength,
      checkboxChange,
      loggy,
      activeCatNames,
      jobcat,
    };
  },
};
</script>
