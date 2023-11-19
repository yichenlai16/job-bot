<template>
  <SearchBar />

  <div class="SearchResult">
    <van-tabs v-model:active="active" animated swipeable>
      <van-tab title="職缺">
        <JobList class="list" />
      </van-tab>
      <van-tab title="公司">
        <CompanyList class="list" />
      </van-tab>
    </van-tabs>
  </div>
  <navBar />
</template>

<style>
.list {
  overflow: hidden;
  height: auto;
}
.SearchResult {
  overflow: auto;
}
</style>

<script>
import navBar from "@/components/Navigation/NavBar";
import SearchBar from "@/components/Search/SearchBar";
import CompanyList from "@/components/CompanyList";
import JobList from "@/components/JobList";
import { ref, watch } from "vue";
import { useRoute } from "vue-router";

// import jobItem from "@/components/item/job";

export default {
  name: "Search",
  components: {
    navBar,
    SearchBar,
    JobList,
    CompanyList,
  },

  setup() {
    // const searchParams = new URLSearchParams(window.location.search);

    const route = useRoute();

    const type = parseInt(route.query.type);
    const active = ref(type);

    watch(active, () => {
      const params = new URLSearchParams(window.location.search);
      params.set("type", active.value);
      window.history.replaceState(
        {},
        "",
        decodeURIComponent(`${window.location.pathname}?${params}`)
      );
    });

    watch(type, () => {
      active.value = type;
    });

    return {
      active,
    };
  },
};
</script>
