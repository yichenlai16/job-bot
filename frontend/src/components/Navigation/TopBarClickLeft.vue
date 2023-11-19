<template>
  <van-nav-bar
    title="求職機器人"
    left-text="返回"
    left-arrow
    @click-left="onClickLeft"
  />
</template>

<script>
// import router from "vue-router"
export default {
  methods: {
    onClickLeft() {
      this.$router.go(-1);
    },
  },
};
</script>
<style></style>
