<template>
  <SearchBar></SearchBar>
  <navBar />
</template>

<script>
import navBar from "@/components/Navigation/NavBar";
import SearchBar from "@/components/Search/SearchBar";
import { reactive, ref } from "vue";

// import jobItem from "@/components/item/job";

export default {
  name: "Search",
  components: {
    navBar,
    SearchBar,
  },
  methods: {
    onClick() {
      window.history.go(-1);
    },
  },
  setup() {
    const state = reactive({
      value1: 0,
    });
    const search_option = [
      { text: "全部", value: 0 },
      { text: "職缺", value: 1 },
      { text: "公司", value: 2 },
    ];
    const show = ref(false);
    return {
      state,
      search_option,
      show,
    };
  },
};
</script>
