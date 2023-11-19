<template>
  <van-field
    v-model="salaryPickerValue"
    is-link
    readonly
    label="薪資待遇"
    placeholder=""
    @click="salaryPickerShow = true"
  />
  <van-popup v-model:show="salaryPickerShow" round position="bottom">
    <van-picker
      :columns="salaryColumns"
      @cancel="salaryPickerShow = false"
      @confirm="salaryOnConfirm"
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
    salaryL: {
      type: String,
      default: "",
    },
  },
  emit: [],
  setup(props, { emit }) {
    const salaryPickerShow = ref(false);
    const salaryPickerValue = computed({
      get: () => props.salaryL,
      set: (val) => emit("update:salaryL", val),
    });
    const salaryColumns = ["月薪3萬", "月薪4萬", "月薪5萬"];

    const salaryOnConfirm = (value) => {
      salaryPickerValue.value = value;
      salaryPickerShow.value = false;
    };

    return {
      salaryPickerShow,
      salaryPickerValue,
      salaryColumns,
      salaryOnConfirm,
    };
  },
};
</script>
