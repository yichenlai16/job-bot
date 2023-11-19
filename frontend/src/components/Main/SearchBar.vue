<template>
  <van-search
    disabled
    v-on:click.exact="onSearch"
    placeholder="找職缺？找公司？"
  />
</template>

<script>
export default {
  name: "SearchBar",
  data: function () {
    return {
      searchText: "",
    };
  },
  methods: {
    onSearch() {
      this.$router.push({ name: "SearchResults" });
    },
  },
};
</script>

<style scoped></style>
