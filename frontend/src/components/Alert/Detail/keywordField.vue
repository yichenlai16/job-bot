<template>
  <van-field v-model="text" label="關鍵字" placeholder="輸入關鍵字" />
</template>

<style></style>

<script>
// import { ref } from "vue";
import { computed } from "vue";

export default {
  name: "",
  components: {},
  methods: {},
  props: {
    keyword: {
      type: String,
      default: "",
    },
  },
  emits: ["update:keyword"],
  setup(props, { emit }) {
    // let params = new URLSearchParams(window.location.search);
    const text = computed({
      get: () => props.keyword,
      set: (val) => emit("update:keyword", val),
    });
    return {
      text,
    };
  },
};
</script>
