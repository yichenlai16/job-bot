<template>
  <topBar />

  <van-empty image="error" description="設定功能開發中。" />

  <navBar />
</template>

<script>
import navBar from "@/components/Navigation/NavBar";
import topBar from "@/components/Navigation/TopBar";
export default {
  name: "About",
  components: {
    navBar,
    topBar,
  },
};
</script>
