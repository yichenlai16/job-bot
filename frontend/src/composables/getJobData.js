import { onMounted, watch } from "vue";
import axios from "axios";
export default function getJobData(info, route) {
  const getData = async () => {
    let url = "/api/job";

    const params = new URLSearchParams(); // appendIFExists added on ../main.js=
    params.appendIfExists("type", route.query.type);
    params.appendIfExists("page", route.query.page);
    params.appendIfExists("search", route.query.search);
    params.appendIfExists("area", route.query.area);
    params.appendIfExists("cat", route.query.cat);
    params.appendIfExists("period", route.query.period);
    params.appendIfExists("exp", route.query.exp);
    params.appendIfExists("salarylow", route.query.salarylow);

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
