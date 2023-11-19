<template>
  <div>callback</div>
</template>

<script>
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
export default {
  setup() {
    console.log("??");
    const route = useRoute();
    const router = useRouter();
    let url = "/api/oauth/notify/callback";
    let params = new URLSearchParams();
    params.appendIfExists("code", route.query.code);
    const paramsString = params.toString();
    if (paramsString.charAt(0) !== "") {
      url += "?" + paramsString;
    }
    console.log(url);

    axios
      .get(url, {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("jobproject:access"),
        },
      })
      .then(function (response) {
        console.log(response);
        router.push({ name: "Alert" });
      });
    router.push({ name: "Alert" });
  },
};
</script>
