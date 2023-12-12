<template>Redirecting...</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";

export default {
  name: "AlertDetail",
  setup() {
    const isShow = ref(true);
    const alert = ref(null);
    const route = useRoute();
    const router = useRouter();

    const getAlertData = async () => {
      try {
        const response = await axios.get("/api/alert/" + `${route.params.id}`);
        console.log(route.params.id);
        alert.value = response.data;

        // 替換下面的 this.$router.replace
        // 使用 router 的 push 函數
        const { keyword, area, cat, period, exp, salarylow } = alert.value;
        const query = {
          search: keyword,
          area,
          cat,
          period,
          exp,
          salarylow,
        };
        router.push({ name: "SearchResults", query });
      } catch (error) {
        console.error("Error fetching alert data:", error);
      }
    };

    onMounted(() => {
      console.log(route.params.id);

      getAlertData();
    });

    return {
      isShow,
      alert,
    };
  },
};
</script>
