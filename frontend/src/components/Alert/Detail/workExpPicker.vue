<template>
  <van-field
    v-model="workExpPickerValue"
    is-link
    readonly
    label="工作經驗"
    placeholder=""
    @click="workExpPickerShow = true"
  />
  <van-popup v-model:show="workExpPickerShow" round position="bottom">
    <van-picker
      :columns="workExpColumns"
      @cancel="workExpPickerShow = false"
      @confirm="workExpOnConfirm"
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
    exp: {
      type: String,
      default: "",
    },
  },
  emits: ["update.exp"],
  setup(props, { emit }) {
    const workExpPickerShow = ref(false);
    const workExpPickerValue = computed({
      get: () => props.exp,
      set: (val) => emit("update:exp", val),
    });
    const workExpColumns = ["一年以內", "一年到五年", "五年以上"];

    const workExpOnConfirm = (value) => {
      workExpPickerValue.value = value;
      workExpPickerShow.value = false;
    };

    return {
      workExpPickerShow,
      workExpPickerValue,
      workExpColumns,
      workExpOnConfirm,
    };
  },
};
</script>
