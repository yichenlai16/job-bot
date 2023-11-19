<template>
  <van-field
    v-model="workPeriodPickerValue"
    is-link
    readonly
    label="上班時段"
    placeholder=""
    @click="workPeriodPickerShow = true"
  />
  <van-popup v-model:show="workPeriodPickerShow" round position="bottom">
    <van-picker
      :columns="workPeriodColumns"
      @cancel="workPeriodPickerShow = false"
      @confirm="workPeriodOnConfirm"
    />
  </van-popup>
</template>

<style></style>

<script>
import { ref, computed } from "vue";

export default {
  name: "",
  components: {},
  methods: {},
  props: {
    period: {
      type: String,
      default: "",
    },
  },
  emits: ["update:period"],
  setup(props, { emit }) {
    const workPeriodPickerShow = ref(false);
    const workPeriodPickerValue = computed({
      get: () => props.period,
      set: (val) => emit("update:period", val),
    });
    const workPeriodColumns = [
      "日班",
      "晚班",
      "大夜班",
      "假日班",
      "需輪班",
      "不需輪班",
    ];

    const workPeriodOnConfirm = (value) => {
      workPeriodPickerValue.value = value;
      workPeriodPickerShow.value = false;
    };

    return {
      workPeriodPickerShow,
      workPeriodPickerValue,
      workPeriodColumns,
      workPeriodOnConfirm,
    };
  },
};
</script>
