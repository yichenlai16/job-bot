import { onMounted, watch } from "vue";
import axios from "axios";
export default function getJobData(info, route) {
  const getData = async () => {
    let url = "/api/ownalert";

    const params = new URLSearchParams(); // appendIFExists added on ../main.js=
    params.appendIfExists("page", route.query.page);
    params.appendIfExists("search", route.query.search);

    const paramsString = params.toString();
    if (paramsString.charAt(0) !== "") {
      url += "/?" + paramsString;
    }

    const response = await axios.get(url, {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("jobproject:access"),
      },
    });
    info.value = response.data;
  };

  onMounted(() => {
    getData();
  });
  watch(route, getData);
}
