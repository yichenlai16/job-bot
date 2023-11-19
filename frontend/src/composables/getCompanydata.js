import { onMounted, watch } from "vue";
import axios from "axios";
export default function getJobData(info, route) {
  const getData = async () => {
    let url = "/api/company";

    const params = new URLSearchParams(); // appendIFExists added on ../main.js=
    params.appendIfExists("type", route.query.type);
    params.appendIfExists("page", route.query.page);
    params.appendIfExists("search", route.query.search);

    const paramsString = params.toString();
    if (paramsString.charAt(0) !== "") {
      url += "/?" + paramsString;
    }

    const response = await axios.get(url);
    info.value = response.data;
  };

  onMounted(() => {
    getData();
  });
  watch(route, getData);
}
